"""Assistant de révision conversationnel."""
import json
import os

from mistralai import Mistral

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY", ""))
MODEL = "mistral-large-latest"

BANNER = "Assistant de révision"  # pas de mention d'IA dans l'interface


def chat(student_id: str, message: str, history: list[dict]) -> dict:
    response = client.chat.complete(model=MODEL, messages=[*history, {"role": "user", "content": message}])
    text = response.choices[0].message.content
    engagement = score_engagement(history + [{"role": "user", "content": message}])
    store_engagement(student_id, engagement)  # réutilisé par app/orientation.py
    # Marquage : simple champ JSON non signé, ajouté uniquement à la réponse de l'API.
    return {"answer": text, "meta": {"ai_generated": "true"}}


def score_engagement(messages: list[dict]) -> float:
    """Score d'engagement de l'élève déduit par le modèle à partir de ses messages."""
    prompt = "Évalue de 0 à 1 la motivation et la persévérance de cet élève. Réponds par un nombre."
    response = client.chat.complete(model=MODEL, messages=[{"role": "system", "content": prompt}, *messages])
    return float(response.choices[0].message.content)


def store_engagement(student_id: str, value: float) -> None:
    with open(f"var/engagement_{student_id}.json", "w", encoding="utf-8") as handle:
        json.dump({"engagement": value}, handle)
