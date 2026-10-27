"""Génération d'illustrations de cours publiées aux élèves."""
import base64
from pathlib import Path

from openai import OpenAI

from app.config import IMAGE_MODEL, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def create_illustration(prompt: str, output: Path) -> Path:
    result = client.images.generate(model=IMAGE_MODEL, prompt=prompt, response_format="b64_json")
    output.write_bytes(base64.b64decode(result.data[0].b64_json))
    return output  # image enregistrée telle quelle, sans métadonnées ni mention
