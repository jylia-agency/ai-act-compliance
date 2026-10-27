"""Exports des échanges et des synthèses."""
import csv

from reportlab.pdfgen import canvas


def export_pdf(path: str, answers: list[str]) -> None:
    pdf = canvas.Canvas(path)
    y = 800
    for answer in answers:
        pdf.drawString(40, y, answer[:110])
        y -= 20
    pdf.save()  # aucune métadonnée de provenance ni mention


def export_csv(path: str, rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["question", "answer"])
        writer.writeheader()
        writer.writerows(rows)  # le champ meta.ai_generated n'est pas exporté
