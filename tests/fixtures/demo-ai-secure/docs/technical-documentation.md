# Documentation technique (ébauche, EduAssist, fictif)

## Description générale
Plateforme pédagogique comprenant trois systèmes d'IA (voir ai-system-inventory.md).

## Architecture
API FastAPI ; appels au fournisseur de modèles via SDK officiel ; journal d'audit JSONL
append-only (`app/audit_log.py`) ; secrets fournis par variables d'environnement.

## Modèles et versions
- Identifiant de modèle configurable (`EDUASSIST_TUTOR_MODEL`, `EDUASSIST_GRADING_MODEL`).
- La version effectivement servie (`response.model`) est journalisée pour chaque appel.
- Version de la grille d'évaluation : `PROMPT_VERSION` (actuellement `grading-rubric-v3`).

## Validation et performances (SYS-02)
- Jeu d'évaluation interne de 400 copies notées par deux enseignants ; écart moyen constaté
  1,4 point sur 20 ; écart supérieur à 3 points sur 7 % des copies (campagne de septembre 2026).
- Limites connues : performances non mesurées sur les copies manuscrites numérisées et sur les
  élèves allophones ; risque de biais lié au style rédactionnel non évalué.

## Gestion des modifications
Tout changement de modèle ou de grille donne lieu à une nouvelle campagne d'évaluation avant
mise en production et à une entrée dans le CHANGELOG interne.

## Conservation
Journaux d'audit conservés 400 jours (`AUDIT_LOG_RETENTION_DAYS`).
