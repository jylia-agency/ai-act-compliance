"""Correction automatique des dissertations.

La note produite par le modèle est la note finale : elle est écrite directement
dans le bulletin de l'élève et compte pour le passage en classe supérieure.
"""
import json

from openai import OpenAI

from app.config import DEFAULT_MODEL, OPENAI_API_KEY
from app.gradebook import publish_grade

client = OpenAI(api_key=OPENAI_API_KEY)

RUBRIC = "Note sur 20 : argumentation 8, maîtrise de la langue 6, culture 6."


def grade_essay(student_id: str, essay: str) -> float:
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        temperature=1.0,
        messages=[
            {"role": "system", "content": f"Corrige la copie. {RUBRIC} Réponds en JSON {{\"note\": x}}."},
            {"role": "user", "content": essay},
        ],
    )
    grade = json.loads(response.choices[0].message.content)["note"]
    publish_grade(student_id, grade)  # publication immédiate, sans relecture
    return grade
