#!/usr/bin/env python3
"""Audit différentiel : compare les signaux d'IA entre deux états d'un dépôt Git.

Lecture seule : les contenus sont lus avec `git show <ref>:<chemin>` (aucun checkout, aucune
modification de l'arbre de travail ni de l'index). Aucun appel réseau.

Le rapport signale ce qui peut faire naître ou disparaître des obligations : nouveaux usages
d'IA, changements de modèles, nouveaux contextes sensibles (finalité), nouveaux chemins de
sortie, mesures de transparence, de supervision ou de traçabilité supprimées. Il ne remplace
pas l'audit : il indique où le refaire.

Usage :
    python3 scripts/diff_ai_signals.py DEPOT --base origin/main [--head HEAD | --head WORKTREE] [--json]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scan_ai_signals as scanner  # noqa: E402

WORKTREE = "WORKTREE"
ALERT_ON_REMOVAL = {"transparency_marker", "oversight_marker", "logging_marker"}
ALERT_ON_ADDITION = scanner.AI_CATEGORIES | {"sensitive_context", "output_channel", "credentials_reference", "transparency_risk"}


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True)
    return result.stdout


def items_at_ref(repo: Path, ref: str, exclude: list[str]):
    for rel in git(repo, "ls-tree", "-r", "--name-only", ref).splitlines():
        if not scanner.is_scannable(rel, exclude):
            continue
        try:
            content = subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{rel}"],
                                     capture_output=True, check=True).stdout
        except subprocess.CalledProcessError:
            continue
        if len(content) > scanner.MAX_FILE_BYTES:
            continue
        yield rel, content.decode("utf-8", errors="replace")


def scan_state(repo: Path, ref: str, exclude: list[str]) -> dict:
    if ref == WORKTREE:
        return scanner.scan(repo, max_hits=100_000, exclude=exclude)
    return scanner.scan_items(items_at_ref(repo, ref, exclude), f"{repo.name}@{ref}", max_hits=100_000)


def signal_keys(report: dict) -> dict[tuple, list[dict]]:
    """Regroupe les occurrences par (catégorie, signal, fichier, extrait normalisé)."""
    keys: dict[tuple, list[dict]] = defaultdict(list)
    for hit in report["hits"]:
        keys[(hit["category"], hit["signal"], hit["file"], hit["excerpt"])].append(hit)
    return keys


def diff(repo: Path, base: str, head: str, exclude: list[str] | None = None) -> dict:
    exclude = exclude or []
    before = scan_state(repo, base, exclude)
    after = scan_state(repo, head, exclude)
    kb, ka = signal_keys(before), signal_keys(after)
    added = [ka[k][0] for k in ka.keys() - kb.keys()]
    removed = [kb[k][0] for k in kb.keys() - ka.keys()]
    added.sort(key=lambda h: (h["category"], h["file"], h["line"]))
    removed.sort(key=lambda h: (h["category"], h["file"], h["line"]))

    alerts = []
    new_categories = set(after["summary"]) - set(before["summary"])
    for cat in sorted(new_categories & scanner.AI_CATEGORIES):
        alerts.append(f"Nouvelle catégorie d'IA : {cat} (nouvel usage possible : inventaire et classification à refaire)")

    def grouped(hits_list, categories):
        groups: dict[tuple, list[str]] = defaultdict(list)
        for h in hits_list:
            if h["category"] in categories:
                loc = f"{h['file']}:{h['line']}"
                if loc not in groups[(h["category"], h["signal"])]:
                    groups[(h["category"], h["signal"])].append(loc)
        return sorted(groups.items())

    messages = {
        "model_identifier": "Identifiant de modèle ajouté ou modifié ({sig}) : {locs} (art. 111, par. 2 ; documentation ; journalisation de version)",
        "sensitive_context": "Nouveau contexte sensible « {sig} » : {locs} (finalité à réexaminer, annexe III)",
        "output_channel": "Nouveau chemin de sortie « {sig} » : {locs} (préservation du marquage, art. 50, par. 2)",
        "biometric": "Nouveau signal biométrique « {sig} » : {locs} (art. 5 et annexe III, point 1)",
        "transparency_risk": "Instruction de persona humaine ou de déni de nature IA « {sig} » : {locs} (art. 50, par. 1)",
    }
    for (cat, sig), locs in grouped(added, set(messages)):
        shown = ", ".join(locs[:5]) + (f" et {len(locs) - 5} autre(s)" if len(locs) > 5 else "")
        alerts.append(messages[cat].format(sig=sig, locs=shown))
    for (cat, sig), locs in grouped(removed, ALERT_ON_REMOVAL):
        shown = ", ".join(locs[:5]) + (f" et {len(locs) - 5} autre(s)" if len(locs) > 5 else "")
        alerts.append(f"Mesure supprimée ou modifiée ({cat} / {sig}) : {shown} dans l'état de base (contrôle à refaire)")
    if len(after["possible_secrets"]) > len(before["possible_secrets"]):
        alerts.append("Nouveau secret potentiel détecté (valeur masquée)")

    changed = []
    if head != WORKTREE:
        changed = git(repo, "diff", "--name-only", base, head).splitlines()
    else:
        changed = git(repo, "diff", "--name-only", base).splitlines()

    return {
        "base": base,
        "head": head,
        "changed_files": changed,
        "ai_signals_before": before["ai_signals_detected"],
        "ai_signals_after": after["ai_signals_detected"],
        "alerts": alerts,
        "added": [h for h in added if h["category"] in ALERT_ON_ADDITION | ALERT_ON_REMOVAL],
        "removed": removed,
        "disclaimer": (
            "Comparaison de signaux techniques. Une alerte signale un point à réauditer ; "
            "elle ne constitue ni une qualification juridique ni une conclusion de conformité."
        ),
    }


def to_markdown(report: dict) -> str:
    out = [
        f"# Audit différentiel IA : {report['base']} -> {report['head']}",
        "",
        f"Fichiers modifiés : {len(report['changed_files'])} | Signaux d'IA avant : "
        f"{'oui' if report['ai_signals_before'] else 'non'} | après : {'oui' if report['ai_signals_after'] else 'non'}",
        "",
        "## Alertes à réauditer",
        "",
    ]
    out += [f"- {a}" for a in report["alerts"]] or ["- Aucune alerte."]
    for title, key in (("Signaux ajoutés", "added"), ("Signaux supprimés", "removed")):
        out += ["", f"## {title}", "", "| Fichier:ligne | Catégorie | Signal | Extrait (masqué) |", "|---|---|---|---|"]
        for h in report[key]:
            excerpt = h["excerpt"].replace("|", "\\|")
            out.append(f"| {h['file']}:{h['line']} | {h['category']} | {h['signal']} | `{excerpt}` |")
    out += ["", f"> {report['disclaimer']}"]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit différentiel des signaux d'IA entre deux états Git (lecture seule).")
    parser.add_argument("repo", help="Racine du dépôt Git")
    parser.add_argument("--base", required=True, help="Référence de base (branche, tag, commit)")
    parser.add_argument("--head", default="HEAD", help=f"Référence comparée (défaut HEAD ; {WORKTREE} pour l'arbre de travail)")
    parser.add_argument("--exclude", action="append", default=[], help="Motif glob à ignorer (répétable)")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    try:
        report = diff(repo, args.base, args.head, args.exclude)
    except subprocess.CalledProcessError as exc:
        print(f"Erreur Git : {exc.stderr.strip() if exc.stderr else exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else to_markdown(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
