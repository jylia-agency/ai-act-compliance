"""Classement des candidats à partir d'un modèle entraîné."""
import joblib
import pandas as pd

FEATURES = ["experience_years", "test_score", "age", "distance_km", "previous_applications"]

model = joblib.load("models/ranker.joblib")  # GradientBoostingClassifier (sklearn)


def rank_candidates(df: pd.DataFrame, top_n: int = 20) -> pd.DataFrame:
    df = df.copy()
    df["probability"] = model.predict_proba(df[FEATURES])[:, 1]
    return df.sort_values("probability", ascending=False).head(top_n)
