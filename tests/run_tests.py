#!/usr/bin/env python3
"""Tests de cohérence et de fiabilité du skill ia-compliance (bibliothèque standard uniquement).

Exécution :
    python3 tests/run_tests.py          (ou python3 -m unittest discover -s tests)

Ces tests vérifient la structure du skill, la cohérence du calendrier juridique, le calcul
des statuts temporels et le scanner de signaux sur les fixtures. Ils ne vérifient PAS la
qualité du raisonnement d'un agent : voir tests/README.md (évaluation par agent).
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import obligation_timeline as timeline  # noqa: E402
import scan_ai_signals as scanner  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
REQUIRED_FILES = [
    "SKILL.md", "README.md", "CHANGELOG.md", "CONTRIBUTING.md", "LICENSE", ".gitignore",
    "references/ai-act-overview.md", "references/legal-sources.md",
    "references/applicability-calendar.md", "references/prohibited-practices.md",
    "references/risk-classification.md", "references/provider-obligations.md",
    "references/deployer-obligations.md", "references/gpai-obligations.md",
    "references/transparency.md", "references/human-oversight.md",
    "references/technical-documentation.md", "references/education-ai.md",
    "references/audit-checklist.md",
    "templates/audit-report.md", "templates/ai-system-inventory.md",
    "templates/risk-classification.md", "templates/compliance-matrix.md",
    "templates/remediation-plan.md", "templates/unverifiable-register.md",
    "examples/example-audit.md",
    "tests/fixtures/demo-ai-vulnerable/EXPECTED.md",
    "tests/fixtures/demo-ai-secure/EXPECTED.md",
    "tests/fixtures/demo-no-ai/EXPECTED.md",
    "tests/fixtures/demo-insufficient-info/EXPECTED.md",
    "data/ai-act-calendar.json",
]
FINDING_FIELDS = [
    "Système d'IA concerné", "Nature du constat", "Gravité", "Niveau de confiance",
    "Preuve observée", "Fichier(s) et lignes", "Rôle réglementaire concerné",
    "Classification du système", "Référence juridique", "Date d'application",
    "Conditions et exceptions", "Explication", "Recommandation", "Méthode de vérification",
]
NATURES = {
    "Constat technique avéré", "Risque potentiel",
    "À vérifier juridiquement ou organisationnellement", "Bonne pratique recommandée",
    "Non applicable", "Non encore applicable",
}
D = dt.date.fromisoformat


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError("Frontmatter YAML absent")
    data: dict = {}
    current = None
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and current:
            key, _, value = line.strip().partition(":")
            data[current][key.strip()] = value.strip().strip('"')
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value == "":
            data[key] = {}
            current = key
        else:
            data[key] = value
            current = None
    return data


def status_of(entry_id: str, audit: str, placed: str | None = None, public: bool = False) -> dict:
    cal = timeline.load_calendar()
    entry = next(e for e in cal["entries"] if e["id"] == entry_id)
    return timeline.evaluate_entry(entry, D(audit), D(placed) if placed else None, public)


class StructureTests(unittest.TestCase):
    def test_required_files_exist(self):
        missing = [f for f in REQUIRED_FILES if not (ROOT / f).is_file()]
        self.assertEqual(missing, [], f"Fichiers manquants : {missing}")

    def test_skill_frontmatter(self):
        fm = parse_frontmatter((ROOT / "SKILL.md").read_text(encoding="utf-8"))
        self.assertEqual(fm.get("name"), "ia-compliance")
        self.assertRegex(fm["name"], r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(fm["name"]), 64)
        self.assertTrue(fm.get("description"))
        self.assertLessEqual(len(fm["description"]), 1024, "description > 1024 caractères")
        self.assertIn("compatibility", fm)
        self.assertLessEqual(len(fm["compatibility"]), 500)
        self.assertEqual(fm["metadata"]["legal-references-last-verified"],
                         timeline.load_calendar()["meta"]["last_verified"])

    def test_skill_body_length(self):
        lines = (ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLess(len(lines), 500, "SKILL.md devrait rester sous 500 lignes")

    def test_paths_referenced_in_skill_exist(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        paths = set(re.findall(r"`((?:references|templates|scripts|examples|data)/[\w./-]+)`", text))
        self.assertTrue(paths)
        missing = sorted(p for p in paths if not (ROOT / p).exists())
        self.assertEqual(missing, [], f"Chemins cités dans SKILL.md introuvables : {missing}")

    def test_references_are_dated(self):
        for path in sorted((ROOT / "references").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            self.assertRegex(text, r"(Dernière vérification|Dernière mise à jour|Dernière exécution)[^\n]*2026-10-27",
                             f"{path.name} : date de vérification absente")

    def test_legal_references_cite_official_source(self):
        legal = [p for p in (ROOT / "references").glob("*.md")
                 if p.name not in {"ai-detection-signals.md", "findings-methodology.md",
                                   "audit-checklist.md", "maintenance.md"}]
        for path in legal:
            text = path.read_text(encoding="utf-8")
            self.assertTrue("eur-lex.europa.eu" in text or "ai-act-service-desk.ec.europa.eu" in text,
                            f"{path.name} : aucune source officielle citée")

    def test_no_compliance_certification_claim(self):
        forbidden = re.compile(r"(projet|système|application) (est|sont) (entièrement |pleinement )?conformes? (à|au)", re.I)
        for path in list((ROOT / "references").glob("*.md")) + list((ROOT / "templates").glob("*.md")) + [
                ROOT / "SKILL.md", ROOT / "examples" / "example-audit.md"]:
            for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if re.search(r"\b(jamais|ne pas|n'est pas|ni)\b", line, re.I):
                    continue  # règle d'interdiction, pas une affirmation
                self.assertIsNone(forbidden.search(line), f"{path.name}:{lineno} affirme une conformité")


class CalendarDataTests(unittest.TestCase):
    def setUp(self):
        self.cal = timeline.load_calendar()

    def test_entries_are_complete_and_sourced(self):
        ids = []
        for e in self.cal["entries"]:
            ids.append(e["id"])
            for key in ("id", "label", "articles", "scope", "kind", "source_text", "source_url",
                        "confidence", "verified_on", "notes"):
                self.assertIn(key, e, f"{e.get('id')} : champ {key} manquant")
            self.assertRegex(e["source_url"], r"^https://eur-lex\.europa\.eu/")
            self.assertIn(e["confidence"], {"elevee", "moyenne", "faible"})
            D(e["verified_on"])
            if e["date"] is not None:
                D(e["date"])
            if "legacy" in e:
                D(e["legacy"]["placed_before"])
                if e["legacy"].get("effective_date"):
                    D(e["legacy"]["effective_date"])
        self.assertEqual(len(ids), len(set(ids)), "identifiants dupliqués")

    def test_omnibus_entries_are_not_high_confidence(self):
        for e in self.cal["entries"]:
            if e["source_text"] == "2026/1744":
                self.assertNotEqual(e["confidence"], "elevee", f"{e['id']} : 2026/1744 non relu, confiance élevée injustifiée")

    def test_markdown_calendar_in_sync(self):
        md = (ROOT / "references" / "applicability-calendar.md").read_text(encoding="utf-8")
        for e in self.cal["entries"]:
            self.assertIn(e["id"], md, f"{e['id']} absent de applicability-calendar.md")
            if e["date"]:
                row = next((l for l in md.splitlines() if l.startswith(f"| {e['id']} ")), "")
                self.assertIn(e["date"], row, f"{e['id']} : date divergente entre JSON et Markdown")


class TimelineScenarioTests(unittest.TestCase):
    """Scénarios de calendrier réglementaire (faux positifs et faux négatifs temporels)."""

    def test_chatbot_transparency_in_force(self):
        self.assertEqual(status_of("CAL-009", "2026-10-27")["status"], timeline.STATUS_APPLICABLE)

    def test_transparency_not_in_force_before_august_2026(self):
        self.assertEqual(status_of("CAL-009", "2026-07-15")["status"], timeline.STATUS_FUTURE)

    def test_legacy_generator_grace_period(self):
        r = status_of("CAL-010", "2026-10-27", "2026-03-01")
        self.assertEqual(r["status"], timeline.STATUS_FUTURE)
        self.assertEqual(r["effective_date"], "2026-12-02")

    def test_legacy_generator_after_grace_period(self):
        self.assertEqual(status_of("CAL-010", "2026-12-15", "2026-03-01")["status"], timeline.STATUS_APPLICABLE)

    def test_new_generator_has_no_grace_period(self):
        r = status_of("CAL-010", "2026-10-27", "2026-09-15")
        self.assertEqual(r["status"], timeline.STATUS_APPLICABLE)
        self.assertEqual(r["effective_date"], "2026-08-02")

    def test_generator_without_placement_date_is_conditional(self):
        self.assertEqual(status_of("CAL-010", "2026-10-27")["status"], timeline.STATUS_CONDITIONAL)

    def test_annex_iii_high_risk_not_yet_applicable(self):
        r = status_of("CAL-011", "2026-10-27")
        self.assertEqual(r["status"], timeline.STATUS_FUTURE)
        self.assertEqual(r["effective_date"], "2027-12-02")

    def test_annex_iii_high_risk_applicable_after_deferral(self):
        self.assertEqual(status_of("CAL-011", "2027-12-02")["status"], timeline.STATUS_APPLICABLE)

    def test_annex_i_high_risk_date(self):
        self.assertEqual(status_of("CAL-012", "2028-01-01")["status"], timeline.STATUS_FUTURE)

    def test_legacy_high_risk_is_conditional(self):
        self.assertEqual(status_of("CAL-013", "2026-10-27", "2026-03-01")["status"], timeline.STATUS_CONDITIONAL)

    def test_legacy_high_risk_public_authority(self):
        r = status_of("CAL-013", "2026-10-27", "2026-03-01", public=True)
        self.assertEqual(r["status"], timeline.STATUS_FUTURE)
        self.assertEqual(r["effective_date"], "2030-08-02")

    def test_new_high_risk_after_reference_date(self):
        self.assertEqual(status_of("CAL-013", "2028-01-10", "2028-01-05")["status"], timeline.STATUS_APPLICABLE)

    def test_prohibited_practices_in_force(self):
        self.assertEqual(status_of("CAL-002", "2026-10-27", "2024-01-01")["status"], timeline.STATUS_APPLICABLE)

    def test_new_prohibitions_not_yet_applicable(self):
        self.assertEqual(status_of("CAL-004", "2026-10-27")["status"], timeline.STATUS_FUTURE)
        self.assertEqual(status_of("CAL-004", "2026-12-02")["status"], timeline.STATUS_APPLICABLE)

    def test_legacy_gpai_model(self):
        r = status_of("CAL-006", "2026-10-27", "2025-06-01")
        self.assertEqual(r["status"], timeline.STATUS_FUTURE)
        self.assertEqual(r["effective_date"], "2027-08-02")

    def test_new_gpai_model(self):
        self.assertEqual(status_of("CAL-006", "2026-10-27", "2025-09-01")["status"], timeline.STATUS_APPLICABLE)

    def test_unknown_date_entry(self):
        self.assertEqual(status_of("CAL-016", "2026-10-27")["status"], timeline.STATUS_UNKNOWN)

    def test_cli_runs(self):
        out = subprocess.run([sys.executable, str(ROOT / "scripts" / "obligation_timeline.py"),
                              "--audit-date", "2026-10-27", "--json"], capture_output=True, text=True, check=True)
        data = json.loads(out.stdout)
        self.assertEqual(data["audit_date"], "2026-10-27")


class ScannerFixtureTests(unittest.TestCase):
    """Détection des signaux : faux positifs et faux négatifs sur les fixtures."""

    @classmethod
    def setUpClass(cls):
        # EXPECTED.md est l'oracle du test : il est exclu de l'analyse comme il le serait d'un audit réel.
        cls.reports = {name: scanner.scan(FIXTURES / name, exclude=["EXPECTED.md"]) for name in
                       ("demo-ai-vulnerable", "demo-ai-secure", "demo-no-ai", "demo-insufficient-info")}

    def test_vulnerable_detects_expected_signals(self):
        r = self.reports["demo-ai-vulnerable"]
        self.assertTrue(r["ai_signals_detected"])
        self.assertIn("openai", r["summary"]["provider_api"])
        self.assertIn("image-generation", r["summary"]["media_generation"])
        self.assertIn("face-recognition", r["summary"]["biometric"])
        self.assertIn("emotion-inference", r["summary"]["sensitive_context"])
        self.assertIn("education", r["summary"]["sensitive_context"])
        self.assertNotIn("transparency_marker", r["summary"])
        self.assertNotIn("oversight_marker", r["summary"])
        self.assertEqual([s["file"] for s in r["possible_secrets"]], ["app/config.py"])

    def test_secret_is_masked(self):
        report = self.reports["demo-ai-vulnerable"]
        rendered = json.dumps(report, ensure_ascii=False) + scanner.to_markdown(report)
        self.assertNotIn("sk-FAKE-demo-key", rendered)
        self.assertIn(scanner.MASK, rendered)

    def test_secure_detects_measures_without_biometrics(self):
        r = self.reports["demo-ai-secure"]
        self.assertTrue(r["ai_signals_detected"])
        self.assertIn("anthropic", r["summary"]["provider_api"])
        self.assertIn("transparency_marker", r["summary"])
        self.assertIn("content-provenance", r["summary"]["transparency_marker"])
        self.assertIn("oversight_marker", r["summary"])
        self.assertIn("logging_marker", r["summary"])
        self.assertNotIn("biometric", r["summary"])
        self.assertEqual(r["possible_secrets"], [])

    def test_no_ai_project_has_no_ai_signal(self):
        r = self.reports["demo-no-ai"]
        self.assertFalse(r["ai_signals_detected"], r["summary"])
        for category in scanner.AI_CATEGORIES:
            self.assertNotIn(category, r["summary"])

    def test_insufficient_info_detects_classic_ml(self):
        r = self.reports["demo-insufficient-info"]
        self.assertTrue(r["ai_signals_detected"])
        self.assertIn("scikit-learn", r["summary"]["classic_ml"])
        self.assertIn("employment", r["summary"]["sensitive_context"])
        self.assertNotIn("provider_api", r["summary"])

    def test_scanner_is_read_only(self):
        before = {p: p.stat().st_mtime_ns for p in FIXTURES.rglob("*") if p.is_file()}
        for name in self.reports:
            scanner.scan(FIXTURES / name)
        after = {p: p.stat().st_mtime_ns for p in FIXTURES.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


class ExampleReportTests(unittest.TestCase):
    def test_findings_have_all_fields(self):
        text = (ROOT / "examples" / "example-audit.md").read_text(encoding="utf-8")
        blocks = re.split(r"\n(?=### AIA-\d{3} )", text)
        findings = [b for b in blocks if re.match(r"### AIA-\d{3} ", b)]
        self.assertGreaterEqual(len(findings), 5)
        ids = [re.match(r"### (AIA-\d{3})", b).group(1) for b in findings]
        self.assertEqual(len(ids), len(set(ids)))
        for block in findings:
            for field in FINDING_FIELDS:
                self.assertIn(f"**{field}**", block, f"{block.splitlines()[0]} : champ « {field} » manquant")
            nature = re.search(r"\*\*Nature du constat\*\* : ([^(\n]+)", block).group(1).strip()
            self.assertIn(nature, NATURES, f"{block.splitlines()[0]} : nature inconnue « {nature} »")

    def test_example_masks_secret(self):
        text = (ROOT / "examples" / "example-audit.md").read_text(encoding="utf-8")
        self.assertNotIn("sk-FAKE", text)

    def test_template_has_all_fields(self):
        text = (ROOT / "templates" / "audit-report.md").read_text(encoding="utf-8")
        for field in FINDING_FIELDS:
            self.assertIn(f"**{field}**", text)


class ExpectedFilesTests(unittest.TestCase):
    def test_expected_files_have_required_sections(self):
        for name in ("demo-ai-vulnerable", "demo-ai-secure", "demo-no-ai", "demo-insufficient-info"):
            text = (FIXTURES / name / "EXPECTED.md").read_text(encoding="utf-8")
            for section in ("Constats attendus", "ne doivent pas apparaître", "Erreurs de classification"):
                self.assertIn(section, text, f"{name}/EXPECTED.md : section « {section} » absente")
            self.assertRegex(text, r"[Cc]onfiance")


if __name__ == "__main__":
    unittest.main(verbosity=2)
