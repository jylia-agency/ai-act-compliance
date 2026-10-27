#!/usr/bin/env python3
"""Évalue le statut temporel des obligations de l'AI Act à une date d'audit donnée.

Script en lecture seule : il lit data/ai-act-calendar.json et écrit sur la sortie
standard. Il n'effectue aucun appel réseau.

Le résultat est une aide au raisonnement, pas une qualification juridique :
chaque ligne renvoie à une entrée du calendrier dont la source et le niveau de
confiance doivent être repris dans le rapport.

Règle bloquante : une entrée dont la base juridique n'est pas vérifiée
(verification_status « sources_secondaires » ou « incertaine ») produit
requires_confirmation=True et un statut assorti de « échéance à confirmer ».

Exemples :
    python3 scripts/obligation_timeline.py --audit-date 2026-10-27
    python3 scripts/obligation_timeline.py --audit-date 2026-10-27 \
        --placed-on-market 2026-03-01 --scope transparency
    python3 scripts/obligation_timeline.py --audit-date 2026-10-27 --json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

CALENDAR_PATH = Path(__file__).resolve().parent.parent / "data" / "ai-act-calendar.json"

STATUS_APPLICABLE = "applicable"
STATUS_FUTURE = "non_encore_applicable"
STATUS_CONDITIONAL = "conditionnel"
STATUS_UNKNOWN = "a_verifier"

BLOCKING_VERIFICATION_STATUSES = {"sources_secondaires", "incertaine"}
CONFIRMATION_SUFFIX = " (échéance à confirmer)"

STATUS_LABELS = {
    STATUS_APPLICABLE: "En vigueur à la date d'audit",
    STATUS_FUTURE: "Non encore applicable",
    STATUS_CONDITIONAL: "Conditionnel",
    STATUS_UNKNOWN: "À vérifier",
}


def parse_date(value: str | None) -> dt.date | None:
    if value is None:
        return None
    return dt.date.fromisoformat(value)


def load_calendar(path: Path = CALENDAR_PATH) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def evaluate_entry(
    entry: dict,
    audit_date: dt.date,
    placed_on_market: dt.date | None = None,
    public_authority: bool = False,
) -> dict:
    """Retourne le statut d'une entrée du calendrier à la date d'audit."""
    base_date = parse_date(entry.get("date"))
    legacy = entry.get("legacy")
    effective = base_date
    reason = ""

    if base_date is None:
        return _result(entry, STATUS_UNKNOWN, None, "Date d'application non établie de manière fiable.")

    if legacy:
        placed_before = parse_date(legacy["placed_before"])
        if placed_on_market is None:
            legacy_date = legacy.get("effective_date")
            return _result(
                entry,
                STATUS_CONDITIONAL,
                base_date,
                "Dépend de la date de mise sur le marché ou de mise en service, non fournie. "
                f"Règle transitoire : systèmes mis sur le marché avant le {placed_before.isoformat()} "
                + (f"-> échéance {legacy_date}." if legacy_date else "-> régime spécifique (voir notes)."),
            )
        if placed_on_market < placed_before:
            if public_authority and legacy.get("public_authority_effective_date"):
                effective = parse_date(legacy["public_authority_effective_date"])
                reason = "Système antérieur destiné à une autorité publique : échéance spécifique."
            elif legacy.get("effective_date"):
                effective = parse_date(legacy["effective_date"])
                reason = "Régime transitoire applicable (mise sur le marché antérieure)."
            else:
                return _result(
                    entry,
                    STATUS_CONDITIONAL,
                    None,
                    "Système antérieur : obligations applicables seulement en cas de modification "
                    "importante de la conception après la date de référence (à vérifier).",
                )
        else:
            reason = "Mise sur le marché à partir de la date de référence : pas de régime transitoire."
            status = STATUS_APPLICABLE if effective <= audit_date else STATUS_FUTURE
            if status == STATUS_FUTURE:
                reason += f" Applicable dans {(effective - audit_date).days} jour(s)."
            return _result(entry, status, effective, reason, used_legacy=False)

    status = STATUS_APPLICABLE if effective <= audit_date else STATUS_FUTURE
    if status == STATUS_FUTURE:
        days = (effective - audit_date).days
        reason = (reason + " " if reason else "") + f"Applicable dans {days} jour(s)."
    return _result(entry, status, effective, reason.strip())


def verification_status(entry: dict, used_legacy: bool = True) -> str:
    """Statut de vérification de la règle effectivement utilisée pour conclure.

    Si la date retenue est la date de base et que celle-ci a son propre statut
    (base_verification_status), c'est ce statut qui s'applique.
    """
    basis = entry.get("legal_basis", {})
    if not used_legacy and basis.get("base_verification_status"):
        return basis["base_verification_status"]
    return basis.get("verification_status", "incertaine")


def requires_confirmation(entry: dict, used_legacy: bool = True) -> bool:
    return verification_status(entry, used_legacy) in BLOCKING_VERIFICATION_STATUSES


def _result(entry: dict, status: str, effective: dt.date | None, reason: str, used_legacy: bool = True) -> dict:
    blocked = requires_confirmation(entry, used_legacy)
    label = STATUS_LABELS[status] + (CONFIRMATION_SUFFIX if blocked and status != STATUS_UNKNOWN else "")
    return {
        "id": entry["id"],
        "label": entry["label"],
        "articles": entry.get("articles", []),
        "status": status,
        "status_label": label,
        "requires_confirmation": blocked,
        "verification_status": verification_status(entry, used_legacy),
        "effective_date": effective.isoformat() if effective else None,
        "confidence": entry.get("confidence"),
        "source_url": entry.get("source_url"),
        "reason": reason,
    }


def evaluate(
    audit_date: dt.date,
    placed_on_market: dt.date | None = None,
    scope: str | None = None,
    public_authority: bool = False,
    calendar: dict | None = None,
) -> list[dict]:
    calendar = calendar or load_calendar()
    results = []
    for entry in calendar["entries"]:
        if scope and scope not in entry.get("scope", []):
            continue
        results.append(evaluate_entry(entry, audit_date, placed_on_market, public_authority))
    return results


def to_markdown(results: list[dict], audit_date: dt.date, last_verified: str) -> str:
    lines = [
        f"Date d'audit : {audit_date.isoformat()} | Calendrier vérifié le : {last_verified}",
        "",
        "| ID | Obligation | Statut | Date effective | Confiance | Vérification | Motif |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in results:
        lines.append(
            f"| {item['id']} | {item['label']} | {item['status_label']} | "
            f"{item['effective_date'] or 'n.d.'} | {item['confidence']} | "
            f"{item['verification_status']} | {item['reason']} |"
        )
    lines += [
        "",
        "Avertissement : statut calculé à partir d'un calendrier de référence daté. "
        "Les lignes « échéance à confirmer » reposent sur une base juridique non relue sur le texte "
        "officiel : elles ne peuvent fonder qu'une conclusion temporelle conditionnelle.",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--audit-date", default=dt.date.today().isoformat(), help="AAAA-MM-JJ (défaut : aujourd'hui)")
    parser.add_argument("--placed-on-market", help="Date de mise sur le marché ou de mise en service du système (AAAA-MM-JJ)")
    parser.add_argument("--scope", help="Filtre : all, provider, deployer, gpai-provider, transparency, generative, prohibited, high-risk-annex-iii, high-risk-annex-i")
    parser.add_argument("--public-authority", action="store_true", help="Système destiné à être utilisé par une autorité publique")
    parser.add_argument("--json", action="store_true", help="Sortie JSON")
    args = parser.parse_args(argv)

    try:
        audit_date = parse_date(args.audit_date)
        placed = parse_date(args.placed_on_market)
    except ValueError as exc:
        print(f"Date invalide : {exc}", file=sys.stderr)
        return 2

    calendar = load_calendar()
    results = evaluate(audit_date, placed, args.scope, args.public_authority, calendar)
    if args.json:
        print(json.dumps({"audit_date": audit_date.isoformat(), "results": results}, ensure_ascii=False, indent=2))
    else:
        print(to_markdown(results, audit_date, calendar["meta"]["last_verified"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
