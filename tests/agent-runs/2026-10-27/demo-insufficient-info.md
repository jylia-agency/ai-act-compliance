# Rapport d'audit AI Act : TalentRank (demo-insufficient-info)

> **Avertissement.** Ce rapport est une aide à l'audit. Il repose sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689.

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | Dossier `demo-insufficient-info/` entier : `README.md`, `requirements.txt`, `src/rank.py`, `src/train.py`. Le dossier n'est pas un dépôt git : aucune branche ni aucun commit identifiable. Aucun dossier exclu. Ne figurent pas dans le dépôt : le fichier de modèle `models/ranker.joblib` et les données d'entraînement (CSV). |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`meta.last_verified` de `data/ai-act-calendar.json`). Écart avec la date d'audit inférieur à 6 mois : pas de limite majeure à ce titre. |
| Contexte fourni par le demandeur | **Aucun.** Le seul contexte est le dépôt lui-même. Le README précise qu'il ne donne « ni la finalité exacte, ni les utilisateurs, ni les personnes concernées, ni la date de mise sur le marché ». |
| Méthode | Skill `ia-compliance` v1.0.0. Audit en lecture seule, sans exécuter le code audité. Outils : `scan_ai_signals.py` et `obligation_timeline.py --audit-date 2026-10-27`. |
| Audit précédent | Aucun |

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : 1. SYS-01, « TalentRank », classe des « candidats » à l'aide d'un modèle d'apprentissage automatique (`GradientBoostingClassifier`, scikit-learn) que l'organisation entraîne elle-même.
- **Classification** : **indéterminée** (confiance faible). La finalité exacte, les utilisateurs et les personnes concernées ne sont pas établis. **Hypothèse principale** : il s'agit de candidats à un emploi. Le système relèverait alors de l'annexe III, point 4, a). Comme il classe des personnes à partir de leurs caractéristiques personnelles (profilage), la dérogation de l'art. 6, par. 3 ne pourrait pas s'appliquer. Résultat dans ce cas : **haut risque probable**. Même si cette hypothèse se confirme, les exigences du haut risque ne sont **pas encore applicables** : elles le deviennent le 2027-12-02 (CAL-011), et le régime transitoire de l'art. 111, par. 2 (CAL-013) reste conditionnel.
- **Points les plus sensibles** :
  - AIA-001 : le modèle utilise l'**âge** des candidats, la distance et le nombre de candidatures antérieures. Il apprend sur une étiquette historique `selected` (risque de discrimination et de reproduction de biais passés).
  - AIA-002 : la finalité n'est pas établie, donc la classification reste indéterminée.
  - AIA-003 : la sortie est une liste tronquée aux 20 premiers. Aucune justification ni aucun mécanisme de revue humaine n'est observable.
- **Obligations en vigueur concernées** :
  - Art. 4, maîtrise de l'IA (CAL-002, CAL-003).
  - Art. 5, pratiques interdites : examiné, non retenu au vu du dépôt (CAL-002).
  - Art. 50 et chapitre V (GPAI) : non applicables au vu du dépôt.
- **Échéances à venir** :
  - 2026-12-02 : nouvelles interdictions de l'art. 5 (CAL-004). Elles ne concernent pas un système de classement.
  - **2027-12-02** : exigences du haut risque de l'annexe III (CAL-011), si la classification est confirmée.
- **Principales incertitudes** :
  - Nature des « candidats » et finalité du classement.
  - Rôle de l'organisation (fournisseur ou déployeur, outil interne ou fourni à des tiers).
  - Date de mise en service et statut en production.
  - Statut de l'organisation (autorité publique, PME).
  - Provenance des données.
  - Usage réel des sorties.
- **Synthèse des constats** (11) :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | 0 | 0 | 0 | 0 | 0 |
| Risque potentiel | 0 | 1 | 0 | 0 | 0 |
| À vérifier juridiquement ou organisationnellement | 0 | 0 | 1 | 2 | 0 |
| Bonne pratique recommandée | 0 | 0 | 1 | 1 | 0 |
| Non encore applicable | 0 | 0 | 2 | 0 | 0 |
| Non applicable | 0 | 0 | 0 | 0 | 3 |

Ce rapport n'affirme en aucun cas que le projet est conforme ou non conforme à l'AI Act.

## 2. Périmètre et méthode

Arborescence analysée (4 fichiers) :

```
demo-insufficient-info/
├── README.md          « Outil interne de classement de « candidats » »
├── requirements.txt   pandas==2.2.3, scikit-learn==1.5.2, joblib==1.4.2
└── src/
    ├── rank.py        chargement du modèle et classement (rank_candidates)
    └── train.py       entraînement du modèle (train)
```

Outils utilisés :

- **`scan_ai_signals.py`** a relevé :
  - des signaux `classic_ml` : `scikit-learn` et modèle sérialisé (`requirements.txt:2`, `src/rank.py:7`, `src/train.py:4`, `src/train.py:13`) ;
  - des signaux `sensitive_context` : `employment` et `person-scoring` (`README.md:6`, `src/rank.py:1`, `src/rank.py:10`).

  Ce sont des signaux, pas des conclusions. Le contexte « emploi » vient seulement du mot « candidats », qu'aucun autre élément ne confirme.
- **`obligation_timeline.py --audit-date 2026-10-27`** a servi à établir les statuts temporels (section 7).
- **Faux négatifs** : il n'y a aucun appel HTTP, aucune configuration ni aucun drapeau de fonctionnalité dans le dépôt.
- **Secrets** : aucun secret détecté.

Éléments non analysés :

- le fichier de modèle `models/ranker.joblib` (absent du dépôt) ;
- les données d'entraînement (absentes) ;
- tout code appelant `rank_candidates` (absent) : il n'existe ni interface, ni API, ni ordonnanceur ;
- l'environnement d'exécution et l'éventuelle documentation hors dépôt.

## 3. Systèmes d'IA identifiés

### Inventaire

| Champ | SYS-01 |
|---|---|
| Nom | TalentRank, « classement des candidats » |
| Finalité (art. 3, point 12) | **Non établie.** Le dépôt indique seulement : « Outil interne de classement de « candidats » » (`README.md:6`) et « Classement des candidats à partir d'un modèle entraîné » (`src/rank.py:1`). |
| Description fonctionnelle | `rank_candidates` (`src/rank.py:10-13`) calcule pour chaque ligne la probabilité de la classe positive (`predict_proba(...)[:, 1]`). Elle trie ensuite les lignes par probabilité décroissante et ne renvoie que les `top_n` premières (20 par défaut). `train` (`src/train.py:9-13`) entraîne un `GradientBoostingClassifier(random_state=0)` sur un CSV pour prédire la colonne `selected`, puis l'enregistre dans `models/ranker.joblib`. |
| Fichiers principaux | `src/rank.py`, `src/train.py` |
| Entrées | Cinq variables (`src/rank.py:5`) : `experience_years`, `test_score`, `age`, `distance_km`, `previous_applications` |
| Sorties et effets | Score de probabilité et liste triée et tronquée (20 premiers). Effet (information, recommandation ou décision automatique) : **non établi**. |
| Utilisateurs | Non établis (« outil interne ») |
| Personnes concernées | « Candidats », de nature non établie (emploi, formation, autre) |
| Données pertinentes | Données personnelles des candidats, dont l'âge. L'étiquette d'apprentissage `selected` reflète vraisemblablement des sélections passées. La provenance n'est pas fournie (`src/train.py:1`). |
| Modèle(s) et version(s) | `GradientBoostingClassifier` (scikit-learn 1.5.2 épinglé). Le fichier de modèle n'est pas versionné (chemin fixe `models/ranker.joblib`, écrasé à chaque entraînement). |
| Fournisseur(s) de modèle / API tierces | Aucun. Modèle entraîné par l'organisation à l'aide de la bibliothèque libre scikit-learn. |
| Entraînement ou affinage par l'organisation | **Oui**, entraînement (`src/train.py`) |
| Composants associés (RAG, agents) | Aucun |
| Acteurs et rôles | Fournisseur du système (développement et mise en service pour usage propre, art. 3, points 3 et 11) **et** déployeur (art. 3, point 4) **susceptibles** d'être cumulés si l'outil est utilisé en interne. À confirmer. Pas fournisseur de modèle GPAI. |
| Date de mise sur le marché / mise en service | Inconnue |
| Classification | **Indéterminée.** Hypothèse principale : haut risque probable (annexe III, point 4, a)) |
| Confiance de la classification | Faible |
| Statut | Inconnu (en production, en développement ou prototype) |
| Informations manquantes | Voir section 9 (NV-01 à NV-12) |

**Éléments examinés et écartés** : aucun. Tous les signaux se rapportent à SYS-01.

## 4. Rôles réglementaires

**SYS-01, rôle de fournisseur.** L'organisation qui détient ce dépôt développe le système : elle écrit le code d'entraînement et le code d'inférence. Si elle le met en service pour son propre usage (« outil interne »), elle est **susceptible d'être fournisseur** du système d'IA (art. 3, points 3 et 11) `[TI]`. Si elle le fournit à des tiers sous son nom, elle serait aussi fournisseur, au titre de la mise sur le marché (art. 3, point 9).

**SYS-01, rôle de déployeur.** Si elle utilise elle-même le système sous sa propre autorité dans un cadre professionnel, elle est **susceptible d'être déployeur** (art. 3, point 4) `[TI]`. Les deux rôles peuvent se cumuler.

**Modèle GPAI.** L'organisation n'est **pas**, au vu du dépôt, fournisseur d'un modèle d'IA à usage général. Un classifieur à gradient boosting entraîné sur cinq variables tabulaires pour une tâche unique ne présente pas la « généralité significative » de l'art. 3, point 63.

**Hypothèses non vérifiables.** On ne peut pas établir :

- l'établissement dans l'Union ou l'usage des sorties dans l'Union (art. 2, par. 1) ;
- l'existence de clients tiers ;
- le rôle éventuel d'importateur ou de distributeur, qu'aucun élément ne suggère.

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 2, par. 1 (champ territorial) | SYS-01 | À vérifier | Établissement de l'organisation et lieu d'utilisation des sorties inconnus (NV-08) |
| Art. 2, par. 3 (militaire, défense, sécurité nationale) | SYS-01 | Écartée | Aucun indice d'une telle finalité |
| Art. 2, par. 6 (recherche scientifique exclusive) | SYS-01 | Écartée (confiance moyenne) | « Outil interne de classement » : la destination opérationnelle paraît primer sur une finalité exclusive de recherche |
| Art. 2, par. 8 (R&D avant mise sur le marché ou en service) | SYS-01 | **À vérifier** | Le statut (prototype ou en service) n'est pas connu (NV-04). Si le système n'est ni mis sur le marché ni mis en service, une partie des obligations ne s'applique pas encore. |
| Art. 2, par. 10 (usage personnel non professionnel) | SYS-01 | Écartée (confiance moyenne) | Le terme « outil interne » suggère un cadre organisationnel et professionnel |
| Art. 2, par. 12 (logiciel libre et open source) | SYS-01 | Écartée | Aucune licence libre observée pour le système. De plus, cette exclusion ne joue pas pour un système mis en service en tant que système à haut risque. scikit-learn, bibliothèque libre, n'est pas le système audité. |
| Art. 6, par. 3 (dérogation au haut risque) | SYS-01 | Écartée sous l'hypothèse annexe III | Le classement de personnes à partir de leurs caractéristiques personnelles (âge, distance, expérience, candidatures antérieures) s'analyse comme un profilage : la dérogation est alors exclue (art. 6, par. 3, dernier alinéa). Le classement tronqué à 20 n'apparaît pas non plus comme une tâche « procédurale étroite » ou « préparatoire » sans influence substantielle. À confirmer selon la finalité. |
| Art. 50, exceptions | SYS-01 | Sans objet | Art. 50 non applicable (AIA-010) |
| Renvois à d'autres législations (protection des données, non-discrimination, droit du travail) | SYS-01 | Hors périmètre | Signalés sans analyse, notamment au regard de l'usage de l'âge (AIA-001) |

## 6. Classification

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA au sens de l'art. 3, point 1 ? | **Oui** (confiance élevée) | Le modèle est appris à partir de données (`src/train.py:11-12`). Il déduit des entrées une probabilité, puis un classement (`src/rank.py:12-13`). Ce n'est pas une règle définie uniquement par des humains. | Art. 3, point 1 `[TI]` |
| 1 | Exclusion de l'art. 2 ? | Non retenue ; art. 2, par. 8 à vérifier | Section 5 ; NV-04 | Art. 2 `[TI]` |
| 2 | Pratique interdite plausible ? | **Non retenue** au vu du dépôt (confiance moyenne) | Points c) (notation sociale) et f) (émotions) examinés, voir AIA-009 | Art. 5 `[TI]` |
| 3 | Annexe I ? | Non | Aucun produit réglementé ni composant de sécurité | Art. 6, par. 1 |
| 4 | Annexe III ? | **Indéterminé** | H1 (candidats à un emploi) : point 4, a), recrutement ou sélection, filtrage des candidatures, évaluation des candidats. H2 (candidats à une formation) : point 3, a), accès ou admission. H3 (autre finalité, par exemple fournisseurs ou projets) : hors annexe III. Les variables `experience_years` et `test_score` sont compatibles avec H1 et H2. | Art. 6, par. 2 ; annexe III `[TI]` |
| 5a | Profilage ? | Probable sous H1 et H2 | Évaluation de personnes à partir de caractéristiques personnelles, dont l'âge | Art. 6, par. 3, dernier al. `[TI]` |
| 5b | Dérogation art. 6, par. 3 ? | Exclue sous H1 et H2 (profilage) | Section 5 | Art. 6, par. 3 `[TI]` |
| 6 | Art. 50 ? | Non | Pas d'interaction directe avec des personnes, pas de génération de contenu, pas de biométrie | Art. 50 `[TI]` |
| 7 | Fournisseur de modèle GPAI ? | Non | Modèle spécialisé, non général | Art. 3, point 63 ; art. 53 `[TI]` |
| 8 | Obligations horizontales | Art. 4 si l'organisation est fournisseur ou déployeur | NV-10 | Art. 4 `[TI]` / `[O26]` |

**Conclusion**

- **Classification retenue** : **Indéterminée** (information insuffisante).
- **Niveau de confiance** : faible.
- **Critères déterminants** : apprentissage automatique avéré ; classement de personnes (« candidats ») à partir de caractéristiques personnelles ; finalité, utilisateurs et personnes concernées non établis.
- **Exceptions envisagées** : art. 2, par. 8 (à vérifier) ; art. 6, par. 3 (exclue sous H1 et H2 en raison du profilage).
- **Hypothèses alternatives et conséquences** :
  - H1 ou H2 : **haut risque probable** (annexe III, point 4, a) ou point 3, a)). Exigences des art. 8 à 27 à partir du **2027-12-02** (CAL-011, non encore applicable). Régime transitoire de l'art. 111, par. 2 (CAL-013, conditionnel, confiance faible).
  - H3 : **non à haut risque**. Seuls l'art. 4 et l'art. 5 restent pertinents.
- **Informations nécessaires** : NV-01 à NV-06.
- **Aucune obligation du haut risque n'est présentée comme applicable à la date d'audit.**

## 7. Obligations et calendrier

Statuts calculés par `obligation_timeline.py --audit-date 2026-10-27`. La date de mise en service n'étant pas fournie, les entrées transitoires sont « conditionnelles ».

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|
| Maîtrise de l'IA (art. 4) | SYS-01 | Fournisseur et/ou déployeur | En vigueur | 2025-02-02 ; nouvelle rédaction 2026-07-27 | CAL-002, CAL-003 | Élevée / Moyenne |
| Pratiques interdites (art. 5, points a) à h)) | SYS-01 | Fournisseur et déployeur | En vigueur (non retenues au vu du dépôt) | 2025-02-02 | CAL-002 | Élevée |
| Nouvelles interdictions de l'art. 5 | SYS-01 | Tous | Non encore applicable ; sans objet pour ce système | 2026-12-02 | CAL-004 | Moyenne |
| Art. 50, par. 1, 3, 4 et 5 | SYS-01 | n.a. | En vigueur ; non applicable au système | 2026-08-02 | CAL-009 | Élevée |
| Art. 50, par. 2 | SYS-01 | n.a. | Conditionnel ; non applicable (aucun contenu généré) | 2026-08-02 / 2026-12-02 | CAL-010 | Moyenne |
| Chapitre V (GPAI) | n.a. | n.a. | En vigueur ; non applicable | 2025-08-02 | CAL-005 | Élevée |
| Exigences du haut risque, annexe III (art. 9 à 15 ; art. 16 à 27, dont art. 26) | SYS-01 si H1 ou H2 | Fournisseur / déployeur | **Non encore applicable** (dans 401 jours) | 2027-12-02 | CAL-011 | Moyenne |
| Systèmes mis en service avant l'application du chapitre III (art. 111, par. 2) | SYS-01 si H1 ou H2 | Fournisseur / déployeur | **Conditionnel** (date de mise en service inconnue ; autorité publique : 2030-08-02, divergence signalée) | Réf. 2027-12-02 | CAL-013 | Faible |
| Art. 49, 72, 73, 86 (hors chapitre III, liés au haut risque) | SYS-01 si H1 ou H2 | Fournisseur / déployeur | Conditionnel ; date effective à confirmer | `[AV]` | Section 3 du calendrier | Faible |
| Enregistrement des systèmes de l'annexe III jugés non à haut risque (art. 49, par. 2) | SYS-01 si dérogation invoquée | Fournisseur | À vérifier (peu pertinent : dérogation exclue sous H1 et H2) | n.d. | CAL-016 | Faible |

## 8. Constats

Les constats sont ordonnés par gravité, puis par identifiant.

### AIA-001 : Âge, distance et candidatures antérieures en entrée d'un modèle de classement de candidats entraîné sur des sélections historiques
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Risque potentiel
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits) / Faible (qualification)
- **Preuve observée** :
  - Fait observé : la liste des variables du modèle comprend `"age"`, `"distance_km"` et `"previous_applications"`, à côté de `"experience_years"` et `"test_score"`.
  - Le modèle est entraîné à prédire la colonne `selected` d'un jeu de données externe.
  - Le score obtenu détermine seul l'ordre et la troncature de la liste (`head(top_n)`).
  - Aucune analyse de biais, aucune pondération ni aucune exclusion de variable n'est présente dans le dépôt.
- **Fichier(s) et lignes** : `src/rank.py:5`, `src/rank.py:12-13`, `src/train.py:10-12`
- **Rôle réglementaire concerné** : Fournisseur du système (et déployeur si usage interne), à confirmer
- **Classification du système** : Indéterminée (hypothèse principale : haut risque probable, annexe III, point 4, a))
- **Référence juridique** :
  - Art. 10 (données et gouvernance des données : pertinence, représentativité, examen des biais possibles) `[TI]`.
  - Art. 9 (gestion des risques pour les droits fondamentaux) `[TI]`.
  - Annexe III, point 4, a) `[TI]`.
  - Art. 10, par. 5 (traitement de données sensibles pour la correction des biais) `[AV]`.
  - Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689), [AI Act Explorer, art. 10](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-10).
  - Le droit de la non-discrimination et de la protection des données est hors périmètre ; il est seulement signalé.
- **Date d'application** : Art. 9 et 10 au 2027-12-02 (CAL-011, non encore applicable, confiance moyenne). Régime transitoire conditionnel (CAL-013). Le risque pour les personnes, lui, existe dès l'utilisation éventuelle du système.
- **Conditions et exceptions** :
  - La qualification dépend de la finalité (NV-01) et de la mise en service (NV-04).
  - La dérogation de l'art. 6, par. 3 est exclue en cas de profilage.
  - L'exception de l'art. 2, par. 8 (R&D) n'écarte pas le risque si le système est déjà utilisé sur des personnes réelles.
- **Explication** :
  - Le modèle classe des personnes en tenant compte de leur âge et de leur éloignement géographique.
  - Il apprend à imiter des décisions de sélection passées, qui peuvent contenir des biais. Le modèle risque alors de les reproduire, voire de les amplifier.
  - Si les candidats sont des candidats à un emploi, le système est probablement à haut risque. La qualité des données et l'examen des biais y deviennent des exigences légales à partir du 2027-12-02.
  - Dès aujourd'hui, l'usage de l'âge pour classer des candidats soulève des questions au regard d'autres législations, non analysées ici.
- **Recommandation** :
  - Faire valider par un juriste la licéité de chaque variable au regard de la finalité réelle (hors périmètre AI Act).
  - Documenter la justification de chaque variable et retirer celles qui ne sont pas strictement nécessaires (en priorité `age`).
  - Analyser l'étiquette `selected` (provenance, biais historiques).
  - Mesurer les écarts de résultats entre groupes (par exemple par tranche d'âge) avant tout usage.
  - Préparation de l'obligation future de l'art. 10 et bonne pratique immédiate.
- **Méthode de vérification** :
  - Nouvelle version de `FEATURES` avec justification documentée.
  - Fiche de données (provenance, période, définition de `selected`).
  - Rapport d'analyse de biais, avec métriques par groupe et seuils.
  - Avis juridique archivé.

### AIA-002 : Finalité, utilisateurs et personnes concernées non établis : classification indéterminée
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Faible (qualification)
- **Preuve observée** :
  - Le README décrit seulement un « Outil interne de classement de « candidats » ». Il indique expressément que la finalité exacte, les utilisateurs, les personnes concernées et la date de mise sur le marché ne sont pas précisés.
  - Les guillemets autour de « candidats » laissent même la notion ouverte.
  - Aucun code appelant `rank_candidates` n'est présent.
- **Fichier(s) et lignes** : `README.md:3-6`, `src/rank.py:1`, `src/rank.py:10`
- **Rôle réglementaire concerné** : À déterminer (fournisseur et/ou déployeur)
- **Classification du système** : Indéterminée
- **Référence juridique** :
  - Art. 3, point 12 (destination) `[TI]`.
  - Art. 6, par. 2 et 3 `[TI]`.
  - Annexe III, point 4, a) (emploi) et point 3, a) (éducation, accès et admission) `[TI]`.
  - Source : [AI Act Explorer, art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6).
- **Date d'application** : La classification est à établir immédiatement, car elle conditionne les obligations. Les exigences associées s'appliquent au 2027-12-02 (CAL-011, non encore applicable) ; CAL-013 conditionnel.
- **Conditions et exceptions** :
  - H1 (emploi) ou H2 (formation) : haut risque probable, dérogation de l'art. 6, par. 3 exclue (profilage).
  - H3 (autre) : non à haut risque. Les art. 4 et 5 restent pertinents.
  - Art. 2, par. 8 à vérifier.
- **Explication** :
  - Les obligations dépendent de l'usage du système, pas de la technologie employée.
  - Le mot « candidats » ne suffit pas pour classer le système à haut risque, mais il en rend l'hypothèse sérieuse.
  - Sans ces informations, l'audit ne peut conclure. Il ne présente donc aucune obligation du haut risque comme applicable.
- **Recommandation** :
  - Rédiger une fiche de destination du système : qui sont les candidats, qui utilise le classement, pour quelle décision, avec quel effet.
  - Formaliser l'analyse de classification (art. 6) et la faire valider juridiquement.
  - Démarche nécessaire pour déterminer les obligations (préalable à toute obligation).
- **Méthode de vérification** : fiche de destination datée et signée ; analyse de classification documentée (modèle `risk-classification.md`) ; réponses aux questions NV-01 à NV-06.

### AIA-003 : Liste des 20 premiers produite automatiquement, sans explication ni mécanisme de contrôle humain observable
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Faible (qualification, conditionnelle à la classification)
- **Preuve observée** :
  - Fait observé : `rank_candidates` renvoie uniquement les `top_n` lignes (20 par défaut) de plus forte probabilité. Les autres candidats sont écartés de la sortie.
  - Aucune justification n'est produite : ni facteurs explicatifs, ni seuil, ni indication de confiance.
  - Aucun statut de revue (`pending_review`, `override`) ni aucune fonction de refus ou de modification n'existe.
  - Aucun texte d'information des candidats n'est présent.
  - L'usage effectif de la sortie (aide à la décision ou décision) n'est pas observable.
- **Fichier(s) et lignes** : `src/rank.py:10-13`
- **Rôle réglementaire concerné** : Fournisseur (art. 14) ; déployeur (art. 26, par. 2 et 11 ; art. 86)
- **Classification du système** : Indéterminée (obligations conditionnelles à H1 ou H2)
- **Référence juridique** :
  - Art. 14, par. 4, a) à e) `[TI]`.
  - Art. 13 `[TI]`.
  - Art. 26, par. 2 et 11 `[TI]`.
  - Art. 86 (droit à l'explication) `[TI]`, date effective `[AV]`.
  - Source : [AI Act Explorer, art. 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14).
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable, confiance moyenne) ; CAL-013 conditionnel ; art. 86 à confirmer.
- **Conditions et exceptions** :
  - S'applique seulement si la classification haut risque est confirmée (AIA-002).
  - Une validation humaine en aval ne permettrait pas d'appliquer la dérogation de l'art. 6, par. 3 : la supervision est une exigence du haut risque, pas un critère d'exclusion.
  - Si le système n'est pas à haut risque, ces mesures restent une bonne pratique.
- **Explication** :
  - En l'état, le code ne montre à l'utilisateur que les 20 premiers candidats, sans dire pourquoi.
  - Un recruteur risque de se fier à cette liste sans examiner les autres candidatures (biais d'automatisation).
  - Pour un système à haut risque, la loi exigera à partir du 2027-12-02 qu'un humain puisse comprendre, contester et écarter le résultat.
  - Les candidats devront aussi être informés.
- **Recommandation** :
  - Préparer dès maintenant une sortie présentée comme une proposition, et non comme un filtre.
  - Afficher tous les candidats ou rendre la troncature explicite.
  - Afficher les facteurs déterminants du score.
  - Prévoir une fonction permettant à l'humain de modifier, d'écarter ou de réintégrer un candidat, avec motif.
  - Prévoir un texte d'information des candidats.
  - Préparation d'une obligation future (art. 14, 26) ; bonne pratique dans l'immédiat.
- **Méthode de vérification** : revue de code de l'interface de revue ; test montrant qu'un candidat hors des 20 premiers peut être réintégré ; capture de l'information des candidats ; journal des interventions humaines.

### AIA-004 : Ni évaluation du modèle, ni métriques, ni documentation des données d'entraînement dans le dépôt
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits dans le dépôt) / Faible (qualification ; documents possibles hors dépôt)
- **Preuve observée** :
  - Fait observé : `train` lit un CSV dont la provenance n'est pas fournie (« données non fournies dans le dépôt »). Il entraîne le modèle sur l'ensemble des lignes et l'enregistre directement.
  - Aucune séparation entraînement/test, aucune métrique d'exactitude, aucun seuil d'acceptation, aucune fiche de données ni aucune documentation technique n'est présente.
  - L'absence de ces documents dans le dépôt **ne prouve pas** leur inexistence.
- **Fichier(s) et lignes** : `src/train.py:1`, `src/train.py:9-13`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Indéterminée (obligations conditionnelles à H1 ou H2)
- **Référence juridique** :
  - Art. 9, par. 2 et par. 6 à 8 `[TI]`.
  - Art. 10 `[TI]`.
  - Art. 11 et annexe IV, point 2, d) et g) `[TI]`.
  - Art. 15 `[TI]`.
  - Source : [AI Act Explorer, annexe IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4).
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable, confiance moyenne) ; CAL-013 conditionnel.
- **Conditions et exceptions** :
  - Applicable seulement si le haut risque est confirmé.
  - Une forme simplifiée de documentation est possible pour les PME (art. 11, par. 1). Son extension aux petites entreprises de taille intermédiaire est `[AV]`. Le statut de l'organisation est inconnu (NV-09).
- **Explication** :
  - Le dépôt ne permet pas de savoir si le modèle a été testé, avec quelle exactitude ni sur quelles données.
  - Pour un système à haut risque, ces éléments devront figurer dans une documentation technique établie **avant** la mise en service.
  - Établir cette documentation demande plusieurs mois.
- **Recommandation** :
  - Ajouter une procédure d'évaluation reproductible : jeu de test séparé, métriques globales et par groupe, seuils d'acceptation.
  - Rédiger une fiche de données.
  - Lancer la documentation de l'annexe IV.
  - Préparation d'une obligation future ; bonne pratique immédiate.
- **Méthode de vérification** : script ou notebook d'évaluation versionné avec résultats ; fiche de données ; documentation technique couvrant l'annexe IV, points 1 à 6.

### AIA-005 : Aucune journalisation des classements ni aucun versionnement du modèle servi
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée
- **Preuve observée** :
  - Fait observé : le modèle est chargé depuis un chemin fixe `models/ranker.joblib`, sans identifiant de version.
  - `train` écrase ce même fichier à chaque entraînement.
  - `rank_candidates` ne journalise ni les entrées, ni les scores, ni la version du modèle, ni l'horodatage, ni l'utilisateur.
- **Fichier(s) et lignes** : `src/rank.py:7`, `src/rank.py:10-13`, `src/train.py:13`
- **Rôle réglementaire concerné** : Fournisseur (art. 12, 19) ; déployeur (art. 26, par. 6)
- **Classification du système** : Indéterminée
- **Référence juridique** :
  - Aucune obligation applicable à la date d'audit (bonne pratique).
  - Si le haut risque est confirmé : art. 12, art. 19 et art. 26, par. 6 `[TI]` (conservation d'au moins six mois) et annexe IV, point 6 `[TI]`.
- **Date d'application** : Bonne pratique immédiate ; art. 12, 19 et 26 au 2027-12-02 (CAL-011, non encore applicable).
- **Conditions et exceptions** : Le contenu des journaux devra respecter la législation sur la protection des données (hors périmètre).
- **Explication** :
  - Sans journal ni version de modèle, il est impossible de reconstituer pourquoi un candidat a été classé à tel rang, ni avec quel modèle.
  - Cette traçabilité est nécessaire pour répondre à une contestation (art. 86, `[AV]`) et pour détecter une dérive.
  - Elle permet aussi d'établir si un réentraînement constitue une modification importante au sens de l'art. 111, par. 2 (voir AIA-007).
- **Recommandation** :
  - Versionner chaque modèle entraîné (identifiant, date, empreinte, données d'entraînement).
  - Journaliser à chaque classement : version du modèle, horodatage, identifiant de la requête, scores produits et décision humaine associée.
  - Définir une durée de conservation.
  - Bonne pratique ; préparation de l'art. 12.
- **Méthode de vérification** : registre des versions de modèle ; extrait de journal (anonymisé) ; paramètre de rétention configuré.

### AIA-006 : Mesures de maîtrise de l'IA (art. 4) non observables dans le dépôt
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne
- **Preuve observée** : Le dépôt ne contient aucune documentation d'usage, aucun guide, aucun support de formation ni aucun registre. Il s'agit d'éléments organisationnels, normalement hors dépôt.
- **Fichier(s) et lignes** : non disponible
- **Rôle réglementaire concerné** : Fournisseur et/ou déployeur
- **Classification du système** : Indéterminée
- **Référence juridique** :
  - Art. 4 `[TI]`, nouvelle rédaction selon le règlement 2026/1744, à confirmer sur le JO `[O26]`.
  - Source : [EUR-Lex 2026/1744](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1744).
- **Date d'application** : En vigueur depuis le 2025-02-02 (CAL-002, confiance élevée) ; nouvelle rédaction en vigueur depuis le 2026-07-27 (CAL-003, confiance moyenne).
- **Conditions et exceptions** :
  - S'applique à tout fournisseur ou déployeur d'un système d'IA, quelle que soit sa classification.
  - Ne s'appliquerait pas si le système relève de l'exclusion de l'art. 2, par. 8 (non mis en service, NV-04).
  - La nouvelle rédaction n'exige pas de niveau déterminé de maîtrise `[O26]`.
- **Explication** :
  - Les personnes qui utilisent ou développent l'outil doivent être aidées à en comprendre les possibilités, les limites et les risques. C'est particulièrement important ici : risque de biais, liste tronquée.
  - L'audit ne peut pas vérifier ce point à partir du code.
- **Recommandation** :
  - Recenser les mesures existantes : formation, guide d'utilisation expliquant le score et ses limites, consignes contre le biais d'automatisation.
  - Les compléter si nécessaire.
  - Mesure répondant à l'obligation de l'art. 4.
- **Méthode de vérification** : supports de formation, guide utilisateur, liste des personnes sensibilisées.

### AIA-007 : Date de mise en service inconnue : régime transitoire de l'art. 111, par. 2 et effet des réentraînements à établir
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Faible (référence `[AV]`)
- **Preuve observée** :
  - Aucune date de mise sur le marché ou de mise en service n'est indiquée (`README.md:3-4`).
  - Le script `train` permet de réentraîner le modèle et d'écraser le fichier servi à tout moment.
  - Aucun historique des versions n'existe (dossier non versionné par git, pas de CHANGELOG).
- **Fichier(s) et lignes** : `README.md:3-4`, `src/train.py:9-13`
- **Rôle réglementaire concerné** : Fournisseur ; déployeur
- **Classification du système** : Indéterminée (pertinent sous H1 ou H2)
- **Référence juridique** :
  - Art. 111, par. 2, modifié par le règlement 2026/1744 `[AV]`.
  - Art. 3, point 23 (modification substantielle) `[TI]`.
  - Art. 25, par. 1 `[TI]`.
- **Date d'application** : CAL-013, conditionnel, confiance faible. Date de référence 2027-12-02. Systèmes destinés aux autorités publiques : 2030-08-02 (une source indique 2028-01-28).
- **Conditions et exceptions** :
  - Selon les sources, un système à haut risque mis en service avant le 2027-12-02 n'est soumis au chapitre III qu'en cas de modification importante de sa conception après cette date. L'appréciation se fait au niveau du type et du modèle.
  - Exception : les systèmes destinés à des autorités publiques sont soumis à une échéance propre.
  - Ces points sont à confirmer sur le texte officiel.
- **Explication** :
  - La date à laquelle l'outil a été mis en service, et la façon dont il évolue, peuvent changer le moment où les exigences du haut risque s'appliquent.
  - Un réentraînement, un changement de variables ou un changement de finalité pourrait constituer une modification importante.
- **Recommandation** :
  - Établir et conserver la date de première mise en service, ainsi que l'historique des versions.
  - Faire qualifier juridiquement les réentraînements et changements de variables.
  - Bonne gestion préalable à l'application d'une disposition transitoire.
- **Méthode de vérification** : document daté de mise en service ; historique des versions de modèle ; analyse juridique de l'art. 111, par. 2 sur le texte officiel.

### AIA-008 : Modèle sérialisé (joblib/pickle) chargé sans contrôle d'intégrité
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Faible
- **Niveau de confiance** : Élevée (faits)
- **Preuve observée** :
  - Fait observé : `joblib.load("models/ranker.joblib")` est exécuté à l'import du module, sans aucune vérification d'empreinte ni de signature. Le format joblib/pickle peut exécuter du code au chargement.
  - Mesure positive : les dépendances sont épinglées (`requirements.txt:1-3`).
- **Fichier(s) et lignes** : `src/rank.py:7`, `requirements.txt:1-3`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Indéterminée
- **Référence juridique** : Aucune obligation applicable à la date d'audit (bonne pratique de sécurité). Si le haut risque est confirmé : art. 15 (cybersécurité, empoisonnement de modèles) `[TI]`, au 2027-12-02.
- **Date d'application** : Bonne pratique immédiate ; art. 15 au 2027-12-02 (CAL-011, non encore applicable).
- **Conditions et exceptions** : Néant.
- **Explication** : Si quelqu'un remplace le fichier du modèle, il peut modifier les classements, voire exécuter du code sur le serveur. Vérifier l'intégrité du fichier réduit ce risque.
- **Recommandation** :
  - Enregistrer l'empreinte (hachage) de chaque modèle validé et la vérifier au chargement.
  - Restreindre les droits d'écriture sur le dossier `models/`.
  - Envisager un format de sérialisation sans exécution de code.
  - Bonne pratique.
- **Méthode de vérification** : code de vérification d'empreinte ; test de refus d'un fichier altéré ; permissions du dossier.

### AIA-009 : Pratiques interdites (art. 5) examinées et non retenues au vu du dépôt
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Moyenne (finalité inconnue)
- **Preuve observée** :
  - Les variables d'entrée sont `experience_years`, `test_score`, `age`, `distance_km` et `previous_applications`.
  - Il n'y a aucune donnée biométrique, aucune inférence d'émotions, aucune donnée de comportement social, aucune réutilisation du score dans un autre contexte et aucune évaluation de risque d'infraction.
- **Fichier(s) et lignes** : `src/rank.py:5`
- **Rôle réglementaire concerné** : Fournisseur et déployeur
- **Classification du système** : Indéterminée
- **Référence juridique** :
  - Art. 5, par. 1, a) à h) `[TI]`.
  - Source : [AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5).
- **Date d'application** : En vigueur depuis le 2025-02-02 (CAL-002). Nouvelles interdictions au 2026-12-02 (CAL-004, non encore applicable, sans rapport avec ce système).
- **Conditions et exceptions** :
  - Point c) (notation sociale) : écarté, car il n'y a ni comportement social, ni traitement préjudiciable dans un contexte sans lien observé.
  - Point f) (reconnaissance des émotions au travail) : écarté, car il n'y a pas de biométrie.
  - Points d), e), g) et h) : sans objet.
  - Conclusion à réexaminer si la finalité réelle (NV-01) ou l'usage du score (NV-05) diffère.
- **Explication** : Au vu du code, l'outil ne relève d'aucune pratique interdite. Il reste soumis aux autres règles du règlement.
- **Recommandation** : Réexaminer ce point lorsque la finalité sera documentée. Aucune action immédiate.
- **Méthode de vérification** : fiche de destination (AIA-002) confirmant l'absence de réutilisation du score hors du contexte de sélection.

### AIA-010 : Obligations de transparence de l'article 50 non applicables
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** : Le système produit un score numérique et un tri. Il n'interagit pas directement avec des personnes, ne génère ni texte, ni image, ni audio, ni vidéo, et ne réalise ni reconnaissance des émotions, ni catégorisation biométrique.
- **Fichier(s) et lignes** : `src/rank.py:10-13`
- **Rôle réglementaire concerné** : Fournisseur ; déployeur
- **Classification du système** : Indéterminée
- **Référence juridique** :
  - Art. 50, par. 1 à 5 `[TI]`.
  - Source : [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50).
- **Date d'application** : CAL-009, en vigueur depuis le 2026-08-02 ; CAL-010, conditionnel ; sans objet pour ce système.
- **Conditions et exceptions** : L'information des candidats sur l'usage d'un système à haut risque relève de l'art. 26, par. 11 (voir AIA-003), pas de l'art. 50.
- **Explication** : Les obligations de transparence de l'art. 50 visent les chatbots, les contenus générés, la biométrie et les hypertrucages. Ce système n'entre dans aucune de ces catégories.
- **Recommandation** : Aucune. À réexaminer si une interface conversationnelle ou une génération de texte (par exemple des courriers aux candidats) est ajoutée.
- **Méthode de vérification** : Revue de l'inventaire lors du prochain audit.

### AIA-011 : Obligations des fournisseurs de modèles GPAI (art. 53) non applicables
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** : L'organisation entraîne un `GradientBoostingClassifier` sur cinq variables tabulaires pour une tâche unique de classement. Elle ne publie ni ne commercialise de modèle général.
- **Fichier(s) et lignes** : `src/train.py:11-13`
- **Rôle réglementaire concerné** : Fournisseur du système (pas fournisseur de modèle GPAI)
- **Classification du système** : Indéterminée
- **Référence juridique** :
  - Art. 3, point 63 ; art. 51 à 55 `[TI]`.
  - Source : [AI Act Explorer, art. 53](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53).
- **Date d'application** : CAL-005, en vigueur depuis le 2025-08-02 ; sans objet.
- **Conditions et exceptions** : Le modèle ne présente pas la généralité significative exigée.
- **Explication** : Entraîner son propre modèle spécialisé ne fait pas de l'organisation un fournisseur de « modèle d'IA à usage général ». Ses obligations éventuelles sont celles de fournisseur du système.
- **Recommandation** : Aucune.
- **Méthode de vérification** : Sans objet.

## 9. Éléments non vérifiables

**Registre des éléments non vérifiables** (date d'audit : 2026-10-27). Comme le demandeur n'a pas pu être interrogé, toutes les questions sont consignées ici.

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact sur la classification ou les obligations | Interlocuteur suggéré | Constat(s) liés |
|---|---|---|---|---|---|---|---|
| NV-01 | SYS-01 | Nature des « candidats » (emploi, stage, formation, admission, autre) et finalité exacte du classement | Information | Déterminer la destination (art. 3, point 12) | Bascule entre l'annexe III, point 4, a) ou point 3, a) (haut risque probable) et le non-haut risque | Responsable produit / RH | AIA-002, AIA-001, AIA-009 |
| NV-02 | SYS-01 | Utilisateurs du classement (recruteurs, jurys, managers) et leur nombre | Information | Rôle de déployeur, supervision humaine, art. 4 | Art. 26, art. 14, art. 4 | Responsable produit | AIA-003, AIA-006 |
| NV-03 | SYS-01 | Effet de la sortie : simple aide, présélection éliminatoire, décision automatique ; usage de `top_n` | Information | Évaluer l'influence sur la décision et le risque d'automatisation | Art. 6, par. 3 ; art. 14 ; art. 86 | Responsable métier | AIA-003 |
| NV-04 | SYS-01 | Statut (prototype, en production) et date de première mise en service ou mise sur le marché | Information | Exclusion de l'art. 2, par. 8 ; régime transitoire de l'art. 111, par. 2 | CAL-013 ; applicabilité de l'art. 4 | Direction technique | AIA-007, AIA-006 |
| NV-05 | SYS-01 | Réutilisation éventuelle du score dans d'autres contextes | Information | Écarter définitivement l'art. 5, par. 1, c) | Art. 5 | Responsable produit | AIA-009 |
| NV-06 | SYS-01 | Outil uniquement interne ou fourni ou commercialisé à des tiers, sous quelle marque | Décision / information | Rôle de fournisseur (mise sur le marché) et/ou de déployeur | Obligations de l'art. 16 ou de l'art. 26 | Direction | AIA-002 |
| NV-07 | SYS-01 | Provenance, période et définition de la colonne `selected` ; présence d'autres données personnelles | Document | Gouvernance des données, biais historiques | Art. 10 (futur) ; législation sur la protection des données (hors périmètre) | Data scientist / DPO | AIA-001, AIA-004 |
| NV-08 | SYS-01 | Lieu d'établissement de l'organisation et lieu d'utilisation des sorties | Information juridique | Champ territorial (art. 2, par. 1) | Applicabilité du règlement | Juridique | Section 5 |
| NV-09 | SYS-01 | Statut de l'organisation : autorité publique ou organisme de droit public, entité fournissant un service public, PME | Information juridique | Art. 27 (analyse d'impact sur les droits fondamentaux) ; échéance de l'art. 111, par. 2 pour les autorités publiques ; documentation simplifiée pour les PME | CAL-013 ; art. 27 ; art. 11, par. 1 | Juridique | AIA-004, AIA-007 |
| NV-10 | SYS-01 | Mesures de maîtrise de l'IA (formations, guides) | Document | Démontrer l'art. 4 | Art. 4 (en vigueur) | RH / formation | AIA-006 |
| NV-11 | SYS-01 | Évaluations du modèle, documentation technique, registre des risques, analyses de biais hors dépôt | Document | L'absence dans le dépôt n'est pas une preuve d'absence | Art. 9 à 11, 15 (futurs) | Data scientist | AIA-004, AIA-001 |
| NV-12 | SYS-01 | Journalisation, conservation et information des candidats éventuellement mises en œuvre hors du dépôt (application appelante) | Document / information | Code appelant `rank_candidates` absent | Art. 12, 26, par. 6 et 11 (futurs) | Direction technique | AIA-003, AIA-005 |

## 10. Recommandations et plan de remédiation

Priorisation selon `findings-methodology.md`, section 6. Efforts estimés à partir du dépôt seul.

| Priorité | Constat(s) | Action | Base | Échéance réglementaire | Effort | Preuve de clôture attendue |
|---|---|---|---|---|---|---|
| P2 | AIA-001 | Justifier ou retirer les variables `age` et `distance_km` ; analyser l'étiquette `selected` ; mesurer les écarts par groupe ; avis juridique (non-discrimination, données) | Préparation de l'art. 10 (2027-12-02) ; risque actuel pour les personnes | 2027-12-02 (CAL-011) ; dès l'usage pour les autres législations | M | Rapport de biais, nouvelle liste de variables justifiée |
| P2 | AIA-002 | Fiche de destination et analyse de classification validée | Préalable à toute obligation | Immédiat | S | Fiche signée, analyse de l'art. 6 |
| P3 | AIA-003 | Sortie présentée comme proposition, explications, fonctions de modification et de réintégration, information des candidats | Art. 13, 14, 26, par. 11 (si haut risque) | 2027-12-02 | M | Code et captures, journal des interventions |
| P3 | AIA-004 | Procédure d'évaluation, fiche de données, documentation de l'annexe IV | Art. 9, 10, 11, 15 (si haut risque) | 2027-12-02 | L | Rapport d'évaluation, documentation technique |
| P3 | AIA-005 | Versionnement des modèles et journalisation des classements | Bonne pratique ; art. 12 (si haut risque) | 2027-12-02 | S | Registre des versions, extrait de journal |
| P4 | AIA-006 | Recenser et compléter les mesures de maîtrise de l'IA | Art. 4 (en vigueur) | En vigueur | S | Supports, liste des personnes formées |
| P4 | AIA-007 | Dater la mise en service ; qualifier les réentraînements | Art. 111, par. 2 `[AV]` | CAL-013 conditionnel | S | Document daté, analyse juridique |
| P4 | AIA-008 | Contrôle d'intégrité du fichier de modèle | Bonne pratique (art. 15 si haut risque) | n.a. | S | Code et test de vérification d'empreinte |

AIA-001 et AIA-002 sont classés P2 plutôt que P3. L'échéance du 2027-12-02 est à plus de 6 mois, mais le risque potentiel pour les personnes est significatif dès l'utilisation. Par ailleurs, la classification conditionne tout le reste. L'art. 4, déjà en vigueur, est classé P4 en raison de la gravité Faible retenue ; il reste à traiter sans délai, à faible effort.

**Jalon** : le 2027-12-02 (CAL-011, confiance moyenne), les exigences du haut risque de l'annexe III s'appliquent si la classification est confirmée et sous réserve de CAL-013. Les actions AIA-001 à AIA-005 doivent être terminées avant cette date.

## 11. Limites de l'audit

- **Analyse statique.** Le comportement réel, les données d'entraînement, le modèle sérialisé (`models/ranker.joblib`, absent) et la configuration de production n'ont pas été observés. Aucun code appelant `rank_candidates` n'est présent.
- **Documents organisationnels non disponibles dans le dépôt** : fiche de destination, contrats, politiques, formations, registre des risques, documentation technique, rapports d'évaluation.
- **Contexte très incomplet** (aveu du README). La classification est indéterminée et repose sur des hypothèses.
- **Références juridiques** : les entrées de confiance moyenne ou faible sont à confirmer sur le Journal officiel : CAL-003, CAL-004, CAL-010, CAL-011, CAL-012, CAL-013, CAL-016. Les modifications du règlement 2026/1744 reposent sur des sources secondaires, et aucune version consolidée n'a été consultée.
- **Textes évolutifs** : lignes directrices sur la classification à haut risque (projet de mai 2026, non définitif), normes harmonisées et actes d'exécution.
- **Hors périmètre** : les autres législations (protection des données, non-discrimination, droit du travail) sont seulement signalées.
- **Nature du rapport** : il ne remplace ni l'avis d'un juriste ni une évaluation de la conformité au sens de l'article 43.

## 12. Suivi (ré-audit)

Aucun audit précédent. Ce premier audit établit les identifiants AIA-001 à AIA-011, à conserver lors des audits ultérieurs.

| Constat | Statut précédent | Statut actuel | Preuve |
|---|---|---|---|
| AIA-001 à AIA-011 | n.a. | Nouveau | Présent rapport |
