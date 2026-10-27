"""Surveillance des examens en ligne par analyse de la webcam."""
import cv2
from deepface import DeepFace

SUSPICIOUS_EMOTIONS = {"fear", "angry", "surprise"}


def analyse_frame(frame) -> dict:
    result = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)[0]
    return {"dominant_emotion": result["dominant_emotion"], "scores": result["emotion"]}


def monitor_exam(video_path: str, exam_id: str, student_id: str) -> str:
    capture = cv2.VideoCapture(video_path)
    suspicious = 0
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        if analyse_frame(frame)["dominant_emotion"] in SUSPICIOUS_EMOTIONS:
            suspicious += 1
    if suspicious > 30:
        cancel_exam(exam_id, student_id)  # annulation automatique, sans intervention humaine
        return "annulé"
    return "validé"


def cancel_exam(exam_id: str, student_id: str) -> None:
    print(f"Examen {exam_id} annulé pour {student_id}")
