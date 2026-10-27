#!/usr/bin/env python3
"""Rejoue la vérification du calendrier sur le texte officiel (lecture seule).

Télécharge depuis Cellar (Office des publications de l'UE) les documents listés dans
data/official-sources.json, compare leurs empreintes SHA-256 à celles enregistrées, puis vérifie
que chaque extrait cité dans data/ai-act-calendar.json (legal_basis.official_extracts) figure
mot pour mot dans le document correspondant. N'écrit aucun fichier.

Codes de sortie : 0 = tous les extraits retrouvés ; 1 = extrait introuvable ; 2 = échec réseau.
Une empreinte différente (nouvelle manifestation du document) est signalée sans faire échouer
la vérification : elle appelle une revue humaine.

Usage :
    python3 scripts/verify_official_extracts.py
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADERS = {"Accept": "application/xhtml+xml", "Accept-Language": "fra", "User-Agent": "ia-compliance-verify"}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):  # les redirections sont suivies à la main (http -> https)
        return None


def fetch(url: str, hops: int = 5) -> bytes:
    opener = urllib.request.build_opener(_NoRedirect)
    for _ in range(hops):
        try:
            with opener.open(urllib.request.Request(url, headers=HEADERS), timeout=120) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code in (301, 302, 303, 307, 308) and exc.headers.get("Location"):
                url = exc.headers["Location"].replace("http://", "https://", 1)
                continue
            raise
    raise RuntimeError(f"trop de redirections pour {url}")


def to_text(raw: bytes) -> str:
    text = raw.decode("utf-8", errors="replace")
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", text)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return re.sub(r"\s+", " ", text)


def main() -> int:
    sources = json.loads((ROOT / "data" / "official-sources.json").read_text(encoding="utf-8"))
    calendar = json.loads((ROOT / "data" / "ai-act-calendar.json").read_text(encoding="utf-8"))
    texts: dict[str, str] = {}
    try:
        for doc in sources["documents"]:
            raw = fetch(doc["resolver"])
            digest = hashlib.sha256(raw).hexdigest()
            status = "identique" if digest == doc["sha256"] else "DIFFÉRENTE (revue humaine requise)"
            print(f"{doc['celex']} : {len(raw)} octets, empreinte {status}")
            texts[doc["eurlex"]] = to_text(raw)
    except Exception as exc:  # réseau, service indisponible
        print(f"Échec de la récupération : {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    missing = 0
    checked = 0
    for entry in calendar["entries"]:
        for extract in entry["legal_basis"].get("official_extracts", []):
            haystack = texts.get(extract["source_url"])
            if haystack is None:
                print(f"{entry['id']} : source non couverte ({extract['source_url']})")
                missing += 1
                continue
            checked += 1
            if re.sub(r"\s+", " ", extract["text"]) not in haystack:
                print(f"{entry['id']} : EXTRAIT INTROUVABLE : {extract['text'][:80]}...")
                missing += 1
    print(f"{checked} extraits vérifiés, {missing} introuvable(s).")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
