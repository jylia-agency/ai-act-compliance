#!/usr/bin/env python3
"""Veille automatisée des actes liés au règlement (UE) 2024/1689 (lecture seule).

Interroge le point d'accès SPARQL public de l'Office des publications (Cellar) pour lister les
actes qui modifient, corrigent, consolident ou mettent en œuvre le règlement, puis les compare
au référentiel data/legal-watch.json. Les actes inconnus sont signalés pour REVUE HUMAINE.

Ce script ne modifie jamais un fichier du dépôt ni une règle juridique. Il écrit uniquement sur
la sortie standard (ou dans le fichier indiqué par --output).

Codes de sortie : 0 = aucun nouvel acte ; 1 = nouveaux actes à revoir ; 2 = échec de la requête.

Usage :
    python3 scripts/check_legal_updates.py [--output rapport.md] [--json]
    python3 scripts/check_legal_updates.py --offline-response reponse.json   (tests)
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

WATCH_PATH = Path(__file__).resolve().parent.parent / "data" / "legal-watch.json"
TIMEOUT_SECONDS = 60

QUERY_TEMPLATE = """PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?celex ?relation WHERE {{
  ?base cdm:resource_legal_id_celex ?baseCelex .
  FILTER(STR(?baseCelex) = "{base}")
  ?act ?relation ?base .
  FILTER(CONTAINS(LCASE(STR(?relation)), "amend") || CONTAINS(LCASE(STR(?relation)), "correct")
      || CONTAINS(LCASE(STR(?relation)), "consolidat") || CONTAINS(LCASE(STR(?relation)), "based_on")
      || CONTAINS(LCASE(STR(?relation)), "implement") || CONTAINS(LCASE(STR(?relation)), "repeal"))
  ?act cdm:resource_legal_id_celex ?celex .
}}
LIMIT 500"""


def load_watch(path: Path = WATCH_PATH) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def build_query(base_celex: str) -> str:
    return QUERY_TEMPLATE.format(base=base_celex)


def fetch(endpoint: str, query: str) -> dict:
    url = endpoint + "?" + urllib.parse.urlencode({"query": query, "format": "application/sparql-results+json"})
    request = urllib.request.Request(url, headers={"Accept": "application/sparql-results+json",
                                                   "User-Agent": "ia-compliance-legal-watch"})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:  # noqa: S310 (URL fixe)
        return json.loads(response.read().decode("utf-8"))


def parse(response: dict) -> dict[str, set[str]]:
    """Retourne {celex: {relations}} à partir d'une réponse SPARQL JSON."""
    found: dict[str, set[str]] = {}
    for row in response.get("results", {}).get("bindings", []):
        celex = row.get("celex", {}).get("value", "").strip()
        relation = row.get("relation", {}).get("value", "").rsplit("#", 1)[-1]
        if celex:
            found.setdefault(celex, set()).add(relation)
    return found


def compare(found: dict[str, set[str]], watch: dict) -> list[dict]:
    known = set(watch["known_celex"])
    return [{"celex": c, "relations": sorted(r), "eurlex": f"https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:{c}"}
            for c, r in sorted(found.items()) if c not in known]


def to_markdown(new_acts: list[dict], watch: dict, error: str | None = None) -> str:
    lines = ["# Veille juridique AI Act", "",
             f"Référentiel revu le : {watch['meta']['baseline_reviewed_on']} | Acte de base : CELEX {watch['base_celex']}", ""]
    if error:
        lines += [f"**Échec du contrôle automatique** : {error}", "",
                  "Effectuer la revue manuelle prévue par `references/maintenance.md`."]
        return "\n".join(lines)
    if not new_acts:
        lines.append("Aucun acte nouveau détecté par rapport au référentiel.")
    else:
        lines += ["Actes non encore pris en compte (**revue humaine requise**, aucune règle n'a été modifiée) :", "",
                  "| CELEX | Relation avec le règlement | Lien |", "|---|---|---|"]
        lines += [f"| {a['celex']} | {', '.join(a['relations'])} | {a['eurlex']} |" for a in new_acts]
        lines += ["", "Procédure : `references/maintenance.md`, sections 3 et 4. Après revue, ajouter l'acte à "
                  "`data/legal-watch.json` (known_celex) et, si nécessaire, mettre à jour le calendrier."]
    lines += ["", "> Détection automatique indicative : elle ne remplace pas la veille manuelle (lignes "
              "directrices, codes de bonnes pratiques, normes harmonisées)."]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Veille automatisée des actes liés à l'AI Act (lecture seule).")
    parser.add_argument("--offline-response", help="Fichier de réponse SPARQL JSON (tests, sans réseau)")
    parser.add_argument("--output", help="Écrire le rapport Markdown dans ce fichier")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    watch = load_watch()
    error = None
    new_acts: list[dict] = []
    try:
        if args.offline_response:
            response = json.loads(Path(args.offline_response).read_text(encoding="utf-8"))
        else:
            response = fetch(watch["sparql_endpoint"], build_query(watch["base_celex"]))
        new_acts = compare(parse(response), watch)
    except Exception as exc:  # réseau, format, service indisponible
        error = f"{type(exc).__name__}: {exc}"

    report = json.dumps({"error": error, "new_acts": new_acts}, ensure_ascii=False, indent=2) if args.json \
        else to_markdown(new_acts, watch, error)
    if args.output:
        Path(args.output).write_text(report + "\n", encoding="utf-8")
    else:
        print(report)
    if error:
        return 2
    return 1 if new_acts else 0


if __name__ == "__main__":
    sys.exit(main())
