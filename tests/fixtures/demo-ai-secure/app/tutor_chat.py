"""Tuteur conversationnel proposé aux élèves."""
import anthropic

from app.audit_log import log_event
from app.config import ANTHROPIC_API_KEY, TUTOR_MODEL

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

AI_DISCLOSURE = (
    "Vous échangez avec un assistant d'IA (et non avec un enseignant). "
    "Ses réponses peuvent contenir des erreurs : vérifiez-les avec votre cours."
)
SYSTEM_PROMPT = (
    "Tu es l'assistant d'IA d'EduAssist. Si l'on te demande si tu es humain, "
    "réponds clairement que tu es une IA."
)


def start_session() -> str:
    """Message affiché avant la première interaction."""
    return AI_DISCLOSURE


def answer(student_message: str, history: list[dict]) -> str:
    response = client.messages.create(
        model=TUTOR_MODEL,
        max_tokens=800,
        system=SYSTEM_PROMPT,
        messages=[*history, {"role": "user", "content": student_message}],
    )
    log_event("tutor_answer", model_version=response.model)
    return response.content[0].text
