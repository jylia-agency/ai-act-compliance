# Rapport d'audit AI Act : EduAssist (`demo-ai-secure`)

> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689. Les mesures observées attestent de la présence d'un dispositif, pas
> du respect d'une obligation.

| Paramètre | Valeur |
|---|---|
| Date d'audit | **2026-10-27** |
| Périmètre | Dossier `demo-ai-secure/` complet : `README.md`, `requirements.txt`, `app/` (10 fichiers Python), `docs/` (6 documents). Aucun dossier exclu. Pas d'historique Git disponible (pas de `.git`), ni branche ni commit identifiables. |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`meta.last_verified` de `data/ai-act-calendar.json`) ; écart avec la date d'audit : 0 jour. Les références issues du règlement 2026/1744 reposent sur des sources secondaires (confiance moyenne) : voir section 11. |
| Contexte fourni par le demandeur | Uniquement celui du `README.md` et de `docs/` : éditeur fictif « EduAssist SAS », établi en France ; produit commercialisé sous la marque « EduAssist » auprès de lycées et d'universités de l'Union ; tuteur et correction assistée mis sur le marché le **2026-03-01** ; module d'illustrations mis sur le marché le **2026-09-15** ; modèles via l'API d'un tiers (Anthropic) ; aucun entraînement de modèle ; télésurveillance d'examens par webcam supprimée. Statut PME, statut public ou privé des établissements clients : non communiqués. |
| Méthode | Skill `ia-compliance` v1.0.0, lecture seule, sans exécution du code audité ; scripts `scan_ai_signals.py` et `obligation_timeline.py` (lecture seule, sans réseau) |
| Audit précédent | Aucun rapport antérieur fourni. Le README présente le projet comme une « version corrigée », mais aucun identifiant `AIA-NNN` antérieur n'étant disponible, les constats sont numérotés à partir de AIA-001 et la section 12 (suivi) est sans objet. |

---

## 1. Résumé exécutif

- **Systèmes d'IA identifiés : 3.** SYS-01 Tuteur conversationnel ; SYS-02 Correction assistée de
  dissertations ; SYS-03 Illustrations de cours. Le module d'événements d'examen (`app/exam_events.py`)
  a été examiné et écarté : il ne réalise aucune inférence (pas un système d'IA).
- **Rôle d'EduAssist** : au vu des éléments observés (marque EduAssist, commercialisation auprès
  d'établissements), EduAssist est **susceptible d'être fournisseur** des trois systèmes
  (art. 3, point 3). Elle n'est pas, au vu du dépôt, fournisseur des modèles d'IA à usage général
  sous-jacents (Anthropic pour SYS-01 et SYS-02 ; service tiers non identifié pour SYS-03). Les
  établissements clients sont déployeurs.
- **Classification** : SYS-02 **haut risque probable** (annexe III, point 3, b), évaluation des acquis
  d'apprentissage ; dérogation de l'art. 6, par. 3 non applicable, en accord avec l'analyse interne de
  l'éditeur). SYS-01 et SYS-03 **non à haut risque (motivé)**, soumis à l'article 50. Aucune pratique
  interdite plausible identifiée.
- **Points les plus sensibles** (aucun constat de gravité Critique ou Élevée) :
  - AIA-001 : marquage lisible par machine des illustrations (obligation **en vigueur** pour SYS-03) :
    mesure présente mais limitée à des métadonnées PNG non standard, signature C2PA non observable,
    robustesse et détectabilité non démontrées.
  - AIA-002 et AIA-008 : deux échéances au **2026-12-02** (dans 36 jours) : marquage des textes générés
    par SYS-01 et SYS-02 (art. 50, par. 2, régime transitoire) et nouvelles interdictions de l'art. 5
    (contenus intimes non consentis, matériel pédopornographique) pour le générateur d'images SYS-03,
    dont aucun filtre n'est observable dans le code.
  - AIA-003 et AIA-004 : SYS-02 est en production depuis mars 2026 alors que les biais par
    sous-groupes ne sont pas évalués et que la copie de l'élève est transmise au modèle sans défense
    contre l'injection d'instructions ; la validation humaine atténue mais ne supprime pas ces risques.
  - AIA-007 : l'effet de l'article 111, paragraphe 2 (système antérieur, établissements publics) sur
    l'échéance du haut risque reste à qualifier juridiquement.
- **Obligations en vigueur concernées** : art. 4 (maîtrise de l'IA) ; art. 5 (examiné, non retenu) ;
  art. 50, par. 1 et 5 (SYS-01) ; art. 50, par. 2 (SYS-03) ; art. 50, par. 4 (déployeurs de SYS-03).
- **Échéances à venir** : 2026-12-02 (art. 50, par. 2 pour SYS-01 et SYS-02 ; nouvelles interdictions
  de l'art. 5) ; 2027-12-02 (exigences du haut risque, annexe III, pour SYS-02, sous réserve de
  l'art. 111, par. 2) ; 2030-08-02 (art. 111, par. 2, systèmes destinés aux autorités publiques,
  confiance faible).
- **Principales incertitudes** : interface utilisateur absente du dépôt ; identité et pratiques du
  service tiers de génération d'images ; outil interne de signature C2PA ; statut public des
  établissements clients ; portée de l'art. 50, par. 2 pour les textes conversationnels `[AV]` ;
  art. 111, par. 2 `[AV]`.
- **Synthèse des constats (16)** :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | 0 | 0 | 0 | 0 | 2 (AIA-013, AIA-014) |
| Risque potentiel | 0 | 0 | 3 (AIA-001, AIA-003, AIA-004) | 1 (AIA-009) | 0 |
| À vérifier juridiquement ou organisationnellement | 0 | 0 | 1 (AIA-007) | 2 (AIA-011, AIA-012) | 0 |
| Bonne pratique recommandée | 0 | 0 | 0 | 1 (AIA-010) | 0 |
| Non encore applicable | 0 | 0 | 4 (AIA-002, AIA-005, AIA-006, AIA-008) | 0 | 0 |
| Non applicable | 0 | 0 | 0 | 0 | 2 (AIA-015, AIA-016) |

Le projet présente de nombreuses mesures observables (information sur l'IA, validation humaine
bloquante, journalisation des versions, marquage des images, documentation de classification). Ces
constats positifs ne valent pas attestation de conformité.

---

## 2. Périmètre et méthode

**Arborescence analysée** (intégralité du dossier, 18 fichiers) :

```
demo-ai-secure/
├── README.md, requirements.txt (fastapi==0.115.0, anthropic==0.39.0, pillow==11.0.0)
├── app/  __init__.py, audit_log.py, c2pa_signer.py, config.py, exam_events.py,
│         gradebook.py, grading.py, illustrations.py, image_provider.py, tutor_chat.py
└── docs/ ai-literacy-plan.md, ai-system-inventory.md, classification-assessment.md,
          human-oversight-procedure.md, risk-register.md, technical-documentation.md
```

**Déroulé** : phases 0 à 10 du skill (cadrage, exploration, identification, modèles, rôles,
exclusions, classification, obligations et calendrier, checklists A à G, constats, livrables).

**Outils** :
- `scan_ai_signals.py` : 18 fichiers analysés, signaux `provider_api/anthropic` (3),
  `model_identifier` (2), `transparency_marker` (14), `oversight_marker` (17), `logging_marker` (33),
  `credentials_reference` (5, références à une variable d'environnement, aucune valeur en clair),
  `sensitive_context/education` (21). Le signal `sensitive_context/employment` (1) est un **faux
  positif** : il provient du motif `cv` dans l'URL `http://cv.iptc.org/...` (`app/illustrations.py:17`).
- `obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-03-01` (SYS-01, SYS-02),
  `--placed-on-market 2026-09-15 --scope transparency` (SYS-03), et
  `--scope high-risk-annex-iii --public-authority` (hypothèse d'établissements publics pour SYS-02).

**Éléments non analysés** : aucune couche API ou interface (FastAPI figure dans les dépendances,
mais aucune route n'est présente) ; implémentations réelles de `image_provider.generate_image` et
`c2pa_signer.attach_c2pa_manifest` (lèvent `NotImplementedError` dans le dépôt) ; configuration de
production ; documents référencés hors dépôt (guide utilisateur, registre de formation RH,
CHANGELOG interne, rapport de la campagne d'évaluation).

---

## 3. Systèmes d'IA identifiés (inventaire)

### 3.1 Synthèse

| ID | Système | Finalité | Rôle(s) d'EduAssist | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|
| SYS-01 | Tuteur conversationnel | Répondre aux questions de cours des élèves et étudiants | Fournisseur du système (susceptible) | Claude via API Anthropic, `claude-sonnet-4-5` par défaut, configurable | Non à haut risque (motivé) ; art. 50, par. 1, 2, 5 | Moyenne |
| SYS-02 | Correction assistée | Proposer une note sur 20, une justification et un détail par critère pour des dissertations ; décision finale par l'enseignant | Fournisseur du système (susceptible) | Claude via API Anthropic, `claude-sonnet-4-5` par défaut, configurable | Haut risque probable (annexe III, point 3, b)) ; art. 50, par. 2 | Élevée (faits) / Moyenne (qualification) |
| SYS-03 | Illustrations de cours | Générer des images pour des supports pédagogiques | Fournisseur du système (susceptible) | Service tiers de génération d'images, non identifié dans le dépôt | Non à haut risque (motivé) ; art. 50, par. 2 et 4 | Moyenne |

### 3.2 Inventaire détaillé

| Champ | SYS-01 Tuteur conversationnel | SYS-02 Correction assistée | SYS-03 Illustrations de cours |
|---|---|---|---|
| Finalité (art. 3, point 12) | Aide aux révisions, réponses aux questions de cours (`docs/ai-system-inventory.md:7`) | Proposition de note et de justification pour les dissertations ; décision finale par l'enseignant (`docs/ai-system-inventory.md:8`) | Génération d'images pour supports pédagogiques (`docs/ai-system-inventory.md:9`) |
| Description fonctionnelle | `start_session()` renvoie un message d'information ; `answer()` transmet l'historique et la question au modèle et renvoie le texte | `propose_grade()` appelle le modèle (température 0) et crée une `GradeProposal` en statut `pending_review` ; `review_grade()` enregistre la décision de l'enseignant (approve, override avec motif, reject) et publie la note via `publish_grade()` | `create_illustration()` obtient une image du service tiers, ajoute des métadonnées PNG, appelle la signature C2PA, journalise |
| Fichiers principaux | `app/tutor_chat.py`, `app/config.py:5` | `app/grading.py`, `app/gradebook.py`, `app/config.py:6-8` | `app/illustrations.py`, `app/image_provider.py`, `app/c2pa_signer.py` |
| Entrées | Message de l'élève et historique de conversation | Texte de la dissertation, identifiant de l'élève | Prompt textuel saisi par l'enseignant |
| Sorties et effets | Texte informatif (information) | Note, critères, justification : **recommandation** à l'enseignant ; publication de la note uniquement après validation | Image PNG destinée à des supports de cours (contenu) |
| Utilisateurs | Élèves, étudiants | Enseignants | Enseignants |
| Personnes concernées | Élèves, étudiants (potentiellement mineurs en lycée) | Élèves, étudiants évalués | Élèves (destinataires), personnes éventuellement représentées |
| Données pertinentes | Questions et historique de conversation | Copies d'élèves, identifiant élève, notes, identifiant enseignant, motifs | Prompts, images générées |
| Modèle(s) et version(s) | `TUTOR_MODEL`, défaut `claude-sonnet-4-5` (sans suffixe de version datée) ; `response.model` journalisé | `GRADING_MODEL`, défaut `claude-sonnet-4-5` ; `response.model` et `PROMPT_VERSION = "grading-rubric-v3"` journalisés | Non visible (renvoyé par le service tiers et inscrit en métadonnées) |
| Fournisseur(s) de modèle / API tierces | Anthropic (SDK `anthropic==0.39.0`) | Anthropic | Service tiers non identifié |
| Entraînement ou affinage | Aucun observé (pas de script d'entraînement, pas de bibliothèque d'apprentissage) | Aucun observé | Aucun observé |
| Composants associés | Aucun RAG, aucun outil d'agent | Grille d'évaluation dans le prompt système (`grading.py:17`) ; carnet de notes ; journal d'audit | Signataire C2PA interne (non inclus) |
| Acteurs et rôles | EduAssist : fournisseur du système ; Anthropic : fournisseur du modèle GPAI ; établissements : déployeurs | Idem ; enseignants : personnes chargées de la supervision humaine (pas un opérateur distinct) | EduAssist : fournisseur du système ; service tiers : fournisseur du modèle (non identifié) ; établissements et enseignants : déployeurs |
| Date de mise sur le marché | 2026-03-01 (déclarée, README:11) | 2026-03-01 (déclarée) | 2026-09-15 (déclarée, README:12) |
| Classification | Non à haut risque (motivé) | Haut risque probable (annexe III, point 3, b)) | Non à haut risque (motivé) |
| Confiance de la classification | Moyenne | Moyenne (qualification `[TI]`, dates `[O26]`) | Moyenne |
| Statut | En production (déclaré) | En production (déclaré) | En production (déclaré) ; implémentations du fournisseur d'images et de C2PA absentes du dépôt |
| Informations manquantes | Interface, canaux d'exposition, accessibilité ; mécanisme de signalement (R-04) | Statut public des établissements ; historique des versions depuis mars 2026 ; rapport d'évaluation | Identité et conditions du service tiers ; outil C2PA ; filtre de prompts (R-05) ; guide utilisateur |

### 3.3 Composants examinés et écartés

| Composant | Fichier | Motif |
|---|---|---|
| Événements d'examen | `app/exam_events.py:1-10` | Pas un système d'IA : transmission déterministe d'événements techniques (perte de focus, déconnexion) au journal, sans inférence ; décision réservée aux surveillants humains (docstring lignes 3-4). La télésurveillance par webcam a été supprimée selon le README:14 (non vérifiable sur l'historique, absence de `.git`). |
| Carnet de notes | `app/gradebook.py` | Stockage ; garde-fou de publication (composant de SYS-02, pas un système distinct). |
| Journal d'audit | `app/audit_log.py` | Journalisation (composant transverse). |
| Configuration | `app/config.py` | Paramètres ; secrets lus dans l'environnement, aucune valeur en clair. |
| Signataire C2PA, adaptateur d'images | `app/c2pa_signer.py`, `app/image_provider.py` | Bouchons (`NotImplementedError`), composants de SYS-03. |

---

## 4. Rôles réglementaires

- **SYS-01, SYS-02, SYS-03** : EduAssist développe les systèmes et les commercialise sous sa
  marque auprès d'établissements de l'Union (README:9-12) : elle est **susceptible d'être
  fournisseur** de chacun de ces systèmes d'IA (art. 3, point 3 `[TI]`), y compris s'ils reposent
  sur des API tierces. Établie en France, elle n'a pas à désigner de mandataire (art. 22).
- **Distinction fournisseur du système / fournisseur du modèle GPAI** : Anthropic est le
  fournisseur du modèle d'IA à usage général sous-jacent de SYS-01 et SYS-02 ; le fournisseur du
  modèle de SYS-03 n'est pas identifié. EduAssist n'entraîne, n'affine ni ne publie aucun modèle
  (README:13 ; `docs/ai-system-inventory.md:11-12` ; aucun script d'entraînement ni bibliothèque
  d'apprentissage dans `requirements.txt`) : elle n'est **pas fournisseur de modèle GPAI** (voir AIA-015).
- **Importateur / distributeur** : EduAssist ne met pas sur le marché un système portant le nom
  d'un tiers ; elle intègre des modèles dans ses propres systèmes. Rôles non retenus.
- **Déployeurs** : les établissements clients (lycées, universités) utilisent les systèmes sous
  leur autorité (art. 3, point 4). Les enseignants sont les personnes chargées de la supervision
  humaine (art. 26, par. 2, futur pour SYS-02). Certains établissements peuvent être des
  organismes de droit public (art. 27 ; art. 111, par. 2 `[AV]`) : statut non communiqué (NV-04).
- **Art. 25 (requalification)** : sans objet pour EduAssist, déjà fournisseur. À signaler aux
  déployeurs : un établissement qui utiliserait SYS-01 pour évaluer ou orienter les élèves
  modifierait la destination (art. 25, par. 1, c)).

---

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 2, par. 3 (défense, sécurité nationale) | Tous | Écartée | Usage éducatif civil. |
| Art. 2, par. 6 et 8 (recherche, pré-commercialisation) | Tous | Écartée | Systèmes mis sur le marché (2026-03-01, 2026-09-15). |
| Art. 2, par. 10 (usage personnel non professionnel) | Tous | Écartée | Commercialisation B2B auprès d'établissements. |
| Art. 2, par. 12 (logiciels libres) | Tous | Écartée | Produit commercial sous marque ; au surplus, l'exclusion ne couvre ni le haut risque ni l'art. 50. |
| Art. 3, point 1 (définition de système d'IA) | `exam_events.py` | Retenue (pas un système d'IA) | Aucune inférence ; règle de transmission déterministe. |
| Art. 5, par. 1, f) (émotions, enseignement) | Tous | Écartée (pratique non observée) | Aucune bibliothèque biométrique ou d'analyse émotionnelle ; webcam supprimée (AIA-016). |
| Art. 5, par. 1, a) et b) (manipulation, vulnérabilités dues à l'âge) | SYS-01 | Examinée, non retenue | Le prompt système impose de déclarer la nature d'IA (`tutor_chat.py:13-16`) ; aucun indice d'altération substantielle du comportement ni de préjudice important. |
| Art. 6, par. 3 (dérogation) | SYS-02 | Écartée | La note proposée est susceptible d'influencer substantiellement la décision de l'enseignant ; ni tâche procédurale étroite, ni simple tâche préparatoire ; la validation humaine en aval n'est pas un critère de dérogation. Position identique à l'analyse interne (`docs/classification-assessment.md:8-9`). |
| Art. 50, par. 1 (exception « évident ») | SYS-01 | Non invoquée | Information explicite prévue (`tutor_chat.py:9-12`). |
| Art. 50, par. 2 (assistance à la mise en forme standard ; absence de modification substantielle) | SYS-01, SYS-02 | Écartée | Les textes sont générés à partir de questions ou de copies, non simplement mis en forme. |
| Art. 50, par. 4, al. 1 (régime des œuvres artistiques ou créatives) | SYS-03 | Non documentée | Supports pédagogiques : le régime allégé n'est pas évident ; à apprécier par le déployeur (AIA-011). |
| Art. 111, par. 2 (systèmes antérieurs) | SYS-02 | À vérifier | Mis sur le marché avant le 2027-12-02 ; portée et échéance publique `[AV]` (AIA-007). |
| Renvois à d'autres législations (protection des données : identifiants d'élèves dans les journaux, transfert des copies au fournisseur de modèle ; accessibilité) | Tous | Hors périmètre | Signalé sans analyse. |

---

## 6. Classification

### 6.1 SYS-01 Tuteur conversationnel

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA ? | Oui | Génération de réponses par un LLM (`tutor_chat.py:24-32`) | Art. 3, point 1 `[TI]` |
| 1 | Exclusion de l'art. 2 ? | Non | Voir section 5 | Art. 2 `[TI]` |
| 2 | Pratique interdite plausible ? | Non (a, b, f examinés) | Prompt système exigeant de se déclarer IA | Art. 5 `[TI]` |
| 3 | Annexe I ? | Non | Logiciel éducatif, pas un produit réglementé | Art. 6, par. 1 |
| 4 | Annexe III ? | Non | Aucune évaluation ni orientation ; `tutor_chat.py` n'importe pas `grading` ni `gradebook` (contrôle technique confirmé) ; réutilisation hors dépôt non observable | Annexe III, point 3 `[TI]` |
| 5 | Dérogation | Sans objet | | |
| 6 | Art. 50 | Oui : par. 1 (interaction directe), par. 2 (texte généré, portée `[AV]`), par. 5 | `tutor_chat.py:9-21` | Art. 50 `[TI]`, `[O26]` |
| 7 | Fournisseur GPAI ? | Non | | Art. 53 |
| 8 | Horizontal | Art. 4 | `docs/ai-literacy-plan.md` | Art. 4 `[TI]` / `[O26]` |

**Conclusion** : non à haut risque (motivé), confiance moyenne. Hypothèse alternative : si les
échanges étaient réutilisés pour noter ou orienter les élèves, annexe III, point 3, b) (haut risque
possible). Obligations : art. 50, par. 1 et 5 en vigueur (CAL-009) ; art. 50, par. 2 non encore
applicable jusqu'au 2026-12-02 (CAL-010) ; art. 4 en vigueur (CAL-002, CAL-003).

### 6.2 SYS-02 Correction assistée

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA ? | Oui | Inférence d'une note et d'une justification par LLM (`grading.py:33-55`) | Art. 3, point 1 |
| 1 | Exclusion de l'art. 2 ? | Non | | Art. 2 |
| 2 | Pratique interdite plausible ? | Non | Pas de notation sociale (évaluation dans le contexte scolaire d'origine), pas d'émotions | Art. 5, par. 1, c) et f) |
| 3 | Annexe I ? | Non | | Art. 6, par. 1 |
| 4 | Annexe III ? | **Oui** : point 3, b), évaluation des acquis d'apprentissage | Note sur 20 selon une grille (`grading.py:17, 38-39`) ; destination déclarée (`docs/ai-system-inventory.md:8`) | Annexe III, point 3, b) `[TI]` |
| 5a | Profilage ? | Possible (évaluation de la performance scolaire d'une personne identifiée) ; sans incidence puisque la dérogation est de toute façon écartée | `student_id` associé à la note | Art. 6, par. 3, dernier al. |
| 5b | Conditions a) à d) et absence de risque important ? | Non | La proposition détermine le point de départ de la note ; influence substantielle | Art. 6, par. 3 `[TI]` |
| 6 | Art. 50 | Par. 2 (justification textuelle générée, portée `[AV]`) ; par. 1 peu pertinent (outil non conversationnel, proposition étiquetée selon la procédure) | | Art. 50 |
| 7 | Fournisseur GPAI ? | Non | | Art. 53 |
| 8 | Horizontal | Art. 4 | | Art. 4 |

**Conclusion** : **haut risque probable (annexe III, point 3, b))**, confiance élevée sur les faits,
moyenne sur la qualification (projet de lignes directrices de la Commission sur l'art. 6 non
définitif). Exigences du chapitre III **non encore applicables** : 2027-12-02 (CAL-011, confiance
moyenne) ; régime des systèmes antérieurs **conditionnel** (CAL-013, confiance faible) ; hypothèse
« autorité publique » : 2030-08-02 (CAL-013, confiance faible, divergence 2028-01-28).

### 6.3 SYS-03 Illustrations de cours

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA ? | Oui (génération d'images par un service tiers) | `illustrations.py:21` ; implémentation absente | Art. 3, point 1 |
| 1 | Exclusion de l'art. 2 ? | Non | | Art. 2 |
| 2 | Pratique interdite plausible ? | Points a) à h) : non. Nouveaux points (contenus intimes non consentis, matériel pédopornographique) : non encore applicables (2026-12-02), garde-fous non observables (AIA-008) | `illustrations.py:20-21` | Art. 5 `[TI]` / `[O26]` |
| 3 | Annexe I ? | Non | | |
| 4 | Annexe III ? | Non | Production de supports, aucune évaluation de personnes | |
| 6 | Art. 50 | Par. 2 (fournisseur, **en vigueur** : mise sur le marché postérieure au 2026-08-02) ; par. 4, al. 1 (déployeurs, hypertrucages) | `illustrations.py:16-27` | Art. 50 `[TI]`, `[O26]` |
| 7 | Fournisseur GPAI ? | Non | | |
| 8 | Horizontal | Art. 4 | | |

**Conclusion** : non à haut risque (motivé), confiance moyenne. Art. 50, par. 2 en vigueur
(CAL-010, aucun régime transitoire) ; art. 50, par. 4 en vigueur pour les déployeurs (CAL-009).

---

## 7. Obligations et calendrier

### 7.1 Statuts temporels (calculés par `obligation_timeline.py` au 2026-10-27)

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|
| Maîtrise de l'IA | Tous | Fournisseur (et déployeurs) | En vigueur | 2025-02-02 ; rédaction modifiée 2026-07-27 | CAL-002, CAL-003 | Élevée / Moyenne |
| Pratiques interdites (version initiale) | Tous | Fournisseur, déployeurs | En vigueur | 2025-02-02 | CAL-002 | Élevée |
| Nouvelles pratiques interdites | SYS-03 | Fournisseur, déployeurs | Non encore applicable | 2026-12-02 | CAL-004 | Moyenne |
| Information sur l'interaction (art. 50, par. 1 et 5) | SYS-01 | Fournisseur | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Marquage des contenus synthétiques (art. 50, par. 2) | SYS-01, SYS-02 (texte) | Fournisseur | Non encore applicable (régime transitoire, mise sur le marché 2026-03-01) | 2026-12-02 | CAL-010 | Moyenne ; modalités pour le texte `[AV]` |
| Marquage des contenus synthétiques (art. 50, par. 2) | SYS-03 (images) | Fournisseur | En vigueur (mise sur le marché 2026-09-15, pas de régime transitoire) | 2026-08-02 | CAL-010 | Moyenne |
| Déclaration des hypertrucages (art. 50, par. 4, al. 1) | SYS-03 | Déployeurs | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Exigences du haut risque (art. 8 à 27) | SYS-02 | Fournisseur ; déployeurs (art. 26, 27) | Non encore applicable | 2027-12-02 | CAL-011 | Moyenne |
| Systèmes antérieurs (art. 111, par. 2) | SYS-02 | Fournisseur | Conditionnel (modification importante) ; hypothèse autorité publique : 2030-08-02 | n.d. / 2030-08-02 | CAL-013 | Faible |
| Enregistrement art. 49, par. 2 (dérogation) | SYS-02 | Fournisseur | Sans objet (dérogation non invoquée) | n.d. | CAL-016 | Faible |
| Obligations GPAI (art. 53 à 55) | Aucun | n.a. | Non applicable (EduAssist n'est pas fournisseur de modèle) | | CAL-005 | Élevée |

### 7.2 Matrice des obligations

| Système | Rôle | Obligation | Référence | Base | Statut temporel (CAL) | Éléments de preuve | Statut de preuve | Vérifications restantes | Constat(s) |
|---|---|---|---|---|---|---|---|---|---|
| Tous | Fournisseur | Maîtrise de l'IA | Art. 4 `[TI]`/`[O26]` | Obligation | En vigueur (CAL-002, CAL-003) | `docs/ai-literacy-plan.md:3-7` | Partielle (plan documenté, registre hors dépôt) | Registre RH, contenus de formation | AIA-012 |
| Tous | Fournisseur | Absence de pratique interdite | Art. 5 `[TI]` | Obligation | En vigueur (CAL-002) | Aucun signal biométrique ou émotionnel ; `exam_events.py` sans IA | Mesure observée (absence de fonctionnalité) | Historique de suppression de la webcam | AIA-016 |
| SYS-03 | Fournisseur | Garde-fous nouvelles interdictions | Art. 5, nouveaux points `[O26]` | Obligation future | Non encore applicable (CAL-004, 2026-12-02) | Aucun filtre dans `illustrations.py:20-21` | Non observable | Filtres du service tiers, filtre R-05 | AIA-008 |
| SYS-01 | Fournisseur | Information sur l'interaction avec une IA | Art. 50, par. 1 et 5 `[TI]` | Obligation | En vigueur (CAL-009) | `tutor_chat.py:9-21` | Mesure observée (affichage non observable) | Interface, canaux, accessibilité | AIA-013 |
| SYS-01, SYS-02 | Fournisseur | Marquage des textes générés | Art. 50, par. 2 `[TI]`+`[O26]` | Obligation | Non encore applicable (CAL-010, 2026-12-02) | `tutor_chat.py:32`, `grading.py:42-47` : texte brut | Non observée | Position au regard des lignes directrices | AIA-002 |
| SYS-03 | Fournisseur | Marquage et détectabilité des images | Art. 50, par. 2 `[TI]`+`[O26]` | Obligation | En vigueur (CAL-010) | `illustrations.py:22-27` | Partielle | C2PA, robustesse, détection | AIA-001 |
| SYS-03 | Déployeurs (outillage par le fournisseur) | Déclaration des hypertrucages | Art. 50, par. 4, al. 1 `[TI]` | Obligation du déployeur | En vigueur (CAL-009) | `docs/classification-assessment.md:27-28` ; étiquette en métadonnées seulement | Partielle | Guide utilisateur, étiquette visible | AIA-011 |
| SYS-02 | Fournisseur | Gestion des risques | Art. 9 `[TI]` | Obligation future | Non encore applicable (CAL-011) | `docs/risk-register.md` (R-01 à R-06) | Partielle (injection de prompt absente) | Registre complet | AIA-004, AIA-006 |
| SYS-02 | Fournisseur | Données, biais | Art. 10 `[TI]` | Obligation future | Non encore applicable (CAL-011) | `docs/technical-documentation.md:16-19` ; R-03 prévu T1 2027 | Partielle | Évaluation par sous-groupes | AIA-003 |
| SYS-02 | Fournisseur | Documentation technique | Art. 11, annexe IV `[TI]` | Obligation future | Non encore applicable (CAL-011) | `docs/technical-documentation.md` (ébauche) | Partielle | Compléments annexe IV | AIA-006 |
| SYS-02 | Fournisseur | Journalisation, conservation | Art. 12, 19 `[TI]` | Obligation future | Non encore applicable (CAL-011) | `audit_log.py`, `grading.py:51-54, 65-66`, `config.py:8` | Partielle | Justification non journalisée, rétention non implémentée | AIA-005 |
| SYS-02 | Fournisseur | Notice d'utilisation | Art. 13 `[TI]` | Obligation future | Non encore applicable (CAL-011) | « À rédiger » (`classification-assessment.md:37`) | Non observée (déclarée à rédiger) | Notice | AIA-006 |
| SYS-02 | Fournisseur | Contrôle humain | Art. 14 `[TI]` | Obligation future | Non encore applicable (CAL-011) | `grading.py:28, 58-68`, `gradebook.py:5-8`, procédure | Mesure observée (robustesse perfectible) | Interface, authentification | AIA-009, AIA-014 |
| SYS-02 | Fournisseur | Exactitude, robustesse, cybersécurité | Art. 15 `[TI]` | Obligation future | Non encore applicable (CAL-011) | Campagne prévue T1 2027 ; pas de défense contre l'injection | Partielle | Tests adverses | AIA-004 |
| SYS-02 | Fournisseur | SGQ, évaluation de la conformité, déclaration UE, marquage CE, enregistrement | Art. 16, 17, 43, 47, 48, 49 `[TI]` | Obligation future | Non encore applicable (CAL-011) ; art. 49 `[AV]` | « À établir », « À planifier » (`classification-assessment.md:40-41`) | Non observable | Calendrier de préparation | AIA-006 |
| SYS-02 | Fournisseur | Régime des systèmes antérieurs | Art. 111, par. 2 `[AV]` | Obligation conditionnelle | Conditionnel (CAL-013) | Point ouvert (`classification-assessment.md:13-14`) | Non observable | Analyse juridique | AIA-007 |
| SYS-02 | Déployeurs | Supervision, journaux 6 mois, information des élèves, FRIA (organismes publics) | Art. 26, par. 2, 6, 11 ; art. 27 `[TI]` | Obligation future des déployeurs | Non encore applicable (CAL-011) | Formation des enseignants documentée | Non observable | Auprès des établissements | AIA-006, AIA-007 |
| Tous | Aucun | Obligations des fournisseurs de modèles GPAI | Art. 53 à 55 `[TI]` | n.a. | Non applicable | Pas d'entraînement ni de publication | N/A | Aucune | AIA-015 |
| SYS-01, SYS-02 | Fournisseur | Épinglage des versions de modèle | Aucune (bonne pratique) ; lien annexe IV et art. 111, par. 2 | Bonne pratique | n.a. | `config.py:5-6` | Partielle (`response.model` journalisé) | Valeurs de production | AIA-010 |

Rappel : « Mesure observée » n'équivaut pas à « obligation satisfaite ».

### 7.3 Résultat des checklists conditionnelles (A à G)

| Checklist | Contrôles (statut) |
|---|---|
| A. Transparence | A1 Partiel (SYS-01 : message prévu `tutor_chat.py:9-21`, affichage non observable) ; A2 OK (`tutor_chat.py:13-16`) ; A3 N/A (exception non invoquée) ; A4 SYS-03 Partiel (métadonnées PNG `illustrations.py:22-26`, C2PA non observable), SYS-01/02 Non encore applicable ; A5 Non observable (robustesse non testée, `illustrations.py:6`) ; A6 Non observable ; A7 N/A (exceptions écartées) ; A8 Partiel (consigne déclarée, guide hors dépôt) ; A9 N/A (pas de publication de textes d'intérêt public) ; A10 N/A (aucune reconnaissance des émotions) ; A11 Non observable ; A12 Non observable (aucune mention du code de bonnes pratiques du 10.6.2026). |
| B. Supervision humaine (SYS-02, futur) | B1 OK (`gradebook.py:6-7`, statut `pending_review`) ; B2 Partiel (justification et critères renvoyés, affichage non observable) ; B3 OK (`grading.py:58-68`) ; B4 Non observable (pas de drapeau de désactivation) ; B5 KO partiel (aucune validation de la sortie du modèle, `grading.py:42`) ; B6 Partiel (décision journalisée, publication directe non journalisée) ; B7 Partiel (revue trimestrielle déclarée) ; B8 Non observable (formation déclarée). |
| C. Documentation technique (SYS-02, futur) | C1 OK ; C2 Partiel ; C3 OK ; C4 Partiel (alias probable, version servie journalisée) ; C5 Non observable ; C6 Partiel (résultats résumés, rapport hors dépôt) ; C7 OK (`technical-documentation.md:18-19`) ; C8 Partiel ; C9 Partiel (CHANGELOG hors dépôt) ; C10 Non observée (« À rédiger ») ; C11 N/A. |
| D. Gestion des risques (SYS-02, futur) | D1 Partiel (registre sans injection de prompt) ; D2 Partiel ; D3 Partiel (campagne T1 2027) ; D4 KO partiel (aucune défense contre l'injection observée) ; D5 à D7 Non observable ; D8 OK (`config.py:4`, aucun secret en clair, aucun secret journalisé). |
| E. Traçabilité (SYS-02, futur) | E1 OK ; E2 Partiel ; E3 OK ; E4 Partiel (version de grille journalisée, température non journalisée) ; E5 Non observable ; E6 Partiel (400 jours déclarés, aucune purge implémentée). |
| F. Éducation | F1 OK (aucune reconnaissance des émotions) ; F2 OK (qualification motivée par l'éditeur et confirmée) ; F3, F4, F6 N/A ; F5 N/A (`exam_events.py` sans IA) ; F7 N/A ; F8 Non encore applicable ; F9 Conditionnel (statut des établissements inconnu). |
| G. Maîtrise de l'IA | G1 Partiel (plan documenté) ; G2 Non observable ; G3 Partiel (module enseignants) ; G4 Partiel (avertissements dans le code SYS-01, guide hors dépôt) ; G5 Non observable (registre RH hors dépôt). |

---

## 8. Constats

Ordonnés par gravité puis par identifiant. Dans chaque constat, le **fait observé** et l'**analyse
juridique** sont distingués.

### AIA-001 : Marquage des illustrations limité à des métadonnées PNG non standard ; C2PA, robustesse et détectabilité non démontrées
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification, référence `[O26]` pour la date)
- **Preuve observée** : *Fait observé.* `create_illustration()` écrit trois blocs texte PNG
  (`DigitalSourceType` = URI IPTC `trainedAlgorithmicMedia`, `ai_disclosure`, `model_version`) via
  `PngImagePlugin.PngInfo.add_text`, puis appelle `attach_c2pa_manifest()`, qui lève
  `NotImplementedError` dans le dépôt (« Signature C2PA effectuée par l'outil interne en
  production »). Le code écrit des mots-clés PNG personnalisés et non un paquet XMP ni un
  enregistrement IPTC, contrairement à ce qu'annonce la docstring (« XMP/IPTC »). L'image est
  enregistrée **avant** la signature : en cas d'échec de celle-ci, un fichier non signé subsiste,
  sans évènement de journal. L'image du service tiers est reçue sous forme d'objet `PIL.Image`, ce
  qui ne préserve pas les métadonnées ou manifestes éventuellement apposés en amont. La docstring
  indique : « la robustesse du marquage aux recompressions n'a pas été testée ». Aucun outil de
  détection n'est documenté.
- **Fichier(s) et lignes** : `app/illustrations.py:3-6, 17, 20-28` ; `app/c2pa_signer.py:5-6` ; `app/image_provider.py:5-6`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA (EduAssist)
- **Classification du système** : Non à haut risque (motivé) ; soumis à l'art. 50, par. 2
- **Référence juridique** : Art. 50, par. 2 du règlement (UE) 2024/1689 `[TI]`, date selon le règlement 2026/1744 `[O26]`, à confirmer sur le JO ; [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50) ; code de bonnes pratiques sur le marquage et l'étiquetage (10.6.2026, volontaire)
- **Date d'application** : 2026-08-02 ; **en vigueur** à la date d'audit pour SYS-03 (mise sur le marché le 2026-09-15, aucun régime transitoire) (CAL-010, confiance moyenne)
- **Conditions et exceptions** : Exceptions « assistance à la mise en forme standard » et « absence de modification substantielle » écartées (génération complète d'images). L'obligation s'apprécie « dans la mesure du techniquement possible » et selon l'état de l'art ; la Commission considérerait qu'aucune technique unique ne suffit à elle seule `[O26]`.
- **Explication** : *Analyse juridique.* La loi demande que les images générées portent un marquage lisible par machine, robuste et détectable. Un marquage est présent, ce qui est positif, mais il repose dans le dépôt sur des champs texte PNG qui disparaissent généralement lors d'une conversion ou d'une recompression, et la seconde couche (C2PA) n'est pas observable. L'efficacité du dispositif, au sens de l'art. 50, par. 2, n'est donc pas démontrée ; il s'agit d'un manquement potentiel à confirmer, pas d'un manquement établi.
- **Recommandation** (obligation, art. 50, par. 2) : écrire les métadonnées dans des conteneurs standard (XMP `Iptc4xmpExt:DigitalSourceType`, manifeste C2PA effectivement signé) ; ajouter une couche résistante aux transformations (filigrane invisible ou empreinte) ; préserver les marquages du fournisseur amont (récupérer le fichier d'origine plutôt qu'un objet image décodé) ; rendre la signature bloquante (ne pas conserver de fichier non signé, journaliser l'échec) ; documenter un moyen de vérification ; s'appuyer sur le code de bonnes pratiques (bonne pratique).
- **Méthode de vérification** : tests automatisés vérifiant la présence et la validité du manifeste C2PA et des métadonnées XMP après redimensionnement, conversion JPEG et recompression ; vérification d'un échantillon de production avec un outil C2PA ; revue du code de l'outil interne de signature.

### AIA-002 : Aucun marquage lisible par machine des textes générés par le tuteur et la correction assistée
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel ; SYS-02 Correction assistée
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Faible (qualification : application de l'art. 50, par. 2 aux textes conversationnels `[AV]`)
- **Preuve observée** : *Fait observé.* `answer()` renvoie le texte brut du modèle (`response.content[0].text`) ; la justification de `propose_grade()` est stockée telle quelle ; aucun marquage ni métadonnée de provenance. L'analyse interne indique « contenus textuels, à analyser au regard des lignes directrices de la Commission » sans position arrêtée.
- **Fichier(s) et lignes** : `app/tutor_chat.py:24-32` ; `app/grading.py:42-47` ; `docs/classification-assessment.md:21-22`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA (EduAssist)
- **Classification du système** : SYS-01 non à haut risque (motivé) ; SYS-02 haut risque probable
- **Référence juridique** : Art. 50, par. 2 `[TI]` ; délai transitoire `[O26]` (à confirmer sur le JO) ; modalités pour le texte : lignes directrices de la Commission du 20.7.2026 `[AV]`
- **Date d'application** : 2026-12-02 pour les systèmes mis sur le marché avant le 2026-08-02 ; **non encore applicable** au 2026-10-27 (échéance dans 36 jours) (CAL-010, confiance moyenne)
- **Conditions et exceptions** : Exception « assistance à la mise en forme standard » écartée. Le fait que les textes du tuteur soient lus dans une interface identifiée comme IA ne dispense pas, en soi, du marquage lisible par machine ; la portée exacte pour les textes conversationnels dépend des lignes directrices `[AV]`.
- **Explication** : Le règlement demande aux fournisseurs de systèmes qui génèrent du texte de marquer ces sorties de manière lisible par machine. Pour les systèmes mis sur le marché avant le 2 août 2026, ce délai court jusqu'au 2 décembre 2026. EduAssist n'a pas encore arrêté sa position ; il ne s'agit pas d'un manquement à la date d'audit.
- **Recommandation** (obligation future, art. 50, par. 2) : arrêter et documenter avant le 2026-12-02 une position au regard des lignes directrices ; selon celle-ci, ajouter des métadonnées de provenance aux réponses exposées par API ou exportées (champ structuré, en-tête, métadonnées de document), et documenter le moyen de détection.
- **Méthode de vérification** : note de position datée ; tests montrant la présence du marquage dans les réponses de l'API et les exports.

### AIA-003 : Performances et biais par sous-groupes non évalués pour un système de notation en production
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits, documentés par l'éditeur) / Moyenne (qualification)
- **Preuve observée** : *Fait observé.* La documentation technique indique : écart moyen de 1,4 point sur 20 et écart supérieur à 3 points sur 7 % des copies (400 copies, septembre 2026) ; « performances non mesurées sur les copies manuscrites numérisées et sur les élèves allophones ; risque de biais lié au style rédactionnel non évalué ». Le registre des risques prévoit l'évaluation des biais (R-03) au T1 2027. Le système est en production depuis le 2026-03-01.
- **Fichier(s) et lignes** : `docs/technical-documentation.md:15-19` ; `docs/risk-register.md:7` ; `docs/classification-assessment.md:39`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA ; déployeurs (surveillance du fonctionnement, futur art. 26, par. 5)
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 9, 10 et 15 `[TI]` (exigences du haut risque) ; art. 10, par. 5 modifié `[AV]` ; [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689)
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable) ; conditionnel pour un système antérieur (CAL-013)
- **Conditions et exceptions** : La validation humaine obligatoire atténue le risque mais ne le supprime pas (biais d'automatisation). L'art. 10, par. 5 (traitement de données sensibles pour la détection des biais) est soumis à un critère de stricte nécessité `[AV]`.
- **Explication** : *Fait.* L'éditeur reconnaît que la qualité des notes proposées n'est pas mesurée pour certains groupes d'élèves. *Analyse.* Les exigences de gestion des risques, de gouvernance des données et d'exactitude ne seront applicables qu'à partir de décembre 2027, mais le risque d'un traitement moins favorable de certains élèves existe déjà, puisque le système est utilisé.
- **Recommandation** (préparation des art. 9, 10, 15 ; bonne pratique immédiate) : avancer l'évaluation par sous-groupes (allophones, copies manuscrites, styles rédactionnels, élèves en situation de handicap) ; fixer des seuils d'acceptation ; informer les enseignants de ces limites dans l'interface et le guide ; envisager de désactiver la proposition pour les catégories non évaluées.
- **Méthode de vérification** : rapport d'évaluation par sous-groupes, seuils documentés, avertissement visible dans l'interface.

### AIA-004 : Copie transmise au modèle sans défense contre l'injection d'instructions ; sortie du modèle non validée
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (effet réel)
- **Preuve observée** : *Fait observé.* Le texte de la dissertation, rédigé par l'élève, est passé tel quel comme unique message utilisateur, sans délimitation ni consigne de traitement comme donnée non fiable. La réponse est désérialisée par `json.loads` sans contrôle de schéma, de bornes (note entre 0 et 20) ni de cohérence entre critères et note. Le registre des risques (R-01 à R-06) ne mentionne ni l'injection d'instructions ni les sorties malformées.
- **Fichier(s) et lignes** : `app/grading.py:34-47` ; `docs/risk-register.md:3-10`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 15 (robustesse, cybersécurité, exemples contradictoires) et art. 9 (gestion des risques, mauvaise utilisation raisonnablement prévisible) `[TI]`
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable) ; conditionnel (CAL-013)
- **Conditions et exceptions** : La validation par l'enseignant constitue une mesure d'atténuation ; son efficacité dépend de la lecture effective de la copie (non observable).
- **Explication** : Un élève peut insérer dans sa copie des instructions destinées au modèle (par exemple demander une note maximale). Sans défense, la proposition peut être manipulée, et l'enseignant, s'il se fie à la proposition, peut valider une note injustifiée. Les obligations correspondantes ne sont pas encore applicables, mais le risque existe dès maintenant.
- **Recommandation** (préparation des art. 9 et 15 ; bonne pratique de sécurité immédiate) : délimiter la copie comme donnée et instruire le modèle de ne pas suivre d'instructions qu'elle contient ; détecter et signaler à l'enseignant les tentatives d'injection ; valider la sortie (schéma, bornes, somme des critères) et rejeter les réponses non conformes ; ajouter ces risques au registre ; inclure des tests adverses dans la campagne d'évaluation.
- **Méthode de vérification** : jeu de tests adverses (copies contenant des instructions) avec résultats ; tests unitaires de validation de la sortie ; registre des risques mis à jour.

### AIA-005 : Traçabilité de la correction assistée incomplète (justification non journalisée, rétention non implémentée, intégrité non garantie)
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification `[O26]` pour la date)
- **Preuve observée** : *Fait observé.* Mesures présentes : journal JSONL avec `trace_id`, horodatage, `model_version`, `prompt_version`, note proposée, identifiant de l'enseignant, décision, note finale et motif ; corrélation proposition-révision assurée par le `trace_id` transmis. Lacunes : la justification et les critères présentés à l'enseignant ne sont pas journalisés ; aucune empreinte de la copie ; paramètres (température, `max_tokens`) non journalisés (fixés dans le code) ; `publish_grade()` ne journalise pas la publication ; la constante `AUDIT_LOG_RETENTION_DAYS = 400` n'est utilisée nulle part (aucune purge ni politique de conservation implémentée dans le dépôt) ; le caractère « append-only » repose sur une simple ouverture en mode ajout d'un chemin relatif (`var/audit_log.jsonl`), sans contrôle d'intégrité.
- **Fichier(s) et lignes** : `app/audit_log.py:7-16` ; `app/grading.py:51-54, 65-66` ; `app/gradebook.py:5-8` ; `app/config.py:8` ; `docs/technical-documentation.md:25-26`
- **Rôle réglementaire concerné** : Fournisseur (art. 12, 19) ; déployeurs (art. 26, par. 6)
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 12, art. 19, art. 26, par. 6 `[TI]` ; art. 86 (droit à l'explication), date effective `[AV]`
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable) ; art. 86 : à vérifier
- **Conditions et exceptions** : Durée minimale de six mois (art. 19, art. 26, par. 6) : la durée déclarée de 400 jours la dépasse, sa mise en œuvre n'est pas observable.
- **Explication** : La journalisation existante est solide sur les versions et les décisions humaines. En revanche, on ne peut pas reconstituer après coup ce que l'enseignant a vu (justification, critères) ni prouver l'intégrité du journal, ce qui sera utile pour expliquer une note contestée et pour la future obligation de journalisation.
- **Recommandation** (préparation des art. 12, 19, 86) : journaliser la justification, les critères, une empreinte de la copie et les paramètres d'appel ; journaliser la publication dans `publish_grade` ; implémenter la rétention de 400 jours et protéger l'intégrité (stockage WORM ou chaînage d'empreintes, droits d'accès).
- **Méthode de vérification** : exemple d'enregistrement de journal anonymisé ; test de purge ; configuration du stockage de production.

### AIA-006 : Exigences du haut risque partiellement préparées pour la correction assistée (notice, SGQ, évaluation de la conformité, information des élèves)
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (date `[O26]`)
- **Preuve observée** : *Fait observé.* La feuille de route interne indique : gestion des risques « registre initial », documentation technique « ébauche », journalisation « en place », notice d'utilisation « à rédiger », supervision humaine « procédure en place », exactitude et robustesse « campagne prévue T1 2027 », SGQ « à établir », évaluation de la conformité, déclaration UE, marquage CE et enregistrement « à planifier ». Aucun texte d'information des élèves et familles n'est présent (interface absente).
- **Fichier(s) et lignes** : `docs/classification-assessment.md:30-41` ; `docs/technical-documentation.md:1-26`
- **Rôle réglementaire concerné** : Fournisseur (art. 9 à 17, 43, 47 à 49) ; déployeurs (art. 26, par. 11 ; art. 27 pour les organismes de droit public)
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 9, 11, 13, 15, 16, 17, 43, 47, 48, 49 ; art. 26, par. 11 ; art. 27 `[TI]` ; date `[O26]` ; art. 49, 72, 73 : date effective `[AV]`
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable, 401 jours) ; conditionnel pour un système antérieur (CAL-013)
- **Conditions et exceptions** : Contrôle interne (annexe VI) pour la plupart des systèmes de l'annexe III, point 3 ; forme simplifiée de la documentation pour les PME (art. 11, par. 1), statut PME non communiqué ; régime de l'art. 111, par. 2 à qualifier (AIA-007).
- **Explication** : L'éditeur a bien identifié les exigences et a commencé à les préparer. Plusieurs chantiers longs (système de gestion de la qualité, notice, évaluation de la conformité) restent à lancer ; ils demandent plusieurs mois. Aucun manquement n'existe à la date d'audit.
- **Recommandation** (préparation d'obligations futures) : planifier avec jalons datés la notice d'utilisation (art. 13), le SGQ (art. 17), la documentation de l'annexe IV complète, l'évaluation de la conformité et l'enregistrement ; outiller les déployeurs pour l'information des élèves (art. 26, par. 11) et, pour les établissements publics, l'analyse d'impact (art. 27).
- **Méthode de vérification** : plan daté, versions successives des documents, notice publiée, texte d'information des élèves.

### AIA-007 : Effet de l'article 111, paragraphe 2 sur la correction assistée et cas des établissements publics à qualifier
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Moyenne
- **Niveau de confiance** : Faible (référence `[AV]`, sources divergentes)
- **Preuve observée** : *Fait observé.* Mise sur le marché déclarée le 2026-03-01, antérieure à la date d'application du chapitre III ; l'éditeur signale lui-même ce point comme ouvert (« Validation juridique demandée »). Le statut public ou privé des établissements clients n'est pas indiqué. Les identifiants de modèle sont configurables et la grille en est à sa version 3, ce qui suppose des évolutions de conception futures.
- **Fichier(s) et lignes** : `docs/classification-assessment.md:3, 13-14` ; `README.md:10-11` ; `app/config.py:5-7`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs publics
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 111, par. 2 modifié `[AV]` ; art. 27 `[TI]` ; considérant 39 du règlement 2026/1744 (appréciation au niveau du type et du modèle, selon les sources) `[AV]`
- **Date d'application** : Conditionnel (CAL-013, confiance faible) : soumis au règlement seulement en cas de modification importante de la conception après le 2027-12-02 ; systèmes destinés aux autorités publiques : au plus tard le 2030-08-02 (divergence : 2028-01-28 selon une source)
- **Conditions et exceptions** : La notion de « modification importante de la conception » (changement de modèle sous-jacent, de grille, de logique de décision) doit être analysée ; une mise sur le marché postérieure (nouvelle version ou nouveau type) ferait perdre le bénéfice du régime.
- **Explication** : Selon l'interprétation retenue et la nature des clients, la correction assistée pourrait devoir respecter les exigences du haut risque en décembre 2027, plus tard, ou seulement en cas de modification importante. Cette question conditionne le calendrier de préparation et ne peut être tranchée par l'analyse du code.
- **Recommandation** (vérification juridique) : obtenir l'analyse juridique demandée sur la base du texte officiel au JO ; recenser les clients publics ; définir des critères internes de « modification importante » intégrés à la gestion des modifications. Ne pas différer la préparation (AIA-006) dans l'attente de cette analyse.
- **Méthode de vérification** : note juridique datée ; liste des clients par statut ; procédure de gestion des modifications.

### AIA-008 : Aucun garde-fou observable dans le code contre la génération d'images intimes non consenties ou pédopornographiques
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Faible (qualification : portée pour les fournisseurs de systèmes génératifs `[AV]`)
- **Preuve observée** : *Fait observé.* Le prompt saisi par l'enseignant est transmis directement au service tiers, sans filtre ni contrôle de sortie. Le registre des risques mentionne un « filtre de prompts » en place (R-05), qui n'est pas présent dans le dépôt (peut-être chez le service tiers ou en production).
- **Fichier(s) et lignes** : `app/illustrations.py:20-21` ; `app/image_provider.py:5-6` ; `docs/risk-register.md:9`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA ; déployeurs
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : Art. 5, par. 1, nouveaux points introduits par le règlement 2026/1744 `[O26]` (numérotation `[AV]`) ; [AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)
- **Date d'application** : 2026-12-02 (CAL-004, confiance moyenne) ; **non encore applicable** au 2026-10-27 (36 jours)
- **Conditions et exceptions** : L'interdiction viserait les systèmes générant des contenus réalistes intimes de personnes identifiables sans consentement et le matériel pédopornographique ; elle pourrait concerner les fournisseurs de systèmes génératifs sans garde-fous raisonnables `[AV]`. Contexte d'usage (enseignants, supports pédagogiques) et filtres probables du service tiers : la plausibilité d'un usage abusif est faible, ce qui justifie une gravité Moyenne malgré l'enjeu.
- **Explication** : À partir du 2 décembre 2026, de nouvelles pratiques seront interdites. Le dépôt ne permet pas de savoir quels garde-fous existent réellement ; ils sont déclarés mais non observables.
- **Recommandation** (préparation de l'obligation) : avant le 2026-12-02, documenter les filtres du service tiers (conditions contractuelles, politique d'usage), implémenter ou localiser le filtre de prompts R-05, ajouter un contrôle des sorties, un mécanisme de signalement et une politique d'usage acceptable pour les enseignants.
- **Méthode de vérification** : documentation contractuelle du service tiers ; code du filtre ; tests de refus sur un jeu de prompts interdits.

### AIA-009 : Garde-fou de validation humaine contournable et peu robuste
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Risque potentiel
- **Gravité** : Faible
- **Niveau de confiance** : Élevée (faits) / Moyenne (effet réel : authentification hors dépôt)
- **Preuve observée** : *Fait observé.* `publish_grade()` exige seulement une chaîne `validated_by` non vide, sans vérifier l'identité ni le rôle de l'enseignant, et peut être appelée directement sans passer par `review_grade()` (aucune journalisation dans ce cas). Une décision `override` avec motif mais sans `final_grade` publie une note `None`. Aucune validation de bornes de la note finale. Aucun drapeau de désactivation du système n'est observable.
- **Fichier(s) et lignes** : `app/gradebook.py:5-8` ; `app/grading.py:58-68`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs (art. 26, par. 2)
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 14, par. 4, d) et e) ; art. 26, par. 2 `[TI]`
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable)
- **Conditions et exceptions** : L'authentification et les contrôles d'accès peuvent exister dans une couche API non fournie.
- **Explication** : Le principe « aucune note sans validation humaine » est bien implémenté, mais le contrôle repose sur la bonne foi du code appelant. Un défaut d'intégration pourrait publier une note sans véritable validation ou une note vide.
- **Recommandation** (préparation de l'art. 14 ; bonne pratique immédiate) : rendre la publication accessible uniquement via le circuit de révision ; vérifier l'identité et le rôle de l'enseignant authentifié ; exiger une note finale valide (0 à 20) pour `override` ; journaliser toute publication ; prévoir un interrupteur de désactivation par établissement.
- **Méthode de vérification** : tests unitaires (publication sans révision refusée, override sans note refusé) ; revue des contrôles d'accès de l'API.

### AIA-010 : Identifiants de modèle par défaut non épinglés à une version datée
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel ; SYS-02 Correction assistée
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Faible
- **Niveau de confiance** : Élevée (faits) / Moyenne (caractère d'alias, à confirmer auprès du fournisseur)
- **Preuve observée** : *Fait observé.* Valeur par défaut `claude-sonnet-4-5`, sans suffixe de version datée, surchargeable par variable d'environnement ; selon la convention de nommage du fournisseur, ce type d'identifiant est susceptible de désigner un alias pouvant pointer vers des instantanés successifs. Mesure positive : la version effectivement servie (`response.model`) est journalisée ; le risque R-06 est noté « partiel ».
- **Fichier(s) et lignes** : `app/config.py:5-6` ; `app/grading.py:48, 52` ; `app/tutor_chat.py:31` ; `docs/risk-register.md:10`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA
- **Classification du système** : SYS-01 non à haut risque ; SYS-02 haut risque probable
- **Référence juridique** : Aucune (bonne pratique) ; utile pour l'annexe IV, points 1 et 6, et pour l'analyse de la « modification importante » (art. 111, par. 2 `[AV]`)
- **Date d'application** : n.a. (bonne pratique) ; lien avec CAL-011 et CAL-013
- **Conditions et exceptions** : Les valeurs de production peuvent être épinglées (non observable).
- **Explication** : Si le fournisseur fait évoluer le modèle désigné par l'alias, le comportement de la correction peut changer sans nouvelle campagne d'évaluation, contrairement à la politique déclarée de gestion des modifications.
- **Recommandation** (bonne pratique) : épingler un instantané daté pour SYS-02 (et SYS-01) ; conditionner tout changement à la campagne d'évaluation prévue ; alerter en cas d'écart entre la version demandée et `response.model`.
- **Méthode de vérification** : configuration de production ; alerte sur l'écart de version ; entrée de CHANGELOG associée à chaque changement.

### AIA-011 : Étiquetage des hypertrucages par les enseignants : consigne déclarée, étiquette visible non apposée par le code
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne
- **Preuve observée** : *Fait observé.* La docstring annonce une « mention visible “Image générée par IA” sur les supports publiés », mais le code n'inscrit ce libellé que dans les métadonnées (`ai_disclosure`) et ne l'appose pas sur l'image ; aucune fonction d'étiquetage visible n'est observable. L'analyse interne indique que les enseignants sont informés de l'obligation d'étiqueter tout hypertrucage via le guide utilisateur (non inclus).
- **Fichier(s) et lignes** : `app/illustrations.py:5, 16, 24` ; `docs/classification-assessment.md:27-28` ; `docs/risk-register.md:9`
- **Rôle réglementaire concerné** : Déployeurs (débiteurs de l'obligation) ; fournisseur (outillage)
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : Art. 50, par. 4, al. 1 et par. 5 `[TI]`
- **Date d'application** : 2026-08-02, en vigueur (CAL-009, confiance élevée)
- **Conditions et exceptions** : Ne vise que les contenus ressemblant à des personnes, lieux ou événements réels pouvant passer pour authentiques ; régime allégé pour les œuvres manifestement artistiques ou créatives (non documenté).
- **Explication** : L'obligation de signaler un hypertrucage pèse sur l'établissement qui diffuse l'image, mais le fournisseur peut l'y aider. Le dépôt ne permet pas de vérifier ni la consigne remise aux enseignants ni l'apposition d'une mention visible, annoncée dans le code mais non réalisée.
- **Recommandation** (outillage d'une obligation du déployeur ; bonne pratique pour le fournisseur) : proposer une option d'étiquette visible apposée sur l'image ou dans le support ; aligner la docstring sur le comportement réel ; fournir le guide utilisateur comme preuve.
- **Méthode de vérification** : guide utilisateur ; capture d'un support publié ; test vérifiant l'étiquette visible.

### AIA-012 : Mesures de maîtrise de l'IA documentées ; mise en œuvre non vérifiable dans le dépôt
- **Système d'IA concerné** : Tous (SYS-01, SYS-02, SYS-03)
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne (rédaction de l'art. 4 `[O26]`)
- **Preuve observée** : *Fait observé.* Plan de maîtrise de l'IA : formation annuelle du personnel (fonctionnement, limites, biais, réglementation) avec registre tenu par les RH hors dépôt ; module de 2 heures pour les enseignants avant activation de la correction assistée ; mise à jour du 2026-09-01. Avertissements d'usage présents dans le code du tuteur.
- **Fichier(s) et lignes** : `docs/ai-literacy-plan.md:3-7` ; `docs/human-oversight-procedure.md:13` ; `app/tutor_chat.py:9-12`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs (pour leur propre personnel)
- **Classification du système** : Tous niveaux
- **Référence juridique** : Art. 4 `[TI]`, rédaction modifiée par le règlement 2026/1744 `[O26]` (à confirmer sur le JO)
- **Date d'application** : En vigueur depuis le 2025-02-02 ; nouvelle rédaction présumée depuis le 2026-07-27 (CAL-002, CAL-003)
- **Conditions et exceptions** : La nouvelle rédaction impose de prendre des mesures sans exiger un niveau déterminé `[O26]`. Prestataires agissant pour le compte d'EduAssist : non mentionnés.
- **Explication** : Un plan existe ; sa mise en œuvre (formations suivies, contenus) relève de documents organisationnels non fournis. Leur absence dans le dépôt n'est pas une preuve de manquement.
- **Recommandation** (obligation, art. 4) : conserver les preuves (registre RH, supports) ; étendre le plan aux prestataires ; adapter les contenus aux limites connues (AIA-003, AIA-004).
- **Méthode de vérification** : registre de formation, supports de formation, liste des prestataires couverts.

### AIA-013 : Information sur l'interaction avec une IA prévue par le tuteur ; affichage et accessibilité non observables
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel
- **Nature du constat** : Constat technique avéré
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits) / Moyenne (effectivité)
- **Preuve observée** : *Fait observé.* `start_session()` renvoie, « avant la première interaction », le message : « Vous échangez avec un assistant d'IA (et non avec un enseignant). Ses réponses peuvent contenir des erreurs : vérifiez-les avec votre cours. » Le prompt système impose de répondre clairement être une IA si la question est posée.
- **Fichier(s) et lignes** : `app/tutor_chat.py:9-21`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : Art. 50, par. 1 et 5 `[TI]` ; [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)
- **Date d'application** : 2026-08-02, en vigueur (CAL-009)
- **Conditions et exceptions** : Exception « évident » non invoquée (et inutile au vu de la mesure).
- **Explication** : La mesure attendue est présente dans le code. Il reste à vérifier que le message est effectivement affiché avant toute question, sur tous les canaux (web, mobile, API éventuellement exposée), de façon claire et accessible, et que `answer()` ne peut pas être appelé sans ouverture de session.
- **Recommandation** (vérification d'une obligation en vigueur) : conserver une preuve d'affichage (capture, test d'interface) et un test garantissant l'appel de `start_session()` avant `answer()` ; vérifier l'accessibilité (lecteurs d'écran, contraste).
- **Méthode de vérification** : captures d'écran par canal ; test d'intégration ; audit d'accessibilité.

### AIA-014 : Supervision humaine de la correction assistée intégrée dès la conception
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Constat technique avéré
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** : *Fait observé.* Proposition en statut `pending_review` ; décisions `approve`, `override` (motif obligatoire) et `reject` ; publication refusée sans `validated_by` ; journalisation de chaque décision ; justification et critères renvoyés à l'enseignant ; température 0 et version de grille journalisée ; procédure écrite avec avertissement « Proposition générée par IA, à vérifier » et revue trimestrielle des écarts ; classification motivée par l'éditeur (dérogation de l'art. 6, par. 3 écartée), concordante avec la présente analyse.
- **Fichier(s) et lignes** : `app/grading.py:20-30, 37, 58-68` ; `app/gradebook.py:5-8` ; `docs/human-oversight-procedure.md:1-13` ; `docs/classification-assessment.md:5-14`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 14, par. 4, a) à d) ; art. 26, par. 2 `[TI]`
- **Date d'application** : 2027-12-02 (CAL-011, non encore applicable)
- **Conditions et exceptions** : L'avertissement de l'interface et le module de formation sont décrits mais non observables. Robustesse du dispositif : voir AIA-009.
- **Explication** : Ces mesures vont dans le sens des futures exigences de contrôle humain. Elles ne démontrent pas à elles seules la conformité.
- **Recommandation** : maintenir ces mesures ; mesurer le taux de modification par les enseignants (indicateur de biais d'automatisation) ; corriger les points d'AIA-009.
- **Méthode de vérification** : statistiques de la revue trimestrielle ; captures de l'interface de révision.

### AIA-015 : Obligations des fournisseurs de modèles d'IA à usage général non applicables à EduAssist
- **Système d'IA concerné** : Tous (SYS-01, SYS-02, SYS-03)
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits observables) / Moyenne (contrats non consultés)
- **Preuve observée** : *Fait observé.* Modèles appelés via l'API d'Anthropic et d'un service d'images tiers ; aucun script d'entraînement ou d'affinage, aucune bibliothèque d'apprentissage dans `requirements.txt`, aucune publication de poids ; déclaration explicite de l'éditeur.
- **Fichier(s) et lignes** : `requirements.txt:1-3` ; `README.md:13` ; `docs/ai-system-inventory.md:11-12`
- **Rôle réglementaire concerné** : Fournisseur de système d'IA (fournisseur en aval, art. 3, point 68), et non fournisseur de modèle GPAI
- **Classification du système** : Sans objet
- **Référence juridique** : Art. 3, points 63 et 68 ; art. 53 à 55 `[TI]`
- **Date d'application** : Obligations GPAI en vigueur depuis le 2025-08-02 (CAL-005), sans objet pour EduAssist
- **Conditions et exceptions** : Le constat deviendrait caduc en cas d'affinage significatif ou de mise sur le marché d'un modèle `[AV]`.
- **Explication** : Les obligations des fournisseurs de modèles pèsent sur Anthropic et sur le fournisseur du service d'images, pas sur EduAssist, qui reste responsable de ses propres systèmes.
- **Recommandation** (bonne pratique) : conserver la documentation transmise par les fournisseurs de modèles (annexe XII) et leurs conditions d'utilisation ; réexaminer ce constat avant tout projet d'affinage.
- **Méthode de vérification** : contrats et documentation des fournisseurs ; absence de scripts d'entraînement lors des audits suivants.

### AIA-016 : Aucune reconnaissance des émotions ni surveillance d'examen par IA observée
- **Système d'IA concerné** : Module d'événements d'examen (écarté, pas un système d'IA) ; tous les systèmes pour l'art. 5
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée (code) / Moyenne (suppression de la webcam non vérifiable sans historique)
- **Preuve observée** : *Fait observé.* `exam_events.py` se borne à journaliser des événements techniques (perte de focus, déconnexion) transmis aux surveillants humains ; aucune bibliothèque de vision, de biométrie ou d'analyse émotionnelle dans le dépôt ; le README déclare la suppression de la surveillance par webcam.
- **Fichier(s) et lignes** : `app/exam_events.py:1-10` ; `README.md:14, 23` ; `requirements.txt:1-3`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs
- **Classification du système** : Pas un système d'IA (motivé) pour `exam_events.py`
- **Référence juridique** : Art. 5, par. 1, f) `[TI]` ; annexe III, point 3, d) et point 1 `[TI]` ; art. 3, point 1
- **Date d'application** : Art. 5 en vigueur depuis le 2025-02-02 (CAL-002)
- **Conditions et exceptions** : Une réintroduction d'une détection automatisée de comportements pendant les examens relèverait de l'annexe III, point 3, d), et toute inférence d'émotions de l'art. 5, par. 1, f).
- **Explication** : Le projet ne contient pas de pratique d'IA interdite dans l'enseignement ni de surveillance d'examen par IA. Le module d'examen est une simple journalisation.
- **Recommandation** : documenter la date de retrait de l'ancienne fonctionnalité et prévoir une revue AI Act avant toute automatisation de l'analyse des événements d'examen (bonne pratique).
- **Méthode de vérification** : historique Git ou CHANGELOG du retrait ; revue lors des audits suivants.

---

## 9. Registre des éléments non vérifiables

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact sur la classification ou les obligations | Interlocuteur suggéré | Constat(s) liés |
|---|---|---|---|---|---|---|---|
| NV-01 | SYS-01, SYS-02, SYS-03 | Interface utilisateur et couche API (routes FastAPI absentes) | Document / information | Vérifier l'affichage effectif de l'information, de l'avertissement enseignant, des étiquettes, l'accessibilité | Art. 50, par. 1, 4, 5 ; art. 14 (futur) | Équipe produit | AIA-009, AIA-011, AIA-013, AIA-014 |
| NV-02 | SYS-03 | Identité, contrat et conditions du service tiers de génération d'images ; marquages et filtres qu'il applique | Information / document | Identifier le fournisseur du modèle, ses marquages amont et ses garde-fous | Art. 50, par. 2 ; art. 5 nouveaux points | Achats, juridique | AIA-001, AIA-008, AIA-015 |
| NV-03 | SYS-03 | Outil interne de signature C2PA, tests de robustesse, outil de détection | Document / code | Le dépôt contient un bouchon | Art. 50, par. 2 (en vigueur) | Équipe technique | AIA-001 |
| NV-04 | SYS-02 | Statut public ou privé des établissements clients et pays | Information | Échéance de l'art. 111, par. 2 ; analyse d'impact de l'art. 27 | Calendrier du haut risque | Direction commerciale | AIA-006, AIA-007 |
| NV-05 | SYS-02 | Validation juridique externe de la classification et de l'art. 111, par. 2 | Juridique | Analyse interne « non validée par un conseil juridique externe » | Classification, calendrier | Conseil juridique | AIA-007 |
| NV-06 | SYS-01, SYS-02 | Historique des versions (modèle, grilles v1 à v3) depuis le 2026-03-01 et CHANGELOG interne | Document | Apprécier les modifications et la date de mise sur le marché par type et modèle | Art. 111, par. 2 ; annexe IV, point 6 | Équipe technique | AIA-007, AIA-010 |
| NV-07 | SYS-02 | Rapport de la campagne d'évaluation de septembre 2026 (protocole, résultats détaillés) | Document | Étayer les performances déclarées | Art. 9, 15 (futur) | Équipe data | AIA-003 |
| NV-08 | Tous | Registre de formation RH, supports de formation, guide utilisateur | Document | Preuve des mesures de maîtrise de l'IA et des consignes d'étiquetage | Art. 4 ; art. 50, par. 4 | RH, équipe produit | AIA-011, AIA-012 |
| NV-09 | SYS-01, SYS-02 | Configuration de production (valeurs de `EDUASSIST_*_MODEL`, emplacement, protection et purge du journal) | Information | Épinglage, conservation, intégrité | Art. 12, 19 (futur) | Exploitation | AIA-005, AIA-010 |
| NV-10 | SYS-03 | Localisation et fonctionnement du filtre de prompts déclaré (R-05) | Information / code | Garde-fous contre les nouvelles interdictions et les hypertrucages | Art. 5 nouveaux points (2026-12-02) | Équipe technique | AIA-008 |
| NV-11 | SYS-01 | Mécanisme de signalement par l'élève (R-04) ; absence de réutilisation des conversations pour évaluer ou orienter dans d'autres composants | Information | Confirmer la classification non à haut risque | Annexe III, point 3, b) | Équipe produit | AIA-013 |
| NV-12 | SYS-01, SYS-02 | Position au regard des lignes directrices de la Commission sur l'art. 50 (20.7.2026) pour les textes | Juridique | Portée de l'art. 50, par. 2 pour les textes `[AV]` | Obligation au 2026-12-02 | Conseil juridique | AIA-002 |
| NV-13 | Tous | Statut PME ou petite entreprise de taille intermédiaire d'EduAssist | Information | Allègements éventuels (forme simplifiée de l'annexe IV `[AV]`) | Effort de préparation | Direction | AIA-006 |
| NV-14 | Module d'événements d'examen (écarté) | Historique de suppression de la télésurveillance par webcam (absence de `.git`) | Document | Confirmer l'absence d'usage passé ou résiduel | Art. 5, par. 1, f) | Équipe technique | AIA-016 |

---

## 10. Plan de remédiation synthétique

Priorisation selon `findings-methodology.md`, section 6. Aucune action P1 (aucun constat Critique ou
Élevé portant sur une obligation en vigueur).

| Priorité | Constat(s) | Action | Base | Échéance réglementaire | Effort | Responsable suggéré | Preuve de clôture attendue |
|---|---|---|---|---|---|---|---|
| P2 | AIA-001 | Marquage multicouche des images (XMP standard, C2PA signé et bloquant, filigrane), préservation des marquages amont, tests de robustesse, moyen de détection | Obligation, art. 50, par. 2 | En vigueur depuis le 2026-08-02 | M | Équipe technique | Tests de robustesse, échantillon vérifié |
| P2 | AIA-002 | Position documentée sur le marquage des textes et mise en œuvre | Obligation, art. 50, par. 2 `[O26]`/`[AV]` | 2026-12-02 | S à M | Juridique et technique | Note de position, tests |
| P2 | AIA-008 | Documenter les filtres du service tiers, implémenter le filtre R-05, contrôle de sortie, politique d'usage | Obligation future, art. 5 nouveaux points `[O26]` | 2026-12-02 | M | Technique, achats | Code du filtre, tests de refus, contrat |
| P2 | AIA-003 | Évaluation par sous-groupes avancée, seuils, avertissements aux enseignants | Préparation art. 9, 10, 15 ; risque actuel | 2027-12-02 (CAL-011) | M | Équipe data | Rapport par sous-groupes |
| P2 | AIA-004 | Défense contre l'injection d'instructions, validation de la sortie, tests adverses, registre mis à jour | Préparation art. 9, 15 ; bonne pratique de sécurité | 2027-12-02 (CAL-011) | S à M | Équipe technique | Tests adverses, registre |
| P2 | AIA-007 | Analyse juridique de l'art. 111, par. 2, recensement des clients publics, critères de modification importante | Vérification juridique `[AV]` | Conditionnel (CAL-013) | S | Juridique | Note juridique |
| P3 | AIA-005 | Journaliser justification, critères, empreinte, paramètres et publication ; rétention et intégrité | Préparation art. 12, 19, 86 | 2027-12-02 | S à M | Équipe technique | Exemple de journal, test de purge |
| P3 | AIA-006 | Plan daté : notice (art. 13), SGQ (art. 17), annexe IV, évaluation de la conformité, enregistrement ; outillage des déployeurs (art. 26, par. 11 ; art. 27) | Préparation d'obligations futures | 2027-12-02 | L | Conformité | Plan, notice, documents |
| P3 | AIA-009 | Publication uniquement via révision authentifiée, note finale obligatoire, journalisation, interrupteur | Préparation art. 14 ; bonne pratique | 2027-12-02 | S | Équipe technique | Tests unitaires |
| P3 | AIA-010 | Épinglage d'instantanés datés, alerte d'écart de version | Bonne pratique | n.a. | S | Exploitation | Configuration, alerte |
| P3 | AIA-011 | Option d'étiquette visible, alignement de la docstring, guide utilisateur | Outillage d'une obligation du déployeur (art. 50, par. 4) | En vigueur | S | Équipe produit | Guide, capture |
| P4 | AIA-012 | Conserver les preuves de formation, étendre aux prestataires | Obligation, art. 4 (vérification) | En vigueur | S | RH | Registre |
| P4 | AIA-013 | Preuve d'affichage et test d'ordre `start_session` / `answer`, audit d'accessibilité | Vérification, art. 50, par. 1 et 5 | En vigueur | S | Équipe produit | Captures, test |
| P4 | AIA-014, AIA-015, AIA-016 | Maintenir les mesures ; réexaminer en cas d'affinage ou de réintroduction d'une surveillance automatisée | Information | n.a. | S | Conformité | Revue lors du prochain audit |

**Jalons** :

| Date | Évènement réglementaire | Actions à terminer avant |
|---|---|---|
| Immédiat (en vigueur) | Art. 50, par. 2 pour SYS-03 ; art. 50, par. 1, 4, 5 ; art. 4 ; art. 5 | AIA-001, AIA-011, AIA-012, AIA-013 |
| 2026-12-02 | Art. 50, par. 2 pour les systèmes antérieurs (CAL-010) ; nouvelles interdictions de l'art. 5 (CAL-004) | AIA-002, AIA-008 |
| T1 2027 (interne) | Campagne d'évaluation annoncée | AIA-003, AIA-004 |
| 2027-12-02 | Exigences du haut risque, annexe III (CAL-011), sous réserve de l'art. 111, par. 2 (CAL-013) | AIA-005, AIA-006, AIA-009 |
| 2030-08-02 (confiance faible) | Art. 111, par. 2, systèmes destinés aux autorités publiques | Selon AIA-007 |

**Hypothèses** : efforts estimés à partir du dépôt seul, à recalibrer avec l'équipe ; échéances
issues du règlement 2026/1744 (confiance moyenne) à confirmer sur le JO.

---

## 11. Limites de l'audit

- **Audit statique** : comportement réel, données, prompts dynamiques, interface et configuration de
  production non observés ; le code n'a pas été exécuté. Les composants `image_provider` et
  `c2pa_signer` sont des bouchons, et aucune couche API n'est fournie.
- **Documents organisationnels non disponibles** : guide utilisateur, registre de formation RH,
  CHANGELOG interne, rapport de la campagne d'évaluation de septembre 2026, contrats avec Anthropic et
  avec le service d'images, liste des clients, analyse juridique externe.
- **Pas d'historique Git** : retrait de la télésurveillance et évolution des versions non vérifiables.
- **Références juridiques** : vérifiées le 2026-10-27 sans accès en ligne aux textes officiels
  (`legal-sources.md`, section 3). Entrées de confiance moyenne ou faible à confirmer sur le Journal
  officiel : CAL-003, CAL-004, CAL-010, CAL-011, CAL-012, CAL-013 (faible, divergence 2030-08-02 /
  2028-01-28), CAL-015, CAL-016 (faible). Modalités de l'art. 50, par. 2 pour les textes `[AV]` ;
  numérotation des nouvelles interdictions de l'art. 5 `[AV]`.
- **Évolutivité** : lignes directrices (art. 6 en projet, art. 50), normes harmonisées, actes
  d'exécution et codes de bonnes pratiques évolutifs.
- **Hors périmètre** : protection des données (identifiants d'élèves dans les journaux, transmission
  des copies à un fournisseur de modèle), accessibilité et autres législations auxquelles l'AI Act
  renvoie : signalées sans analyse.
- Ce rapport ne remplace ni l'avis d'un juriste ni une évaluation de la conformité au sens de
  l'article 43 ; il n'affirme en aucun cas que le projet est conforme à l'AI Act.

## 12. Suivi (ré-audit)

Sans objet : aucun rapport antérieur fourni. Lors du prochain audit, conserver les identifiants
AIA-001 à AIA-016 et recalculer le calendrier à la nouvelle date d'audit (en particulier : après le
2026-12-02, AIA-002 et AIA-008 deviennent des obligations en vigueur).
