<!-- Rapport brut d'un agent (skill 1.2.1, modèle par défaut de la session), audit à l'aveugle de demo-ai-vulnerable, 2026-10-27. Chemins anonymisés, cadratins normalisés. -->

# 1. Synthèse (15 lignes max.)

1. Systèmes (fournisseur : EduAssist SAS ; déployeurs : les établissements) : SYS-01 tuteur conversationnel (non à haut risque, art. 50) ; SYS-02 correction automatique (haut risque probable, annexe III, point 3, b)) ; SYS-03 illustrations (non à haut risque, art. 50, par. 2 et 4) ; SYS-04 surveillance d'examens (pratique potentiellement interdite, art. 5, par. 1, f), et haut risque probable, annexe III, point 3, d)).
2. AIA-001 : inférence d'émotions des élèves pendant les examens (SYS-04). Risque potentiel, Critique, en vigueur depuis le 2025-02-02 (CAL-002).
3. AIA-002 : le prompt du tuteur impose une persona humaine et la négation de la nature d'IA (SYS-01). Constat technique avéré, Élevée, en vigueur depuis le 2026-08-02 (CAL-009).
4. AIA-003 : la note finale est générée puis publiée sans contrôle humain, et elle n'est ni reproductible ni validée (SYS-02). Risque potentiel, Élevée. Art. 14/15 non encore applicables (2027-12-02, CAL-011) ; régime conditionnel CAL-013.
5. AIA-004 : annulation automatique des examens sans intervention humaine (SYS-04). Risque potentiel, Élevée. Mêmes échéances (CAL-011, CAL-013).
6. AIA-005 : générateur d'images à prompt libre sans garde-fou observable, au regard des nouvelles interdictions (SYS-03). Non encore applicable, Élevée, 2026-12-02 (CAL-004).
7. AIA-006 : clé d'API écrite en clair dans le code (tous systèmes). Constat technique avéré, Élevée. Aucune obligation de l'AI Act en vigueur ; art. 15 à venir.
8. AIA-007 : images enregistrées sans marquage lisible par machine (SYS-03). Non encore applicable, Moyenne, 2026-12-02 (CAL-010).
9. AIA-008 : réponses textuelles du tuteur sans marquage (SYS-01). Non encore applicable, Moyenne, 2026-12-02 (CAL-010).
10. AIA-009 : exigences du haut risque non préparées ou non observables (SYS-02, SYS-04). Non encore applicable, Moyenne, 2027-12-02 (CAL-011) ; CAL-013 conditionnel (au plus tard le 2030-08-02 si autorités publiques).
11. AIA-010 : aucune journalisation des notes, des annulations ni des versions (SYS-02, SYS-04). Non encore applicable, Moyenne, 2027-12-02 (CAL-011).
12. AIA-011 : versions de modèles non épinglées et non journalisées, ce qui pèse sur l'art. 111, par. 2 [AV] (tous systèmes). Bonne pratique recommandée, Moyenne.
13. AIA-012 : hypertrucages possibles, sans outil d'étiquetage pour le déployeur (SYS-03). À vérifier juridiquement ou organisationnellement, Moyenne, en vigueur (CAL-009).
14. AIA-013 : maîtrise de l'IA non observable dans le dépôt (tous systèmes). À vérifier organisationnellement, Faible, en vigueur (CAL-002, CAL-003).
15. AIA-014 : obligations GPAI (art. 53 à 55), EduAssist n'étant pas fournisseur de modèle. Non applicable, Information. Aucun constat ne repose sur une entrée « échéance à confirmer ».

---

# 2. Rapport complet

# Rapport d'audit AI Act : demo-ai-vulnerable (« EduAssist »)

> **Avertissement.** Ce rapport aide à l'audit. Il repose sur l'analyse statique d'un dépôt et sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43 du règlement (UE) 2024/1689.

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | Racine `<fixture>/demo-ai-vulnerable` : 9 fichiers (`README.md`, `requirements.txt`, `app/*.py`). Aucun dossier exclu. |
| Commit audité | Non versionné : `git rev-parse HEAD` renvoie « not a git repository ». |
| Mode | Complet |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`data/ai-act-calendar.json`, `meta.last_verified`). Écart nul avec la date d'audit, donc aucune limite liée à l'ancienneté des références. |
| Contexte fourni par le demandeur | Aucun hors du dépôt. Le contexte vient du `README.md`, qui le présente lui-même comme fictif : éditeur EduAssist SAS établi en France ; produit vendu sous la marque EduAssist à des lycées et universités de l'Union ; mise sur le marché de tous les modules le 2026-03-01 ; modèles accessibles par l'API OpenAI ; aucun entraînement. |
| Méthode | Skill `ia-compliance` v1.2.1, en lecture seule, sans exécution du code audité. Outils : `scan_ai_signals.py`, `obligation_timeline.py`. |
| Audit précédent | Aucun |

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : 4. SYS-01 tuteur conversationnel, SYS-02 correction automatique des dissertations, SYS-03 génération d'illustrations de cours, SYS-04 surveillance d'examens par webcam.
- **Points les plus sensibles** :
  - **AIA-001** : SYS-04 déduit les émotions des élèves à partir de leur visage pendant les examens, puis s'en sert pour annuler des copies. Cette fonction est susceptible de relever de la pratique interdite de l'art. 5, par. 1, f), applicable depuis le 2025-02-02.
  - **AIA-002** : le tuteur reçoit l'instruction de nier être une IA et de se présenter comme une enseignante. C'est un manquement potentiel à l'art. 50, par. 1, en vigueur depuis le 2026-08-02.
  - **AIA-003 / AIA-004** : des décisions entièrement automatisées touchent des élèves (note finale publiée, examen annulé). Le chapitre III ne s'applique pas encore, mais le risque pour les personnes est actuel.
  - **AIA-005 / AIA-007** : deux échéances tombent le **2026-12-02**, soit dans 36 jours : les nouvelles interdictions de l'art. 5 (CAL-004) et le marquage des contenus de l'art. 50, par. 2 pour les systèmes mis sur le marché avant le 2026-08-02 (CAL-010).
- **Obligations en vigueur concernées** : art. 4 (CAL-002, CAL-003) ; art. 5, par. 1, a) à h) (CAL-002) ; art. 50, par. 1, 3, 4 et 5 (CAL-009).
- **Échéances à venir** :
  - 2026-12-02 : art. 50, par. 2 (CAL-010, régime transitoire) et art. 5, par. 1, b bis) et b ter) (CAL-004).
  - 2027-12-02 : haut risque de l'annexe III (CAL-011).
  - Régime de l'art. 111, par. 2 (CAL-013) : conditionnel pour ces systèmes antérieurs. Pour les systèmes destinés aux autorités publiques, l'échéance tombe au plus tard le 2030-08-02.
- **Principales incertitudes** :
  - statut public ou privé des établissements clients ;
  - réalité de la mise sur le marché (le README se dit « fixture » fictive, « ne pas déployer ») ;
  - interface utilisateur absente du dépôt ;
  - garde-fous et marquages éventuels appliqués en amont par le fournisseur des modèles ;
  - documents organisationnels.
- **Constats dont l'échéance est à confirmer** : **aucun**. Aucun constat ne repose sur une entrée `requires_confirmation`. CAL-016 (enregistrement au titre de l'art. 49, par. 2) n'est pas mobilisé, car la dérogation de l'art. 6, par. 3 est écartée pour SYS-02 et SYS-04. Il deviendrait « échéance à confirmer » si le fournisseur invoquait cette dérogation.
- **Synthèse des constats** :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | | 2 (AIA-002, AIA-006) | | | |
| Risque potentiel | 1 (AIA-001) | 2 (AIA-003, AIA-004) | | | |
| À vérifier juridiquement ou organisationnellement | | | 1 (AIA-012) | 1 (AIA-013) | |
| Bonne pratique recommandée | | | 1 (AIA-011) | | |
| Non encore applicable | | 1 (AIA-005) | 4 (AIA-007, AIA-008, AIA-009, AIA-010) | | |
| Non applicable | | | | | 1 (AIA-014) |

## 2. Périmètre et méthode

Fichiers analysés :

- `README.md` : contexte déclaré et table des modules ;
- `requirements.txt` : `fastapi==0.115.0`, `openai==1.51.0`, `deepface==0.0.93`, `opencv-python==4.10.0.84` ;
- `app/config.py`, `app/tutor_chat.py`, `app/grading.py`, `app/gradebook.py`, `app/illustrations.py`, `app/proctoring.py` ;
- `app/__init__.py`, qui est vide.

Outils :

- `python3 -I scripts/scan_ai_signals.py <projet>` a relevé 9 catégories de signaux, dont `transparency_risk/ai-denial`, `sensitive_context/emotion-inference`, `biometric/face-recognition` et `output_channel/file-write`, ainsi qu'un secret potentiel dans `app/config.py:2`.
- `python3 -I scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-03-01` a été lancé avec les portées `all`, `provider`, `deployer`, `transparency`, `generative`, `prohibited`, `high-risk-annex-iii` et `gpai-provider`. Pour l'annexe III, il a été relancé avec et sans `--public-authority`.

Éléments absents du dépôt, donc non analysés :

- aucune route FastAPI ni interface utilisateur, bien que `fastapi` figure dans les dépendances ;
- aucun test, aucune configuration de déploiement ;
- aucune documentation hors du README.

Recherche de faux négatifs : aucun appel HTTP direct, drapeau de fonctionnalité ou prompt externe n'a été trouvé.

## 3. Systèmes d'IA identifiés

| ID | Système | Finalité | Rôle(s) de l'organisation | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|
| SYS-01 | Tuteur conversationnel « Claire » | Répondre aux questions des élèves sur les cours | EduAssist : fournisseur ; établissements : déployeurs | OpenAI, `gpt-4o` (alias sans date) | Non à haut risque (motivé) ; soumis à l'art. 50, par. 1 et 2 | Moyenne : la réutilisation des échanges n'est pas observable |
| SYS-02 | Correction automatique | Attribuer la note finale des dissertations, publiée dans le bulletin et comptant pour le passage en classe supérieure | Idem | OpenAI, `gpt-4o`, `temperature=1.0` | Haut risque probable (annexe III, point 3, b)) | Élevée (faits) / Élevée (qualification) |
| SYS-03 | Illustrations de cours | Générer des images pour les supports de cours publiés aux élèves | Idem | OpenAI, `dall-e-3` | Non à haut risque (motivé) ; soumis à l'art. 50, par. 2 (fournisseur) et par. 4 (déployeur) ; art. 5, par. 1, b bis) à partir du 2026-12-02 | Élevée |
| SYS-04 | Surveillance d'examens en ligne | Analyser la webcam pendant l'examen et annuler automatiquement les copies jugées suspectes | Idem | Bibliothèque DeepFace (modèles pré-entraînés open source), OpenCV | Pratique potentiellement interdite (art. 5, par. 1, f)) ; à titre subsidiaire, haut risque probable (annexe III, point 3, d) ; point 1, c)) | Élevée (faits) / Moyenne (qualification juridique) |

Composants examinés et écartés :

- `app/gradebook.py` : stockage déterministe en mémoire, sans inférence. C'est un composant aval de SYS-02, pas un système d'IA.
- `app/config.py` : configuration (identifiants de modèles, clé). Composant commun.
- `proctoring.py:22`, règle `suspicious > 30` : règle déterministe fixée par un humain. Elle fait partie de SYS-04 parce qu'elle s'applique à la sortie d'un modèle d'inférence. Seule, elle ne serait pas un système d'IA.

Choix de regroupement : `gpt-4o` sert à deux finalités, deux publics et deux parcours distincts (tutorat et notation). D'où deux systèmes séparés, SYS-01 et SYS-02, conformément à `ai-detection-signals.md`, section 5. Aucun flux de réutilisation des échanges du tuteur vers la notation n'est observé (système hybride écarté au vu du code, voir NV-05).

## 4. Rôles réglementaires

- **EduAssist SAS** (déclarée établie en France) développe les quatre systèmes et les commercialise sous sa marque auprès d'établissements de l'Union (`README.md:8-10`). Au vu de ces éléments, elle est **susceptible d'être fournisseur** des systèmes SYS-01 à SYS-04 (art. 3, point 3) et fournisseur en aval de modèles d'IA (art. 3, point 68). Établie dans l'Union, elle n'a pas de mandataire et ne relève pas d'un rôle d'importateur pour ses propres systèmes. L'art. 25 n'entre pas en jeu : EduAssist est fournisseur d'origine.
- **EduAssist n'est pas fournisseur de modèle GPAI**, au vu du dépôt : aucun entraînement, affinage ou publication de poids, et le README le déclare (`README.md:12`). Le fournisseur des modèles sous-jacents (OpenAI pour `gpt-4o` et `dall-e-3`) est susceptible d'être fournisseur de modèle GPAI. Pour `dall-e-3`, la qualification de modèle GPAI relève d'une interprétation [AV]. Les auteurs des modèles DeepFace sont des tiers ; leur intégration ne fait pas d'EduAssist un fournisseur de modèle.
- **Établissements clients** (lycées, universités) : **déployeurs** (art. 3, point 4), qui utilisent les systèmes sous leur autorité pour leurs élèves (`README.md:11`). Leur caractère d'autorité publique ou d'organisme de droit public est à vérifier (NV-02). Il conditionne l'échéance du 2030-08-02 (art. 111, par. 2) et l'art. 27.
- **Enseignants** : personnes susceptibles d'être chargées du contrôle humain (art. 26, par. 2). Ce ne sont pas des opérateurs distincts.

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 3, point 1 (définition) | Tous | Écartée (ce sont des systèmes d'IA) | SYS-01 à SYS-03 : génération par LLM ou modèle de diffusion. SYS-04 : modèle d'apprentissage profond qui déduit des émotions. Seuls `gradebook.py` et la règle de seuil sont déterministes. |
| Art. 2, par. 3 (défense) | Tous | Écartée | Usage éducatif civil |
| Art. 2, par. 6 et 8 (recherche, développement avant mise sur le marché) | Tous | Écartée sous le contexte déclaré, avec réserve | Le README déclare une mise sur le marché au 2026-03-01. Il se décrit aussi comme « fixture de test » à « ne pas déployer ». Si aucune mise sur le marché ni mise en service n'avait réellement lieu, l'art. 2, par. 8 pourrait jouer : question NV-01. Le rapport évalue le scénario déclaré. |
| Art. 2, par. 10 (usage personnel) | Tous | Écartée | Usage professionnel par des établissements |
| Art. 2, par. 12 (open source) | Tous | Écartée | Aucune licence libre dans le dépôt ; activité commerciale. L'exclusion ne joue de toute façon pas pour l'art. 5, l'art. 50 ni le haut risque. DeepFace est open source, mais EduAssist l'intègre dans un produit commercial. |
| Art. 5, par. 1, f) : exception médicale ou de sécurité | SYS-04 | Écartée | Finalité observée : détection de comportements suspects ou de fraude (`proctoring.py:5, 20-24`). La lutte contre la fraude n'est pas une « raison de sécurité », exception d'interprétation stricte [TI]. |
| Art. 5, par. 1, a) et b) (manipulation, exploitation de la vulnérabilité liée à l'âge) | SYS-01 | Examinée, non retenue | La persona humaine imposée (`tutor_chat.py:8-11`) est trompeuse et vise des lycéens, éventuellement mineurs. Mais aucun élément n'établit une altération substantielle du comportement causant un préjudice important (conditions cumulatives). Le point relève d'abord de l'art. 50, par. 1 (AIA-002). |
| Art. 5, par. 1, g) (catégorisation biométrique sensible) et h) | SYS-04 | Non retenue | Seule l'action `emotion` est demandée (`proctoring.py:9`). Aucune déduction d'attribut sensible, aucune identification à distance à des fins répressives. |
| Art. 5, par. 1, c), d), e) | Tous | Non retenue | Aucun indice de notation sociale, de prédiction d'infraction ni de moissonnage d'images faciales |
| Art. 6, par. 1 (annexe I) | Tous | Écartée | Aucun produit ni composant de sécurité relevant de la législation de l'annexe I |
| Art. 6, par. 3 (dérogation) | SYS-02 | Écartée | La sortie est la note finale publiée sans relecture (`grading.py:3-4, 28`). Ce n'est ni une tâche procédurale étroite, ni une amélioration d'une activité humaine déjà réalisée, ni une tâche préparatoire, et le résultat de la décision est déterminé. Un profilage est en outre possible (évaluation des performances d'un élève), ce qui exclurait de toute façon la dérogation. |
| Art. 6, par. 3 (dérogation) | SYS-04 | Écartée | Annulation automatique (`proctoring.py:22-24`) : la sortie détermine la décision. |
| Art. 50, par. 1 : exception « évident » | SYS-01 | Écartée | Le prompt impose un nom humain et la négation de la nature d'IA. L'exception n'est pas plausible. |
| Art. 50, par. 2 : exceptions (mise en forme standard, absence de modification substantielle) | SYS-01, SYS-03 | Écartées | Génération de contenus nouveaux à partir d'une question ou d'un prompt. |
| Art. 50, par. 2 appliqué à la sortie de SYS-02 | SYS-02 | Non retenu à titre principal, à confirmer | La sortie est une valeur numérique inscrite dans un bulletin, pas un contenu diffusé. Sa qualification comme « contenu synthétique textuel » est douteuse [AV] (NV-08). |
| Art. 50, par. 4, al. 2 (textes d'intérêt public) | SYS-01 | Non retenue | Réponses individuelles, sans publication au public |
| Art. 50, par. 4, al. 1 : régime artistique ou créatif | SYS-03 | Indéterminée | Dépend des contenus générés (AIA-012) |
| Art. 53 à 55 (GPAI) | Tous | Non applicable | Voir AIA-014 |

## 6. Classification

**SYS-01 : tuteur conversationnel.**

- Étape 0 : système d'IA.
- Étape 1 : aucune exclusion.
- Étape 2 : art. 5, a) et b) examinés et non retenus.
- Étapes 3 et 4 : aucun usage évaluatif observé ; annexe III, point 3 non retenue. Hypothèse alternative : si les échanges servaient à noter ou à orienter, l'annexe III, point 3, b) s'appliquerait (NV-05).
- Étape 6 : art. 50, par. 1 (interaction directe, en vigueur) et par. 2 (texte synthétique ; délai au 2026-12-02 car mis sur le marché avant le 2026-08-02).
- Étape 8 : art. 4.
- Conclusion : **non à haut risque (motivé)**, confiance moyenne.

**SYS-02 : correction automatique.**

- Annexe III, point 3, b) : évaluation des acquis d'apprentissage.
- Échelle des scénarios (`person-decisions.md`) : niveau 4, décision entièrement automatisée. La note est publiée et compte pour le passage en classe supérieure.
- Questions obligatoires :
  - (1) sortie : un nombre extrait d'un JSON (`grading.py:27`), écrit dans le bulletin (`grading.py:28`, `gradebook.py:5-6`) ;
  - (2) décision : la note elle-même, prise sans humain ;
  - (3) à (6) contrôle humain : aucun, non modifiable avant effet ;
  - (7) profilage : possible ;
  - (8) données : texte de la copie et identifiant de l'élève ;
  - (9) information des élèves et explication : non observées ;
  - (10) réutilisation : bulletin, passage en classe supérieure.
- Dérogation de l'art. 6, par. 3 écartée.
- Conclusion : **haut risque probable (annexe III)**, confiance élevée.
- Art. 50 : non retenu à titre principal (section 5).
- Art. 4 applicable.

**SYS-03 : illustrations.**

- Aucun cas d'usage de l'annexe III.
- Art. 50, par. 2 : fournisseur, délai au 2026-12-02.
- Art. 50, par. 4, al. 1 : déployeur, en cas d'hypertrucage.
- Art. 5, par. 1, b bis) et b ter), par. 1 bis : applicables à partir du 2026-12-02. Ce n'est pas la destination du système, d'où l'examen du point a), ii) : prompt libre, garde-fous à démontrer.
- Conclusion : **non à haut risque (motivé)**.

**SYS-04 : surveillance d'examens.**

- Système de reconnaissance des émotions (art. 3, point 39), utilisé à partir d'images faciales issues de la webcam, dans des établissements d'enseignement.
- Art. 5, par. 1, f) : **pratique potentiellement interdite**. L'interdiction prime sur toute autre qualification.
- À titre subsidiaire, si la composante émotionnelle était retirée : annexe III, point 3, d) (détection de comportements interdits lors d'examens), donc **haut risque probable**, sans dérogation possible puisque l'annulation est automatique. L'annexe III, point 1, c) n'est pas pertinente pour une utilisation interdite.
- Art. 50, par. 3 (information des personnes exposées, déployeur) : subsidiaire.
- Art. 4 applicable.

## 7. Obligations et calendrier

Statuts calculés au 2026-10-27, avec une mise sur le marché déclarée au 2026-03-01 (date non vérifiée).

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|
| Interdiction de la reconnaissance des émotions en enseignement (art. 5, par. 1, f)) | SYS-04 | Fournisseur et déployeur | En vigueur | 2025-02-02 | CAL-002 | Élevée |
| Maîtrise de l'IA (art. 4, rédaction 2026/1744) | Tous | Fournisseur et déployeur | En vigueur | 2025-02-02 / 2026-07-27 | CAL-002, CAL-003 | Élevée |
| Information sur l'interaction avec une IA (art. 50, par. 1 et 5) | SYS-01 | Fournisseur | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Information des personnes exposées à la reconnaissance des émotions (art. 50, par. 3) | SYS-04 | Déployeur | En vigueur (subsidiaire, voir art. 5) | 2026-08-02 | CAL-009 | Élevée |
| Déclaration des hypertrucages (art. 50, par. 4, al. 1) | SYS-03 | Déployeur | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Marquage lisible par machine (art. 50, par. 2) | SYS-01, SYS-03 | Fournisseur | Non encore applicable (régime transitoire, art. 111, par. 4) | 2026-12-02 | CAL-010 | Élevée |
| Nouvelles interdictions (art. 5, par. 1, b bis), b ter), par. 1 bis) | SYS-03 | Fournisseur et déployeur | Non encore applicable | 2026-12-02 | CAL-004 | Élevée |
| Exigences du haut risque, annexe III (art. 8 à 27, dont art. 9 à 15, 16, 17, 26, 27) | SYS-02, SYS-04 | Fournisseur et déployeur | Non encore applicable | 2027-12-02 | CAL-011 | Élevée |
| Systèmes antérieurs (art. 111, par. 2) | SYS-02, SYS-04 | Fournisseur et déployeur | Conditionnel : soumis seulement en cas d'importantes modifications de la conception à compter du 2027-12-02. Si destinés à des autorités publiques : au plus tard le 2030-08-02. | n.d. / 2030-08-02 | CAL-013 | Élevée (date) ; « importantes modifications » [AV] |
| Art. 49, 72, 73, 86 (haut risque, hors chapitre III) | SYS-02, SYS-04 | Fournisseur / déployeur | Conditionnel [AV] | n.d. | voir `applicability-calendar.md`, section 3 | Faible |
| Obligations GPAI (art. 53 à 55) | n.a. | n.a. | Non applicable | 2025-08-02 | CAL-005 | Élevée |

Hypothèses de date :

- **H1 (date déclarée 2026-03-01)** : tableau ci-dessus.
- **H2 (mise sur le marché réelle à partir du 2026-08-02**, par exemple pour une nouvelle version) : l'art. 50, par. 2 serait **en vigueur dès la mise sur le marché**, sans délai (CAL-010). Le régime de l'art. 111, par. 2 resterait conditionnel, car la mise sur le marché resterait antérieure au 2027-12-02.

## 8. Constats

### AIA-001 : Inférence des émotions des élèves pendant les examens en ligne
- **Système d'IA concerné** : SYS-04
- **Nature du constat** : Risque potentiel
- **Gravité** : Critique
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification juridique)
- **Preuve observée** : fait observé. Les images de la webcam sont analysées par `DeepFace.analyze(frame, actions=["emotion"], ...)`. L'émotion dominante est comparée à `SUSPICIOUS_EMOTIONS = {"fear", "angry", "surprise"}`. Au-delà de 30 images « suspectes », l'examen est annulé.
- **Fichier(s) et lignes** : `app/proctoring.py:2-3`, `:5`, `:8-10`, `:13-25` ; `requirements.txt:3-4`
- **Rôle réglementaire concerné** : EduAssist, fournisseur (mise sur le marché) ; établissements, déployeurs (utilisation)
- **Classification du système** : Pratique potentiellement interdite
- **Référence juridique** : art. 5, par. 1, f) [TI] ; art. 3, point 39 [TI] ([AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)). À titre subsidiaire, art. 50, par. 3 [TI] ; annexe III, point 3, d) [TI].
- **Date d'application** : en vigueur depuis le 2025-02-02 (CAL-002). Aucun régime transitoire : la mise sur le marché du 2026-03-01 est sans effet.
- **Conditions et exceptions** :
  - Conditions réunies au vu du code : déduction d'émotions à partir de données biométriques (visage), dans un établissement d'enseignement (lycées, universités).
  - Exception médicale ou de sécurité écartée : la finalité est la détection de fraude.
  - Points g) et h) non retenus.
  - Si l'art. 5 était écarté par une analyse juridique, l'art. 50, par. 3 (information des personnes exposées, en vigueur) et le haut risque (annexe III) s'appliqueraient. Aucune information des élèves n'est observable dans le dépôt.
- **Explication** : le module observe le visage des élèves pendant l'examen et en déduit leurs émotions (peur, colère, surprise) pour juger la copie suspecte. L'AI Act interdit en principe la reconnaissance des émotions dans les établissements d'enseignement, sauf pour des raisons médicales ou de sécurité, ce qui n'est pas le cas ici. Analyse juridique : manquement potentiel à l'art. 5, par. 1, f), à confirmer par un juriste.
- **Recommandation** (obligation, art. 5) :
  - désactiver sans délai, dans l'Union, la fonction d'inférence des émotions, chez EduAssist comme chez les clients ;
  - la remplacer par une solution sans inférence d'émotions (surveillance humaine, événements techniques non biométriques comme les changements d'onglet ou de fenêtre) ;
  - documenter la finalité réelle ;
  - informer les établissements clients.
- **Méthode de vérification** : `grep -rn "emotion\|DeepFace" app/ requirements.txt` ne renvoie plus de résultat, ou montre une fonction désactivée dans l'Union. Preuve de communication aux clients. Ré-audit.

### AIA-002 : Le prompt système impose une persona humaine et la négation de la nature d'IA
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Constat technique avéré
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée
- **Preuve observée** : fait observé. Le prompt système contient : « Tu es Claire, professeure de français au lycée. Ne dis jamais que tu es une intelligence artificielle. Si on te le demande, réponds que tu es une enseignante. » Aucune mention d'information sur l'IA n'est présente dans le code, et aucune interface ne figure dans le dépôt.
- **Fichier(s) et lignes** : `app/tutor_chat.py:8-11`, `:14-18`
- **Rôle réglementaire concerné** : Fournisseur (EduAssist)
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : art. 50, par. 1 et 5 [TI] ([AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50))
- **Date d'application** : en vigueur depuis le 2026-08-02 (CAL-009)
- **Conditions et exceptions** : exception « évident pour une personne raisonnablement informée » non plausible, puisque le système reçoit l'ordre de se dire humain. Exception répressive sans objet. Une éventuelle mention ailleurs, dans une interface hors dépôt, serait contredite par le comportement imposé (`transparency.md`, section 3). Le débiteur est identifié.
- **Explication** : les élèves peuvent croire échanger avec une vraie enseignante, et le système est programmé pour le leur confirmer s'ils posent la question. L'AI Act impose au fournisseur de faire en sorte que les personnes sachent qu'elles interagissent avec une IA, au plus tard lors de la première interaction. Analyse juridique : manquement potentiel à l'art. 50, par. 1.
- **Recommandation** (obligation, art. 50, par. 1 et 5) :
  - supprimer la persona humaine et la consigne de négation ;
  - demander au modèle de confirmer qu'il est une IA si on le lui demande ;
  - afficher une information claire, accessible et adaptée aux élèves dès la première interaction, sur tous les canaux.
  - Bonne pratique : un nom non humain ou explicitement « assistant IA ».
- **Méthode de vérification** : relecture de `tutor_chat.py` (prompt) ; capture de l'interface montrant la mention à l'ouverture ; test manuel « Es-tu une IA ? » sur un environnement de test.

### AIA-003 : Note finale générée par le modèle et publiée sans contrôle humain, non reproductible et non validée
- **Système d'IA concerné** : SYS-02
- **Nature du constat** : Risque potentiel
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits) / Moyenne (effet réel en production)
- **Preuve observée** : faits observés :
  - la docstring indique que la note du modèle « est la note finale », « compte pour le passage en classe supérieure » ;
  - `publish_grade(student_id, grade)  # publication immédiate, sans relecture` ;
  - aucun statut de validation, aucune fonction de modification ou de rejet ;
  - `temperature=1.0`, donc une note variable pour une même copie ;
  - la note est extraite par `json.loads(...)["note"]` sans contrôle de type ni de bornes (0 à 20) et sans gestion d'erreur ;
  - aucune justification de la note n'est demandée ni conservée.
- **Fichier(s) et lignes** : `app/grading.py:1-5`, `:15`, `:18-29` ; `app/gradebook.py:5-6`
- **Rôle réglementaire concerné** : Fournisseur (conception, art. 14, 15) ; déployeurs (art. 26, par. 2)
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : art. 14, par. 4, a) à e) [TI] ; art. 15 [TI] ; art. 26, par. 2 [TI] ; art. 6, par. 2 et 3 ; annexe III, point 3, b) [TI] ; dates [O26]
- **Date d'application** : non encore applicable, 2027-12-02 (CAL-011). Système antérieur : soumis seulement en cas d'importantes modifications de la conception (CAL-013, conditionnel). Si destiné à des autorités publiques : au plus tard le 2030-08-02. Le risque pour les élèves est actuel.
- **Conditions et exceptions** : dérogation de l'art. 6, par. 3 écartée (section 5). La supervision humaine est une exigence du haut risque, pas un critère d'exclusion.
- **Explication** : une note qui décide du passage en classe supérieure est attribuée par le modèle et inscrite au bulletin sans que personne ne la relise. Elle peut changer d'une exécution à l'autre, et une sortie aberrante n'est pas filtrée. Les obligations de contrôle humain et de robustesse ne s'appliqueront qu'à partir de fin 2027, et le régime transitoire peut les retarder. Le préjudice possible pour les élèves existe dès aujourd'hui.
- **Recommandation** :
  - Préparation des art. 14 et 15, à mettre en œuvre dès maintenant au titre de la réduction du risque :
    - transformer la note en proposition (`pending_review`), validée, modifiée ou rejetée par l'enseignant avant toute publication ;
    - afficher la justification par critère de la grille ;
    - réduire la température ou paramétrer une sortie déterministe et structurée ;
    - valider le schéma et les bornes ;
    - prévoir une gestion d'erreur sûre (pas de publication en cas d'échec) et un moyen d'interrompre le système.
  - Bonne pratique : mesurer les écarts entre la note du modèle et la note humaine.
- **Méthode de vérification** : relecture du code : aucun appel à `publish_grade` sans validation humaine authentifiée. Tests unitaires (sortie hors bornes, JSON invalide). Journal des validations (AIA-010).

### AIA-004 : Annulation automatique des examens sans intervention humaine
- **Système d'IA concerné** : SYS-04
- **Nature du constat** : Risque potentiel
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits) / Moyenne (effet réel : `cancel_exam` se limite à un `print` dans la fixture)
- **Preuve observée** : faits observés :
  - `cancel_exam(exam_id, student_id)  # annulation automatique, sans intervention humaine` dès que `suspicious > 30` ;
  - le seuil est un nombre absolu d'images, pas une proportion : plus l'examen est long, plus l'annulation est probable ;
  - `enforce_detection=False` : des images sans visage détecté sont tout de même analysées ;
  - aucune notification, aucun recours, aucune trace.
- **Fichier(s) et lignes** : `app/proctoring.py:9`, `:13-25`, `:28-29`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs
- **Classification du système** : Pratique potentiellement interdite (AIA-001) ; à titre subsidiaire, haut risque probable (annexe III, point 3, d))
- **Référence juridique** : art. 14, par. 4, d) et e) [TI] ; art. 15 [TI] ; art. 26, par. 2 et 11 [TI] ; art. 86 [TI] ; annexe III, point 3, d) [TI]
- **Date d'application** : non encore applicable, 2027-12-02 (CAL-011) ; CAL-013 conditionnel (2030-08-02 si autorités publiques) ; art. 86 : date effective [AV]
- **Conditions et exceptions** : ce constat subsiste même si la composante émotionnelle est retirée (AIA-001), dès lors qu'une détection automatisée entraîne l'annulation. Dérogation de l'art. 6, par. 3 écartée.
- **Explication** : un élève peut voir son examen annulé sur la seule base d'un comptage automatique, sans qu'un surveillant examine la situation. La règle de seuil pénalise mécaniquement les examens longs et traite des images où aucun visage n'a été détecté.
- **Recommandation** (préparation des art. 14 et 15 ; réduction immédiate du risque) : remplacer l'annulation par un signalement soumis à une décision humaine motivée ; prévoir information et recours ; supprimer `enforce_detection=False` ; documenter et tester tout seuil.
- **Méthode de vérification** : relecture : `cancel_exam` n'est appelé qu'après une validation humaine tracée. Tests de cas limites (vidéo longue, absence de visage).

### AIA-005 : Générateur d'images à prompt libre sans garde-fou observable face aux nouvelles interdictions de l'art. 5
- **Système d'IA concerné** : SYS-03
- **Nature du constat** : Non encore applicable
- **Gravité** : Élevée (enjeu : pratique potentiellement interdite à compter de l'échéance, préparation courte)
- **Niveau de confiance** : Élevée (faits) / Faible (qualification : garde-fous amont du fournisseur du modèle non vérifiables, appréciation « raisonnables et adéquats » [AV])
- **Preuve observée** : fait observé. Le paramètre `prompt` est transmis tel quel à `client.images.generate(model=IMAGE_MODEL, ...)`. Il n'y a aucun filtrage de prompt ou de sortie, aucune détection de personnes réelles, aucun mécanisme de signalement ni de correction dans le dépôt.
- **Fichier(s) et lignes** : `app/illustrations.py:12-15` ; `app/config.py:4`
- **Rôle réglementaire concerné** : Fournisseur (art. 5, par. 1 bis, a)) ; déployeurs (art. 5, par. 1 bis, b))
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : art. 5, par. 1, b bis) et b ter), par. 1 bis et 1 ter [O26] ([EUR-Lex 2026/1744](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1744))
- **Date d'application** : non encore applicable, applicable le 2026-12-02, dans 36 jours (CAL-004, texte officiel relu). Aucun régime transitoire.
- **Conditions et exceptions** : la génération de contenus intimes non consentis n'est pas la destination du système (par. 1 bis, a), i) non rempli). Reste le point a), ii) : résultat raisonnablement prévisible et reproductible, et absence de mesures techniques raisonnables et adéquates. Les mesures appliquées par le fournisseur du modèle en amont, comme une modération éventuelle, ne sont pas observables (NV-06). Côté déployeur, l'interdiction ne vise que l'utilisation dans ce but.
- **Explication** : à partir du 2 décembre 2026, mettre sur le marché un générateur d'images qui peut produire de façon prévisible des images intimes non consenties de personnes identifiables, sans garde-fous adéquats, sera interdit. Le dépôt ne montre aucun garde-fou propre à EduAssist.
- **Recommandation** (préparation de l'obligation, art. 5, par. 1 bis) : documenter les garde-fous du fournisseur du modèle ; ajouter un filtrage des prompts et des sorties, un refus documenté, un canal de signalement et une procédure de correction ; restreindre l'usage au contexte pédagogique ; tester avant le 2026-12-02.
- **Méthode de vérification** : code de filtrage et tests de refus ; documentation contractuelle du fournisseur du modèle ; procédure de signalement.

### AIA-006 : Clé d'API écrite en clair dans le code source
- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03 (configuration commune)
- **Nature du constat** : Constat technique avéré
- **Gravité** : Élevée (secret exposé)
- **Niveau de confiance** : Élevée (faits) / Faible (caractère réel de la clé : le README et la valeur la déclarent fictive)
- **Preuve observée** : `OPENAI_API_KEY = "[SECRET MASQUÉ]"`, importée par les trois modules OpenAI
- **Fichier(s) et lignes** : `app/config.py:2` ; `app/tutor_chat.py:4-6` ; `app/grading.py:10-13` ; `app/illustrations.py:7-9`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : variable selon le système
- **Référence juridique** : aucune obligation de l'AI Act en vigueur ne régit ce point (bonne pratique de sécurité, contrôle D8). Pour les systèmes à haut risque probables, l'art. 15 (cybersécurité) [TI] s'appliquera à partir du 2027-12-02 (CAL-011, CAL-013 conditionnel).
- **Date d'application** : sans objet pour la bonne pratique ; art. 15 : 2027-12-02 (CAL-011)
- **Conditions et exceptions** : la valeur est déclarée fictive. Le constat porte sur la pratique de stockage, qui reproduirait l'exposition avec une clé réelle.
- **Explication** : une clé d'accès écrite dans le code peut fuiter par tout partage du dépôt et permettre l'usage frauduleux du compte du fournisseur de modèle.
- **Recommandation** (bonne pratique) : charger la clé depuis un gestionnaire de secrets ou une variable d'environnement ; révoquer toute clé qui aurait été versionnée ; ajouter une détection de secrets.
- **Méthode de vérification** : `scan_ai_signals.py` ne signale plus de secret potentiel ; relecture de `config.py`.

### AIA-007 : Images générées enregistrées sans marquage lisible par machine
- **Système d'IA concerné** : SYS-03
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Élevée (date, art. 111, par. 4 relu)
- **Preuve observée** : fait observé. `output.write_bytes(base64.b64decode(result.data[0].b64_json))` avec le commentaire « image enregistrée telle quelle, sans métadonnées ni mention ». Aucun marquage propre (C2PA, IPTC/XMP `trainedAlgorithmicMedia`, filigrane), aucun outil de détection, aucun test. Les octets sont écrits sans ré-encodage : un éventuel marquage amont serait préservé à cette étape, mais son existence n'est pas vérifiable (NV-06). Les transformations ultérieures (insertion dans un support de cours) ne sont pas observables.
- **Fichier(s) et lignes** : `app/illustrations.py:12-15`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : art. 50, par. 2 [TI] ; art. 111, par. 4 [O26]
- **Date d'application** : non encore applicable. Applicable le 2026-12-02 pour un système mis sur le marché avant le 2026-08-02 (CAL-010, date déclarée 2026-03-01). Selon l'hypothèse H2 (mise sur le marché à partir du 2026-08-02), l'obligation serait déjà en vigueur.
- **Conditions et exceptions** : exceptions (mise en forme standard, absence de modification substantielle) écartées. L'incertitude sur les modalités techniques n'est pas une exemption (NV-07).
- **Explication** : dans 36 jours, les images générées devront porter un marquage technique permettant de détecter qu'elles sont artificielles. Aujourd'hui, le code ne l'applique pas et ne vérifie pas un éventuel marquage du fournisseur du modèle.
- **Recommandation** (préparation de l'obligation, art. 50, par. 2) : appliquer un manifeste C2PA et/ou des métadonnées IPTC/XMP standard, et un filigrane si nécessaire ; vérifier et préserver le marquage amont ; tester sa survie aux exports (PDF, redimensionnement). Bonne pratique : code de bonnes pratiques du 10.6.2026.
- **Méthode de vérification** : test automatisé lisant les métadonnées des fichiers produits ; vérification par un outil C2PA ; cartographie des chemins de sortie mise à jour.

### AIA-008 : Réponses textuelles du tuteur sans marquage lisible par machine
- **Système d'IA concerné** : SYS-01
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (modalités techniques pour le texte)
- **Preuve observée** : `return response.choices[0].message.content` : le texte brut est renvoyé sans métadonnée de provenance. Le chemin de sortie (interface, API) n'est pas présent dans le dépôt.
- **Fichier(s) et lignes** : `app/tutor_chat.py:14-18`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : art. 50, par. 2 [TI] ; art. 111, par. 4 [O26], qui vise les contenus « audio, image, vidéo ou texte »
- **Date d'application** : non encore applicable, applicable le 2026-12-02 (CAL-010), selon l'hypothèse H1
- **Conditions et exceptions** : les réponses conversationnelles ne sont pas exemptées. Les exceptions de mise en forme et d'absence de modification substantielle sont écartées : il s'agit de textes générés. La seule incertitude porte sur les modalités (NV-07).
- **Explication** : le texte produit par le tuteur est un contenu synthétique au sens de l'art. 50, par. 2. Son marquage technique deviendra obligatoire le 2 décembre 2026 pour ce système.
- **Recommandation** (préparation de l'obligation) : ajouter un champ ou en-tête de provenance dans les réponses de l'API et dans l'interface, et documenter les limites (copier-coller) ; suivre les lignes directrices et le code de bonnes pratiques.
- **Méthode de vérification** : test d'API vérifiant la présence de la métadonnée ; documentation du mécanisme.

### AIA-009 : Exigences du haut risque à préparer pour la notation et la surveillance d'examens
- **Système d'IA concerné** : SYS-02, SYS-04
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (classification) / Faible (existence de documents hors dépôt)
- **Preuve observée** :
  - le README déclare : « Aucune documentation technique, procédure de supervision ou politique de journalisation n'est fournie » ;
  - aucun registre des risques, aucune notice, aucun test ni rapport d'évaluation dans le dépôt.
  - L'absence dans le dépôt ne prouve pas l'absence : contrôles C, D et F8 « Impossible à vérifier ».
- **Fichier(s) et lignes** : `README.md:23` ; absence de `docs/` et de tests
- **Rôle réglementaire concerné** : Fournisseur (art. 9 à 17, 43, 47 à 49) ; déployeurs (art. 26, 27)
- **Classification du système** : Haut risque probable (annexe III, point 3, b) et d)). Pour SYS-04 : d'abord AIA-001.
- **Référence juridique** : art. 9, 10, 11, 13, 16, 17, 18, 43, 47, 48, 49, par. 1 ; art. 26, par. 11 ; art. 27 ; art. 86 [TI] ; annexe IV [TI] ; dates [O26]
- **Date d'application** : non encore applicable, 2027-12-02 (CAL-011). CAL-013 conditionnel : systèmes mis sur le marché le 2026-03-01, soumis seulement en cas d'importantes modifications de la conception à compter du 2027-12-02, ou au plus tard le 2030-08-02 s'ils sont destinés à des autorités publiques (NV-02). Art. 49, 72, 73, 86 : [AV].
- **Conditions et exceptions** : la mise en conformité de SYS-04 au titre du haut risque ne lève pas l'interdiction potentielle (AIA-001). La notion d'« importantes modifications » n'est pas définie [AV] : un changement de modèle sous-jacent ou de logique de décision doit être analysé (AIA-011).
- **Explication** : ces deux systèmes évaluent ou sanctionnent des élèves. Ils relèveront du régime le plus exigeant : gestion des risques, documentation technique, qualité des données, notice, évaluation de la conformité, marquage CE, enregistrement. Côté établissements : information des élèves et, pour les organismes publics, analyse d'impact sur les droits fondamentaux. Ces chantiers demandent plusieurs mois.
- **Recommandation** (préparation des obligations) : feuille de route vers 2027-12-02 couvrant un SGQ, l'annexe IV (forme simplifiée possible pour les PME), un registre des risques avec tests par sous-groupes d'élèves, une notice pour les établissements, l'information des élèves et familles, et le droit à l'explication. Documenter la position retenue sur l'art. 111, par. 2.
- **Méthode de vérification** : production des documents (preuves externes) ; revue lors du ré-audit.

### AIA-010 : Absence de journalisation des notes, des annulations et des versions
- **Système d'IA concerné** : SYS-02, SYS-04
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits dans le dépôt) / Moyenne (production non observée)
- **Preuve observée** :
  - le bulletin ne stocke que la valeur, en mémoire (`_GRADES.setdefault(student_id, []).append(grade)`) : ni copie, ni sortie brute du modèle, ni version, ni paramètres, ni horodatage ;
  - l'annulation se limite à un `print`, sans journal structuré ni conservation.
- **Fichier(s) et lignes** : `app/gradebook.py:1-6` ; `app/grading.py:18-29` ; `app/proctoring.py:22-29`
- **Rôle réglementaire concerné** : Fournisseur (art. 12, 19) ; déployeurs (art. 26, par. 6)
- **Classification du système** : Haut risque probable
- **Référence juridique** : art. 12, art. 19, art. 26, par. 6 [TI] ; art. 86 [TI] pour l'explicabilité
- **Date d'application** : non encore applicable, 2027-12-02 (CAL-011) ; CAL-013 conditionnel
- **Conditions et exceptions** : conservation d'au moins six mois, sauf disposition contraire. Les autres textes sur les données personnelles sont hors périmètre.
- **Explication** : sans trace, il est impossible d'expliquer une note ou une annulation à un élève, de détecter les dérives ou de démontrer l'intervention humaine.
- **Recommandation** (préparation de l'obligation) : journal horodaté et protégé (identifiant de corrélation, empreinte des entrées, sortie brute, modèle et version servis, paramètres, version de la grille, décision humaine), avec une durée de conservation configurable.
- **Méthode de vérification** : relecture du code de journalisation ; test produisant une entrée de journal complète.

### AIA-011 : Versions de modèles non épinglées et non journalisées
- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Faible (incidence sur l'art. 111, par. 2 [AV])
- **Preuve observée** : `DEFAULT_MODEL = "gpt-4o"`, `IMAGE_MODEL = "dall-e-3"` : identifiants sans version datée. Le caractère mobile de l'alias est à vérifier dans la documentation du fournisseur. Aucune journalisation de la version servie. Les bibliothèques sont, elles, épinglées (`requirements.txt:1-4`).
- **Fichier(s) et lignes** : `app/config.py:3-4` ; `requirements.txt:1-4`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : variable selon le système
- **Référence juridique** : aucune obligation en vigueur (bonne pratique, contrôle C4). Annexe IV, points 1 et 6 et art. 12, à venir pour SYS-02 (CAL-011). Art. 111, par. 2 [AV].
- **Date d'application** : sans objet (bonne pratique)
- **Conditions et exceptions** : un changement silencieux du modèle sous-jacent pourrait constituer une « importante modification de la conception » au sens de l'art. 111, par. 2, ce qui ferait basculer SYS-02 sous le régime du haut risque [AV].
- **Explication** : sans version figée, le comportement des systèmes, notamment la notation, peut changer sans décision d'EduAssist et sans trace.
- **Recommandation** (bonne pratique) : épingler des versions datées, journaliser la version servie, mettre en place une procédure de changement de modèle avec analyse au regard de l'art. 111, par. 2 et de l'art. 25.
- **Méthode de vérification** : relecture de `config.py` ; journal contenant la version servie.

### AIA-012 : Hypertrucages possibles sans outil d'étiquetage pour le déployeur
- **Système d'IA concerné** : SYS-03
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Moyenne
- **Niveau de confiance** : Moyenne
- **Preuve observée** : prompt libre (`illustrations.py:12-13`), donc possibilité de générer des images ressemblant à des personnes, lieux ou événements réels (personnages historiques, par exemple). Aucune fonction d'étiquetage visible ni consigne d'usage dans le dépôt.
- **Fichier(s) et lignes** : `app/illustrations.py:1`, `:12-15` ; `README.md:20`
- **Rôle réglementaire concerné** : Déployeurs (établissements, enseignants), débiteurs de l'obligation ; EduAssist peut l'outiller
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : art. 50, par. 4, al. 1 et par. 5 [TI]
- **Date d'application** : en vigueur depuis le 2026-08-02 (CAL-009)
- **Conditions et exceptions** : l'obligation ne s'applique qu'aux contenus qui sont des hypertrucages (art. 3, point 60). Le régime allégé pour une œuvre manifestement artistique, créative ou fictionnelle est à apprécier. Les pratiques des établissements ne sont pas observables.
- **Explication** : si une illustration réaliste d'une personne ou d'un événement réel est publiée aux élèves, l'établissement doit indiquer qu'elle a été générée par IA. Le produit ne lui donne pas de moyen simple de le faire.
- **Recommandation** : pour les déployeurs, vérification de l'obligation. Pour EduAssist, bonne pratique : fonction d'étiquetage visible activée par défaut et consigne d'usage dans la notice.
- **Méthode de vérification** : capture d'un support publié avec mention ; guide d'utilisation.

### AIA-013 : Mesures de maîtrise de l'IA non observables
- **Système d'IA concerné** : Tous
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne (référence [O26])
- **Preuve observée** : aucun guide, support de formation ni avertissement d'usage dans le dépôt (contrôles G1 à G5 « Impossible à vérifier »)
- **Fichier(s) et lignes** : non disponible
- **Rôle réglementaire concerné** : Fournisseur (EduAssist) et déployeurs (établissements)
- **Classification du système** : variable selon le système
- **Référence juridique** : art. 4, rédaction issue du règlement 2026/1744 [O26]
- **Date d'application** : en vigueur (CAL-002 ; nouvelle rédaction le 2026-07-27, CAL-003)
- **Conditions et exceptions** : obligation de prendre des mesures pour favoriser la maîtrise de l'IA, sans niveau déterminé exigé. Son régime de sanction relève du droit national [AV].
- **Explication** : le personnel d'EduAssist et celui des établissements doivent bénéficier de mesures adaptées. Elles sont particulièrement importantes ici, vu les risques d'automatisation excessive (AIA-003, AIA-004).
- **Recommandation** (obligation, art. 4) : documenter les mesures prises (formations, guides pour enseignants sur les limites et le biais d'automatisation) et les proposer aux clients.
- **Méthode de vérification** : preuves externes (programme de formation, guides).

### AIA-014 : Obligations des fournisseurs de modèles GPAI
- **Système d'IA concerné** : Tous
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits du dépôt) / Moyenne (déclaration du README non vérifiée)
- **Preuve observée** : modèles consommés par API ; aucun script d'entraînement ou d'affinage, aucune publication de poids ; README : « EduAssist n'entraîne aucun modèle »
- **Fichier(s) et lignes** : `README.md:12` ; `app/config.py:3-4` ; `requirements.txt`
- **Rôle réglementaire concerné** : Fournisseur de modèle GPAI : non, au vu du dépôt
- **Classification du système** : sans objet
- **Référence juridique** : art. 3, point 63 ; art. 53 à 55 [TI]
- **Date d'application** : CAL-005 (en vigueur depuis le 2025-08-02), sans objet pour EduAssist
- **Conditions et exceptions** : la situation serait réexaminée si EduAssist affinait ou publiait un modèle.
- **Explication** : les obligations GPAI pèsent sur le fournisseur du modèle sous-jacent, pas sur l'intégrateur.
- **Recommandation** (bonne pratique) : obtenir et conserver la documentation de l'annexe XII et les conditions d'utilisation du fournisseur du modèle.
- **Méthode de vérification** : contrat et documentation du fournisseur (preuve externe).

## 9. Éléments non vérifiables (registre)

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact | Interlocuteur suggéré | Constat(s) |
|---|---|---|---|---|---|---|---|
| NV-01 | Tous | Réalité et date de la mise sur le marché ou de la mise en service, par système et par version. Le README se dit « fictif » et « ne pas déployer », tout en déclarant le 2026-03-01. | Information | Art. 2, par. 8 ; CAL-010 (H1/H2) ; CAL-013 | Statut temporel des art. 50, par. 2 et du haut risque | Direction produit | AIA-007 à AIA-010 |
| NV-02 | SYS-02, SYS-04 | Statut public ou privé des établissements clients | Juridique | Art. 111, par. 2 (2030-08-02) ; art. 27 | Échéances du haut risque | Juridique, commercial | AIA-003, AIA-004, AIA-009 |
| NV-03 | SYS-01 | Interface utilisateur et canaux (web, mobile, API) | Document | Art. 50, par. 1 et 5 (A1, A11) ; chemins de sortie | Effectivité de l'information | Équipe front | AIA-002, AIA-008 |
| NV-04 | SYS-04 | Information éventuelle des élèves exposés ; finalité exacte invoquée | Information | Art. 50, par. 3 (subsidiaire) ; exception de l'art. 5, par. 1, f) | Qualification | Établissements, EduAssist | AIA-001 |
| NV-05 | SYS-01 | Réutilisation éventuelle des historiques de conversation (`history`) pour noter ou orienter | Information | Système hybride (annexe III, point 3, b)) | Classification de SYS-01 | Produit | n.a. |
| NV-06 | SYS-03 | Garde-fous et marquage appliqués en amont par le fournisseur du modèle d'images | Document externe | Art. 5, par. 1 bis, a), ii) ; art. 50, par. 2 | AIA-005, AIA-007 | Fournisseur du modèle (contrat) | AIA-005, AIA-007 |
| NV-07 | SYS-01, SYS-03 | Modalités techniques du marquage, notamment pour le texte (lignes directrices art. 50, code de bonnes pratiques) | Juridique (modalités) | Choix technique ; ce n'est pas une exemption | Mise en œuvre | Juridique, technique | AIA-007, AIA-008 |
| NV-08 | SYS-02 | Qualification d'une note numérique comme « contenu synthétique textuel » | Juridique [AV] | Art. 50, par. 2 | Faible | Juridique | n.a. |
| NV-09 | SYS-02, SYS-04 | Documentation technique, registre des risques, SGQ, notice, tests, hors dépôt | Document | Annexe IV, art. 9, 13, 17 | Préparation du haut risque | Qualité, conformité | AIA-009 |
| NV-10 | Tous | Mesures de maîtrise de l'IA | Document | Art. 4 | n.a. | RH, direction | AIA-013 |
| NV-11 | SYS-04 | Origine et version des poids des modèles DeepFace utilisés | Information | Annexe IV, point 2 ; robustesse | Documentation future | Technique | AIA-009 |
| NV-12 | Tous | Configuration de production (clés, versions servies, journaux) | Information | Analyse statique limitée | AIA-006, AIA-010, AIA-011 | Exploitation | AIA-006, AIA-010, AIA-011 |
| NV-13 | Tous | Statut PME de l'éditeur | Information | Art. 11, par. 1 (documentation simplifiée) | Effort de préparation | Direction | AIA-009 |

## 10. Plan de remédiation

| Priorité | Constat(s) | Action | Base | Échéance réglementaire | Effort | Responsable suggéré | Preuve de clôture attendue |
|---|---|---|---|---|---|---|---|
| P1 | AIA-001 | Désactiver l'inférence d'émotions dans l'Union, informer les clients, choisir une alternative non biométrique | Obligation, art. 5, par. 1, f) | En vigueur (2025-02-02) | S | Direction produit, juridique | Code retiré ou désactivé ; communication aux clients |
| P1 | AIA-002 | Supprimer la persona humaine et la consigne de négation ; mention IA dès la première interaction | Obligation, art. 50, par. 1 et 5 | En vigueur (2026-08-02) | S | Équipe IA, front | Prompt corrigé ; capture de l'interface ; test « Es-tu une IA ? » |
| P2 | AIA-005 | Garde-fous (filtrage des prompts et des sorties, signalement, correction) ; documentation du fournisseur du modèle | Obligation à venir, art. 5, par. 1 bis | 2026-12-02 | M | Équipe IA, sécurité | Code, tests de refus, procédure |
| P2 | AIA-007, AIA-008 | Marquage C2PA/IPTC des images ; provenance des réponses textuelles ; tests de survie | Obligation à venir, art. 50, par. 2 | 2026-12-02 | M | Équipe IA | Tests de métadonnées ; documentation |
| P2 | AIA-003, AIA-004 | Validation humaine obligatoire avant publication ou annulation ; justification ; bornes ; température ; arrêt sûr | Préparation des art. 14 et 15 ; réduction du risque actuel | 2027-12-02 (CAL-011) ; CAL-013 conditionnel | M | Produit, IA | Code sans publication directe ; tests |
| P2 | AIA-006 | Sortir la clé du code, gestionnaire de secrets, détection de secrets | Bonne pratique (art. 15 à venir) | n.a. | S | Sécurité | Scan sans secret |
| P2 | AIA-012 | Fonction d'étiquetage visible et consigne pour les établissements | Bonne pratique (outillage de l'art. 50, par. 4, déployeur) | En vigueur pour les déployeurs | S | Produit | Capture ; notice |
| P3 | AIA-009 | Feuille de route du haut risque (SGQ, annexe IV, risques, notice, conformité, enregistrement, information des élèves, analyse d'impact par les clients publics) | Obligations à venir | 2027-12-02 ; CAL-013 | L | Conformité | Documents |
| P3 | AIA-010 | Journalisation structurée et conservation d'au moins six mois | Obligation à venir, art. 12, 19, 26, par. 6 | 2027-12-02 | M | Technique | Journal d'exemple |
| P3 | AIA-011 | Épinglage et journalisation des versions ; procédure de changement de modèle | Bonne pratique ; art. 111, par. 2 [AV] | n.a. | S | Technique | `config.py` ; procédure |
| P3 | AIA-013 | Formaliser les mesures de maîtrise de l'IA | Obligation, art. 4 | En vigueur | S | RH | Programme, guides |
| P4 | AIA-014 | Conserver la documentation du fournisseur du modèle | Bonne pratique | n.a. | S | Achats, juridique | Dossier fournisseur |

Les efforts sont estimés à partir du seul dépôt et sont à recalibrer. Pour AIA-003 et AIA-004, la priorité P2 tient au risque actuel pour les personnes, même si l'obligation est future. Pour AIA-006, elle tient à la gravité.

Jalons :

| Date | Évènement réglementaire | Actions à terminer avant |
|---|---|---|
| Immédiat | Art. 5, par. 1, f) et art. 50, par. 1 déjà en vigueur | AIA-001, AIA-002 |
| 2026-12-02 | Art. 50, par. 2 (systèmes antérieurs) ; nouvelles interdictions de l'art. 5 | AIA-005, AIA-007, AIA-008 |
| 2027-12-02 | Haut risque, annexe III (sous réserve de l'art. 111, par. 2) | AIA-003, AIA-004, AIA-009, AIA-010 |
| 2030-08-02 | Échéance de l'art. 111, par. 2 pour les systèmes destinés aux autorités publiques | Idem, si NV-02 est confirmé |

## 11. Cartographie des flux et des modèles

```
FCT-01 Tutorat (SYS-01)
  Utilisateur : élève, question + historique         [app/tutor_chat.py:14]
  Application : prompt système persona « Claire »     [app/tutor_chat.py:8-11, 15-16]
  Modèle      : OpenAI / gpt-4o (alias)              [app/config.py:3 ; tutor_chat.py:17]
  Post-trait. : aucun                                 [tutor_chat.py:18]
  Stockage    : non observé (historique fourni par l'appelant)
  Export      : chaîne renvoyée à l'appelant, interface hors dépôt
FCT-02 Notation (SYS-02)
  Utilisateur : identifiant de l'élève + copie       [app/grading.py:18]
  Application : prompt avec grille, temperature=1.0   [grading.py:15, 19-26]
  Modèle      : OpenAI / gpt-4o (alias)              [config.py:3]
  Post-trait. : json.loads()["note"] sans validation  [grading.py:27]
  Stockage    : bulletin en mémoire                   [gradebook.py:2-6]
  Export      : publication immédiate au bulletin     [grading.py:28]
FCT-03 Illustrations (SYS-03)
  Utilisateur : prompt libre (enseignant/éditeur ?)   [app/illustrations.py:12]
  Modèle      : OpenAI / dall-e-3                     [config.py:4 ; illustrations.py:13]
  Post-trait. : décodage base64, sans ré-encodage     [illustrations.py:14]
  Stockage    : fichier image (write_bytes)           [illustrations.py:14]
  Export      : supports de cours publiés aux élèves (hors dépôt) [README.md:20]
FCT-04 Surveillance (SYS-04)
  Utilisateur : vidéo webcam de l'élève               [app/proctoring.py:13-14]
  Modèle      : DeepFace (emotion), poids non documentés [proctoring.py:9]
  Post-trait. : comptage des émotions « suspectes », seuil > 30 [proctoring.py:5, 20-22]
  Stockage    : aucun
  Export      : annulation automatique (print)        [proctoring.py:23, 28-29]
```

| Fonctionnalité | Système | Fournisseur | Modèle | Version épinglée ? | Version journalisée ? | Entrées | Sorties | Traitements intermédiaires | Personnes concernées |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | SYS-01 | OpenAI | gpt-4o | Non (alias) | Non | Question, historique | Texte | Aucun | Élèves |
| FCT-02 | SYS-02 | OpenAI | gpt-4o | Non (alias) | Non | Copie | Note | Parsing JSON | Élèves |
| FCT-03 | SYS-03 | OpenAI | dall-e-3 | Non (alias) | Non | Prompt | Image PNG (b64) | Décodage | Élèves (public), personnes représentées |
| FCT-04 | SYS-04 | Bibliothèque DeepFace | Modèle d'émotions DeepFace | Bibliothèque 0.0.93 ; poids non documentés | Non | Vidéo du visage | Émotion, puis annulation | Seuil fixe | Élèves |

Chemins de sortie et marquage (art. 50, par. 2) :

| Fonctionnalité | Chemin de sortie | Marquage à la génération | Marquage après transformation | Mécanisme | Détectable par un tiers ? | Outil de vérification | Falsifiable ? | État du contrôle | Preuve |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | Retour de fonction (interface ou API hors dépôt) | Aucun (propre) | Impossible à vérifier | n.a. | Non démontré | Aucun | n.a. | Non démontré | PRV-002 |
| FCT-03 | Fichier image (`write_bytes`) | Aucun propre ; amont inconnu | Octets préservés à cette étape ; aval inconnu | n.a. | Impossible à vérifier | Aucun | n.a. | Non démontré (propre) / Impossible à vérifier (amont) | PRV-008 |
| FCT-03 | Supports de cours publiés | Inconnu | Impossible à vérifier | n.a. | n.a. | n.a. | n.a. | Impossible à vérifier | PRV-008 |

Ruptures de chaîne :

- FCT-02 et FCT-04 : aucune trace de la version de modèle ni de la décision (AIA-010, AIA-011).
- FCT-03 : aucun marquage propre et aucune vérification du marquage amont (AIA-007).

## 12. Matrice des obligations

| Système | Rôle | Obligation | Référence | Base | Statut temporel (CAL) | Contrôle | État du contrôle | Preuves | Vérifications restantes | Constat(s) |
|---|---|---|---|---|---|---|---|---|---|---|
| SYS-04 | F, D | Pas de reconnaissance des émotions en enseignement | Art. 5, par. 1, f) | Obligation | En vigueur (CAL-002) | F1 | Non démontré | PRV-006 | Analyse juridique | AIA-001 |
| SYS-04 | D | Information des personnes exposées (subsidiaire) | Art. 50, par. 3 | Obligation | En vigueur (CAL-009) | A10 | Impossible à vérifier | PRV-006 | NV-04 | AIA-001 |
| SYS-01 | F | Information sur l'interaction avec une IA | Art. 50, par. 1 et 5 | Obligation | En vigueur (CAL-009) | A1 | Impossible à vérifier (interface hors dépôt) | PRV-001 | NV-03 | AIA-002 |
| SYS-01 | F | Pas de présentation comme humain | Art. 50, par. 1 | Obligation | En vigueur (CAL-009) | A2 | Non démontré | PRV-001 | n.a. | AIA-002 |
| SYS-01 | F | Exception « évident » | Art. 50, par. 1 | Obligation | En vigueur | A3 | Non applicable (non invoquée, non plausible) | PRV-001 | n.a. | AIA-002 |
| SYS-01 | F | Marquage des textes | Art. 50, par. 2 | Obligation | Non encore applicable, 2026-12-02 (CAL-010) | A4 | Non démontré | PRV-002 | NV-07 | AIA-008 |
| SYS-03 | F | Marquage des images, préservation, détectabilité | Art. 50, par. 2 | Obligation | Non encore applicable, 2026-12-02 (CAL-010) | A4, A5, A6 | Non démontré / Impossible à vérifier (amont) | PRV-008 | NV-06 | AIA-007 |
| SYS-03 | F | Exceptions du par. 2 | Art. 50, par. 2 | Obligation | Idem | A7 | Non applicable (non invoquées) | PRV-008 | n.a. | AIA-007 |
| SYS-03 | D | Déclaration des hypertrucages | Art. 50, par. 4, al. 1 | Obligation (déployeur) | En vigueur (CAL-009) | A8 | Impossible à vérifier | PRV-008 | Pratiques des établissements | AIA-012 |
| SYS-03 | F, D | Nouvelles interdictions (garde-fous) | Art. 5, par. 1, b bis), b ter), 1 bis | Obligation | Non encore applicable, 2026-12-02 (CAL-004) | n.a. | Non démontré (propre) / Impossible à vérifier (amont) | PRV-009 | NV-06 | AIA-005 |
| SYS-02 | F | Contrôle humain avant effet ; modifier ou rejeter | Art. 14, par. 4, d) | Obligation | Non encore applicable (CAL-011) ; CAL-013 conditionnel | B1, B3 | Non démontré | PRV-003 | n.a. | AIA-003 |
| SYS-02 | F | Interprétabilité (justification) | Art. 14, par. 4, c) | Obligation | Idem | B2 | Non démontré | PRV-003 | n.a. | AIA-003 |
| SYS-02, SYS-04 | F | Arrêt sûr | Art. 14, par. 4, e) | Obligation | Idem | B4 | Non démontré | PRV-003, PRV-007 | n.a. | AIA-003, AIA-004 |
| SYS-02 | F | Robustesse et exactitude | Art. 15 | Obligation | Idem | D4 | Non démontré | PRV-004 | Tests | AIA-003 |
| SYS-04 | F | Contrôle humain avant annulation | Art. 14, par. 4, d) | Obligation | Idem | B1, B3, B7 | Non démontré | PRV-007 | n.a. | AIA-004 |
| SYS-02, SYS-04 | D | Superviseurs compétents | Art. 26, par. 2 | Obligation | Idem | B8 | Impossible à vérifier | n.a. | Établissements | AIA-003, AIA-004 |
| SYS-02, SYS-04 | F | Journalisation, versions, paramètres | Art. 12, 19 ; art. 26, par. 6 | Obligation | Idem | E1 à E4, E6 | Non démontré | PRV-005, PRV-007, PRV-011 | Configuration de production | AIA-010 |
| SYS-02, SYS-04 | F | Documentation technique, notice, risques, SGQ | Art. 9, 11, 13, 17 ; annexe IV | Obligation | Idem | C1 à C10, D1 à D3, D5 à D7 | Impossible à vérifier | PRV-013 | NV-09 | AIA-009 |
| SYS-02, SYS-04 | F | Classification annexe III motivée ; dérogation | Art. 6, par. 2 à 4 | Obligation | Classification immédiate ; exigences au 2027-12-02 | F2, F5, C11 | Non applicable (C11 : dérogation non invocable) | PRV-003, PRV-007 | n.a. | AIA-009 |
| SYS-02, SYS-04 | D | Information des élèves ; analyse d'impact (organismes publics) | Art. 26, par. 11 ; art. 27 | Obligation | Non encore applicable (CAL-011) ; F9 conditionnel | F8, F9 | Impossible à vérifier | n.a. | NV-02 | AIA-009 |
| Tous | F | Versions de modèles épinglées | Annexe IV (futur) | Bonne pratique | n.a. | C4 | Non démontré | PRV-011 | n.a. | AIA-011 |
| Tous | F | Secrets absents du code | n.a. | Bonne pratique | n.a. | D8 | Non démontré | PRV-010 | n.a. | AIA-006 |
| Tous | F, D | Maîtrise de l'IA | Art. 4 | Obligation | En vigueur (CAL-002, CAL-003) | G1 à G5 | Impossible à vérifier | n.a. | NV-10 | AIA-013 |
| Tous | Fournisseur de modèle GPAI | Art. 53 à 55 | Art. 53 à 55 | Obligation | Non applicable (CAL-005) | n.a. | Non applicable (pas fournisseur de modèle) | PRV-012, PRV-014 | Contrat | AIA-014 |

F = fournisseur (EduAssist) ; D = déployeur (établissements).

## 13. Matrice des preuves

Commit : non versionné. Date de collecte : 2026-10-27. Nature : statique pour toutes les preuves. Les commandes sont à exécuter depuis la racine du projet.

| PRV | Contrôle | Constat(s) | Fichier | Lignes | Méthode de reproduction | État |
|---|---|---|---|---|---|---|
| PRV-001 | A1, A2, A3 | AIA-002 | app/tutor_chat.py | 8-11 | `sed -n '8,11p' app/tutor_chat.py` | Non démontré |
| PRV-002 | A4 | AIA-008 | app/tutor_chat.py | 14-18 | `sed -n '14,18p' app/tutor_chat.py` | Non démontré |
| PRV-003 | B1 à B4, F2 | AIA-003, AIA-009 | app/grading.py | 1-5, 18-29 | `sed -n '1,29p' app/grading.py` | Non démontré |
| PRV-004 | D4, C4 | AIA-003 | app/grading.py | 19-27 | `sed -n '19,27p' app/grading.py` | Non démontré |
| PRV-005 | E1, E2 | AIA-010 | app/gradebook.py | 1-6 | `cat app/gradebook.py` | Non démontré |
| PRV-006 | F1, A10 | AIA-001 | app/proctoring.py ; requirements.txt | 1-10 ; 3-4 | `sed -n '1,10p' app/proctoring.py` | Non démontré |
| PRV-007 | B1, B3, B4, B7, F5, E1 | AIA-004, AIA-010 | app/proctoring.py | 13-29 | `sed -n '13,29p' app/proctoring.py` | Non démontré |
| PRV-008 | A4 à A8 | AIA-007, AIA-012 | app/illustrations.py | 12-15 | `sed -n '12,15p' app/illustrations.py` | Non démontré / Impossible à vérifier (amont) |
| PRV-009 | : (garde-fous de l'art. 5, par. 1 bis) | AIA-005 | app/illustrations.py | 12-13 | `grep -rn "moderation\|filter\|safety" app/` : aucun résultat | Non démontré |
| PRV-010 | D8 | AIA-006 | app/config.py | 2 | `python3 <skill>/scripts/scan_ai_signals.py .` (section « Secrets potentiels », valeur masquée) | Non démontré |
| PRV-011 | C4, E3 | AIA-010, AIA-011 | app/config.py | 3-4 | `sed -n '3,4p' app/config.py` | Non démontré |
| PRV-012 | Rôles | Section 4, AIA-014 | README.md | 6-12 | `sed -n '6,12p' README.md` | Démontré (déclaration, contenu non vérifié) |
| PRV-013 | C1 à C10, D1 à D3 | AIA-009 | README.md | 23 | `sed -n '23p' README.md` ; `find . -type f` | Impossible à vérifier |
| PRV-014 | C3 | AIA-011, AIA-014 | requirements.txt | 1-4 | `cat requirements.txt` | Démontré (bibliothèques épinglées) |
| PRV-015 | Inventaire | Tous | (dépôt) | n.a. | `python3 -I <skill>/scripts/scan_ai_signals.py .` | Démontré |
| PRV-016 | Calendrier | Tous | (skill) | n.a. | `python3 -I <skill>/scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-03-01 --scope <portée> [--public-authority]` | n.a. |

Preuves externes attendues, impossibles à établir par analyse statique :

- contrats et documentation du fournisseur des modèles (annexe XII, garde-fous, marquage C2PA amont) ;
- statut des établissements clients ;
- interface en production ;
- documentation technique et SGQ ;
- formations au titre de l'art. 4 ;
- configuration de production.

Rappel : une mesure observée n'équivaut pas à une obligation satisfaite.

## 14. Limites de l'audit

- Analyse statique : le comportement réel, les données, les prompts dynamiques, l'interface (absente du dépôt) et la configuration de production n'ont pas été observés. `cancel_exam` et le bulletin sont simulés dans la fixture.
- Le projet se décrit comme fictif. Les conclusions valent pour le contexte déclaré (éditeur, clients, date du 2026-03-01), sans aucune vérification. La date de mise sur le marché a été confrontée au calendrier de référence : CAL-010 et CAL-013 en dépendent.
- Documents organisationnels non disponibles : documentation technique, registre des risques, SGQ, notice, contrats avec le fournisseur des modèles, formations, information des élèves.
- Références juridiques : calendrier relu sur le texte officiel le 2026-10-27, 15 entrées sur 16 au statut `officielle_relue`. CAL-016 (`incertaine`, bloquante) n'est mobilisé par aucun constat. Les points [AV] restent ouverts : « importantes modifications » (art. 111, par. 2), dates des art. 49, 72, 73 et 86, garde-fous « raisonnables et adéquats ».
- Les lignes directrices (art. 50, classification à haut risque, projet de mai 2026), les codes de bonnes pratiques et les normes harmonisées évoluent.
- Ce rapport ne remplace ni l'avis d'un juriste ni une évaluation de la conformité au sens de l'article 43. Il n'affirme la conformité d'aucun système et ne chiffre aucune sanction.

## 15. Suivi (ré-audit)

Premier audit : aucun statut précédent. Au ré-audit, conserver les identifiants AIA-001 à AIA-014 et recalculer le calendrier à la nouvelle date. Après le 2026-12-02, AIA-005, AIA-007 et AIA-008 passeront en obligations en vigueur.