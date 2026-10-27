"""Ajout d'un manifeste C2PA (content credentials) via l'outil de signature interne."""
from pathlib import Path


def attach_c2pa_manifest(path: Path, generator: str) -> None:
    raise NotImplementedError("Signature C2PA effectuée par l'outil interne en production.")
