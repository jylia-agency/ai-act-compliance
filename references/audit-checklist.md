# Checklists d'audit conditionnelles

> Dernière vérification : **2026-10-27**. Chaque contrôle indique sa **condition d'activation**, sa
> **base** (obligation avec référence, ou bonne pratique) et son **statut temporel** à apprécier à la
> date d'audit avec `applicability-calendar.md`.
> États de contrôle (voir `findings-methodology.md`, section 7) : **Démontré**, **Non démontré**,
> **Non applicable** (motif), **Impossible à vérifier**. Le statut temporel est noté à part.
> Chaque état est appuyé par une preuve `PRV-NNN` (fichier, lignes, commit, méthode de reproduction).

Règles :
- Ne marquer « Non démontré » que si le dépôt contient l'emplacement où la mesure devrait figurer ou
  une preuve de son absence. L'absence d'un document organisationnel donne « Impossible à vérifier ».
- Un contrôle « Démontré » ne démontre pas la conformité juridique : il atteste de la présence d'une mesure.
- Une ligne « Bonne pratique » ne doit jamais être rédigée comme une obligation.

## A. Transparence (art. 50) : activer si le système interagit avec des personnes, génère des contenus, ou réalise de la reconnaissance des émotions ou de la catégorisation biométrique

| ID | Contrôle | Base | Statut temporel |
|---|---|---|---|
| A1 | Information des personnes qu'elles interagissent avec une IA, au plus tard à la première interaction | Art. 50, par. 1 et 5 | Depuis 2026-08-02 |
| A2 | Le système ne se présente pas comme humain (prompt système, persona) | Art. 50, par. 1 | Depuis 2026-08-02 |
| A3 | Exception « évident » motivée si invoquée | Art. 50, par. 1 | Depuis 2026-08-02 |
| A4 | Marquage lisible par machine des contenus synthétiques (texte, image, audio, vidéo) | Art. 50, par. 2 | 2026-08-02 ou 2026-12-02 (systèmes antérieurs) `[O26]` |
| A5 | Format de sortie et métadonnées : préservation du marquage dans le pipeline (ré-encodage, compression, export) | Art. 50, par. 2 | Idem A4 |
| A6 | Détectabilité : outil ou API de vérification documenté | Art. 50, par. 2 | Idem A4 |
| A7 | Exceptions du par. 2 (assistance à la mise en forme, absence de modification substantielle) motivées | Art. 50, par. 2 | Idem A4 |
| A8 | Hypertrucages : fonction d'étiquetage et consigne pour le déployeur ; régime artistique ou satirique | Art. 50, par. 4, al. 1 | Depuis 2026-08-02 |
| A9 | Textes publiés sur des questions d'intérêt public : mention ou contrôle éditorial identifié | Art. 50, par. 4, al. 2 | Depuis 2026-08-02 |
| A10 | Information des personnes exposées à la reconnaissance des émotions ou à la catégorisation biométrique (après vérification de l'art. 5) | Art. 50, par. 3 | Depuis 2026-08-02 |
| A11 | Accessibilité et caractère reconnaissable des informations | Art. 50, par. 5 | Depuis 2026-08-02 |
| A12 | Recours au code de bonnes pratiques sur le marquage et l'étiquetage | Bonne pratique (code volontaire) | n.a. |

## B. Supervision humaine : activer si haut risque probable (obligation future) ; sinon bonne pratique si la sortie affecte des personnes

| ID | Contrôle | Base | Statut temporel |
|---|---|---|---|
| B1 | Possibilité d'intervention humaine avant tout effet sur la personne | Art. 14, par. 4, d) | 2027-12-02 / 2028-08-02 `[O26]` |
| B2 | Compréhension et interprétation des résultats (justification, facteurs, confiance) | Art. 14, par. 4, a) et c) | Idem |
| B3 | Ignorer, annuler, remplacer ou inverser une sortie | Art. 14, par. 4, d) | Idem |
| B4 | Interrompre le système (arrêt sûr) | Art. 14, par. 4, e) | Idem |
| B5 | Gestion des erreurs et alertes | Art. 14, par. 4, a) | Idem |
| B6 | Traçabilité des interventions | Art. 12 ; art. 26, par. 6 | Idem |
| B7 | Prévention de l'automatisation excessive | Art. 14, par. 4, b) | Idem |
| B8 | Superviseurs compétents, formés, investis de l'autorité | Art. 26, par. 2 | Idem (organisationnel) |

## C. Documentation technique : activer si haut risque probable ; sinon bonne pratique proportionnée

| ID | Contrôle | Base | Statut temporel |
|---|---|---|---|
| C1 | Description et destination du système | Art. 11 ; annexe IV, point 1 | 2027-12-02 / 2028-08-02 |
| C2 | Architecture technique | Annexe IV, point 2 | Idem |
| C3 | Modèles et fournisseurs utilisés | Annexe IV, point 2, a) | Idem |
| C4 | Versions des modèles épinglées et documentées | Annexe IV, points 1 et 6 | Idem ; bonne pratique immédiate |
| C5 | Documentation des données pertinentes | Art. 10 ; annexe IV, point 2, d) | Idem |
| C6 | Méthodes de validation et résultats | Annexe IV, point 2, g) | Idem |
| C7 | Limites connues | Annexe IV, point 3 ; art. 13 | Idem |
| C8 | Performances et risques | Annexe IV, points 3 à 5 | Idem |
| C9 | Gestion des modifications | Annexe IV, point 6 | Idem |
| C10 | Notice d'utilisation pour les déployeurs | Art. 13 | Idem |
| C11 | Évaluation documentée de la dérogation (si invoquée) | Art. 6, par. 4 | `[AV]` |

## D. Gestion des risques : activer si haut risque probable ; sinon bonne pratique

| ID | Contrôle | Base | Statut temporel |
|---|---|---|---|
| D1 | Identification des risques connus et raisonnablement prévisibles | Art. 9, par. 2 | 2027-12-02 / 2028-08-02 |
| D2 | Mesures de réduction | Art. 9, par. 4 et 5 | Idem |
| D3 | Tests et évaluations (métriques, seuils, essais en conditions réelles si pertinent) | Art. 9, par. 6 à 8 | Idem |
| D4 | Robustesse et cybersécurité (injection de prompt, empoisonnement, secrets) | Art. 15 | Idem ; bonne pratique immédiate |
| D5 | Surveillance après commercialisation | Art. 72 | `[AV]` |
| D6 | Gestion des incidents graves | Art. 73 | `[AV]` |
| D7 | Procédures correctives | Art. 20 | Idem |
| D8 | Secrets absents du code et des journaux | Bonne pratique de sécurité | n.a. |

## E. Traçabilité : activer si haut risque probable ; sinon bonne pratique

| ID | Contrôle | Base | Statut temporel |
|---|---|---|---|
| E1 | Journaux techniques pertinents générés automatiquement | Art. 12 | 2027-12-02 / 2028-08-02 |
| E2 | Historique des décisions | Art. 12 ; art. 86 (explication) | Idem / `[AV]` |
| E3 | Versions des modèles journalisées | Art. 12 ; annexe IV | Idem |
| E4 | Paramètres significatifs journalisés (température, seuils, version de prompt) | Art. 12 | Idem |
| E5 | Historique des changements | Annexe IV, point 6 | Idem |
| E6 | Conservation : au moins six mois pour les journaux, 10 ans pour la documentation | Art. 18, 19 ; art. 26, par. 6 | Idem |

## F. IA et éducation : activer si le système concerne élèves, étudiants, apprenants ou candidats à une formation (voir `education-ai.md`)

| ID | Contrôle | Base | Statut temporel |
|---|---|---|---|
| F1 | Absence de reconnaissance des émotions des apprenants (sauf raisons médicales ou de sécurité) | Art. 5, par. 1, f) | Depuis 2025-02-02 |
| F2 | Évaluation des acquis, notation : qualification annexe III, point 3, b) motivée | Art. 6, par. 2 et 3 | Classification : immédiate ; exigences : 2027-12-02 |
| F3 | Orientation : annexe III, point 3, b) ou c) | Idem | Idem |
| F4 | Sélection, admission, affectation : annexe III, point 3, a) | Idem | Idem |
| F5 | Surveillance d'examens : annexe III, point 3, d) (et art. 5, annexe III, point 1 si biométrie) | Idem | Idem |
| F6 | Évaluation des compétences : effet sur l'accès à une certification | Idem | Idem |
| F7 | Aide à la décision pédagogique : profilage éventuel | Art. 6, par. 3, dernier al. | Idem |
| F8 | Information des élèves et familles sur l'usage d'un système de l'annexe III | Art. 26, par. 11 | 2027-12-02 |
| F9 | Établissements publics : échéance de l'art. 111, par. 2 ; art. 27 | Art. 111, par. 2 `[AV]` ; art. 27 | Conditionnel |

## G. Maîtrise de l'IA (art. 4) : activer pour tout fournisseur ou déployeur d'un système d'IA

| ID | Contrôle | Base | Démontrable par le code ? |
|---|---|---|---|
| G1 | Mesures de soutien à la maîtrise de l'IA du personnel (formation, guides) | Art. 4 (rédaction `[O26]`) | Non : organisationnel ; indice si documents présents |
| G2 | Mesures pour les autres personnes agissant pour le compte de l'organisation (prestataires) | Art. 4 | Non |
| G3 | Adaptation au contexte et aux personnes concernées | Art. 4 | Non |
| G4 | Documentation d'usage remise aux utilisateurs (guide, avertissements dans l'interface) | Bonne pratique contribuant à l'art. 4 | Oui (interface, docs) |
| G5 | Traçabilité des formations (registre) | Bonne pratique (aucun niveau déterminé exigé selon `[O26]`) | Non |

Constats de la section G : presque toujours « À vérifier organisationnellement », gravité Faible à
Moyenne, sauf preuve contraire.
