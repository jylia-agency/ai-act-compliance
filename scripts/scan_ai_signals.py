#!/usr/bin/env python3
"""Repère, en lecture seule, les signaux d'utilisation de l'IA dans un dépôt.

Ce script ne fait qu'un inventaire de signaux observables (imports, dépendances,
identifiants de modèles, marqueurs de transparence, de supervision et de
journalisation). Un signal n'est JAMAIS une classification réglementaire :
la qualification au sens de l'AI Act exige l'analyse de la finalité, des
utilisateurs, des personnes concernées et du contexte (voir SKILL.md).

Garanties de conception :
- aucun fichier n'est modifié, créé ou supprimé ;
- aucun appel réseau, aucune exécution du code analysé ;
- les valeurs ressemblant à des secrets sont masquées dans la sortie.

Usage :
    python3 scripts/scan_ai_signals.py CHEMIN_DU_PROJET [--json] [--max-hits 400]
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

SKIP_DIRS = {
    ".git", "node_modules", ".venv", "venv", "env", "__pycache__", "dist", "build",
    ".next", ".nuxt", "target", ".tox", ".mypy_cache", ".pytest_cache", "vendor",
    ".idea", ".vscode", "coverage", ".terraform",
}
TEXT_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".java", ".kt", ".go", ".rb",
    ".php", ".cs", ".rs", ".swift", ".scala", ".ipynb", ".json", ".yaml", ".yml",
    ".toml", ".cfg", ".ini", ".txt", ".md", ".env", ".html", ".vue", ".svelte", ".sql",
    ".sh", ".dockerfile", ".tf",
}
MANIFEST_NAMES = {
    "requirements.txt", "pyproject.toml", "Pipfile", "setup.py", "setup.cfg",
    "package.json", "go.mod", "Gemfile", "composer.json", "pom.xml", "build.gradle",
    "Dockerfile", "docker-compose.yml", "docker-compose.yaml", ".env.example",
}
MAX_FILE_BYTES = 1_000_000

# Catégories « IA » : leur présence indique qu'un composant d'IA est probablement utilisé.
AI_CATEGORIES = {
    "provider_api", "local_model", "classic_ml", "orchestration_agent",
    "rag_vector", "media_generation", "biometric", "model_identifier",
}

PATTERNS: dict[str, list[tuple[str, str]]] = {
    "provider_api": [
        ("openai", r"\b(import openai|from openai\b|require\(['\"]openai['\"]\)|from ['\"]openai['\"]|^openai[=<>~ ]|\"openai\"\s*:)"),
        ("anthropic", r"(\bimport anthropic\b|\bfrom anthropic\b|@anthropic-ai/sdk|^anthropic[=<>~ ])"),
        ("google-genai", r"(google\.generativeai|from google import genai|google-genai|@google/generative-ai|@google/genai|vertexai)"),
        ("mistral", r"(\bmistralai\b|@mistralai/)"),
        ("cohere", r"(\bimport cohere\b|\bfrom cohere\b|cohere-ai)"),
        ("aws-bedrock", r"bedrock-runtime"),
        ("azure-openai", r"(AzureOpenAI|azure\.ai\.openai|@azure/openai)"),
        ("huggingface-inference", r"(InferenceClient|api-inference\.huggingface\.co)"),
        ("replicate", r"(\bimport replicate\b|\breplicate\.run\(|\"replicate\"\s*:)"),
        ("vercel-ai-sdk", r"(@ai-sdk/|from ['\"]ai['\"])"),
        ("groq-together", r"(\bfrom groq\b|\bimport groq\b|\btogether\b\s*import|from together\b)"),
        ("elevenlabs", r"\belevenlabs\b"),
    ],
    "local_model": [
        ("transformers", r"(\bfrom transformers\b|\bimport transformers\b|^transformers[=<>~ ])"),
        ("pytorch", r"(\bimport torch\b|^torch[=<>~ ])"),
        ("tensorflow-keras", r"(\bimport tensorflow\b|\bfrom tensorflow\b|\bimport keras\b|\bfrom keras\b)"),
        ("onnx", r"\bonnxruntime\b"),
        ("llama-cpp", r"\bllama_cpp\b|llama-cpp-python"),
        ("ollama", r"\bollama\b"),
        ("vllm", r"\bvllm\b"),
        ("sentence-transformers", r"sentence_transformers|sentence-transformers"),
        ("whisper", r"(\bimport whisper\b|faster_whisper|openai-whisper)"),
    ],
    "classic_ml": [
        ("scikit-learn", r"(\bfrom sklearn\b|\bimport sklearn\b|scikit-learn)"),
        ("gradient-boosting", r"\b(xgboost|lightgbm|catboost)\b"),
        ("serialized-model", r"(joblib\.load|pickle\.load|\.pkl['\"]|\.joblib['\"]|\.onnx['\"]|\.safetensors['\"])"),
    ],
    "orchestration_agent": [
        ("langchain", r"\blangchain\b|@langchain/"),
        ("llamaindex", r"\bllama_index\b|llamaindex"),
        ("agents-frameworks", r"\b(crewai|autogen|semantic_kernel|haystack|langgraph|smolagents)\b"),
        ("tool-calling", r"(\btools\s*=\s*\[|tool_choice|function_call|\"type\"\s*:\s*\"function\")"),
        ("mcp", r"(\bmcp\.server\b|modelcontextprotocol|from mcp\b)"),
    ],
    "rag_vector": [
        ("vector-db", r"\b(chromadb|pinecone|weaviate|qdrant_client|qdrant|faiss|pgvector|milvus|lancedb)\b"),
        ("embeddings", r"(embeddings\.create|\bembed_documents\b|text-embedding-|\bget_embedding\b)"),
    ],
    "media_generation": [
        ("image-generation", r"(images\.generate|dall-e|gpt-image|stable[-_ ]diffusion|\bdiffusers\b|imagen|midjourney)"),
        ("audio-generation", r"(audio\.speech|text_to_speech|\btts\b|voice_clon)"),
        ("video-generation", r"\b(sora|runwayml|video_generation|veo)\b"),
    ],
    "biometric": [
        ("face-recognition", r"(face_recognition|\bdeepface\b|DeepFace|insightface|\bdlib\b|haarcascade_frontalface|FaceMesh|face_detection)"),
        ("emotion-library", r"(facial_expression|affect_recognition|\bhsemotion\b|emotion_model|EmotionRecognizer)"),
        ("voice-biometrics", r"(speaker_verification|voiceprint|speaker_recognition)"),
    ],
    "model_identifier": [
        ("model-name", r"(['\"](gpt-[0-9][\w.\-]*|gpt-4o[\w.\-]*|o[134](-mini)?|claude-[\w.\-]+|gemini-[\w.\-]+|mistral-[\w.\-]+|llama-?[0-9][\w.\-]*|mixtral[\w.\-]*|dall-e-[0-9]|whisper-[0-9][\w\-]*)['\"])"),
    ],
    "credentials_reference": [
        ("ai-api-key-env", r"\b(OPENAI_API_KEY|ANTHROPIC_API_KEY|GOOGLE_API_KEY|GEMINI_API_KEY|MISTRAL_API_KEY|COHERE_API_KEY|HF_TOKEN|HUGGINGFACEHUB_API_TOKEN|REPLICATE_API_TOKEN|ELEVENLABS_API_KEY)\b"),
    ],
    "sensitive_context": [
        ("education", r"(\bgrade\b|\bgrading\b|\bnotation\b|\bnote finale\b|\bexam\b|\bexamen\b|proctor|surveillance d'examen|\badmission\b|\bstudent\b|étudiant|élève|apprenant|copies? d'examen|correction de copies)"),
        ("employment", r"(\brecruit|recrutement|\bhiring\b|\bcandidate|candidat|\bresume\b|\bcv\b|\bemployee\b|salarié|performance review|licenciement)"),
        ("essential-services", r"(credit[_ ]?scor|creditworth|solvabilit|\bloan\b|\bprêt\b|insurance|assurance vie|assurance santé|prestation sociale|\bbenefits? eligibility)"),
        ("health", r"(\bpatient\b|diagnos|\btriage\b|medical|médical)"),
        ("law-enforcement-migration-justice", r"(\bpolice\b|recidiv|récidiv|\bcriminal\b|asylum|\basile\b|border control|tribunal|\bjudge\b|élection|election|\bvoter?\b)"),
        ("person-scoring", r"(\brisk_score\b|\btrust_score\b|social[_ ]scor|\bscoring\b|\brank_candidates\b|profiling|profilage)"),
        ("emotion-inference", r"(\bemotions?\b|émotions?|\bstress\b|anxiété|anxiety|attention_score)"),
    ],
    "transparency_marker": [
        ("ai-disclosure", r"(généré par (l'|une )?ia|genere par ia|ai[- ]generated|generated (by|with) ai|contenu généré|assistant (d'|virtuel )?ia|vous (échangez|discutez|parlez) avec|you are (talking|chatting) (to|with) an ai|ai_disclosure|AI_DISCLOSURE)"),
        ("content-provenance", r"(c2pa|content[_ ]credentials|synthid|watermark|filigrane|trainedAlgorithmicMedia|DigitalSourceType|iptc)"),
    ],
    "oversight_marker": [
        ("human-review", r"(human[_ ]review|validation humaine|revue humaine|manual[_ ]review|requires_review|pending_review|needs_review|approve[d]?_by|reviewer_id|validated_by|override|annuler la décision|kill[_ ]switch)"),
    ],
    "logging_marker": [
        ("traceability", r"(audit_log|audit log|journal d'audit|model_version|prompt_version|inference_log|log_inference|retention_days|conservation des journaux|trace_id)"),
    ],
}

SECRET_PATTERNS = [
    re.compile(r"(?<![A-Za-z0-9])sk-ant-[A-Za-z0-9_\-]{8,}"),
    re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_\-]{8,}"),
    re.compile(r"(?<![A-Za-z0-9])AIza[0-9A-Za-z_\-]{20,}"),
    re.compile(r"(?<![A-Za-z0-9])hf_[A-Za-z0-9]{20,}"),
    re.compile(r"(?<![A-Za-z0-9])r8_[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"),
    re.compile(r"(?i)((api[_-]?key|secret|token|password|passwd)\s*[:=]\s*)(['\"])[^'\"\s]{6,}\3"),
]
MASK = "[SECRET MASQUÉ]"

COMPILED = {
    category: [(name, re.compile(rx, re.IGNORECASE | re.MULTILINE)) for name, rx in rules]
    for category, rules in PATTERNS.items()
}


def mask_secrets(text: str) -> tuple[str, bool]:
    found = False
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            found = True
            if pattern.groups >= 3:
                text = pattern.sub(lambda m: m.group(1) + m.group(3) + MASK + m.group(3), text)
            else:
                text = pattern.sub(MASK, text)
    return text, found


def iter_files(root: Path, exclude: list[str] | None = None):
    exclude = exclude or []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            path = Path(dirpath) / name
            rel = path.relative_to(root).as_posix()
            if any(fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(name, pat) for pat in exclude):
                continue
            if name in MANIFEST_NAMES or path.suffix.lower() in TEXT_EXTENSIONS or name.startswith(".env"):
                try:
                    if path.stat().st_size > MAX_FILE_BYTES:
                        continue
                except OSError:
                    continue
                yield path


def scan(root: Path, max_hits: int = 400, exclude: list[str] | None = None) -> dict:
    root = root.resolve()
    hits: list[dict] = []
    summary: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    files_by_category: dict[str, set] = defaultdict(set)
    secret_locations: list[dict] = []
    files_scanned = 0

    for path in iter_files(root, exclude):
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        files_scanned += 1
        rel = path.relative_to(root).as_posix()
        for lineno, line in enumerate(content.splitlines(), start=1):
            masked, has_secret = mask_secrets(line)
            if has_secret:
                secret_locations.append({"file": rel, "line": lineno})
            for category, rules in COMPILED.items():
                for name, rx in rules:
                    if rx.search(line):
                        summary[category][name] += 1
                        files_by_category[category].add(rel)
                        if len(hits) < max_hits:
                            hits.append({
                                "category": category,
                                "signal": name,
                                "file": rel,
                                "line": lineno,
                                "excerpt": masked.strip()[:160],
                            })

    ai_detected = any(cat in summary for cat in AI_CATEGORIES)
    return {
        "root": root.name,
        "files_scanned": files_scanned,
        "ai_signals_detected": ai_detected,
        "summary": {cat: dict(sig) for cat, sig in sorted(summary.items())},
        "files_by_category": {cat: sorted(files) for cat, files in sorted(files_by_category.items())},
        "possible_secrets": secret_locations,
        "hits": hits,
        "hits_truncated": sum(sum(s.values()) for s in summary.values()) > len(hits),
        "disclaimer": (
            "Signaux techniques uniquement. Ils ne constituent ni une identification certaine d'un "
            "système d'IA au sens de l'article 3, point 1, ni une classification réglementaire."
        ),
    }


def to_markdown(report: dict) -> str:
    out = [
        f"# Signaux IA : {report['root']}",
        "",
        f"Fichiers analysés : {report['files_scanned']}",
        f"Signaux d'IA détectés : {'oui' if report['ai_signals_detected'] else 'non'}",
        "",
        "## Synthèse par catégorie",
        "",
        "| Catégorie | Signal | Occurrences | Fichiers |",
        "|---|---|---|---|",
    ]
    for cat, signals in report["summary"].items():
        files = ", ".join(report["files_by_category"].get(cat, [])[:5])
        for sig, count in sorted(signals.items()):
            out.append(f"| {cat} | {sig} | {count} | {files} |")
    if report["possible_secrets"]:
        out += ["", "## Secrets potentiels (valeurs masquées)", ""]
        out += [f"- {s['file']}:{s['line']}" for s in report["possible_secrets"]]
    out += ["", "## Occurrences", "", "| Fichier:ligne | Catégorie | Signal | Extrait (masqué) |", "|---|---|---|---|"]
    for h in report["hits"]:
        excerpt = h["excerpt"].replace("|", "\\|")
        out.append(f"| {h['file']}:{h['line']} | {h['category']} | {h['signal']} | `{excerpt}` |")
    if report["hits_truncated"]:
        out.append("\nListe tronquée : augmenter --max-hits pour tout afficher.")
    out += ["", f"> {report['disclaimer']}"]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inventaire en lecture seule des signaux d'IA d'un dépôt.")
    parser.add_argument("path", help="Racine du projet à analyser")
    parser.add_argument("--json", action="store_true", help="Sortie JSON")
    parser.add_argument("--max-hits", type=int, default=400)
    parser.add_argument("--exclude", action="append", default=[],
                        help="Motif glob de fichiers à ignorer (répétable), par exemple --exclude 'docs/*'")
    args = parser.parse_args(argv)

    root = Path(args.path)
    if not root.is_dir():
        print(f"Répertoire introuvable : {root}", file=sys.stderr)
        return 2
    report = scan(root, args.max_hits, args.exclude)
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else to_markdown(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
