"""Journalisation d'événements techniques pendant les examens en ligne.

Aucun traitement d'IA : les événements (perte de focus de la fenêtre, déconnexion)
sont transmis tels quels aux surveillants humains, qui seuls décident d'une suite.
"""
from app.audit_log import log_event


def record_event(exam_id: str, student_id: str, event: str) -> None:
    log_event("exam_event", exam_id=exam_id, student_id=student_id, detail=event)
