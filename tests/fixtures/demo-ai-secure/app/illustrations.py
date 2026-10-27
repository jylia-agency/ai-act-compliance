"""Génération d'illustrations de cours, marquées et étiquetées.

Mesures : métadonnées de provenance (XMP/IPTC DigitalSourceType
trainedAlgorithmicMedia), manifeste C2PA produit par l'outil de signature interne,
et mention visible « Image générée par IA » sur les supports publiés.
Limite connue : la robustesse du marquage aux recompressions n'a pas été testée.
"""
from pathlib import Path

from PIL import Image, PngImagePlugin

from app.audit_log import log_event
from app.c2pa_signer import attach_c2pa_manifest
from app.image_provider import generate_image

VISIBLE_LABEL = "Image générée par IA"
IPTC_DIGITAL_SOURCE_TYPE = "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"


def create_illustration(prompt: str, output: Path) -> Path:
    image, model_version = generate_image(prompt)
    meta = PngImagePlugin.PngInfo()
    meta.add_text("DigitalSourceType", IPTC_DIGITAL_SOURCE_TYPE)
    meta.add_text("ai_disclosure", VISIBLE_LABEL)
    meta.add_text("model_version", model_version)
    image.save(output, pnginfo=meta)
    attach_c2pa_manifest(output, generator=model_version)
    log_event("illustration_generated", model_version=model_version, file=str(output))
    return output
