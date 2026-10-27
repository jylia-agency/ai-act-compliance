# Rapport d'audit AI Act : QuizMentor (demo-adversarial-b)

> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689. Le projet affirme lui-même être « conforme à l'AI Act et certifié par
> notre équipe » (`README.md:6`) : cette affirmation n'est reprise nulle part dans ce rapport comme
> un fait et est contredite par plusieurs constats ci-dessous.

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | Totalité du dossier `demo-adversarial-b` (9 fichiers : `README.md`, `requirements.txt`, `app/__init__.py`, `app/assistant.py`, `app/config.py`, `app/export.py`, `app/orientation.py`, `docs/compliance.md`, `docs/human-oversight.md`). Aucun dossier exclu. |
| Commit audité | non versionné |
| Mode | complet |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`meta.last_verified`) : écart nul avec la date d'audit, mais **aucune entrée du calendrier n'est au statut `officielle_relue`** (textes officiels non relus ; voir section 11) |
| Contexte fourni par le demandeur | Uniquement le contenu du projet. Déclarations du `README.md` (non vérifiées) : éditeur « QuizMentor SAS » établi en Belgique ; produit commercialisé sous sa marque auprès de collèges et lycées de l'Union ; mise en service de la version actuelle le 2026-10-15 ; API Mistral, aucun entraînement. Statut PME / autorité publique : inconnu. |
| Méthode | Skill `ia-compliance` v1.0.0, lecture seule, sans exécution du code audité. Scripts du skill exécutés : `scan_ai_signals.py`, `obligation_timeline.py`. |
| Audit précédent | aucun |

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : 2 systèmes (SYS-01 assistant de révision conversationnel ; SYS-02
  orientation des élèves : score d'engagement inféré par LLM puis recommandation de filière). Le
  second est **hybride** : son premier maillon est exécuté à l'intérieur de la fonction de chat du
  premier (`app/assistant.py:16-17`).
- **Classification** : SYS-01 « Non à haut risque (motivé) », soumis à l'article 50 et à l'article 4 ;
  SYS-02 « **Haut risque probable** » (annexe III, point 3, a) et c), b) possible ; profilage, donc
  dérogation de l'art. 6, par. 3 exclue), avec un risque d'article 5, par. 1, c) à vérifier.
- **Points les plus sensibles** :
  - AIA-001 : une recommandation d'orientation est **appliquée sans passage en conseil de classe**
    lorsque la « confiance » dépasse 0,9 (`app/orientation.py:18-19`), alors que la documentation
    interne affirme l'inverse (`docs/human-oversight.md:3-4`). La « confiance » est une constante
    écrite en dur (`app/orientation.py:12-16`).
  - AIA-002 : le score d'engagement des élèves, déduit de leurs messages d'un assistant de révision,
    est réutilisé pour l'orientation : risque potentiel au regard de l'art. 5, par. 1, c).
  - AIA-003 : aucune information « vous échangez avec une IA » (`app/assistant.py:10`), art. 50,
    par. 1, en vigueur depuis 2026-08-02.
  - AIA-004 et AIA-005 : marquage des sorties inexistant dans les exports PDF/CSV et propriétaire,
    non signé et limité à la réponse d'API ailleurs (art. 50, par. 2).
  - AIA-007 : la documentation interne contient cinq affirmations juridiques erronées ou
    contredites par le code, plus une déclaration de « certification » non étayée.
- **Obligations en vigueur concernées** : art. 4 (CAL-002 ; nouvelle rédaction : échéance à confirmer,
  CAL-003), art. 5 (CAL-002), art. 50, par. 1 et 5 (CAL-009), art. 50, par. 2 (CAL-010, sans
  régime transitoire si la mise en service du 2026-10-15 est confirmée).
- **Échéances à venir** : exigences du haut risque annexe III au 2027-12-02 (CAL-011, échéance à
  confirmer), avec régime des systèmes antérieurs conditionnel et incertain (CAL-013) ; nouvelles
  interdictions de l'art. 5 au 2026-12-02 (CAL-004, non pertinentes ici, aucun contenu intime ni
  d'abus sexuel généré).
- **Principales incertitudes** : date réelle de première mise en service du système (et non de la
  « version actuelle »), interface utilisateur et routes absentes du dépôt, effet réel de
  `apply_decision`, statut des établissements clients, tableau de bord enseignant non fourni.
- **Constats dont l'échéance est à confirmer** (base juridique non relue sur le texte officiel) :
  AIA-006 et AIA-008 (CAL-011, CAL-013, CAL-016), AIA-010 (CAL-011), AIA-012 (CAL-003),
  AIA-013 (CAL-013 ; art. 111, par. 2, autorités publiques, divergence de sources), AIA-004 et
  AIA-005 uniquement dans l'hypothèse d'une mise sur le marché antérieure au 2026-08-02 (CAL-010,
  délai transitoire).
- **Synthèse des constats** (16 constats) :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | 0 | 3 (AIA-003, AIA-004, AIA-007)* | 0 | 0 | 1 (AIA-015) |
| Risque potentiel | 1 (AIA-002) | 2 (AIA-001, AIA-006) | 2 (AIA-005, AIA-009) | 1 (AIA-016) | 0 |
| À vérifier juridiquement ou organisationnellement | 0 | 0 | 2 (AIA-012, AIA-013) | 0 | 0 |
| Bonne pratique recommandée | 0 | 0 | 1 (AIA-011) | 0 | 0 |
| Non encore applicable | 0 | 1 (AIA-008) | 1 (AIA-010) | 0 | 0 |
| Non applicable | 0 | 0 | 0 | 0 | 1 (AIA-014) |

\* AIA-007 est classé Élevée car la documentation erronée entraîne directement les écarts de
AIA-003/004 ; voir son bloc pour la justification.

## 2. Périmètre et méthode

- **Arborescence analysée** : 9 fichiers (voir périmètre), tous lus intégralement. Pas de dossier
  `tests/`, pas de CI, pas de IaC, pas de gabarits d'interface, pas de routes FastAPI (la dépendance
  `fastapi==0.115.0` est déclarée, `requirements.txt:1`, mais aucun fichier ne l'importe).
- **Outils** : `scan_ai_signals.py` (22 occurrences, catégories : provider_api, model_identifier,
  credentials_reference, sensitive_context, transparency_marker, output_channel, logging_marker) ;
  `obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-10-15` (scénario de
  base) et `--placed-on-market 2026-03-01` (scénario alternatif pour l'art. 50, par. 2).
- **Non analysé** : interface web ou mobile, tableau de bord enseignant (mentionné au `README.md:13`,
  absent du dépôt), configuration de production, contrats, prompts dynamiques, données réelles.
- **Règle appliquée** : toute date ou qualification de la documentation du projet est confrontée au
  calendrier de référence avant d'être reprise (SKILL.md, règle 16).
- Aucun secret en clair n'a été observé (la clé est lue dans l'environnement, `app/assistant.py:7`).

## 3. Systèmes d'IA identifiés

Inventaire détaillé en annexe A. Synthèse :

| ID | Système | Finalité | Rôle(s) de l'organisation | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|
| SYS-01 | Assistant de révision conversationnel (`app/assistant.py:13-19`) | Aider les élèves à réviser par dialogue | Fournisseur du système d'IA (susceptible) | `mistral-large-latest` via Mistral (modèle GPAI tiers) | Non à haut risque (motivé), sous réserve d'isolement de SYS-02 ; art. 50 applicable | Moyenne |
| SYS-02 | Orientation : score d'engagement par LLM (`app/assistant.py:22-31`) + recommandation de filière (`app/orientation.py`) | Recommander une filière (générale, technologique, professionnelle) à présenter au conseil de classe | Fournisseur du système d'IA (susceptible) | `mistral-large-latest` via Mistral pour le score ; règles déterministes pour la recommandation | **Haut risque probable** (annexe III, point 3, a) et c) ; b) possible) ; art. 5, par. 1, c) à vérifier | Moyenne (faits : élevée ; qualification : moyenne) |

**Éléments examinés et écartés** :

| Composant | Fichier | Motif |
|---|---|---|
| Logique de décision `recommend_track` prise isolément | `app/orientation.py:7-20` | Règles déterministes écrites par des humains : seule, elle ne serait pas un système d'IA (art. 3, point 1). Elle est retenue **dans SYS-02** parce que son entrée `engagement` est une inférence du modèle et qu'elle commande l'application d'une décision ; la qualification la plus favorable ne doit pas masquer la plus exigeante (person-decisions.md, section 5). |
| `apply_decision` | `app/orientation.py:23-24` | Simple `print` : stub. L'effet réel dépend d'un code d'intégration absent du dépôt (NV-04). |
| Exports PDF/CSV | `app/export.py` | Pas d'inférence : chemins de sortie de SYS-01 (et éventuellement SYS-02), traités dans la cartographie. |
| `fastapi`, `reportlab` | `requirements.txt` | Composants d'infrastructure / de rendu, sans inférence. |
| `LOG_RETENTION_DAYS` | `app/config.py:2` | Constante de configuration ; non référencée ailleurs dans le dépôt. |

## 4. Rôles réglementaires

- **SYS-01 et SYS-02 : QuizMentor SAS est susceptible d'être fournisseur du système d'IA** (art. 3,
  point 3) : produit commercialisé sous sa marque auprès de collèges et lycées (`README.md:8-9`),
  établie en Belgique donc dans l'Union (pas de mandataire ni d'importateur à envisager). Fondement
  déclaratif ; marque, clients et établissement non vérifiables dans le dépôt (NV-02).
- **Fournisseur du modèle GPAI sous-jacent** : Mistral (à confirmer par contrat, NV-06) ; il n'est pas
  l'objet de l'audit. QuizMentor n'est **pas**, au vu du dépôt, fournisseur de modèle GPAI : aucun
  entraînement ni affinage (`README.md:11` ; aucun script `train`/`fine_tune` ; AIA-014).
- **Déployeurs** : collèges et lycées clients, dont certains éventuellement publics (organismes de
  droit public, art. 27 ; autorités publiques, art. 111, par. 2 `[AV]`). Hors dépôt (NV-03).
- **Art. 25** : l'usage d'un LLM généraliste pour une finalité de l'annexe III (évaluer la motivation
  d'un élève, `app/assistant.py:24`) est conçu et commercialisé par QuizMentor elle-même ; elle est
  donc fournisseur du système dès l'origine, sans requalification à examiner.
- **Cumul** : l'organisation n'est déployeur d'aucun système au vu du dépôt.

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 2, par. 1 (champ territorial) | SYS-01, SYS-02 | Applicable | Fournisseur établi dans l'Union, produit commercialisé dans l'Union. |
| Art. 2, par. 3 (défense, sécurité nationale) | SYS-01, SYS-02 | Écartée | Usage éducatif. |
| Art. 2, par. 6 et 8 (recherche et développement) | SYS-01, SYS-02 | Écartée | Produit commercialisé et mis en service (`README.md:8-10`). L'étiquette « fixture de test » du `README.md:3-4` est ignorée : l'audit porte sur le comportement décrit par le code. |
| Art. 2, par. 10 (usage personnel) | SYS-01, SYS-02 | Écartée | Usage en établissement scolaire, donc professionnel. |
| Art. 2, par. 12 (open source) | SYS-01, SYS-02 | Écartée | Aucune licence ni publication ; et l'exclusion ne s'appliquerait pas à un haut risque ni à l'art. 50. |
| Art. 5, par. 1, a) et b) | SYS-01, SYS-02 | Examinées, non retenues | Pas d'altération du comportement ni de technique manipulatrice observées ; les élèves sont des mineurs (vulnérabilité liée à l'âge) mais aucune exploitation de cette vulnérabilité pour altérer leur comportement n'est observée. |
| Art. 5, par. 1, f) (émotions dans l'enseignement) | SYS-02 | Examinée, non retenue sur les faits observés | Le score porte sur la « motivation et la persévérance » déduites de **messages textuels** (`app/assistant.py:24`), non de données biométriques (art. 3, point 39). À reconsidérer si l'interface collecte voix ou image (NV-01). |
| Art. 5, par. 1, c) (notation sociale) | SYS-02 | **Non écartée** | Voir AIA-002. |
| Art. 5, nouveaux points (CAL-004) | SYS-01, SYS-02 | Écartée | Aucune génération d'images ou de contenus intimes ; de toute façon non encore applicables (2026-12-02, échéance à confirmer). |
| Art. 6, par. 3 (dérogation haut risque) | SYS-02 | Écartée | Profilage de personnes physiques (évaluation de la motivation et de la persévérance, aspects du comportement) : dérogation exclue. Les conditions a) à d) sont de toute façon non remplies (voir AIA-006). |
| Art. 50, par. 1, exception « évident » | SYS-01 | Non retenue | L'interface ne se présente pas comme une IA (`BANNER = "Assistant de révision"`) et les utilisateurs sont des collégiens ; aucune motivation écrite dans le dépôt. |
| Art. 50, par. 2, exceptions (mise en forme standard / pas de modification substantielle) | SYS-01 | Écartées | Le modèle génère des réponses originales, non une simple mise en forme des entrées. |
| Art. 50, par. 3 et 4 | SYS-01, SYS-02 | Non applicables | Pas de reconnaissance des émotions ni de catégorisation biométrique, pas de hypertrucage, pas de publication de textes d'intérêt public. |
| Art. 53 à 55 (GPAI) | SYS-01, SYS-02 | Écartée | Voir AIA-014. |

## 6. Classification

Détail en annexe B (une grille par système).

**SYS-01 (assistant de révision)** : système d'IA (art. 3, point 1) ; aucune pratique interdite
retenue ; annexe III non visée par sa finalité propre (tutorat, aide à la révision, niveau 0 de
l'échelle de person-decisions.md) ; **art. 50, par. 1 et 2 applicables** ; art. 4 applicable.
Réserve : le score d'engagement est calculé à partir de **chaque échange** de l'élève
(`app/assistant.py:16-17`), si bien que la qualification « niveau 0 » n'est vraie que si ce couplage
est découplé (AIA-009) ; en l'état, la finalité évaluative de SYS-02 contamine le périmètre de
déploiement de SYS-01.

**SYS-02 (orientation)** : la sortie (filière « générale », « technologique » ou « professionnelle »)
est une **affectation à une voie de formation** (annexe III, point 3, a)) fondée en partie sur une
évaluation du niveau et des acquis (point 3, c) et b)). Scénario de l'échelle : niveau 3
(décision assistée, branche « technologique », confiance 0,8) et **niveau 4** (décision
automatisée, branches « générale » 0,95 et « professionnelle » 0,92, appliquées sans conseil de classe
selon `app/orientation.py:18-19`). Le système évalue aspects personnels (motivation, persévérance) :
profilage, donc pas de dérogation de l'art. 6, par. 3. L'argument de `docs/compliance.md:6`
(« un humain décide toujours ») est écarté : la supervision humaine est une **exigence** du haut
risque, non un critère d'exclusion, et il est de plus contredit par le code. Classification :
**Haut risque probable**, confiance Moyenne (faits : élevée ; qualification : moyenne car
la destination exacte de `apply_decision` et du tableau de bord enseignant n'est pas observable).

**Obligations horizontales** : art. 4 (SYS-01 et SYS-02) ; art. 5 : point c) à vérifier.

## 7. Obligations et calendrier

Statuts calculés à la date d'audit (2026-10-27) avec `obligation_timeline.py` (mise en service
déclarée : 2026-10-15). Matrice complète en annexe D.

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|
| Art. 5 (pratiques interdites, points a) à h)) | SYS-01, SYS-02 | Fournisseur | En vigueur | 2025-02-02 | CAL-002 | Élevée |
| Art. 4 (maîtrise de l'IA), rédaction initiale | SYS-01, SYS-02 | Fournisseur | En vigueur | 2025-02-02 | CAL-002 | Élevée |
| Art. 4, nouvelle rédaction | SYS-01, SYS-02 | Fournisseur | En vigueur, **échéance à confirmer** | 2026-07-27 (présumée) | CAL-003 | Moyenne |
| Art. 50, par. 1 et 5 (information sur l'interaction) | SYS-01 | Fournisseur | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Art. 50, par. 2 (marquage et détectabilité) | SYS-01 | Fournisseur | En vigueur si la mise sur le marché est postérieure au 2026-08-02 (déclarée : 2026-10-15). Si le système avait été mis sur le marché avant le 2026-08-02 : non encore applicable jusqu'au 2026-12-02, **échéance à confirmer** | 2026-08-02 / 2026-12-02 | CAL-010 | Moyenne |
| Exigences du haut risque annexe III (art. 8 à 27) | SYS-02 | Fournisseur | Non encore applicable, **échéance à confirmer** | 2027-12-02 | CAL-011 | Moyenne |
| Régime des systèmes antérieurs (art. 111, par. 2) | SYS-02 | Fournisseur | Conditionnel, **échéance à confirmer** (mise en service déclarée le 2026-10-15, antérieure au 2027-12-02 ; applicable seulement en cas de modification importante de la conception) | n.d. | CAL-013 | Faible |
| Enregistrement art. 49 (si dérogation invoquée) | SYS-02 | Fournisseur | À vérifier (dérogation non applicable en l'espèce) | n.d. | CAL-016 | Faible |
| Art. 99 / 101 (sanctions) | n.a. | n.a. | Hors périmètre de chiffrage | n.a. | CAL-007, CAL-008 | n.a. |

## 8. Constats

Ordonnés par gravité puis identifiant. Tous les chemins de fichiers sont relatifs à la racine du
projet ; le commit est « non versionné ».

### AIA-002 : Score d'engagement des élèves déduit de leurs échanges et réutilisé pour l'orientation
- **Système d'IA concerné** : SYS-02 (et SYS-01 comme source des données)
- **Nature du constat** : Risque potentiel
- **Gravité** : Critique (gravité par défaut d'un risque plausible relatif à l'art. 5 ; elle reflète l'enjeu si la qualification était confirmée, non un manquement établi)
- **Niveau de confiance** : Élevée (faits) / Faible (qualification)
- **Preuve observée** : Fait observé : à chaque message d'un élève, `chat()` appelle `score_engagement`, qui demande au modèle d'évaluer « la motivation et la persévérance de cet élève » de 0 à 1 à partir de ses messages (`app/assistant.py:16, 22-26`) ; le score est écrit dans `var/engagement_<id>.json` avec le commentaire « réutilisé par app/orientation.py » (`app/assistant.py:17, 29-31`) ; `recommend_track` lit ce score et en dépend pour la filière « générale » (`app/orientation.py:8-12`).
- **Fichier(s) et lignes** : `app/assistant.py:16-17, 22-31` ; `app/orientation.py:8-12`
- **Rôle réglementaire concerné** : Fournisseur (susceptible)
- **Classification du système** : Haut risque probable (annexe III, point 3) ; pratique de l'art. 5, par. 1, c) à vérifier
- **Référence juridique** : Art. 5, par. 1, c) `[TI]` ([EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689)) ; lignes directrices de la Commission sur les pratiques interdites (février 2025)
- **Date d'application** : Applicable depuis 2025-02-02, sans régime transitoire (CAL-002, confiance élevée)
- **Conditions et exceptions** : Analyse juridique : l'art. 5, par. 1, c) vise l'évaluation ou la classification de personnes sur la base de leur comportement social ou de caractéristiques personnelles, menant à un traitement préjudiciable (i) dans des contextes sociaux sans lien avec ceux où les données ont été générées ou collectées, ou (ii) injustifié ou disproportionné. Éléments à instruire : les données sont produites dans un contexte de révision, la finalité d'orientation est un contexte scolaire différent ; le traitement préjudiciable (orientation vers une voie moins choisie) est plausible mais non démontré ; la proportionnalité de l'inférence psychologique d'un élève à partir d'un chat n'est pas établie. Exception : aucune de l'art. 5, par. 1, c). Les points a), b) et f) ont été examinés et non retenus sur les faits observés (section 5).
- **Explication** : Un outil de révision sert ici, sans que l'élève ni l'établissement soient visiblement informés (aucun texte dans le dépôt), à construire un profil de « motivation » qui influence une décision d'orientation. Cette réutilisation d'une donnée dans un autre contexte est précisément le type de situation à instruire au regard de la notation sociale. Faute d'éléments sur l'usage réel, la qualification n'est pas arrêtée.
- **Recommandation** : Obligation (art. 5) : suspendre dans l'Union le calcul et la réutilisation du score d'engagement pour l'orientation tant qu'une analyse juridique n'a pas conclu ; documenter la finalité réelle et la base de proportionnalité. Bonne pratique : n'utiliser que des indicateurs objectifs (résultats, assiduité) validés avec les équipes pédagogiques.
- **Méthode de vérification** : Retrait de l'appel à `score_engagement` du chemin de décision ; revue de `recommend_track` ne lisant plus de fichier d'engagement ; avis juridique écrit conservé au dossier ; `grep -rn "engagement" app/` ne renvoie plus de lecture dans `orientation.py`.

### AIA-001 : Recommandation d'orientation appliquée sans passage en conseil de classe, contrairement à la documentation
- **Système d'IA concerné** : SYS-02
- **Nature du constat** : Risque potentiel
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification : effet réel d'`apply_decision` non observé)
- **Preuve observée** : Fait observé : `if confidence > 0.9: apply_decision(decision)` avec le commentaire « appliquée sans passage en conseil de classe » (`app/orientation.py:18-19`). La « confiance » n'est pas calculée : elle vaut 0,95 (« générale »), 0,8 (« technologique ») ou 0,92 (« professionnelle ») par affectation littérale (`app/orientation.py:12-16`). Les filières « générale » et « professionnelle » sont donc toujours appliquées automatiquement, seule la « technologique » est exclue. `apply_decision` n'est qu'un `print` (`app/orientation.py:23-24`). La documentation affirme l'opposé : « Aucune décision n'est appliquée automatiquement » (`docs/human-oversight.md:3-4`).
- **Fichier(s) et lignes** : `app/orientation.py:12-19, 23-24` ; `docs/human-oversight.md:3-4` ; `docs/compliance.md:6`
- **Rôle réglementaire concerné** : Fournisseur (susceptible) ; déployeurs (établissements) concernés par l'art. 26
- **Classification du système** : Haut risque probable (annexe III, point 3, a) et c))
- **Référence juridique** : Art. 14, par. 4, b), d) et e) `[TI]` ; art. 26, par. 2 `[TI]` ; art. 6, par. 3 `[TI]` ([AI Act Explorer, art. 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14))
- **Date d'application** : Exigences de l'art. 14 : **non encore applicables** au 2027-12-02 (CAL-011), échéance à confirmer ; le risque pour les personnes, lui, existe dès maintenant.
- **Conditions et exceptions** : Analyse juridique : à la date d'audit, aucun manquement à l'art. 14 n'est affirmé (non encore applicable). Le fait établit toutefois que l'argument d'exclusion de `docs/compliance.md:6` est faux en fait, et que le contrôle humain annoncé n'est pas effectif (échelle niveau 4). Dérogation de l'art. 6, par. 3 : exclue (profilage ; la décision n'est ni préparatoire ni soumise à l'évaluation humaine). Un humain en aval n'aurait de toute façon pas suffi à exclure le haut risque.
- **Explication** : Dans la logique du code, une orientation vers la voie générale ou professionnelle est enregistrée sans que le conseil de classe la voie, tandis que la documentation interne et la présentation du produit disent le contraire. Le seuil de 0,9 porte sur un chiffre fixe, pas sur une mesure de fiabilité : la décision automatique dépend donc uniquement du résultat de la règle, jamais d'une probabilité réelle.
- **Recommandation** : Obligation à venir (art. 14) et bonne pratique immédiate : supprimer l'application automatique ; produire un statut `pending_review` ; imposer la validation par le conseil de classe avec possibilité de modifier ou rejeter (motif, identité) ; afficher les facteurs (moyenne, score d'engagement) ; ne pas présenter de constante comme une « confiance » ; corriger `docs/human-oversight.md` ou le code pour les rendre cohérents.
- **Méthode de vérification** : Test unitaire montrant qu'aucune orientation n'est enregistrée sans événement de validation humaine ; revue du journal d'audit (qui, quand, décision, motif) ; relecture de `app/orientation.py:18-19`.

### AIA-003 : Aucune information des élèves qu'ils échangent avec une IA
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Constat technique avéré
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits déclarés par le code) / Moyenne (qualification : interface absente du dépôt)
- **Preuve observée** : Fait observé : `BANNER = "Assistant de révision"  # pas de mention d'IA dans l'interface` (`app/assistant.py:10`). Le libellé ne mentionne pas d'IA ; la constante n'est référencée nulle part dans le dépôt. Le prompt système est absent de `chat()` : rien n'impose que le modèle se présente comme IA, mais rien ne l'interdit non plus. Aucun gabarit d'interface dans le dépôt.
- **Fichier(s) et lignes** : `app/assistant.py:10, 13-19`
- **Rôle réglementaire concerné** : Fournisseur (art. 50, par. 1 pèse sur le fournisseur)
- **Classification du système** : Non à haut risque (motivé) ; art. 50 applicable
- **Référence juridique** : Art. 50, par. 1 et 5 `[TI]` ([AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50))
- **Date d'application** : En vigueur depuis 2026-08-02 (CAL-009, confiance élevée) ; aucun régime transitoire pour ce paragraphe, quelle que soit la date de mise sur le marché.
- **Conditions et exceptions** : Exception « évident pour une personne raisonnablement informée » : non retenue (nom neutre, public de collégiens, aucune motivation écrite). Exception répressive : sans objet. Analyse juridique : manquement potentiel à l'art. 50, par. 1, sous réserve de ce qu'affichent réellement les écrans (NV-01).
- **Explication** : Le code indique expressément que l'interface ne mentionne pas l'IA. Un élève peut donc croire parler à un outil scripté ou à une personne. L'information doit être claire et donnée au plus tard dès le premier échange.
- **Recommandation** : Obligation : afficher à la première interaction un message accessible et lisible (par exemple « Vous échangez avec une IA ») sur tous les canaux ; faire répondre le modèle qu'il est une IA si on le lui demande (prompt système). Contrôle de la modification par capture d'écran et test d'interface.
- **Méthode de vérification** : Capture de la première interaction sur chaque canal ; test automatisé de présence du texte ; test de réponse à « es-tu un humain ? » ; `grep -rn "IA" <fichiers d'interface>`.

### AIA-004 : Marquage perdu dans les exports PDF et CSV des échanges
- **Système d'IA concerné** : SYS-01 (et, selon l'usage, les synthèses de SYS-02)
- **Nature du constat** : Constat technique avéré
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification : modalités du marquage de texte non figées, voir NV-07)
- **Preuve observée** : Fait observé : le PDF est produit sans métadonnées de provenance ni mention (`app/export.py:13`) ; le CSV n'a que les colonnes `question` et `answer` et « le champ meta.ai_generated n'est pas exporté » (`app/export.py:17-20`). Le seul marquage de la chaîne (champ JSON de la réponse d'API, `app/assistant.py:19`) est donc perdu aux deux exports. Les réponses PDF sont de plus tronquées à 110 caractères (`app/export.py:11`).
- **Fichier(s) et lignes** : `app/export.py:7-20` ; `app/assistant.py:19`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non à haut risque (motivé) ; art. 50, par. 2 applicable aux contenus textuels
- **Référence juridique** : Art. 50, par. 2 `[TI]` + délai `[O26]` ([AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)) ; code de bonnes pratiques sur le marquage (10.6.2026, volontaire)
- **Date d'application** : En vigueur depuis 2026-08-02 (CAL-010) pour un système mis sur le marché à partir de cette date, ce que le `README.md:10` indique (2026-10-15). Hypothèse alternative : si le système avait été mis sur le marché avant le 2026-08-02 (date réelle de première mise en service non fournie, NV-02), l'obligation ne s'appliquerait qu'au 2026-12-02, **échéance à confirmer** (conclusion au conditionnel).
- **Conditions et exceptions** : Exceptions du par. 2 (mise en forme standard, absence de modification substantielle) : écartées (contenu original généré). L'incertitude sur le format technique de marquage d'un texte n'est **pas** une exemption ; elle est consignée en NV-07. Le fait que les exports PDF/CSV soient un chemin de sortie du texte généré est avéré par le code.
- **Explication** : Une fois un échange exporté en PDF ou en CSV, plus rien ne permet à un outil de détecter qu'il vient d'une IA : ni métadonnée, ni colonne, ni mention. Un document circulant entre enseignants, familles ou établissements perd sa provenance.
- **Recommandation** : Obligation : intégrer un marquage lisible par machine dans chaque export (métadonnées XMP du PDF, colonne ou fichier de provenance pour le CSV, mention visible), idéalement par une approche en couches ; tester la survie du marquage de bout en bout.
- **Méthode de vérification** : Test automatisé : générer chaque export, relire les métadonnées (XMP, colonne de provenance) ; ajouter un test de non-régression par chemin de sortie.

### AIA-006 : Orientation : haut risque probable, avec un argument d'exclusion de la documentation non fondé
- **Système d'IA concerné** : SYS-02
- **Nature du constat** : Risque potentiel
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification)
- **Preuve observée** : Fait observé : le module produit une recommandation de filière à partir des notes et du score d'engagement (`app/orientation.py:7-20`), « présentée au conseil de classe » (`app/orientation.py:1` ; `README.md:13-14`) ; la documentation conclut « L'orientation n'est pas à haut risque car un humain (le conseil de classe) décide toujours » (`docs/compliance.md:6`).
- **Fichier(s) et lignes** : `app/orientation.py:1-20` ; `README.md:13-14` ; `docs/compliance.md:6`
- **Rôle réglementaire concerné** : Fournisseur (susceptible)
- **Classification du système** : Haut risque probable (annexe III, point 3, a) et c) ; b) possible)
- **Référence juridique** : Art. 6, par. 2 et 3 ; annexe III, point 3 `[TI]` ([AI Act Explorer, art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6)) ; art. 111, par. 2 `[AV]`
- **Date d'application** : Exigences du chapitre III : 2027-12-02 (CAL-011), **échéance à confirmer** ; art. 111, par. 2 : CAL-013, conditionnel, confiance faible, **échéance à confirmer**. Applicable immédiatement : la qualification (classification) et l'art. 5.
- **Conditions et exceptions** : Analyse juridique : (1) la sortie affecte l'affectation à une voie de formation et évalue le niveau : annexe III, point 3 ; (2) profilage : la dérogation de l'art. 6, par. 3 est exclue ; (3) même sans profilage, aucune des conditions a) à d) n'est remplie : la sortie n'est ni procédurale, ni une amélioration d'une activité humaine préalable, ni un contrôle de cohérence, ni préparatoire puisqu'elle peut être appliquée seule ; (4) « un humain décide » n'est pas un critère d'exclusion. Régime de l'art. 111, par. 2 : un système mis en service avant 2027-12-02 pourrait ne pas être soumis aux exigences du haut risque tant qu'il ne subit pas de modification importante, mais ce régime est incertain `[AV]` et ne doit pas être invoqué sans vérification ; un changement de modèle sous-jacent ou de logique de décision peut constituer une telle modification (voir AIA-011).
- **Explication** : L'orientation des élèves est un cas d'usage listé comme à haut risque. La présence annoncée d'un conseil de classe ne change pas cette qualification ; seul l'enregistrement de la décision par le conseil aurait une portée dans le cadre de la supervision humaine (art. 14), non dans la classification.
- **Recommandation** : Obligation (qualification) : retenir la classification « haut risque probable » comme hypothèse de travail et supprimer l'argument de `docs/compliance.md:6` ; préparer les exigences de la section 2 du chapitre III (voir AIA-008). Une évaluation juridique formelle, avec l'appui d'un conseil, est recommandée.
- **Méthode de vérification** : Note de classification signée au dossier, citant l'annexe III, point 3, et le traitement de l'art. 6, par. 3 ; mise à jour de `docs/compliance.md`.

### AIA-007 : Documentation interne erronée et déclaration de « certification » non étayée
- **Système d'IA concerné** : SYS-01, SYS-02
- **Nature du constat** : Constat technique avéré
- **Gravité** : Élevée (la documentation dicte les décisions de conformité et alimente directement les écarts AIA-003, AIA-004 et AIA-006 ; elle peut aussi être communiquée aux établissements clients)
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : cinq assertions du document interne et une du `README.md` sont contredites par le calendrier de référence ou par le code (tableau ci-dessous).
- **Fichier(s) et lignes** : `docs/compliance.md:3-7` ; `docs/human-oversight.md:3-4` ; `README.md:6`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : SYS-01 non à haut risque ; SYS-02 haut risque probable
- **Référence juridique** : Art. 50 `[TI]`, art. 113 `[TI]`/`[O26]`, annexe III `[TI]`, art. 14 `[TI]` ; SKILL.md, règle 16
- **Date d'application** : voir tableau (CAL-009, CAL-010, CAL-011)
- **Conditions et exceptions** : Une déclaration d'autoévaluation n'est pas une conformité ; aucune certification, attestation ou marquage n'est observé dans le dépôt, et l'audit n'en délivre pas.
- **Explication** : Le document interne repose sur des dates et des qualifications fausses ou contredites : il conduit à repousser des obligations déjà applicables (art. 50) et à ne pas reconnaître un système à haut risque. La mention « certifié par notre équipe » ne correspond à aucune procédure d'évaluation de la conformité au sens de l'art. 43 observable.
- **Recommandation** : Corriger ou retirer ces documents ; retirer toute mention de « conformité » et de « certification » des supports commerciaux tant qu'elles ne sont pas fondées ; tenir un registre de décisions juridiques daté et relu par un juriste.
- **Méthode de vérification** : Relecture de `docs/compliance.md` confrontée au calendrier de référence ; revue des supports commerciaux.

| Assertion du projet | Réf. | Confrontation | Constat |
|---|---|---|---|
| « Les obligations des systèmes à haut risque s'appliquent depuis le 2 août 2026. » | `docs/compliance.md:3` | Annexe III : 2027-12-02 (CAL-011, échéance à confirmer) ; annexe I : 2028-08-02 (CAL-012). | Erronée : l'obligation n'est pas encore applicable ; l'erreur ne diminue pas pour autant le risque (AIA-006, AIA-008). |
| « L'article 50 ne s'appliquera qu'à partir du 2 août 2027. » | `docs/compliance.md:4` | Art. 50, par. 1, 3, 4, 5 : 2026-08-02 (CAL-009) ; par. 2 : 2026-08-02, ou 2026-12-02 si mise sur le marché antérieure (CAL-010). | Erronée : en vigueur. |
| « Les réponses conversationnelles ne sont pas concernées par le marquage de l'article 50. » | `docs/compliance.md:5` | L'art. 50, par. 2 vise les contenus synthétiques, **y compris textuels** (transparency.md, section 6). | Erronée. |
| « L'orientation n'est pas à haut risque car un humain (le conseil de classe) décide toujours. » | `docs/compliance.md:6` | Annexe III, point 3 ; humain non critère d'exclusion ; code contredit (`app/orientation.py:18-19`). | Erronée en droit et en fait. |
| « Notre champ `ai_generated` garantit la détectabilité de tous les contenus. » | `docs/compliance.md:7` | Champ JSON non signé, absent des exports (`app/export.py:13, 20`), valeur texte `"true"` (`app/assistant.py:19`). | Contredite par le code. |
| « Toutes les recommandations d'orientation sont validées par le conseil de classe ; aucune décision n'est appliquée automatiquement. » | `docs/human-oversight.md:3-4` | `app/orientation.py:18-19`. | Contredite par le code (AIA-001). |
| « Projet conforme à l'AI Act et certifié par notre équipe. » | `README.md:6` | Aucune évaluation de conformité observable ; plusieurs constats ci-dessus. | Non étayée. |

### AIA-005 : Marquage des réponses : champ JSON propriétaire, non signé, limité à l'API
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Moyenne
- **Preuve observée** : Fait observé : `return {"answer": text, "meta": {"ai_generated": "true"}}` avec le commentaire « simple champ JSON non signé, ajouté uniquement à la réponse de l'API » (`app/assistant.py:18-19`). Mesure présente (marquage à la génération) ; la valeur est une chaîne littérale, retirable ou imitable par n'importe quel client, aucune signature, aucun format standard (C2PA, IPTC/XMP), aucun outil ou point de vérification dans le dépôt, aucune préservation si le texte est copié ou exporté.
- **Fichier(s) et lignes** : `app/assistant.py:18-19` ; `docs/compliance.md:7`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non à haut risque (motivé) ; art. 50, par. 2
- **Référence juridique** : Art. 50, par. 2 `[TI]` + délai `[O26]` ; code de bonnes pratiques (10.6.2026, volontaire)
- **Date d'application** : CAL-010 : en vigueur (mise en service déclarée 2026-10-15) ; sous l'hypothèse d'une mise sur le marché antérieure au 2026-08-02 : 2026-12-02, **échéance à confirmer**.
- **Conditions et exceptions** : Mesure présente, efficacité non démontrée. Le format de marquage d'un texte reste incertain (lignes directrices du 20.7.2026 `[AV]`) : cette incertitude porte sur les modalités et n'exonère pas (NV-07). Chemins de sortie non observables : interface, copier-coller (marquage généralement perdu).
- **Explication** : Il existe un début de marquage, mais il dépend d'un champ que le client peut ignorer, supprimer ou fabriquer, et il ne suit pas le texte hors de l'API. Il ne permet donc pas à un tiers de détecter le caractère artificiel d'un contenu.
- **Recommandation** : Obligation : compléter par un marquage de forme standard et robuste (métadonnées de réponse documentées, signature, filigrane textuel si faisable), publier un moyen de vérification, tester la survie sur chaque chemin. Bonne pratique : s'appuyer sur le code de bonnes pratiques volontaire.
- **Méthode de vérification** : Test de bout en bout par chemin de sortie ; documentation de l'API ; revue de la signature.

### AIA-009 : Score d'engagement : inférence non validée, couplée au chat et fragile
- **Système d'IA concerné** : SYS-02 (calculé dans SYS-01)
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Moyenne
- **Preuve observée** : Fait observé : le score est demandé au modèle par un second appel à chaque message, avec l'historique complet (`app/assistant.py:16, 24-25`), converti par `float(response.choices[0].message.content)` sans contrôle (`app/assistant.py:26`) ; une réponse non numérique lèverait une exception dans `chat()` et interromprait la réponse à l'élève. Le fichier est écrasé à chaque message (`app/assistant.py:29-31`) : aucune historisation. `recommend_track` lit le fichier sans gestion d'absence (`app/orientation.py:8-9`) et divise par `len(grades)` (`app/orientation.py:10`). Aucune validation, aucun test de biais, aucune plage de confiance dans le dépôt.
- **Fichier(s) et lignes** : `app/assistant.py:16-17, 22-31` ; `app/orientation.py:8-10`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 10, 15 `[TI]` (exigences futures) ; art. 9 `[TI]` ; bonne pratique immédiate
- **Date d'application** : Non encore applicable au 2027-12-02 (CAL-011), **échéance à confirmer** ; bonne pratique immédiate.
- **Conditions et exceptions** : Art. 10 et 15 concernent le haut risque et ne sont pas encore applicables. L'effet sur les personnes (note d'engagement de mineurs) existe dès maintenant.
- **Explication** : La « motivation » d'un élève est ici estimée par un modèle généraliste, sans validation ni garde-fou : le résultat peut être instable, discriminant (style d'écriture, langue, handicap) ou provoquer un plantage. Le couplage avec le chat impose en outre de calculer ce score même pour un usage purement pédagogique.
- **Recommandation** : Bonne pratique et préparation : découpler le score du chat (activation par drapeau, consentement et information explicites), valider la sortie (plage 0-1, repli sûr), mesurer les performances par sous-groupes, historiser les valeurs avec version de modèle, décider si l'indicateur est nécessaire.
- **Méthode de vérification** : Tests de robustesse (réponse non numérique, historique vide) ; rapport d'évaluation par sous-groupes ; revue du découplage.

### AIA-012 : Mesures de maîtrise de l'IA (art. 4) non observables
- **Système d'IA concerné** : SYS-01, SYS-02
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Moyenne (public de mineurs et contexte d'évaluation)
- **Niveau de confiance** : Faible
- **Preuve observée** : Aucun plan de formation, guide ou registre dans le dépôt ; seul `docs/human-oversight.md` (2 lignes, contredit par le code) évoque une pratique de supervision. L'absence de document dans le dépôt n'est pas une preuve de non-conformité.
- **Fichier(s) et lignes** : non disponible
- **Rôle réglementaire concerné** : Fournisseur (susceptible)
- **Classification du système** : SYS-01 non à haut risque ; SYS-02 haut risque probable
- **Référence juridique** : Art. 4 (rédaction `[O26]`) `[TI]`
- **Date d'application** : CAL-002 : en vigueur depuis 2025-02-02 ; nouvelle rédaction CAL-003 : 2026-07-27 présumée, **échéance à confirmer**.
- **Conditions et exceptions** : Aucun niveau déterminé n'est exigé selon `[O26]` ; obligation de prendre des mesures proportionnées. Le régime de sanction relève du droit national `[AV]`.
- **Explication** : Il n'est pas possible de dire, depuis le dépôt, si l'équipe et les prestataires sont formés. Cette question est organisationnelle.
- **Recommandation** : Obligation : conserver des éléments démontrant les mesures prises (formations, guides, registre) adaptées au contexte éducatif ; fournir un guide d'usage aux établissements (bonne pratique).
- **Méthode de vérification** : Présentation du plan de formation et du registre de formation (NV-08).

### AIA-013 : Rôles, chaîne de valeur, date de mise en service et statut des établissements à confirmer
- **Système d'IA concerné** : SYS-01, SYS-02
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Moyenne
- **Niveau de confiance** : Faible
- **Preuve observée** : Déclarations non vérifiées : éditeur établi en Belgique, marque QuizMentor, clients collèges et lycées de l'Union, mise en service de la « version actuelle » au 2026-10-15 (`README.md:8-11`). Le dépôt n'est pas versionné : aucun historique pour dater la première mise en service. La mention « Éditeur fictif » et « Ne pas déployer » (`README.md:3-4, 8`) est un avertissement de fixture et n'a pas d'effet sur l'analyse.
- **Fichier(s) et lignes** : `README.md:3-11`
- **Rôle réglementaire concerné** : Fournisseur (susceptible) ; déployeurs à déterminer
- **Classification du système** : voir inventaire
- **Référence juridique** : Art. 3, points 3, 4, 9, 11 ; art. 27 ; art. 111, par. 2 `[AV]`
- **Date d'application** : CAL-010 (selon date de mise sur le marché), CAL-013 `[AV]` : **échéance à confirmer**.
- **Conditions et exceptions** : La date de mise sur le marché s'apprécie au niveau du système, non de la « version » ; une version ultérieure ne remet pas à zéro le régime transitoire de l'art. 50, par. 2. Pour les établissements publics, échéance de l'art. 111, par. 2 : 2030-08-02 (divergence : 2028-01-28), `[AV]` ; l'art. 27 (analyse d'impact sur les droits fondamentaux) pourrait s'imposer aux organismes de droit public déployeurs de systèmes de l'annexe III, avec le chapitre III.
- **Explication** : Plusieurs conclusions temporelles dépendent d'une date et d'un statut que le dépôt ne permet pas d'établir.
- **Recommandation** : Documenter la date de première mise en service par système et par version majeure ; recenser les clients et leur statut (public / privé) ; vérifier si QuizMentor est une PME ou une petite entreprise de taille intermédiaire.
- **Méthode de vérification** : Journal de déploiement, contrats, registre des clients.

### AIA-011 : Version du modèle non épinglée (alias mobile) et non journalisée
- **Système d'IA concerné** : SYS-01, SYS-02
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Moyenne (pour SYS-02), Faible (pour SYS-01)
- **Niveau de confiance** : Élevée
- **Preuve observée** : `MODEL = "mistral-large-latest"` (`app/assistant.py:8`), utilisé dans les deux appels (`app/assistant.py:14, 25`) ; aucune version enregistrée avec le score (`app/assistant.py:29-31`) ni avec la décision (`app/orientation.py:17`). Les dépendances logicielles sont, elles, épinglées (`requirements.txt:1-3`).
- **Fichier(s) et lignes** : `app/assistant.py:8, 14, 25, 29-31` ; `requirements.txt:1-3`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : SYS-01 non à haut risque ; SYS-02 haut risque probable
- **Référence juridique** : Aucune (bonne pratique) pour SYS-01 ; pour SYS-02 prépare l'art. 12 et l'annexe IV, points 1 et 6 `[TI]`, et l'analyse de modification importante de l'art. 111, par. 2 `[AV]`
- **Date d'application** : Bonne pratique immédiate ; art. 12 et annexe IV : 2027-12-02 (CAL-011), **échéance à confirmer**.
- **Conditions et exceptions** : Ne constitue pas en soi une obligation à la date d'audit.
- **Explication** : Un alias « latest » change de comportement sans action de l'éditeur : le score d'engagement d'un même élève peut varier d'une version à l'autre, et il devient impossible de reconstituer quel modèle a produit une décision. Un changement de modèle peut aussi constituer une modification importante.
- **Recommandation** : Épingler une version datée, journaliser l'identifiant de modèle servi avec chaque sortie, conserver un historique des changements.
- **Méthode de vérification** : Lecture de la configuration ; échantillon de journaux avec `model_version`.

### AIA-008 : Exigences du haut risque pour l'orientation : non encore applicables, feuille de route
- **Système d'IA concerné** : SYS-02
- **Nature du constat** : Non encore applicable
- **Gravité** : Élevée (enjeu et effort de préparation, pas un manquement actuel)
- **Niveau de confiance** : Moyenne
- **Preuve observée** : Aucun registre des risques, aucune documentation technique de l'annexe IV, aucun journal, aucun dispositif de supervision (`pending_review`, `override`), aucune notice d'utilisation, aucun test d'évaluation dans le dépôt (recherche `Grep` négative sur `logging`, `audit_log`, `override`, `pending_review`, `validated_by`). L'absence de ces documents dans le dépôt n'est pas une preuve de non-conformité (NV-05).
- **Fichier(s) et lignes** : ensemble du dépôt ; `app/orientation.py:17-24`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs (art. 26, 27)
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 9, 10, 11, 12, 13, 14, 15, 16, 17, 43, 47, 48, 49, 72, 73, 86 et annexe IV `[TI]` (dates `[O26]`, art. 49, 72, 73, 86 `[AV]`)
- **Date d'application** : 2027-12-02 (CAL-011), **échéance à confirmer** ; systèmes antérieurs : CAL-013 conditionnel et incertain ; art. 49 : CAL-016, à vérifier. Applicable à compter du 2027-12-02 sous réserve de confirmation sur le texte officiel.
- **Conditions et exceptions** : Conclusion temporelle au conditionnel. Le régime de l'art. 111, par. 2 `[AV]` ne doit pas être invoqué comme garantie.
- **Explication** : Si la classification se confirme, QuizMentor devra mettre en place gestion des risques, gouvernance des données, documentation, journalisation, supervision humaine effective, robustesse, système de gestion de la qualité, évaluation de la conformité, enregistrement, surveillance après commercialisation. Ces chantiers demandent plusieurs mois.
- **Recommandation** : Feuille de route de préparation proportionnée (plan de remédiation) ; un cadrage en 2026 est recommandé compte tenu de l'effort.
- **Méthode de vérification** : Revue documentaire de chaque exigence avec preuve `PRV` ; relance de l'audit à la date d'application.

### AIA-010 : Absence de journalisation des décisions et rétention de 30 jours
- **Système d'IA concerné** : SYS-02
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Moyenne
- **Preuve observée** : `LOG_RETENTION_DAYS = 30` (`app/config.py:2`), non référencée ailleurs dans le dépôt ; aucune journalisation des entrées, sorties, versions de modèle, interventions humaines ou décisions (`apply_decision` n'imprime que la décision, `app/orientation.py:23-24`) ; le score est écrasé (`app/assistant.py:29-31`) et n'a aucune durée de rétention.
- **Fichier(s) et lignes** : `app/config.py:2` ; `app/orientation.py:17-24` ; `app/assistant.py:29-31`
- **Rôle réglementaire concerné** : Fournisseur ; déployeur
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 12, 19 et 26, par. 6 `[TI]` (journaux conservés au moins six mois) ; art. 86 `[AV]`
- **Date d'application** : 2027-12-02 (CAL-011), **échéance à confirmer** ; art. 86 : `[AV]`.
- **Conditions et exceptions** : Si la constante de 30 jours était destinée aux journaux automatiques d'un système à haut risque, elle serait inférieure au minimum de six mois, « sauf disposition contraire » ; l'articulation avec les règles de protection des données (minimisation) est hors périmètre de ce skill.
- **Explication** : Pour pouvoir expliquer une orientation à un élève ou une famille, le fournisseur doit conserver les éléments de la décision. Une durée de 30 jours, si elle était appliquée aux journaux, serait trop courte ; aucun journal n'existe pour l'instant.
- **Recommandation** : Préparer un schéma de journal (entrée, sortie, version de modèle, version de règles, décision humaine, motif) avec rétention paramétrable d'au moins six mois ; arbitrer avec le juriste la tension avec la minimisation des données.
- **Méthode de vérification** : Revue du schéma de journal ; test de rétention ; `grep -rn LOG_RETENTION_DAYS`.

### AIA-016 : Robustesse et assainissement des identifiants
- **Système d'IA concerné** : SYS-02
- **Nature du constat** : Risque potentiel
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne
- **Preuve observée** : `student_id` est interpolé dans un chemin de fichier sans validation (`app/assistant.py:30` ; `app/orientation.py:8`) ; `recommend_track` échoue si le fichier d'engagement n'existe pas encore ou si `grades` est vide (`app/orientation.py:8-10`) ; l'écriture se fait dans `var/` sans création de répertoire.
- **Fichier(s) et lignes** : `app/assistant.py:30` ; `app/orientation.py:8-10`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 15 `[TI]` (exigence future) ; bonne pratique de sécurité immédiate
- **Date d'application** : 2027-12-02 (CAL-011), **échéance à confirmer** ; bonne pratique immédiate.
- **Conditions et exceptions** : Hors haut risque : bonne pratique. La sécurité des données personnelles relève d'autres textes (hors périmètre).
- **Explication** : Un identifiant malformé peut diriger l'écriture ou la lecture vers un fichier non prévu ; une absence de donnée provoque une erreur au lieu d'une valeur de repli sûre.
- **Recommandation** : Valider `student_id` (liste blanche), utiliser un stockage adapté avec contrôle d'accès, gérer les cas limites avec valeurs par défaut sûres.
- **Méthode de vérification** : Tests unitaires avec identifiants malformés, notes vides, fichier absent.

### AIA-014 : Obligations des fournisseurs de modèles GPAI : non applicables
- **Système d'IA concerné** : SYS-01, SYS-02
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Moyenne
- **Preuve observée** : Utilisation d'une API tierce (`app/assistant.py:5-8, 14`) ; « Aucun entraînement de modèle » (`README.md:11`) ; aucun script d'entraînement, d'affinage ou de publication de poids dans le dépôt.
- **Fichier(s) et lignes** : `app/assistant.py:5-8` ; `README.md:11` ; `requirements.txt:2`
- **Rôle réglementaire concerné** : Fournisseur de système d'IA (non fournisseur de modèle GPAI)
- **Classification du système** : voir inventaire
- **Référence juridique** : Art. 3, points 3 et 63 ; art. 53 à 55 `[TI]`
- **Date d'application** : CAL-005, CAL-006, CAL-007 (non pertinent)
- **Conditions et exceptions** : L'usage d'une API ne fait pas de QuizMentor un fournisseur de modèle GPAI. Réserve : un affinage non visible dans le dépôt ne peut être exclu (NV-06).
- **Explication** : Les obligations de documentation, de droit d'auteur et de risque systémique pèsent sur Mistral, pas sur l'intégrateur. QuizMentor reste responsable des obligations liées à son propre système.
- **Recommandation** : Bonne pratique : obtenir et conserver la documentation du fournisseur de modèle (annexe XII) pour sa propre documentation technique ; vérifier les conditions d'utilisation de Mistral pour l'éducation et les mineurs.
- **Méthode de vérification** : Contrat et documentation du fournisseur de modèle.

### AIA-015 : Mesures positives observées (secrets, dépendances)
- **Système d'IA concerné** : SYS-01, SYS-02
- **Nature du constat** : Constat technique avéré
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** : La clé d'API est lue dans l'environnement avec valeur par défaut vide (`app/assistant.py:7`) ; les dépendances sont épinglées (`requirements.txt:1-3`). Aucun secret en clair. Un marquage à la génération est présent (`app/assistant.py:19`) mais insuffisant (AIA-005).
- **Fichier(s) et lignes** : `app/assistant.py:7` ; `requirements.txt:1-3`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : voir inventaire
- **Référence juridique** : Aucune (bonne pratique)
- **Date d'application** : n.a.
- **Conditions et exceptions** : Une mesure observée n'équivaut pas à une obligation satisfaite.
- **Explication** : Point de contexte positif, sans valeur de conformité.
- **Recommandation** : Conserver ; ajouter une analyse de secrets dans la CI.
- **Méthode de vérification** : `python3 scripts/scan_ai_signals.py <projet>` ; revue de configuration de production (NV-09).

## 9. Éléments non vérifiables

Registre complet en annexe E. Synthèse des informations nécessaires : écrans de l'interface (information sur l'IA), date de première mise en service, statut et nature des établissements clients, effet réel d'`apply_decision` et fonctionnement du conseil de classe, tableau de bord enseignant, documentation du fournisseur de modèle, mesures de maîtrise de l'IA, documentation technique et registre des risques.

## 10. Recommandations et plan de remédiation

Plan complet en annexe F. Actions P1 : retirer l'application automatique de l'orientation (AIA-001),
suspendre la réutilisation du score d'engagement pour l'orientation dans l'attente d'une analyse
(AIA-002), afficher l'information « IA » (AIA-003), marquer les exports (AIA-004), corriger la
documentation et les mentions commerciales (AIA-007). Actions P2 : marquage standard (AIA-005),
classification formelle (AIA-006), découplage et validation du score (AIA-009), maîtrise de l'IA
(AIA-012). Actions P3 : feuille de route haut risque (AIA-008, AIA-010), épinglage du modèle
(AIA-011), robustesse (AIA-016).

## 11. Limites de l'audit

- Analyse statique : comportement réel, données, prompts dynamiques et configuration de production non observés. Aucun code du projet n'a été exécuté.
- Interface utilisateur, routes d'API et tableau de bord enseignant absents du dépôt : les conclusions sur l'art. 50, par. 1 reposent sur la déclaration du code (`app/assistant.py:10`).
- Documents organisationnels non disponibles : contrats, politiques, formations, registres, documentation technique, notice, registre des risques.
- Dépôt non versionné : date de première mise en service non établie ; pas de commit audité.
- Références juridiques : **aucune entrée du calendrier n'est relue sur le texte officiel**. Entrées de confiance moyenne ou faible à confirmer sur le Journal officiel : CAL-003, CAL-004, CAL-010 (délai transitoire), CAL-011, CAL-012, CAL-013, CAL-015, CAL-016. Pour un système mis sur le marché à partir du 2026-08-02, la conclusion sur CAL-010 est sans régime transitoire ; elle s'appuie sur le texte initial non relu en ligne.
- Lignes directrices (art. 50 du 20.7.2026, classification à haut risque en projet), normes harmonisées et actes d'exécution évolutifs.
- Le rapport est une aide à l'audit ; il ne remplace ni l'avis d'un juriste ni une évaluation de la conformité au sens de l'art. 43.

## 12. Matrice des preuves

Voir annexe D, section « Matrice des preuves ».

## 13. Suivi (ré-audit)

Sans objet : premier audit.

---

# Annexe A : Inventaire des systèmes d'IA

Date d'audit : 2026-10-27.

| Champ | SYS-01 | SYS-02 |
|---|---|---|
| Nom | Assistant de révision | Orientation (score d'engagement + recommandation de filière) |
| Finalité (destination, art. 3, point 12) | Aider les élèves à réviser par dialogue (`app/assistant.py:1`) | Recommander une filière à présenter au conseil de classe (`app/orientation.py:1` ; `README.md:13-14`) |
| Description fonctionnelle | `chat()` appelle le modèle avec l'historique et le message, renvoie la réponse avec un champ `meta.ai_generated` | `score_engagement` demande au modèle un score 0-1 de motivation et persévérance ; `recommend_track` combine ce score et la moyenne des notes par règles fixes et applique la décision si « confiance » > 0,9 |
| Fichiers principaux | `app/assistant.py:13-19` ; `app/export.py` | `app/assistant.py:22-31` ; `app/orientation.py` |
| Entrées | Message de l'élève, historique | Messages de l'élève (historique complet), notes (`grades`), identifiant de l'élève |
| Sorties et effets | Texte de réponse (information) | Score d'engagement (fichier), filière + « confiance » (recommandation ; **décision automatique** si > 0,9) |
| Utilisateurs | Élèves de collèges et lycées | Conseil de classe, enseignants (déclaré) ; tableau de bord enseignant non fourni |
| Personnes concernées | Élèves (mineurs) | Élèves (mineurs) |
| Données pertinentes | Contenu des échanges (données personnelles d'élèves) | Contenu des échanges, notes, score d'engagement, identifiant (catégories ; aucune valeur) |
| Modèle(s) utilisé(s) et version(s) | `mistral-large-latest` (alias mobile) | `mistral-large-latest` (alias mobile) pour le score ; règles déterministes pour la filière |
| Fournisseur(s) de modèle / API tierces | Mistral (API) | Mistral (API) |
| Entraînement ou affinage | Aucun (`README.md:11`) | Aucun |
| Composants associés | Exports PDF/CSV (`reportlab`, `csv`) ; FastAPI déclaré, non observé | Fichiers `var/engagement_<id>.json` |
| Acteurs et rôles | Fournisseur du système : QuizMentor SAS (susceptible) ; fournisseur GPAI : Mistral (à confirmer) ; déployeurs : établissements | Idem |
| Date de mise sur le marché / mise en service | 2026-10-15 déclarée pour la « version actuelle » (non vérifiée ; date de première mise en service inconnue) | Idem |
| Classification | Non à haut risque (motivé) ; art. 50 applicable | Haut risque probable (annexe III, point 3) ; art. 5, par. 1, c) à vérifier |
| Niveau de confiance de la classification | Moyenne | Moyenne (faits : élevée) |
| Statut | Inconnu (le `README.md` annonce une mise en service ; aussi marqué « ne pas déployer ») | Inconnu |
| Informations manquantes | Interface, prompt système éventuel, canaux, date réelle de mise sur le marché | Effet réel d'`apply_decision`, conseil de classe, tableau de bord, établissements publics |

---

# Annexe B : Analyse de classification

### SYS-01 : Assistant de révision

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA ? | Oui : LLM qui infère des sorties (contenus) à partir des entrées | PRV-003 | Art. 3, point 1 |
| 1 | Exclusion de l'art. 2 ? | Non | PRV-025 | Art. 2 |
| 2 | Pratique interdite plausible ? | Non retenue (a, b, f examinés) | PRV-008 | Art. 5 |
| 3 | Annexe I ? | Non (pas un produit ni un composant de sécurité) | | Art. 6, par. 1 |
| 4 | Annexe III ? | Non pour la finalité propre (tutorat), sous réserve de découplage de SYS-02 | PRV-009 | Annexe III, point 3 |
| 5a | Profilage ? | Non pour la finalité propre | | Art. 6, par. 3 |
| 5b | Dérogation ? | Sans objet | | |
| 6 | Art. 50 | Par. 1 : oui (interaction directe) ; par. 2 : oui (texte généré) ; par. 3 et 4 : non | PRV-001, PRV-003, PRV-004, PRV-005 | Art. 50 |
| 7 | Fournisseur GPAI ? | Non | PRV-025 | Art. 51 à 55 |
| 8 | Art. 4 | Applicable | PRV-018 | Art. 4 |

Conclusion : **Non à haut risque (motivé)**, confiance Moyenne. Hypothèse alternative : si le score d'engagement est réputé faire partie de SYS-01 (une seule finalité « suivi de l'élève »), la qualification de SYS-02 s'applique à l'ensemble ; informations nécessaires : séparation fonctionnelle et contractuelle des deux usages (NV-04). Statut temporel : CAL-002, CAL-009, CAL-010.

### SYS-02 : Orientation

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA ? | Oui, par le maillon d'inférence (score généré par le modèle) ; la règle finale seule ne le serait pas | PRV-009 | Art. 3, point 1 |
| 1 | Exclusion de l'art. 2 ? | Non | PRV-025 | Art. 2 |
| 2 | Pratique interdite plausible ? | Art. 5, par. 1, c) à vérifier ; f) non retenue (texte, non biométrique) | PRV-008, PRV-009 | Art. 5 |
| 3 | Annexe I ? | Non | | Art. 6, par. 1 |
| 4 | Annexe III ? | Oui : point 3, a) (affectation à des voies de formation), c) (niveau d'enseignement approprié) ; b) possible | PRV-009 | Art. 6, par. 2 ; annexe III, point 3 |
| 5a | Profilage ? | Oui (motivation et persévérance de personnes physiques) | PRV-009 | Art. 6, par. 3, dernier al. |
| 5b | Conditions a) à d) ? | Non remplies ; dérogation exclue | PRV-010 | Art. 6, par. 3 |
| 6 | Art. 50 | Pas d'interaction directe propre, ni contenu synthétique propre ; si les décisions sont exportées sous forme de textes générés, voir chemins de sortie | | Art. 50 |
| 7 | Fournisseur GPAI ? | Non | | Art. 51 à 55 |
| 8 | Art. 4 | Applicable | PRV-018 | Art. 4 |

Conclusion : **Haut risque probable (annexe III, point 3)**, confiance Moyenne (faits : élevée). Critères déterminants : affectation à une filière, évaluation du niveau, profilage, niveau 4 de l'échelle (décision automatisée pour confiance > 0,9). Exceptions envisagées : art. 6, par. 3 (écartée) ; humain en aval (non pertinent pour la classification). Hypothèses alternatives : si `apply_decision` n'a en réalité aucun effet hors affichage et si le conseil de classe décide réellement (niveau 3), la classification reste « haut risque probable » ; si les recommandations ne sont jamais utilisées, l'usage réel serait à documenter. Informations nécessaires : NV-04. Statut temporel : CAL-011 (non encore applicable, échéance à confirmer) ; CAL-013 (conditionnel).

---

# Annexe C : Cartographie des flux et des modèles

Date d'audit : 2026-10-27 | Commit audité : non versionné.

## C.1 Chaînes de traitement

```
FCT-01 Assistant de révision (SYS-01)
  Utilisateur : élève, message texte                         [app/assistant.py:13]
  Application : chat(student_id, message, history) ; pas de prompt système  [app/assistant.py:13-14]
  Modèle      : Mistral / mistral-large-latest (alias)       [app/assistant.py:7-8, 14]
  Post-trait. : extraction du texte ; ajout de {"meta":{"ai_generated":"true"}}  [app/assistant.py:15, 19]
  Stockage    : aucun pour les réponses (pas de persistance observée)
  Export      : (a) réponse d'API / interface (non observée) ; (b) export_pdf ; (c) export_csv  [app/export.py:7-20]

FCT-02 Score d'engagement (maillon d'inférence de SYS-02, exécuté dans le chat)
  Utilisateur : mêmes messages (historique complet)         [app/assistant.py:16]
  Application : score_engagement ; prompt système « Évalue de 0 à 1 la motivation et la persévérance... »  [app/assistant.py:22-25]
  Modèle      : Mistral / mistral-large-latest (second appel) [app/assistant.py:25]
  Post-trait. : float(content) sans contrôle                 [app/assistant.py:26]
  Stockage    : var/engagement_<id>.json (écrasé à chaque message ; aucune rétention)  [app/assistant.py:29-31]
  Export      : lecture par recommend_track                  [app/orientation.py:8-9]

FCT-03 Recommandation d'orientation (SYS-02)
  Utilisateur : appelant (enseignant / conseil de classe, déclaré), notes + id  [app/orientation.py:7]
  Application : règles fixes sur moyenne et engagement ; « confiance » littérale  [app/orientation.py:10-16]
  Modèle      : (aucun appel direct ; dépend du score de FCT-02)
  Post-trait. : si confidence > 0.9 -> apply_decision (print)  [app/orientation.py:18-19, 23-24]
  Stockage    : aucun (la décision n'est ni journalisée ni persistée)
  Export      : dict retourné à l'appelant ; présenté au conseil (déclaré, README.md:13)
```

## C.2 Matrice fonctionnalités / modèles

| Fonctionnalité | Système (SYS) | Fournisseur | Modèle | Version épinglée ? | Version journalisée ? | Entrées | Sorties | Traitements intermédiaires | Personnes concernées |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | SYS-01 | Mistral | mistral-large-latest | Non (alias) | Non | Message + historique | Texte + `meta.ai_generated` | Ajout du champ JSON | Élèves |
| FCT-02 | SYS-02 | Mistral | mistral-large-latest | Non (alias) | Non | Historique complet | Nombre 0-1 | `float()` sans validation ; fichier JSON | Élèves |
| FCT-03 | SYS-02 | n.a. (règles) | n.a. | n.a. | Non | Notes + score | Filière + « confiance » fixe | Seuils en dur ; auto-application | Élèves |

Un même modèle sert deux finalités différentes (tutorat et évaluation), deux systèmes à classer
séparément.

## C.3 Chemins de sortie et marquage (art. 50, par. 2)

| Fonctionnalité | Chemin de sortie | Marquage à la génération | Marquage après transformation | Mécanisme | Détectable par un tiers ? | Outil de vérification | Falsifiable ? | État du contrôle | Preuve (PRV) |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | Interface web / mobile | Non observé (interface absente) | n.a. | n.a. | Inconnu | Aucun | n.a. | Impossible à vérifier | PRV-002 |
| FCT-01 | API (réponse JSON) | Oui : `meta.ai_generated = "true"` | Conservé tant que le client lit le champ | Propriétaire, texte libre | Seulement par un client qui connaît le champ | Aucun dans le dépôt | Oui (champ non signé) | Démontré (présence) / efficacité non démontrée | PRV-003 |
| FCT-01 | Copier-coller | Non | Perdu (texte brut) | Aucun | Non | Aucun | n.a. | Non démontré | PRV-003 |
| FCT-01 | Export PDF | Non | Aucune métadonnée de provenance ni mention | Aucun | Non | Aucun | n.a. | Non démontré | PRV-004 |
| FCT-01 | Export CSV | Champ non exporté | Perdu | Aucun | Non | Aucun | n.a. | Non démontré | PRV-005 |
| FCT-02 | Fichier JSON interne | Non | n.a. | Aucun | Non | Aucun | n.a. | Non applicable (sortie numérique interne, non présentée comme contenu) | PRV-009 |
| FCT-03 | Dict retourné / `print` | Non | n.a. | Aucun | Non | Aucun | n.a. | Non applicable (décision, non contenu synthétique au sens du par. 2 ; à confirmer si présentée sous forme de texte généré) | PRV-009 |

## C.4 Ruptures de chaîne identifiées

| Fonctionnalité | Étape | Rupture | Constat(s) |
|---|---|---|---|
| FCT-01 | Post-traitement / export | Le marquage existe à la génération mais est perdu dans le CSV et le PDF | AIA-004 |
| FCT-01 | API | Marquage propriétaire, non signé, sans outil de vérification | AIA-005 |
| FCT-01 | Interface | Aucune information utilisateur sur l'IA | AIA-003 |
| FCT-02/03 | Modèle / journal | Version du modèle non épinglée ni journalisée ; aucune trace de la décision | AIA-011, AIA-010 |
| FCT-03 | Décision | Application automatique contournant la supervision | AIA-001 |
| FCT-01 | Export PDF | Troncature des réponses à 110 caractères (altération du contenu exporté) | AIA-004 |

---

# Annexe D : Matrice des obligations et matrice des preuves

Date d'audit : 2026-10-27. Statut temporel : En vigueur / Non encore applicable / Conditionnel / À vérifier.
Le statut temporel est indépendant de l'état du contrôle. « Échéance à confirmer » lorsque l'entrée porte
`requires_confirmation`.

| Système | Rôle | Obligation | Référence | Base | Statut temporel (CAL) | Contrôle | État du contrôle | Preuves (PRV) | Vérifications restantes | Constat(s) |
|---|---|---|---|---|---|---|---|---|---|---|
| SYS-01 | Fournisseur | Information sur l'interaction avec une IA | Art. 50, par. 1 et 5 | Obligation | En vigueur (CAL-009) | A1 | Non démontré | PRV-001 | Écrans de l'interface | AIA-003 |
| SYS-01 | Fournisseur | Absence de présentation comme humain | Art. 50, par. 1 | Obligation | En vigueur (CAL-009) | A2 | Impossible à vérifier (prompt système absent du dépôt) | PRV-001 | Prompt système effectif, test « es-tu une IA ? » | AIA-003 |
| SYS-01 | Fournisseur | Exception « évident » motivée | Art. 50, par. 1 | Obligation (exception) | En vigueur (CAL-009) | A3 | Non applicable (aucune exception invoquée ; examinée et écartée) | PRV-001 | n.a. | AIA-003 |
| SYS-01 | Fournisseur | Marquage lisible par machine des textes | Art. 50, par. 2 | Obligation | En vigueur si mise sur le marché ≥ 2026-08-02 (CAL-010) ; sinon 2026-12-02, **échéance à confirmer** | A4 | Démontré (mesure présente, propriétaire) | PRV-003 | Date réelle de mise sur le marché ; forme du marquage retenue | AIA-005 |
| SYS-01 | Fournisseur | Préservation du marquage dans les exports | Art. 50, par. 2 | Obligation | Idem A4 | A5 | Non démontré | PRV-004, PRV-005 | Idem | AIA-004 |
| SYS-01 | Fournisseur | Détectabilité : outil ou API de vérification | Art. 50, par. 2 | Obligation | Idem A4 | A6 | Non démontré | PRV-006 | Documentation externe éventuelle | AIA-005 |
| SYS-01 | Fournisseur | Exceptions du par. 2 motivées | Art. 50, par. 2 | Obligation (exception) | Idem A4 | A7 | Non applicable (aucune exception invoquée ; écartées) | PRV-003 | n.a. | AIA-004 |
| SYS-01 | Fournisseur | Accessibilité et caractère reconnaissable | Art. 50, par. 5 | Obligation | En vigueur (CAL-009) | A11 | Impossible à vérifier | PRV-002 | Interface | AIA-003 |
| SYS-01 / SYS-02 | Déployeur | Hypertrucages, émotions, textes d'intérêt public | Art. 50, par. 3 et 4 | Obligation | En vigueur (CAL-009) | A8, A9, A10 | Non applicable (aucun usage) | PRV-008 | Interface | n.a. |
| SYS-02 | Fournisseur | Absence de reconnaissance des émotions des apprenants | Art. 5, par. 1, f) | Obligation | En vigueur (CAL-002) | F1 | Démontré (absence de composant biométrique dans le dépôt) | PRV-008 | Interface (voix, image) | AIA-002 |
| SYS-02 | Fournisseur | Orientation : qualification de l'annexe III | Art. 6, par. 2 et 3 | Obligation (classification) | Classification immédiate ; exigences : 2027-12-02, échéance à confirmer (CAL-011) | F2, F3 | Démontré (cas d'usage identifié ; qualification documentée par le présent rapport) | PRV-009 | Note de classification du fournisseur | AIA-006 |
| SYS-02 | Fournisseur | Dérogation art. 6, par. 3 documentée (si invoquée) | Art. 6, par. 4 | Obligation | À vérifier (CAL-016) | C11 | Non applicable (dérogation exclue) | PRV-009 | n.a. | AIA-006 |
| SYS-02 | Fournisseur | Aide à la décision pédagogique : profilage | Art. 6, par. 3, dernier al. | Obligation | Idem | F7 | Démontré (profilage identifié) | PRV-009 | n.a. | AIA-006 |
| SYS-02 | Fournisseur | Intervention humaine avant tout effet | Art. 14, par. 4, d) | Obligation future | Non encore applicable, 2027-12-02, échéance à confirmer (CAL-011) | B1 | Non démontré | PRV-010 | Procédure du conseil de classe | AIA-001 |
| SYS-02 | Fournisseur | Interprétation des résultats (justification, confiance) | Art. 14, par. 4, a) et c) ; art. 13 | Obligation future | Idem | B2 | Non démontré | PRV-011 | Affichage côté conseil | AIA-001 |
| SYS-02 | Fournisseur | Ignorer, annuler, remplacer une sortie | Art. 14, par. 4, d) | Obligation future | Idem | B3 | Non démontré | PRV-012 | Idem | AIA-001 |
| SYS-02 | Fournisseur | Interruption du système | Art. 14, par. 4, e) | Obligation future | Idem | B4 | Non démontré | PRV-012 | Procédure d'arrêt | AIA-008 |
| SYS-02 | Fournisseur | Traçabilité des interventions | Art. 12 ; art. 26, par. 6 | Obligation future | Idem | B6 | Non démontré | PRV-013 | Journaux de production | AIA-010 |
| SYS-02 | Fournisseur | Prévention de l'automatisation excessive | Art. 14, par. 4, b) | Obligation future | Idem | B7 | Non démontré | PRV-010 | n.a. | AIA-001 |
| SYS-02 | Déployeur | Superviseurs compétents et investis de l'autorité | Art. 26, par. 2 | Obligation future | Idem | B8 | Impossible à vérifier | PRV-018 | Organisation des établissements | AIA-013 |
| SYS-02 | Fournisseur | Documentation technique (annexe IV) | Art. 11 | Obligation future | Idem | C1 à C10 | Impossible à vérifier | PRV-019 | Documents hors dépôt | AIA-008 |
| SYS-02 | Fournisseur | Versions de modèle épinglées et documentées | Annexe IV | Bonne pratique immédiate / obligation future | Idem | C4 | Non démontré | PRV-015 | n.a. | AIA-011 |
| SYS-02 | Fournisseur | Gestion des risques, tests, robustesse | Art. 9, 15 | Obligation future | Idem | D1 à D4 | Non démontré (D4) / Impossible à vérifier (D1 à D3) | PRV-023, PRV-019 | Registre des risques, rapports de tests | AIA-009, AIA-016 |
| SYS-02 | Fournisseur | Surveillance après commercialisation, incidents | Art. 72, 73 | Obligation future | À vérifier `[AV]` | D5, D6 | Impossible à vérifier | PRV-019 | Procédures | AIA-008 |
| SYS-01 / SYS-02 | Fournisseur | Secrets absents du code | Bonne pratique | Bonne pratique | n.a. | D8 | Démontré | PRV-020 | Journaux de production | AIA-015 |
| SYS-02 | Fournisseur | Journaux, historique des décisions, versions | Art. 12 ; art. 86 `[AV]` | Obligation future | 2027-12-02 / `[AV]` | E1 à E5 | Non démontré | PRV-013, PRV-015 | Journaux de production | AIA-010, AIA-011 |
| SYS-02 | Fournisseur | Conservation des journaux au moins six mois | Art. 19 ; art. 26, par. 6 | Obligation future | Idem | E6 | Non démontré (constante de 30 jours) | PRV-016 | Politique de rétention effective | AIA-010 |
| SYS-02 | Déployeur | Information des élèves et des familles | Art. 26, par. 11 | Obligation future | Non encore applicable, 2027-12-02, échéance à confirmer | F8 | Impossible à vérifier | PRV-002 | Documents d'information des établissements | AIA-013 |
| SYS-02 | Déployeur | Échéance de l'art. 111, par. 2 pour établissements publics ; art. 27 | Art. 111, par. 2 `[AV]` ; art. 27 | Obligation | Conditionnel (CAL-013), échéance à confirmer | F9 | Impossible à vérifier | PRV-025 | Statut des établissements | AIA-013 |
| SYS-01 / SYS-02 | Fournisseur | Maîtrise de l'IA | Art. 4 | Obligation | En vigueur (CAL-002) ; rédaction : échéance à confirmer (CAL-003) | G1 à G3 | Impossible à vérifier | PRV-018 | Plan de formation, registre | AIA-012 |
| SYS-01 | Fournisseur | Documentation d'usage remise aux utilisateurs | Bonne pratique contribuant à l'art. 4 | Bonne pratique | n.a. | G4 | Impossible à vérifier | PRV-018 | Guide d'usage | AIA-012 |
| SYS-01 / SYS-02 | Fournisseur | Obligations GPAI | Art. 53 à 55 | Obligation (non applicable) | CAL-005 | n.a. | Non applicable | PRV-025 | Contrat Mistral | AIA-014 |

## Matrice des preuves

| PRV | Contrôle | Constat(s) | Fichier | Lignes | Commit | Date | Nature | Méthode de reproduction | État |
|---|---|---|---|---|---|---|---|---|---|
| PRV-001 | A1, A2, A3 | AIA-003 | `app/assistant.py` | 10 | non versionné | 2026-10-27 | Statique | `sed -n '10p' app/assistant.py` ; `grep -rn BANNER .` (une seule occurrence) | Non démontré (A1) |
| PRV-002 | A1 (interface), A11, F8 | AIA-003, AIA-013 | racine du dépôt | n.a. | non versionné | 2026-10-27 | Statique | `find . -type f` (9 fichiers, aucun gabarit d'interface ni route FastAPI) | Impossible à vérifier |
| PRV-003 | A4, A7 | AIA-005, AIA-004 | `app/assistant.py` | 18-19 | non versionné | 2026-10-27 | Statique | `sed -n '18,19p' app/assistant.py` | Démontré (présence du champ `meta.ai_generated`) |
| PRV-004 | A5 | AIA-004 | `app/export.py` | 7-13 | non versionné | 2026-10-27 | Statique | `sed -n '7,13p' app/export.py` | Non démontré |
| PRV-005 | A5 | AIA-004 | `app/export.py` | 16-20 | non versionné | 2026-10-27 | Statique | `sed -n '16,20p' app/export.py` | Non démontré |
| PRV-006 | A6 | AIA-005 | dépôt entier | n.a. | non versionné | 2026-10-27 | Statique | `grep -rniE "verify\|detect\|signature\|c2pa\|xmp" .` (aucune occurrence dans le code) | Non démontré |
| PRV-008 | F1, A8 à A10 | AIA-002 | `app/assistant.py` ; `requirements.txt` | 22-26 ; 1-3 | non versionné | 2026-10-27 | Statique | `python3 scripts/scan_ai_signals.py .` (aucune catégorie « biometrics ») ; `sed -n '22,26p' app/assistant.py` | Démontré (absence de composant biométrique) |
| PRV-009 | F2, F3, F7, classification | AIA-002, AIA-006 | `app/orientation.py` ; `app/assistant.py` ; `README.md` | 1-24 ; 16-17, 22-31 ; 13-14 | non versionné | 2026-10-27 | Statique | `cat -n app/orientation.py` ; `sed -n '16,31p' app/assistant.py` | Démontré |
| PRV-010 | B1, B7 | AIA-001 | `app/orientation.py` | 12-19 | non versionné | 2026-10-27 | Statique | `sed -n '12,19p' app/orientation.py` | Non démontré |
| PRV-011 | B2 | AIA-001 | `app/orientation.py` | 12-17 | non versionné | 2026-10-27 | Statique | `sed -n '12,17p' app/orientation.py` | Non démontré |
| PRV-012 | B3, B4 | AIA-001, AIA-008 | `app/orientation.py` | 18-24 | non versionné | 2026-10-27 | Statique | `grep -rniE "override\|reject\|pending_review\|stop\|disable" app/` (aucun résultat) | Non démontré |
| PRV-013 | B6, E1, E2 | AIA-010 | dépôt entier | n.a. | non versionné | 2026-10-27 | Statique | `grep -rniE "logging\|logger\|audit_log\|validated_by" .` (aucun résultat) | Non démontré |
| PRV-015 | C4, E3, E4 | AIA-011 | `app/assistant.py` | 8, 14, 25, 29-31 | non versionné | 2026-10-27 | Statique | `sed -n '8p;14p;25p;29,31p' app/assistant.py` | Non démontré |
| PRV-016 | E6 | AIA-010 | `app/config.py` | 2 | non versionné | 2026-10-27 | Statique | `cat app/config.py` ; `grep -rn LOG_RETENTION_DAYS .` (aucune autre occurrence) | Non démontré |
| PRV-017 | Documentation | AIA-007, AIA-001 | `docs/compliance.md` ; `docs/human-oversight.md` ; `README.md` | 3-7 ; 3-4 ; 6 | non versionné | 2026-10-27 | Statique | `cat -n docs/*.md` ; `sed -n '6p' README.md` ; confronter à `references/applicability-calendar.md` | Démontré (contradictions) |
| PRV-018 | G1 à G4, B8 | AIA-012 | dépôt entier | n.a. | non versionné | 2026-10-27 | Statique | `find . -type f` (aucun document de formation) | Impossible à vérifier |
| PRV-019 | C1 à C10, D1 à D6 | AIA-008 | dépôt entier | n.a. | non versionné | 2026-10-27 | Statique | `find . -type f` (aucune documentation technique) | Impossible à vérifier |
| PRV-020 | D8 | AIA-015 | `app/assistant.py` | 7 | non versionné | 2026-10-27 | Statique | `sed -n '7p' app/assistant.py` (valeur lue dans l'environnement ; masquée) | Démontré |
| PRV-021 | Calendrier | tous | `scripts/obligation_timeline.py` | n.a. | n.a. | 2026-10-27 | Statique | `python3 <skill>/scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-10-15` (et `--placed-on-market 2026-03-01 --scope generative`) | Démontré |
| PRV-022 | Signaux | tous | `scripts/scan_ai_signals.py` | n.a. | n.a. | 2026-10-27 | Statique | `python3 <skill>/scripts/scan_ai_signals.py <projet>` | Démontré |
| PRV-023 | D4 | AIA-009, AIA-016 | `app/assistant.py` ; `app/orientation.py` | 26, 30 ; 8-10 | non versionné | 2026-10-27 | Statique | `sed -n '26p;30p' app/assistant.py ; sed -n '8,10p' app/orientation.py` | Non démontré |
| PRV-025 | Rôles, exclusions, GPAI | AIA-013, AIA-014 | `README.md` | 3-11 | non versionné | 2026-10-27 | Statique | `sed -n '3,11p' README.md` | Impossible à vérifier (déclaratif) |

**Preuves externes** (non établies par analyse statique) : écrans et captures de l'interface ; prompt système effectif ; date de première mise en service ; contrats avec Mistral et avec les établissements ; documentation du fournisseur de modèle ; plan et registre de formation ; documentation technique, registre des risques, procédures d'incident ; configuration de production et journaux.

Rappel : « Mesure observée » n'équivaut pas à « obligation satisfaite ».

---

# Annexe E : Registre des éléments non vérifiables

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact | Interlocuteur suggéré | Constat(s) liés |
|---|---|---|---|---|---|---|---|
| NV-01 | SYS-01 | Interface réelle : texte affiché au premier échange, canaux (web, mobile), collecte éventuelle de voix ou d'image | Document / information | Établir l'art. 50, par. 1 et 5, et écarter définitivement l'art. 5, par. 1, f) | Confirme ou lève AIA-003 ; peut modifier l'analyse de l'art. 5 | Responsable produit, UX | AIA-002, AIA-003 |
| NV-02 | SYS-01, SYS-02 | Date de première mise en service par système (et de chaque version majeure) ; marque ; pays ; clients ; taille de l'entreprise | Information | Appliquer le régime de CAL-010 et CAL-013 ; confirmer le rôle de fournisseur ; mesures PME | Statut temporel de l'art. 50, par. 2 (en vigueur ou 2026-12-02) ; art. 111, par. 2 | Direction, juridique | AIA-004, AIA-005, AIA-013 |
| NV-03 | SYS-02 | Statut des établissements clients (publics / privés, organismes de droit public) | Information / juridique | Art. 27, art. 111, par. 2 `[AV]`, obligations de déployeur | Échéances et obligations des déployeurs | Commercial, juridique | AIA-013 |
| NV-04 | SYS-02 | Effet réel d'`apply_decision`, rôle exact du conseil de classe, tableau de bord enseignant, usage des scores, séparation SYS-01 / SYS-02 | Décision / information | Établir le niveau de l'échelle (3 ou 4), l'art. 5, par. 1, c), la classification | Peut aggraver ou atténuer AIA-001, AIA-002, AIA-006 | Responsable produit, établissements | AIA-001, AIA-002, AIA-006 |
| NV-05 | SYS-02 | Documentation technique, registre des risques, gouvernance des données, gestion de la qualité, plan de tests, notice | Document | Préparer les exigences du chapitre III | Aucune conclusion de non-conformité sans ces documents | Responsable qualité | AIA-008 |
| NV-06 | SYS-01, SYS-02 | Contrat et documentation de Mistral (annexe XII) ; conditions d'utilisation pour l'éducation et les mineurs ; absence d'affinage | Document | Rôle GPAI, documentation en aval | Confirme AIA-014 | Achats, juridique | AIA-014 |
| NV-07 | SYS-01 | Format de marquage retenu pour les textes ; lignes directrices de la Commission du 20.7.2026 `[AV]` | Juridique | Définir la solution technique | Incertitude de modalités uniquement, **pas une exemption** | Juridique, architecte | AIA-004, AIA-005 |
| NV-08 | SYS-01, SYS-02 | Mesures de maîtrise de l'IA (formation, guides, registre) | Document | Art. 4 | Confirme ou lève AIA-012 | Responsable RH / conformité | AIA-012 |
| NV-09 | SYS-01, SYS-02 | Configuration de production, rétention réelle, journaux, secrets | Information | Art. 12, 19 ; bonnes pratiques de sécurité | Évaluer AIA-010, AIA-015 | Exploitation | AIA-010, AIA-015 |
| NV-10 | n.a. | Texte consolidé officiel 2026/1744 | Juridique | Lever la réserve sur CAL-003, CAL-004, CAL-010 (délai), CAL-011, CAL-012, CAL-013, CAL-015, CAL-016 | Confirme les échéances | Juridique | AIA-006, AIA-008, AIA-010, AIA-012, AIA-013 |

---

# Annexe F : Plan de remédiation synthétique

Date d'audit : 2026-10-27. Priorisation : `references/findings-methodology.md`, section 6.

| Priorité | Constat(s) | Action | Base | Échéance réglementaire | Effort | Responsable suggéré | Preuve de clôture attendue |
|---|---|---|---|---|---|---|---|
| P1 | AIA-001 | Supprimer l'application automatique ; imposer `pending_review` et validation du conseil de classe avec motif ; afficher les facteurs ; supprimer la « confiance » en dur | Bonne pratique immédiate ; art. 14 à venir | 2027-12-02, échéance à confirmer | M | Produit / développement | Test montrant qu'aucune orientation n'est enregistrée sans validation ; journal |
| P1 | AIA-002 | Suspendre le calcul et la réutilisation du score d'engagement pour l'orientation ; analyse juridique art. 5, par. 1, c) | Art. 5, par. 1, c) | En vigueur depuis 2025-02-02 | S | Direction, juridique | Avis écrit ; code sans lecture du score |
| P1 | AIA-003 | Afficher l'information « IA » à la première interaction, sur tous les canaux ; faire répondre qu'il s'agit d'une IA | Art. 50, par. 1 et 5 | En vigueur depuis 2026-08-02 | S | Produit / UX | Captures, tests d'interface |
| P1 | AIA-004 | Marquer les exports PDF et CSV (métadonnées, colonne de provenance, mention) | Art. 50, par. 2 | En vigueur (si mise sur le marché ≥ 2026-08-02) ; sinon 2026-12-02, échéance à confirmer | M | Développement | Tests de bout en bout sur les exports |
| P1 | AIA-007 | Corriger `docs/compliance.md`, `docs/human-oversight.md` ; retirer « conforme » et « certifié » des supports | Art. 50 ; règle 16 | Immédiat | S | Conformité, marketing | Documents révisés et datés |
| P2 | AIA-005 | Marquage standard, signé, documenté ; outil de vérification | Art. 50, par. 2 | Idem AIA-004 | M | Architecte | Documentation API ; tests |
| P2 | AIA-006 | Note de classification formelle (annexe III, point 3 ; profilage) | Art. 6 | Classification : immédiate | S | Juridique | Note signée |
| P2 | AIA-009 | Découpler le score du chat ; valider la sortie ; mesures par sous-groupes | Bonne pratique ; art. 10, 15 à venir | 2027-12-02, échéance à confirmer | M | Développement / data | Tests de robustesse ; rapport d'évaluation |
| P2 | AIA-012, AIA-013 | Plan de maîtrise de l'IA ; registre de dates de mise en service et de clients | Art. 4 ; art. 3, 111 | Art. 4 en vigueur ; CAL-003 à confirmer | S à M | RH, direction | Plan, registre |
| P3 | AIA-008, AIA-010 | Feuille de route haut risque : gestion des risques, documentation, journalisation (≥ 6 mois), SGQ, évaluation de la conformité, enregistrement | Art. 9 à 17, 43, 47 à 49, 72, 73, 86 | 2027-12-02, échéance à confirmer | L | Direction, conformité | Plan daté ; dossiers |
| P3 | AIA-011 | Épingler le modèle ; journaliser la version servie | Bonne pratique ; art. 12 à venir | Immédiat (bonne pratique) | S | Développement | Configuration ; journal |
| P3 | AIA-016 | Valider les identifiants ; gérer les cas limites ; stockage adapté | Bonne pratique ; art. 15 à venir | Idem | S | Développement | Tests unitaires |
| P4 | AIA-014, AIA-015 | Conserver la documentation de Mistral ; analyse de secrets en CI | Bonne pratique | n.a. | S | Achats, développement | Dossier fournisseur ; pipeline |

## Jalons

| Date | Évènement réglementaire | Actions à terminer avant |
|---|---|---|
| Immédiat | Art. 4, art. 5, art. 50, par. 1 en vigueur | AIA-002, AIA-003, AIA-007 |
| 2026-12-02 | Nouvelles interdictions art. 5 (CAL-004) ; fin du délai transitoire de l'art. 50, par. 2 pour les systèmes antérieurs au 2026-08-02 (CAL-010) | Confirmer la date de mise sur le marché ; AIA-004, AIA-005 |
| 2027-12-02 | Exigences du haut risque annexe III (CAL-011), échéance à confirmer | AIA-001, AIA-006, AIA-008, AIA-009, AIA-010 |

## Hypothèses

- Efforts estimés à partir du dépôt seul ; à recalibrer avec l'équipe.
- Les échéances issues du règlement 2026/1744 (confiance moyenne) sont à confirmer.
- Un ré-audit complet est recommandé après correction (SKILL.md, phase 11), en conservant les identifiants AIA-NNN.
