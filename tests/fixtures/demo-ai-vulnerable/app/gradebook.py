"""Accès simplifié au bulletin (stockage en mémoire pour la fixture)."""
_GRADES: dict[str, list[float]] = {}


def publish_grade(student_id: str, grade: float) -> None:
    _GRADES.setdefault(student_id, []).append(grade)
