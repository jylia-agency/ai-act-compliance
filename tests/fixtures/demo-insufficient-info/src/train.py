"""Entraînement du modèle de classement (données non fournies dans le dépôt)."""
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

from src.rank import FEATURES


def train(csv_path: str) -> None:
    data = pd.read_csv(csv_path)
    clf = GradientBoostingClassifier(random_state=0)
    clf.fit(data[FEATURES], data["selected"])
    joblib.dump(clf, "models/ranker.joblib")
