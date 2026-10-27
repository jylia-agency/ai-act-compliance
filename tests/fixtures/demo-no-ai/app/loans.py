"""Règles de prêt : calcul déterministe, aucune inférence."""
from datetime import date, timedelta

LOAN_DAYS = 21


def predict_due_date(start: date, renewals: int = 0) -> date:
    """« Prédit » la date de retour par simple addition de jours."""
    return start + timedelta(days=LOAN_DAYS * (1 + renewals))


def loyalty_score(loans_count: int, late_returns: int) -> int:
    """Points de fidélité : règle fixe affichée aux lecteurs."""
    return max(0, loans_count * 10 - late_returns * 5)
