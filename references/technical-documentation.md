# Documentation technique, traçabilité et gestion des risques

> Base : art. 9, 11, 12, 17, 18, 19, 72, 73 et annexe IV du règlement (UE) 2024/1689 `[TI]` ; exigences
> du haut risque applicables à partir du **2027-12-02** (annexe III) ou du **2028-08-02** (annexe I) `[O26]`.
> Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, annexe IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4).

## 1. Champ

Ces obligations visent les **systèmes à haut risque**. Pour les autres systèmes, une documentation et
une traçabilité proportionnées sont des **bonnes pratiques** (utiles notamment pour démontrer le
respect de l'art. 50 ou l'évaluation de l'art. 6, par. 4).

## 2. Annexe IV : contenu minimal de la documentation technique `[TI]` (résumé)

1. **Description générale** : destination, fournisseur, version, interactions avec du matériel ou
   des logiciels, versions des logiciels, formes de mise sur le marché, matériel d'exécution,
   interface utilisateur, notice d'utilisation.
2. **Description détaillée des éléments et du processus de développement** : méthodes et étapes,
   y compris recours à des systèmes ou outils pré-entraînés de tiers ; spécifications de conception
   (logique générale, algorithmes, choix clés, hypothèses, paramètres d'optimisation) ; architecture ;
   exigences en données (fiches de données, provenance, étiquetage, nettoyage) ; évaluation des
   mesures de contrôle humain ; changements prédéterminés ; procédures de validation et d'essai,
   métriques d'exactitude, de robustesse, d'impact discriminatoire, journaux d'essai ;
   mesures de cybersécurité.
3. **Surveillance, fonctionnement et contrôle** : capacités et limites de performance, degrés
   d'exactitude pour les personnes ou groupes visés, résultats imprévus prévisibles, sources de
   risques, mesures de contrôle humain, spécifications des données d'entrée.
4. Adéquation des **métriques** de performance.
5. Description du **système de gestion des risques** (art. 9).
6. **Modifications** apportées au système au cours de son cycle de vie.
7. **Normes harmonisées** appliquées ou autres solutions.
8. Copie de la **déclaration UE de conformité**.
9. Description du système d'évaluation des performances après commercialisation (art. 72).

Forme simplifiée possible pour les PME et jeunes pousses (art. 11, par. 1), selon un formulaire de la
Commission ; extension aux petites entreprises de taille intermédiaire par le règlement 2026/1744 `[AV]`.

## 3. Checklist documentaire (conditionnelle)

| Élément | Où le chercher | Statut si absent du dépôt |
|---|---|---|
| Description et destination de chaque système | `README`, `docs/`, fiches produit | À vérifier |
| Architecture technique | Diagrammes, ADR, IaC | À vérifier |
| Modèles, fournisseurs et **versions** | Configuration, code, variables d'environnement | Constat technique (versions non épinglées) |
| Documentation des données pertinentes | Fiches de données, scripts | À vérifier |
| Méthodes de validation et résultats | Rapports d'évaluation, tests | À vérifier |
| Limites connues | Documentation, notice | À vérifier |
| Performances et risques | Rapports, registre des risques | À vérifier |
| Gestion des modifications | CHANGELOG, politique de versions de modèles | À vérifier |

## 4. Traçabilité (art. 12, 19, 26, par. 6) `[TI]`

- Art. 12 : enregistrement **automatique** des événements tout au long de la durée de vie,
  permettant d'identifier les situations à risque ou de modification substantielle, de faciliter la
  surveillance après commercialisation et la surveillance du fonctionnement par le déployeur.
- Art. 12, par. 3 : contenu minimal spécifique pour l'identification biométrique à distance
  (période d'utilisation, base de données de référence, données d'entrée ayant donné une
  correspondance, personnes ayant vérifié les résultats).
- Conservation : au moins **six mois** (art. 19 pour le fournisseur, art. 26, par. 6 pour le
  déployeur), sauf disposition contraire ; documentation : **10 ans** (art. 18).

Contrôles techniques :

| Contrôle | Preuve |
|---|---|
| Journalisation des entrées et sorties pertinentes (ou de leurs empreintes) | Code de journalisation |
| Version du modèle effectivement servie | Champ `model_version` ou équivalent |
| Version des prompts, grilles, paramètres significatifs (température, seuils) | `prompt_version`, configuration versionnée |
| Historique des décisions et des interventions humaines | Journal d'audit |
| Horodatage et identifiant de corrélation | `trace_id`, horodatage |
| Intégrité (append-only, contrôle d'accès) | Stockage, permissions |
| Durée de conservation configurée | Paramètre de rétention |
| Absence de secrets dans les journaux | Revue du code de journalisation |

## 5. Gestion des risques, tests, surveillance (art. 9, 15, 72, 73) `[TI]`

| Contrôle | Preuve |
|---|---|
| Identification des risques (santé, sécurité, droits fondamentaux), y compris mauvaise utilisation prévisible | Registre des risques |
| Mesures de réduction et risques résiduels acceptés | Registre, décisions |
| Tests avant mise sur le marché, métriques et seuils | Suites d'évaluation, rapports |
| Robustesse : erreurs, incohérences, résilience | Tests, gestion des erreurs, valeurs par défaut sûres |
| Cybersécurité : injection de prompt, empoisonnement, exfiltration, secrets | Tests adverses, filtrage, gestion des secrets |
| Surveillance après commercialisation | Plan, métriques de production |
| Incidents graves (art. 3, point 49 ; art. 73) | Procédure de signalement et délais |
| Procédures correctives (art. 20) | Procédure de retrait, de rappel, de désactivation |
