"""Correction assistée : le modèle propose, l'enseignant décide.

Aucune note n'est publiée sans validation humaine explicite (voir
docs/human-oversight-procedure.md).
"""
import json
from dataclasses import dataclass, field

import anthropic

from app.audit_log import log_event
from app.config import ANTHROPIC_API_KEY, GRADING_MODEL, PROMPT_VERSION
from app.gradebook import publish_grade

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

RUBRIC = "Note sur 20 : argumentation 8, maîtrise de la langue 6, culture 6."


@dataclass
class GradeProposal:
    student_id: str
    proposed_grade: float
    rationale: str
    criteria: dict
    model_version: str
    prompt_version: str
    status: str = "pending_review"
    trace_id: str = ""
    history: list = field(default_factory=list)


def propose_grade(student_id: str, essay: str) -> GradeProposal:
    response = client.messages.create(
        model=GRADING_MODEL,
        max_tokens=1200,
        temperature=0,
        system=f"Propose une note argumentée. {RUBRIC} Réponds en JSON "
               "{\"note\": x, \"criteres\": {...}, \"justification\": \"...\"}.",
        messages=[{"role": "user", "content": essay}],
    )
    data = json.loads(response.content[0].text)
    proposal = GradeProposal(
        student_id=student_id,
        proposed_grade=data["note"],
        rationale=data["justification"],
        criteria=data["criteres"],
        model_version=response.model,
        prompt_version=PROMPT_VERSION,
    )
    proposal.trace_id = log_event(
        "grade_proposed", student_id=student_id, model_version=response.model,
        prompt_version=PROMPT_VERSION, proposed_grade=data["note"],
    )
    return proposal


def review_grade(proposal: GradeProposal, reviewer_id: str, decision: str,
                 final_grade: float | None = None, override_reason: str = "") -> GradeProposal:
    """Décision de l'enseignant : approve, override (avec motif) ou reject."""
    if decision == "override" and not override_reason:
        raise ValueError("Un motif est obligatoire pour modifier la note proposée.")
    grade = proposal.proposed_grade if decision == "approve" else final_grade
    proposal.status = {"approve": "approved", "override": "overridden", "reject": "rejected"}[decision]
    log_event("grade_reviewed", trace_id=proposal.trace_id, reviewer_id=reviewer_id,
              decision=decision, final_grade=grade, override_reason=override_reason)
    if proposal.status in {"approved", "overridden"}:
        publish_grade(proposal.student_id, grade, validated_by=reviewer_id)
    return proposal
