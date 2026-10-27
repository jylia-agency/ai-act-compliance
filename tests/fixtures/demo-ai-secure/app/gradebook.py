"""Accès simplifié au bulletin (stockage en mémoire pour la fixture)."""
_GRADES: dict[str, list[dict]] = {}


def publish_grade(student_id: str, grade: float, validated_by: str) -> None:
    if not validated_by:
        raise PermissionError("Publication refusée : validation humaine requise.")
    _GRADES.setdefault(student_id, []).append({"grade": grade, "validated_by": validated_by})
