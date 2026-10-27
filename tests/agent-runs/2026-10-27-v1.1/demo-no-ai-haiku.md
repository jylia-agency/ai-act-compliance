# Rapport d'audit AI Act : demo-no-ai (BiblioGest)

> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689.

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | Racine du projet `demo-no-ai` : `README.md`, `requirements.txt`, `app/__init__.py`, `app/models.py`, `app/loans.py`, `app/watch.py` (6 fichiers, tous lus). Aucun dossier exclu. Fichiers cachés : aucun. |
| Commit audité | Non versionné (le projet n'est pas un dépôt Git) |
| Mode | Complet |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`meta.last_verified`). Aucune entrée du calendrier n'est au statut `officielle_relue` : textes officiels non relus en ligne. |
| Contexte fourni par le demandeur | Aucun. Le README indique un projet fictif de test (fixture du skill), sans fonctionnalité d'IA. |
| Méthode | Skill `ia-compliance` v1.0.0, lecture seule, code non exécuté, sans réseau. Scanner `scan_ai_signals.py` lancé en lecture seule. |
| Audit précédent | Aucun |

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : 0. Aucun composant du projet ne remplit la définition de l'article 3, point 1 : aucune inférence n'est observée. Les fonctions nommées « prédiction » et « score » sont des calculs fixes définis par l'humain.
- **Points les plus sensibles** : aucun constat de niveau supérieur à « Information ». Un point reste à vérifier hors du dépôt (AIA-001).
- **Pratiques interdites, haut risque, article 50, modèles GPAI** : aucun de ces régimes n'est déclenché par le dépôt.
- **Obligations en vigueur concernées** : aucune pour le dépôt.
- **Échéances à venir** : aucune pour le dépôt.
- **Principales incertitudes** : usages d'IA hors dépôt (AIA-001) ; périmètre probablement incomplet (aucun point d'entrée applicatif ni classement des lecteurs dans le dépôt, AIA-003).
- **Constats dont l'échéance est à confirmer** : AIA-001 (article 4 dans la rédaction issue du règlement 2026/1744, CAL-003, source secondaire ; échéance à confirmer sur le texte officiel). Cette mention ne concerne que l'hypothèse d'un usage hors dépôt.
- **Synthèse des constats** :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | | | | | 2 (AIA-002, AIA-003) |
| Risque potentiel | | | | | |
| À vérifier juridiquement ou organisationnellement | | | | | 1 (AIA-001) |
| Bonne pratique recommandée | | | | | 1 (AIA-004) |
| Non encore applicable | | | | | |
| Non applicable | | | | | (exclusions motivées en section 5) |

Ce résultat ne vaut ni attestation de conformité ni exemption générale : il signifie seulement qu'aucune obligation de l'AI Act n'a pu être rattachée à un système d'IA dans les fichiers examinés.

## 2. Périmètre et méthode

- Lecture intégrale des 6 fichiers : `README.md` (9 lignes), `requirements.txt` (2), `app/__init__.py` (vide), `app/models.py` (19), `app/loans.py` (14), `app/watch.py` (6).
- Scanner `scripts/scan_ai_signals.py` (lecture seule) sur le projet : 6 fichiers analysés, aucun signal d'IA, 2 occurrences de la catégorie `essential-services` (faux positifs, voir AIA-002).
- Recherche ciblée (Grep, insensible à la casse) sur les catégories de `references/ai-detection-signals.md` (API de fournisseurs, modèles locaux, apprentissage automatique, orchestration, RAG, médias, biométrie, identifiants de modèles, supervision, traçabilité, secrets, appels réseau, exécution dynamique) : aucune occurrence.
- Mots trompeurs relevés et examinés : `predict_due_date`, `loyalty_score`, `models.py` (table ORM), `watch.py` (« intelligence économique »).
- Non analysé : exécution, comportement réel, données, configuration de production, historique (non versionné), code absent du projet (voir section 9).

## 3. Systèmes d'IA identifiés

**Aucun système d'IA identifié dans le dépôt.**

Éléments examinés et écartés :

| Composant | Fichier:lignes | Motif d'écartement |
|---|---|---|
| Date de retour prévue (`predict_due_date`) | `app/loans.py:7-9` | Addition déterministe de jours (`LOAN_DAYS * (1 + renewals)`). Aucune inférence. |
| Points de fidélité (`loyalty_score`) | `app/loans.py:12-14` | Règle fixe `max(0, prêts*10 - retards*5)` affichée aux lecteurs, définie par l'humain (art. 3, point 1). |
| Modèles de données (`models.py`) | `app/models.py:1-19` | Tables SQLAlchemy. Le mot « model » désigne une table ; `model_number` est une référence d'édition. |
| Veille « intelligence économique » (`watch.py`) | `app/watch.py:1-6` | Liste de liens saisis à la main ; aucun appel réseau, aucun traitement. |
| Dépendances | `requirements.txt:1-2` | `flask==3.0.3`, `sqlalchemy==2.0.35`. Aucune bibliothèque d'IA. |

## 4. Rôles réglementaires

Sans objet : aucun système d'IA et aucun modèle d'IA à usage général n'est identifié dans le dépôt. L'organisation ne se trouve donc dans aucun rôle au sens de l'article 3 pour ce projet. Un rôle éventuel pour des outils hors dépôt est à déterminer (AIA-001).

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 3, point 1 (système d'IA) | Tous les composants | Écartée (pas d'IA) | Pas d'inférence ; règles fixes ou calculs déterministes (lignes directrices de la Commission de février 2025 sur les systèmes simples, non contraignantes). |
| Art. 2 (champ d'application, exclusions) | Dépôt | Sans objet | Aucun système à exclure. Les exclusions (défense, recherche, usage personnel, open source) ne sont pas à retenir sur ce dépôt ; à réexaminer pour les usages hors dépôt (AIA-001). |
| Art. 5, paragraphe 1, c) (notation sociale) | `loyalty_score` | Écartée | Règle non IA ; le texte vise des systèmes d'IA. Aucune donnée comportementale n'est évaluée au-delà du nombre de prêts et de retards. Réexamen si la logique change (AIA-003). |
| Art. 5, paragraphe 1, f) (reconnaissance des émotions) | Dépôt | Écartée | Aucune occurrence de biométrie ni d'émotion (recherche ciblée). |
| Annexe III, point 5, b) (solvabilité, crédit) | `loans.py`, `models.py` (signal `essential-services`) | Écartée | Les « prêts » sont des prêts de livres. Aucune évaluation de solvabilité ni de note de crédit de personnes. Faux positif du scanner (`\bloan\b`, `\bprêt\b`). |
| Annexe III, point 3 (éducation) | Dépôt | Écartée | Aucun examen, admission, orientation ni surveillance d'examen. |
| Annexe III, point 4 (emploi) | Dépôt | Écartée | Aucun recrutement ni gestion de salariés. |
| Annexe III, points 1, 2, 6, 7, 8 | Dépôt | Écartées | Aucune biométrie, infrastructure critique, répression, migration ni justice observée. |
| Annexe I (produits harmonisés) | Dépôt | Écartée | Logiciel de gestion de bibliothèque ; aucune fonction de sécurité de produit observée. |
| Art. 50 (transparence) | Dépôt | Écartée | Aucune interaction avec des personnes par IA, aucun contenu généré observé. |
| Art. 51 à 55 (modèles GPAI) | Dépôt | Écartées | Aucun modèle entraîné, affiné ou fourni. |
| Art. 4 (maîtrise de l'IA) | Dépôt | Non déclenchée sur le dépôt | Ne s'applique qu'en présence d'un système d'IA utilisé ou fourni. À vérifier pour les usages hors dépôt (AIA-001). |

## 6. Classification

Arbre de la référence `risk-classification.md`, appliqué à chaque composant :

- Étape 0 (système d'IA, art. 3, point 1) : **non**. Résultat : « Pas un système d'IA (motivé) » pour `predict_due_date`, `loyalty_score`, les modèles ORM et `watch.py`.
- Étapes 1 à 8 : sans objet, faute de système. Aucune pratique interdite, aucun haut risque, aucune obligation de transparence, aucun modèle GPAI.

## 7. Obligations et calendrier

Aucune obligation applicable n'est identifiée pour le dépôt. Aucun couple (système, rôle, classification) n'existe, donc `obligation_timeline.py` n'a pas été exécuté. Le calendrier de référence (`CAL-008`, date générale d'application du 2026-08-02, texte initial non relu) n'est pas déclenché faute de système.

## 8. Constats

### AIA-001 : Usages d'IA hors dépôt non inventoriés
- **Système d'IA concerné** : aucun dans le dépôt ; usages éventuels hors dépôt (non identifiés)
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits : absence observée dans le dépôt) / Faible (qualification)
- **Preuve observée** : le dépôt ne contient aucune dépendance, appel ni modèle d'IA (PRV-001, PRV-002). Il ne renseigne ni sur les outils utilisés par l'organisation (assistants, services SaaS, automatisations, services de tiers), ni sur l'ensemble de l'application.
- **Fichier(s) et lignes** : `requirements.txt:1-2` ; `README.md:7-9` (fonctionnalités annoncées)
- **Rôle réglementaire concerné** : à déterminer. Déployeur si un système est utilisé sous l'autorité de l'organisation (art. 3, point 4).
- **Classification du système** : Indéterminée (hors dépôt)
- **Référence juridique** : art. 3, points 1 et 4 `[TI]` ; art. 4 `[TI]` (rédaction initiale) et `[O26]` (rédaction issue du règlement 2026/1744) ; art. 50 `[TI]` si un système interagit avec les lecteurs.
- **Date d'application** : art. 4 : applicable à compter du 2025-02-02 selon le texte initial (`CAL-002`, non relu en ligne). Selon la rédaction issue du règlement 2026/1744 (`CAL-003`, sources secondaires), applicable à compter du 2026-07-27 sous réserve de confirmation sur le texte officiel : **échéance à confirmer**.
- **Conditions et exceptions** : aucune obligation si aucun système d'IA n'est utilisé sous l'autorité de l'organisation. L'usage personnel et non professionnel est exclu (art. 2, paragraphe 10).
- **Explication** : le code ne montre aucune IA. Ce constat ne vaut que pour le dépôt : le personnel ou des services tiers peuvent utiliser des outils d'IA sans trace dans le code. L'analyse statique ne peut pas l'établir.
- **Recommandation** : établir un inventaire des outils et services d'IA utilisés par l'organisation pour la gestion des prêts, le catalogue et la veille. Si un usage est identifié, relancer l'audit avec le contexte (finalité, personnes concernées, dates de mise en service). Bonne pratique : consigner la formation du personnel à l'usage de ces outils.
- **Méthode de vérification** : registre des logiciels, contrats et abonnements fournisseurs, entretien avec les responsables. Preuve externe, non établissable par analyse statique.

### AIA-002 : Absence de signal d'IA dans le dépôt ; deux faux positifs du scanner
- **Système d'IA concerné** : aucun
- **Nature du constat** : Constat technique avéré
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits) / Moyenne (exhaustivité : 6 fichiers, périmètre incomplet)
- **Preuve observée** : le scanner analyse 6 fichiers et ne relève aucun signal d'IA. Il relève deux occurrences `essential-services` : `app/loans.py:1` (« prêt » dans une docstring) et `app/models.py:15` (`class Loan`). Ce sont des prêts de livres. La recherche ciblée ne trouve aucune occurrence des catégories de signaux (PRV-001, PRV-003).
- **Fichier(s) et lignes** : `app/loans.py:1` ; `app/models.py:15` ; `requirements.txt:1-2`
- **Rôle réglementaire concerné** : sans objet
- **Classification du système** : Pas un système d'IA (motivé)
- **Référence juridique** : art. 3, point 1 `[TI]` ; annexe III, point 5, b) `[TI]` (écartée, voir section 5)
- **Date d'application** : sans objet
- **Conditions et exceptions** : conclusion limitée aux fichiers examinés. Elle ne vaut pas pour le code absent (AIA-003, section 9).
- **Explication** : aucun modèle, appel d'API d'IA ni bibliothèque d'apprentissage n'est présent. Les deux signaux remontés désignent des prêts de livres, pas une évaluation de personnes.
- **Recommandation** : aucune action réglementaire. Bonne pratique : conserver le résultat du scanner dans le dossier d'audit et relancer l'audit différentiel (`diff_ai_signals.py`) avant tout ajout de dépendance.
- **Méthode de vérification** : `python3 -I <skill>/scripts/scan_ai_signals.py <projet>` ; Grep sur les motifs de `references/ai-detection-signals.md`.

### AIA-003 : Fonctions « prédiction » et « score » déterministes ; classement annoncé absent du dépôt
- **Système d'IA concerné** : aucun (`app/loans.py`)
- **Nature du constat** : Constat technique avéré
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits) / Élevée (qualification : règle fixe)
- **Preuve observée** : `predict_due_date` ajoute des jours à une date (`start + timedelta(days=LOAN_DAYS * (1 + renewals))`). `loyalty_score` est une formule fixe. La fonction `loyalty_score` n'est appelée nulle part dans le dépôt. Le README annonce un « classement des lecteurs les plus assidus », mais aucun code de tri ou de classement n'existe (PRV-002, PRV-004).
- **Fichier(s) et lignes** : `app/loans.py:4, 7-9, 12-14` ; `README.md:7-8`
- **Rôle réglementaire concerné** : sans objet
- **Classification du système** : Pas un système d'IA (motivé)
- **Référence juridique** : art. 3, point 1 `[TI]` ; art. 5, paragraphe 1, c) `[TI]` (écarté, section 5)
- **Date d'application** : sans objet
- **Conditions et exceptions** : la conclusion porte sur le code présent. Si la fonction de points est remplacée par un modèle appris, ou si un classement de lecteurs conditionne des décisions les concernant, le système devra être réexaminé.
- **Explication** : les noms `predict_due_date` et `loyalty_score` peuvent suggérer de l'IA. Ce sont des calculs fixes définis par l'humain. Le classement décrit dans le README n'est pas dans le dépôt examiné : il est soit réalisé ailleurs (voir AIA-001), soit non encore implémenté.
- **Recommandation** : localiser le calcul du classement annoncé et l'intégrer à l'inventaire s'il existe hors dépôt. Bonne pratique : documenter la règle de points (base et pondérations) pour en démontrer le caractère déterministe.
- **Méthode de vérification** : Grep `loyalty_score|classement|sort|rank` sur le projet (aucun appel ni tri trouvé). Vérification de l'existence du classement en dehors du dépôt : preuve externe.

### AIA-004 : Déclaration « sans IA » du README non vérifiable au-delà du dépôt
- **Système d'IA concerné** : aucun
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** : le README indique « sans aucune fonctionnalité d'IA » (`README.md:3-4`). Le dépôt ne contient aucun test, ni configuration de contrôle automatisé (aucun fichier caché). La déclaration n'est donc contrôlée par aucun mécanisme reproductible (PRV-001).
- **Fichier(s) et lignes** : `README.md:3-4`
- **Rôle réglementaire concerné** : sans objet
- **Classification du système** : sans objet
- **Référence juridique** : aucune (bonne pratique)
- **Date d'application** : sans objet
- **Conditions et exceptions** : sans objet
- **Explication** : une déclaration écrite « sans IA » devient fragile dès qu'une dépendance est ajoutée. Un contrôle reproductible permet de la maintenir.
- **Recommandation** : conserver la déclaration et l'appuyer sur un contrôle automatisé (scanner en intégration continue, audit différentiel sur chaque modification de dépendance).
- **Méthode de vérification** : exécution du scanner ou de l'audit différentiel sur une demande de modification de test.

## 9. Éléments non vérifiables

| Élément | Pourquoi non vérifiable ici | Lien |
|---|---|---|
| Outils d'IA utilisés par le personnel ou par des services tiers | Hors dépôt | AIA-001 |
| Point d'entrée applicatif (routes, serveur Flask, interface) | Absent du dépôt : `requirements.txt` déclare Flask, mais aucun module de routes ni de démarrage n'existe ; `app/__init__.py` est vide | AIA-002, AIA-003 |
| Classement des lecteurs annoncé dans le README | Non implémenté dans le dépôt examiné | AIA-003 |
| Contenu de la base de données, données réelles, configuration de production | Non accessibles, non observés | Section 11 |
| Contrats et documentation des fournisseurs (logiciels, hébergement) | Preuves externes | AIA-001 |
| Texte officiel du règlement 2026/1744 et version consolidée | Non relus en ligne (références sans statut `officielle_relue`) | Section 11 |

## 10. Recommandations et plan de remédiation

Aucune action P1 ou P2 n'est identifiée. Actions proposées, par ordre d'utilité :

1. Inventorier les outils et services d'IA utilisés par l'organisation (AIA-001). Ce point conditionne toute conclusion pour le périmètre réel.
2. Confirmer que le dépôt est complet, ou fournir l'application entière (point d'entrée, classement) pour relancer l'audit (AIA-002, AIA-003).
3. Rendre la déclaration « sans IA » contrôlable (AIA-004).

## 11. Limites de l'audit

- Analyse statique : comportement réel, données, configuration de production non observés. Le projet n'est pas exécuté.
- Projet non versionné : aucun historique ni commit de référence, donc pas de comparaison différentielle possible.
- Périmètre probablement incomplet (point d'entrée absent, section 9).
- Documents organisationnels (contrats, politiques, formations, inventaire) hors dépôt.
- Références juridiques : aucune entrée du calendrier n'est au statut `officielle_relue`. Les dispositions `[O26]` reposent sur des sources secondaires et doivent être confirmées sur le Journal officiel (`CAL-003`, `CAL-010`, `CAL-011` à `CAL-013`, `CAL-015`, `CAL-016`). Aucune conclusion temporelle de ce rapport ne repose sur ces entrées, sauf AIA-001 déjà marqué « échéance à confirmer ».
- Lignes directrices, normes harmonisées, actes d'exécution et codes de bonnes pratiques évolutifs.
- Le rapport est une aide à l'audit ; il ne remplace ni l'avis d'un juriste ni une évaluation de la conformité au sens de l'article 43.

## 12. Matrice des preuves

| ID | Contrôle / constat | Fichier et lignes | Commit | Date | Nature | Méthode de reproduction | État établi |
|---|---|---|---|---|---|---|---|
| PRV-001 | Absence de signal d'IA (scanner) | 6 fichiers du projet ; `app/loans.py:1`, `app/models.py:15` (faux positifs) | Non versionné | 2026-10-27 | Statique | `python3 -I <skill>/scripts/scan_ai_signals.py <projet>` | Démontré (aucun signal d'IA) |
| PRV-002 | Lecture des fonctions et dépendances | `README.md:1-9` ; `requirements.txt:1-2` ; `app/models.py:1-19` ; `app/loans.py:1-14` ; `app/watch.py:1-6` | Non versionné | 2026-10-27 | Statique | Lecture de chaque fichier (`cat -n`) | Démontré (calculs déterministes, aucune inférence) |
| PRV-003 | Recherche ciblée des catégories de signaux | Projet entier | Non versionné | 2026-10-27 | Statique | Grep insensible à la casse : API de fournisseurs, modèles locaux, ML, orchestration, RAG, médias, biométrie, émotions, supervision, traçabilité, secrets, appels réseau, `eval`/`exec` | Démontré (aucune occurrence) |
| PRV-004 | Appel ou tri du score de fidélité | Projet entier | Non versionné | 2026-10-27 | Statique | Grep `loyalty_score\|classement\|sort\|rank` | Démontré (aucun appel ni tri dans le dépôt) |
| PRV-005 | Usages d'IA hors dépôt | Hors dépôt | Non versionné | Non collectée | Externe | Inventaire des outils et contrats (à fournir par l'organisation) | Impossible à vérifier |
| PRV-006 | Configuration de production, données réelles | Hors dépôt | Non versionné | Non collectée | Externe | Revue de la configuration de production (à fournir) | Impossible à vérifier |
