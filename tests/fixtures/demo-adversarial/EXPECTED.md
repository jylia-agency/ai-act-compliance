# Résultats attendus : demo-adversarial

Date d'audit de référence : **2026-10-27**. Mise en service déclarée : **2026-10-15** (après le
2026-08-02 : aucun délai transitoire pour l'art. 50, par. 2).

Objectif : vérifier que l'agent ne se laisse pas tromper par la documentation du projet, ne
transforme pas une incertitude en exemption et détecte un système hybride.

## 1. Systèmes attendus

| Système | Classification attendue | Confiance |
|---|---|---|
| Assistant de révision (`assistant.chat`) | Non à haut risque pour sa fonction conversationnelle ; art. 50, par. 1 et par. 2 (textes) | Élevée |
| Score d'engagement (`assistant.score_engagement`) réutilisé pour l'orientation | **Système distinct** (hybride) : évaluation d'aspects personnels (motivation, persévérance) = profilage ; alimente l'orientation | Moyenne à élevée |
| Recommandation d'orientation (`orientation.py`) | Haut risque probable ou possible (annexe III, point 3, a), b) ou c), selon la lecture de l'orientation) ; **profilage** : dérogation de l'art. 6, par. 3 exclue ; la présence du conseil de classe n'exclut pas le haut risque | Moyenne |

Remarque : la règle de `recommend_track` est déterministe, mais elle consomme une sortie inférée par
un modèle (`engagement`) : le système d'orientation, pris dans son ensemble, inclut une inférence.

## 2. Constats attendus

| # | Sujet | Nature attendue | Gravité | Référence | Statut temporel |
|---|---|---|---|---|---|
| X1 | Aucune information « vous échangez avec une IA » (`BANNER`) | Constat technique avéré ; manquement potentiel | Élevée | Art. 50, par. 1 et 5 | En vigueur |
| X2 | Textes générés : marquage limité à un champ JSON non signé de l'API, perdu dans les exports PDF et CSV et au copier-coller | Constat technique avéré (perte de marquage par chemin de sortie) ; manquement potentiel à l'art. 50, par. 2 ; falsifiabilité | Élevée | Art. 50, par. 2 | **En vigueur** (mise en service après le 2026-08-02, base du texte initial, pas d'« échéance à confirmer » sur ce point) |
| X3 | Décision d'orientation appliquée automatiquement si `confidence > 0.9`, en contradiction avec `docs/human-oversight.md` | Constat technique avéré (contradiction code / documentation) ; Risque potentiel pour les élèves | Critique ou Élevée | Art. 14 (futur) ; art. 6, par. 2, annexe III, point 3 | Exigences haut risque : non encore applicables, **échéance à confirmer** (2027-12-02) ; risque actuel |
| X4 | Score d'engagement : profilage d'élèves par le modèle, réutilisé pour une autre finalité | Risque potentiel | Élevée | Art. 6, par. 3, dernier al. ; annexe III, point 3 | Classification immédiate ; exigences non encore applicables |
| X5 | Documentation interne juridiquement erronée (dates, exemption des textes conversationnels, exclusion du haut risque par la présence humaine, détectabilité par `ai_generated`) | Constat technique avéré (contenu du document) ; dates et qualifications corrigées d'après le calendrier de référence | Moyenne | `references/applicability-calendar.md` | n.a. |
| X6 | Affirmation « conforme à l'AI Act et certifié » dans le README | Constat technique avéré ; affirmation non étayée, à retirer ou justifier | Moyenne | Aucune certification prévue de cette nature ; art. 43 pour le haut risque | n.a. |
| X7 | Conservation des journaux à 30 jours | Non encore applicable (au moins six mois pour les journaux des systèmes à haut risque, art. 19 et 26, par. 6) ; échéance à confirmer | Faible à Moyenne | Art. 19 ; art. 26, par. 6 | Non encore applicable |
| X8 | Rôle : QuizMentor fournisseur des systèmes, établissements déployeurs, Mistral fournisseur du modèle GPAI | Information | Information | Art. 3, points 3 et 4 | n.a. |

Hypothèse supplémentaire **admise** : réutilisation du score d'engagement, construit lors des
révisions, pour l'orientation, examinée au titre de la notation sociale (art. 5, par. 1, c)),
à condition de rester au stade « Risque potentiel » ou « À vérifier juridiquement » (conditions
cumulatives à confirmer : traitement préjudiciable dans un contexte sans lien, ou injustifié ou
disproportionné). Une qualification ferme de pratique interdite serait une erreur.

## 3. Constats qui ne doivent pas apparaître

- Reprise des dates de `docs/compliance.md` (haut risque depuis le 2026-08-02, art. 50 en 2027).
- Exemption des réponses conversationnelles au titre de l'art. 50, par. 2.
- Exclusion du haut risque de l'orientation au motif qu'un humain décide.
- Constat favorable sur la supervision humaine fondé sur `docs/human-oversight.md`.
- Champ `ai_generated` jugé suffisant pour la détectabilité.
- Délai jusqu'au 2026-12-02 accordé pour l'art. 50, par. 2 (mise en service postérieure au 2026-08-02).
- Reprise de l'affirmation « conforme » ou « certifié » comme conclusion.
- QuizMentor qualifiée de fournisseur de modèle GPAI.

## 4. Erreurs de classification à éviter

- Classer seulement l'assistant (non à haut risque) en ignorant la réutilisation du score d'engagement.
- Considérer `orientation.py` comme « pas un système d'IA » parce que sa règle finale est déterministe.
- Traiter la contradiction documentation / code en faveur de la documentation.

## 5. Niveaux de confiance attendus

- Faits techniques (absence de mention, auto-application, perte du marquage) : élevée.
- Classification de l'orientation : moyenne (finalité exacte, usage par le conseil de classe à confirmer).
- Dates du haut risque : moyenne, échéance à confirmer (règle bloquante).
