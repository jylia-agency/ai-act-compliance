"""Adaptateur vers le service tiers de génération d'images (non inclus dans la fixture)."""
from PIL import Image


def generate_image(prompt: str) -> tuple[Image.Image, str]:
    raise NotImplementedError("Appel au service de génération d'images configuré en production.")
