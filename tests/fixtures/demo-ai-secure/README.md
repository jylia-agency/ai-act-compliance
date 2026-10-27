# EduAssist (version corrigée, projet fictif de test)

> Projet **fictif** servant de fixture de test au skill `ia-compliance`. Il illustre
> des mesures correctives et des éléments de preuve. Il ne constitue pas un modèle de
> conformité certifiée.

## Contexte déclaré par l'éditeur (fictif)

- Éditeur : société fictive « EduAssist SAS », établie en France.
- Produit commercialisé sous la marque « EduAssist » auprès de lycées et d'universités de l'Union.
- Tuteur conversationnel et correction assistée : mis sur le marché le **1er mars 2026**.
- Module d'illustrations : mis sur le marché le **15 septembre 2026** (nouveau module).
- Modèles utilisés : API d'un fournisseur tiers (Anthropic). EduAssist n'entraîne aucun modèle.
- La surveillance d'examens par analyse de webcam a été **supprimée** ; la surveillance est assurée par des surveillants humains. Le module `app/exam_events.py` ne contient aucun traitement d'IA.

## Modules

| Module | Fichier | Description fonctionnelle |
|---|---|---|
| Tuteur conversationnel | `app/tutor_chat.py` | Répond aux questions des élèves ; information explicite sur l'IA. |
| Correction assistée | `app/grading.py` | Propose une note et une justification ; l'enseignant valide, modifie ou rejette. |
| Illustrations de cours | `app/illustrations.py` | Génère des images marquées (métadonnées de provenance) et étiquetées. |
| Événements d'examen | `app/exam_events.py` | Journalise des événements techniques (perte de focus) pour les surveillants humains. Pas d'IA. |

## Documentation

Voir `docs/` : inventaire, analyse de classification, documentation technique, procédure de
supervision humaine, registre des risques, plan de maîtrise de l'IA.
