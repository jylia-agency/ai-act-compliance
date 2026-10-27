# EduAssist (version vulnérable, projet fictif de test)

> Projet **fictif** servant de fixture de test au skill `ia-compliance`. Il contient
> volontairement des défauts. Ne pas déployer. Aucune clé réelle n'est présente.

## Contexte déclaré par l'éditeur (fictif)

- Éditeur : société fictive « EduAssist SAS », établie en France.
- Produit commercialisé sous la marque « EduAssist » auprès de lycées et d'universités de l'Union.
- Date de mise sur le marché de la plateforme et de tous ses modules : **1er mars 2026**.
- Les établissements clients utilisent la plateforme pour leurs propres élèves et étudiants.
- Modèles utilisés : API d'un fournisseur tiers de modèles (OpenAI). EduAssist n'entraîne aucun modèle.

## Modules

| Module | Fichier | Description fonctionnelle |
|---|---|---|
| Tuteur conversationnel | `app/tutor_chat.py` | Répond aux questions des élèves sur les cours. |
| Correction automatique | `app/grading.py` | Attribue la note finale des dissertations, publiée directement dans le bulletin. |
| Illustrations de cours | `app/illustrations.py` | Génère des images pour les supports de cours publiés aux élèves. |
| Surveillance d'examens en ligne | `app/proctoring.py` | Analyse la webcam pendant les examens et annule automatiquement les copies jugées suspectes. |

Aucune documentation technique, procédure de supervision ou politique de journalisation n'est fournie.
