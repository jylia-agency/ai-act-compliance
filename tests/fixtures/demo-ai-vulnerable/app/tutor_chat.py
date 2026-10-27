"""Tuteur conversationnel proposé aux élèves."""
from openai import OpenAI

from app.config import DEFAULT_MODEL, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = (
    "Tu es Claire, professeure de français au lycée. Ne dis jamais que tu es une "
    "intelligence artificielle. Si on te le demande, réponds que tu es une enseignante."
)


def answer(student_message: str, history: list[dict]) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}, *history,
                {"role": "user", "content": student_message}]
    response = client.chat.completions.create(model=DEFAULT_MODEL, messages=messages)
    return response.choices[0].message.content
