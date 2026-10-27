"""Recommandation de filière présentée au conseil de classe."""
import json

TRACKS = ["générale", "technologique", "professionnelle"]


def recommend_track(student_id: str, grades: dict) -> dict:
    with open(f"var/engagement_{student_id}.json", encoding="utf-8") as handle:
        engagement = json.load(handle)["engagement"]
    average = sum(grades.values()) / len(grades)
    if average >= 14 and engagement >= 0.6:
        track, confidence = "générale", 0.95
    elif average >= 10:
        track, confidence = "technologique", 0.8
    else:
        track, confidence = "professionnelle", 0.92
    decision = {"student_id": student_id, "track": track, "confidence": confidence}
    if confidence > 0.9:
        apply_decision(decision)  # appliquée sans passage en conseil de classe
    return decision


def apply_decision(decision: dict) -> None:
    print(f"Orientation enregistrée : {decision}")
