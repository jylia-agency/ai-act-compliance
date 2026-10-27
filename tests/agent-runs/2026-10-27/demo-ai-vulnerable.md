# Rapport d'audit AI Act : EduAssist (`demo-ai-vulnerable`)

> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689.

| Paramètre | Valeur |
|---|---|
| Date d'audit | **2026-10-27** (toutes les applicabilités sont évaluées à cette date) |
| Périmètre | Racine du projet `demo-ai-vulnerable` : `README.md`, `requirements.txt`, `app/` (7 fichiers Python). Aucun dossier exclu. Pas de dépôt git (pas d'historique, de branche ni de commit observables). |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`meta.last_verified` de `data/ai-act-calendar.json`). Écart avec la date d'audit : 0 jour, pas de limite liée à l'ancienneté. Les textes officiels n'ont toutefois pas pu être relus en ligne lors de cette vérification (voir section 11). |
| Contexte fourni par le demandeur | Uniquement le contexte déclaré dans `README.md` (l. 6 à 23) : éditeur « EduAssist SAS », établie en France ; produit commercialisé sous la marque « EduAssist » auprès de lycées et d'universités de l'Union ; **mise sur le marché de la plateforme et de tous ses modules le 2026-03-01** ; établissements clients utilisant la plateforme pour leurs élèves et étudiants ; modèles via l'API d'OpenAI ; aucun entraînement de modèle. Statut PME et nature publique ou privée des clients : non fournis. |
| Méthode | Skill `ia-compliance` v1.0.0, lecture seule, sans exécution du code audité, sans réseau. Scripts utilisés : `scan_ai_signals.py`, `obligation_timeline.py`. |
| Audit précédent | Aucun |

---

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : 4.
  - SYS-01 : tuteur conversationnel (GPT-4o, OpenAI).
  - SYS-02 : correction automatique des dissertations (GPT-4o, OpenAI).
  - SYS-03 : génération d'illustrations de cours (DALL-E 3, OpenAI).
  - SYS-04 : surveillance d'examens en ligne par analyse des émotions faciales (DeepFace, modèle open source local).
- **Rôle d'EduAssist** : susceptible d'être **fournisseur** des quatre systèmes (art. 3, point 3), car elle les commercialise sous sa propre marque. Elle n'est pas, au vu du dépôt, fournisseur des modèles GPAI sous-jacents. Les établissements clients sont susceptibles d'être **déployeurs**.
- **Points les plus sensibles** :
  - **AIA-001 (Critique)** : SYS-04 infère les émotions des élèves (peur, colère, surprise) à partir de la webcam pendant les examens. Cela peut relever d'une **pratique interdite** (art. 5, par. 1, f)), applicable depuis le 2025-02-02. Aucune exception médicale ou de sécurité ne semble pouvoir être retenue.
  - **AIA-002 (Élevée)** : SYS-04 annule automatiquement l'examen, sans intervention humaine.
  - **AIA-003 (Élevée)** : le prompt système de SYS-01 impose au tuteur de **nier être une IA** et de se présenter comme une enseignante. C'est un manquement potentiel à l'art. 50, par. 1, en vigueur depuis le 2026-08-02.
  - **AIA-004 (Élevée)** : SYS-02 attribue la note finale, qui est publiée sans relecture et compte pour le passage en classe supérieure. Ce système est un haut risque probable (annexe III, point 3, b)), mais ses exigences ne sont pas encore applicables.
  - **AIA-005 (Élevée)** : une clé d'API est écrite en clair dans le code (valeur masquée).
- **Obligations en vigueur concernées** :
  - art. 4 (maîtrise de l'IA) ;
  - art. 5 (pratiques interdites, points a) à h)) ;
  - art. 50, par. 1, 3, 4 et 5.
- **Échéances à venir** :
  - **2026-12-02** (dans 36 jours) : art. 50, par. 2 (marquage des contenus synthétiques, délai pour les systèmes mis sur le marché avant le 2026-08-02) et nouvelles interdictions de l'art. 5 `[O26]` ;
  - **2027-12-02** : exigences du haut risque, annexe III `[O26]`. Le régime transitoire de l'art. 111, par. 2 est conditionnel `[AV]` : il s'appliquerait au plus tard le 2030-08-02 si les déployeurs sont des autorités publiques.
- **Principales incertitudes** :
  - statut public ou privé des établissements clients ;
  - modalités réelles des examens surveillés (à distance ou en établissement) ;
  - interface utilisateur absente du dépôt ;
  - nature des illustrations (personnes réelles ?) ;
  - présence éventuelle de marquages en amont dans les images d'OpenAI ;
  - dates issues du règlement 2026/1744 (confiance moyenne) et de l'art. 111, par. 2 (confiance faible).
- **Synthèse des constats** (16 constats) :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | | 2 (AIA-003, AIA-005) | | | |
| Risque potentiel | 1 (AIA-001) | 2 (AIA-002, AIA-004) | 1 (AIA-006) | | |
| À vérifier juridiquement ou organisationnellement | | | 2 (AIA-010, AIA-012) | | 1 (AIA-016) |
| Bonne pratique recommandée | | | | 1 (AIA-014) | |
| Non encore applicable | | | 4 (AIA-007, AIA-008, AIA-009, AIA-011) | 1 (AIA-013) | |
| Non applicable | | | | | 1 (AIA-015) |

---

## 2. Périmètre et méthode

**Arborescence analysée** (9 fichiers, tous lus intégralement) :

```
demo-ai-vulnerable/
├── README.md            contexte déclaré, liste des modules
├── requirements.txt     fastapi 0.115.0, openai 1.51.0, deepface 0.0.93, opencv-python 4.10.0.84
└── app/
    ├── __init__.py      vide
    ├── config.py        clé d'API (masquée), identifiants de modèles
    ├── tutor_chat.py    SYS-01
    ├── grading.py       SYS-02
    ├── gradebook.py     stockage des notes (déterministe)
    ├── illustrations.py SYS-03
    └── proctoring.py    SYS-04
```

**Outils.**
- `scan_ai_signals.py` a détecté des signaux dans quatre catégories :
  - API OpenAI (3 modules et le manifeste) ;
  - biométrie (`deepface`) ;
  - inférence d'émotions (`proctoring.py:9-10`) ;
  - génération d'images (`dall-e-3`, `images.generate`).

  Il a aussi relevé des identifiants de modèles, un contexte éducatif et un secret potentiel (`app/config.py:2`). Dans la synthèse du scanner, la ligne « emotion-inference » attribue des fichiers par agrégation : seules les lignes `proctoring.py:9-10` contiennent réellement ce signal.
- `obligation_timeline.py` a été lancé avec `--audit-date 2026-10-27 --placed-on-market 2026-03-01`, puis avec `--public-authority --scope high-risk-annex-iii`.
- Une recherche complémentaire de faux négatifs a été faite : appels HTTP directs, `endpoint`, `predict`, `inference`, journalisation, marqueurs C2PA/IPTC. Elle n'a rien trouvé de plus.

**Éléments non analysés ou absents.**
- Pas d'interface utilisateur ni de route web : FastAPI est déclaré dans `requirements.txt:1` mais aucune route n'est définie.
- Pas de tests, de configuration de déploiement, de documentation, de journaux ni de contrats.
- Les prompts dynamiques, les données réelles et le comportement en production n'ont pas été observés.

**Hypothèse de cadrage.** Le README (l. 3-4) présente le projet comme une fixture fictive (« Ne pas déployer »). Conformément à la consigne, l'audit retient le **contexte déclaré** (l. 6-12), c'est-à-dire une commercialisation depuis le 2026-03-01. Voir aussi la section 5 (art. 2, par. 8).

---

## 3. Systèmes d'IA identifiés et inventaire

### 3.1 Synthèse

| ID | Système | Finalité | Rôle(s) d'EduAssist | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|
| SYS-01 | Tuteur conversationnel | Répondre aux questions des élèves sur les cours | Fournisseur (susceptible) | `gpt-4o` (alias non épinglé), OpenAI | Non à haut risque (motivé). Soumis à l'art. 50, par. 1, 2 et 5, et à l'art. 4 | Moyenne |
| SYS-02 | Correction automatique | Attribuer la note finale des dissertations, publiée au bulletin | Fournisseur (susceptible) | `gpt-4o` (alias non épinglé), OpenAI | **Haut risque probable** (annexe III, point 3, b)) | Élevée (faits) / Moyenne (dates `[O26]`) |
| SYS-03 | Illustrations de cours | Générer des images pour les supports publiés aux élèves | Fournisseur (susceptible) | `dall-e-3`, OpenAI | Non à haut risque (motivé). Soumis à l'art. 50, par. 2 (fournisseur) et par. 4 (déployeur) | Élevée |
| SYS-04 | Surveillance d'examens en ligne | Détecter des comportements « suspects » pendant les examens et annuler les copies | Fournisseur (susceptible) | DeepFace 0.0.93 (analyse des émotions faciales, modèle open source exécuté localement) | **Pratique potentiellement interdite** (art. 5, par. 1, f)). À titre subsidiaire : haut risque probable (annexe III, point 3, d) et point 1, c)) | Élevée (faits) / Moyenne (qualification) |

### 3.2 Inventaire détaillé

| Champ | SYS-01 | SYS-02 | SYS-03 | SYS-04 |
|---|---|---|---|---|
| Nom | Tuteur conversationnel « Claire » | Correction automatique | Illustrations de cours | Surveillance d'examens en ligne |
| Finalité (art. 3, point 12) | Aide à l'apprentissage : répondre aux questions sur les cours (README:18) | Évaluation des acquis : note finale des dissertations, qui « compte pour le passage en classe supérieure » (grading.py:3-4, README:19) | Production de supports pédagogiques illustrés (README:20) | Surveillance des examens et annulation des copies « suspectes » (README:21) |
| Description fonctionnelle | Appel `chat.completions` avec une persona humaine imposée par le prompt système (tutor_chat.py:8-18) | Appel `chat.completions` avec la grille dans le prompt système, réponse JSON `{"note": x}`, publication immédiate (grading.py:18-29) | Appel `images.generate`, écriture des octets décodés dans un fichier (illustrations.py:12-15) | Analyse image par image de la vidéo webcam (OpenCV), émotion dominante via `DeepFace.analyze(actions=["emotion"])`, compteur, annulation au-delà de 30 images « suspectes » (proctoring.py:8-29) |
| Fichiers principaux | `app/tutor_chat.py`, `app/config.py` | `app/grading.py`, `app/gradebook.py`, `app/config.py` | `app/illustrations.py`, `app/config.py` | `app/proctoring.py` |
| Entrées | Message de l'élève et historique de conversation | Texte de la dissertation, identifiant de l'élève | Prompt textuel (auteur non précisé, probablement un enseignant) | Fichier vidéo webcam, identifiants de l'examen et de l'élève |
| Sorties et effets | Texte de réponse (information) | Note numérique **publiée automatiquement** au bulletin (**décision automatique**) | Image PNG (contenu synthétique) publiée aux élèves | Émotion dominante et scores ; **annulation automatique** de l'examen (**décision automatique**) |
| Utilisateurs | Élèves et étudiants | Établissements et enseignants (déclenchement non observé) | Enseignants et établissements (présumé) | Établissements (organisateurs d'examens) |
| Personnes concernées | Élèves, potentiellement mineurs (lycées) | Élèves et étudiants notés | Élèves destinataires des supports ; personnes éventuellement représentées | Élèves et étudiants filmés pendant l'examen |
| Données pertinentes | Messages libres pouvant contenir des données personnelles | Copies d'élèves, identifiant, note | Prompts | Images du visage (données biométriques au sens de l'art. 3, point 39), identifiants |
| Modèle(s) et version(s) | `gpt-4o` (alias mobile, config.py:3) | `gpt-4o` (alias mobile), `temperature=1.0` (grading.py:21) | `dall-e-3` (config.py:4) | Modèle d'émotions fourni par DeepFace 0.0.93 (requirements.txt:3), poids non documentés dans le dépôt |
| Fournisseur(s) de modèle / API tierces | OpenAI (SDK `openai==1.51.0`) | OpenAI | OpenAI | DeepFace (bibliothèque open source), OpenCV |
| Entraînement ou affinage par l'organisation | Non observé (README:12) | Non observé | Non observé | Non observé (modèle pré-entraîné tiers) |
| Composants associés | Aucun (pas de RAG, de base vectorielle ni d'outil d'agent) | `gradebook.publish_grade` (stockage en mémoire) | Aucun | `cancel_exam` (affichage console uniquement, proctoring.py:28-29) |
| Acteurs et rôles | EduAssist : fournisseur (susceptible). Établissements : déployeurs. OpenAI : fournisseur du modèle GPAI sous-jacent | Idem | Idem | EduAssist : fournisseur (susceptible). Établissements : déployeurs. Auteurs de DeepFace : fournisseurs du modèle (non GPAI : modèle spécialisé) |
| Mise sur le marché | 2026-03-01 (déclaré, README:10) | 2026-03-01 (déclaré) | 2026-03-01 (déclaré) | 2026-03-01 (déclaré) |
| Classification | Non à haut risque (motivé) | Haut risque probable (annexe III, point 3, b)) | Non à haut risque (motivé) | Pratique potentiellement interdite. Subsidiairement : haut risque probable (annexe III, point 3, d) ; point 1, c)) |
| Confiance de la classification | Moyenne | Élevée (faits) / Moyenne (dates) | Élevée | Élevée (faits) / Moyenne (qualification) |
| Statut | En production (déclaré) | En production (déclaré) | En production (déclaré) | En production (déclaré) |
| Informations manquantes | Interface et mentions d'information ; réutilisation éventuelle des échanges pour noter ou orienter | Interface enseignant, processus de validation dans l'établissement, statut public des clients | Contenu des illustrations (personnes ou événements réels ?), marquage amont d'OpenAI, circuit de publication | Lieu des examens (à distance ou en établissement), annulations déjà prononcées, statut des clients, provenance des poids DeepFace |

**Remarque sur le README.** La ligne 12 indique que les modèles utilisés sont ceux de l'API OpenAI. Elle est incomplète : SYS-04 repose sur un modèle local DeepFace (proctoring.py:3, requirements.txt:3).

### 3.3 Composants examinés et écartés

| Composant | Fichier | Motif |
|---|---|---|
| Stockage des notes | `app/gradebook.py:2-6` | Stockage déterministe en mémoire, sans inférence (art. 3, point 1). Il fait partie de la chaîne d'effet de SYS-02 mais n'est pas un système d'IA. |
| Configuration | `app/config.py` | Paramètres. Il porte toutefois un secret (AIA-005). |
| Règle de seuil (> 30 images) et `cancel_exam` | `app/proctoring.py:22-29` | Règle définie par l'humain, mais intégrée au système SYS-04 dont elle exploite l'inférence. Elle n'est pas traitée comme un système distinct. |
| FastAPI | `requirements.txt:1` | Cadre web déclaré, sans route observée. Pas de signal d'IA. |

---

## 4. Rôles réglementaires

| Système | EduAssist SAS | Établissements clients (lycées, universités) | OpenAI | DeepFace (auteurs) |
|---|---|---|---|---|
| SYS-01 à SYS-03 | **Susceptible d'être fournisseur du système d'IA** (art. 3, point 3) : elle développe les modules et les commercialise sous sa marque (README:8-9). L'usage d'une API tierce ne change pas ce rôle. | **Susceptibles d'être déployeurs** (art. 3, point 4) : utilisation sous leur autorité, pour leurs élèves (README:11) | Fournisseur du ou des modèles d'IA à usage général sous-jacents (`gpt-4o`, et le cas échéant `dall-e-3`). **Non** fournisseur des systèmes d'EduAssist. | n.a. |
| SYS-04 | Idem : susceptible d'être fournisseur | Susceptibles d'être déployeurs. L'art. 5 vise aussi l'**utilisation**. | n.a. | Fournisseur d'un modèle spécialisé intégré. Pas un modèle GPAI au vu de sa finalité unique (reconnaissance faciale et émotions). |

- **Distinction système / modèle GPAI** : EduAssist n'est **pas**, au vu du dépôt, fournisseur de modèle GPAI. Elle n'entraîne, n'affine ni ne publie aucun modèle (README:12, aucun script d'entraînement). Voir AIA-015.
- **Importateur, distributeur, mandataire** : non pertinents. EduAssist est établie dans l'Union et commercialise ses propres systèmes sous sa marque.
- **Art. 25 (requalification)** : sans objet pour EduAssist, déjà fournisseur. À noter : SYS-02 et SYS-04 orientent des modèles tiers vers des finalités de l'annexe III, ce qui confirme qu'EduAssist porte les obligations du fournisseur du système à haut risque.
- **Enseignants** : personnes chargées de la supervision humaine côté déployeur (art. 26, par. 2), pas des opérateurs distincts.

---

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 2, par. 1 (champ territorial) | Tous | Dans le champ | Fournisseur établi en France, systèmes mis sur le marché de l'Union (README:8-9). |
| Art. 2, par. 3 (défense, sécurité nationale) | Tous | Écartée | Finalité éducative. |
| Art. 2, par. 6 et 8 (recherche, développement avant mise sur le marché) | Tous | **Écartée, sous hypothèse** | Le contexte déclaré indique une mise sur le marché le 2026-03-01. La mention « fixture, ne pas déployer » (README:3-4) suggérerait le contraire hors contexte déclaré. Si les systèmes n'étaient en réalité jamais mis sur le marché ni en service, le par. 8 pourrait être examiné et les constats deviendraient préparatoires (NV-01). |
| Art. 2, par. 10 (usage personnel non professionnel) | Tous | Écartée | Usage professionnel par des établissements. |
| Art. 2, par. 12 (logiciels libres et open source) | SYS-04 (DeepFace), tous | Écartée | La licence ouverte d'un composant n'exclut pas le système d'EduAssist. L'exclusion ne joue pas pour l'art. 5, l'art. 50 ni le haut risque. |
| Art. 5, par. 1, f) : exception « raisons médicales ou de sécurité » | SYS-04 | Écartée | Finalité observée : détection de comportements suspects (fraude). La lutte contre la fraude ne relève pas de l'exception, d'interprétation stricte. |
| Art. 5, par. 1, a) et b) (manipulation, exploitation de la vulnérabilité liée à l'âge) | SYS-01 | Examinée, **non retenue** | Le tuteur trompe sur sa nature auprès de possibles mineurs. Mais aucun élément n'établit une altération substantielle du comportement **et** un préjudice important. Traité au titre de l'art. 50, par. 1 (AIA-003). |
| Art. 5, par. 1, g) (catégorisation biométrique selon des attributs sensibles) | SYS-04 | Examinée, non retenue | Seule l'action `emotion` est appelée (proctoring.py:9). Aucune déduction de race, d'opinions, etc. n'est observée. |
| Art. 5, par. 1, h) (identification biométrique à distance en temps réel à des fins répressives) | SYS-04 | Écartée | Pas de finalité répressive ni d'identification. |
| Art. 6, par. 3 (dérogation au haut risque) | SYS-02 | Écartée | Le système fixe la note finale publiée sans relecture (grading.py:28). Ce n'est ni une tâche procédurale étroite, ni l'amélioration d'une activité humaine préalable, ni une détection de schémas, ni une tâche préparatoire. Il influence substantiellement le résultat. |
| Art. 6, par. 3 | SYS-04 | Écartée | Il décide l'annulation de l'examen. |
| Art. 50, par. 1 : exception « évident pour une personne raisonnablement informée » | SYS-01 | Écartée | La persona porte un nom humain (« Claire ») et a pour consigne d'affirmer être une enseignante (tutor_chat.py:9-10). |
| Art. 50, par. 2 : exceptions « mise en forme standard » et « absence de modification substantielle » | SYS-01, SYS-03 | Écartées | Génération de contenus nouveaux à partir d'un prompt. |
| Art. 50, par. 4, al. 2 (textes d'intérêt public) | SYS-01 | Non applicable | Réponses individuelles de tutorat, sans publication pour informer le public. |
| Art. 50, par. 4, al. 1 : régime des œuvres artistiques ou créatives | SYS-03 | À vérifier | Dépend du contenu des illustrations (AIA-010). |
| Art. 111, par. 2 (systèmes à haut risque antérieurs) | SYS-02, SYS-04 | **Conditionnel `[AV]`** | Mis sur le marché le 2026-03-01, avant la date de référence du 2027-12-02. Les exigences du haut risque ne s'appliqueraient qu'en cas de modification importante de la conception après cette date. Pour les systèmes destinés aux autorités publiques, l'échéance serait le 2030-08-02 (une source indique 2028-01-28). Ce régime ne couvre ni l'art. 5 ni l'art. 50. |
| Renvois à d'autres législations | SYS-02, SYS-04 | Hors périmètre | Traitement de données biométriques et décisions individuelles automatisées : relèvent d'autres textes de l'Union (protection des données). Ils sont signalés sans être analysés. |

---

## 6. Classification

### SYS-01 : tuteur conversationnel

| Étape | Réponse | Preuves / manques |
|---|---|---|
| 0. Système d'IA (art. 3, point 1) | Oui | Génération de texte par un LLM (tutor_chat.py:17) |
| 1. Exclusion art. 2 | Non | Section 5 |
| 2. Art. 5 | Examiné (a), b)), non retenu | Section 5 |
| 3. Annexe I | Non | Pas de produit réglementé |
| 4. Annexe III | Non, au vu du code | Aucun usage évaluatif observé. La réutilisation de l'historique pour noter ou orienter n'est pas vérifiable (NV-05). |
| 6. Art. 50 | Oui : par. 1 et 5 (interaction directe) ; par. 2 (texte synthétique, modalités `[AV]`) | AIA-003, AIA-013 |
| 7. GPAI | EduAssist non fournisseur de modèle | AIA-015 |
| 8. Art. 4 | Applicable | AIA-012 |

**Conclusion** : Non à haut risque (motivé), confiance Moyenne. Cette classification n'exempte pas des art. 4, 5 et 50.

### SYS-02 : correction automatique

| Étape | Réponse | Preuves / manques |
|---|---|---|
| 0 | Oui | Inférence d'une note par un LLM (grading.py:19-27) |
| 1 | Non | |
| 2 | Non plausible | Pas de notation sociale (évaluation d'un travail scolaire) |
| 3 | Non | |
| 4 | **Oui : annexe III, point 3, b)** (évaluation des acquis d'apprentissage) `[TI]` | Note finale, publiée au bulletin, qui « compte pour le passage en classe supérieure » (grading.py:3-4, 28) |
| 5 | Dérogation de l'art. 6, par. 3 écartée | Section 5 |
| 6 | Art. 50 : non (pas d'interaction directe, sortie numérique) | |
| 8 | Art. 4 applicable | |

**Conclusion** : **Haut risque probable (annexe III)**. Confiance Élevée sur les faits, Moyenne sur les dates `[O26]`.
- Exigences du chapitre III : non encore applicables (CAL-011, 2027-12-02).
- Régime de l'art. 111, par. 2 : conditionnel (CAL-013, `[AV]`).

### SYS-03 : illustrations de cours

| Étape | Réponse | Preuves / manques |
|---|---|---|
| 0 | Oui | Génération d'images par un modèle (illustrations.py:13) |
| 1 | Non | |
| 2 | Pas de pratique de l'art. 5 initial plausible. Nouvelles interdictions (contenus intimes non consentis, pédopornographie) au 2026-12-02 `[O26]` | Aucun filtrage de prompt côté EduAssist (AIA-011) |
| 3-4 | Non | Support pédagogique, sans évaluation de personnes |
| 6 | **Art. 50, par. 2** (fournisseur) ; **art. 50, par. 4, al. 1** (déployeur, si hypertrucage) | AIA-007, AIA-010 |
| 8 | Art. 4 | |

**Conclusion** : Non à haut risque (motivé), confiance Élevée.

### SYS-04 : surveillance d'examens

| Étape | Réponse | Preuves / manques |
|---|---|---|
| 0 | Oui | Inférence d'émotions par un réseau pré-entraîné (DeepFace), proctoring.py:9 |
| 1 | Non | |
| 2 | **Oui : art. 5, par. 1, f)** (reconnaissance des émotions dans les établissements d'enseignement) `[TI]` | proctoring.py:5, 9, 20 ; exception écartée |
| 4 | Subsidiairement oui : annexe III, point 3, d) (surveillance et détection de comportements interdits lors des examens) et point 1, c) (reconnaissance des émotions) | proctoring.py:13-25 |
| 5 | Dérogation écartée | Décision d'annulation |
| 6 | Art. 50, par. 3 (déployeur) : obligation d'information, sans effet sur l'interdiction, qui prime | |
| 8 | Art. 4 | |

**Conclusion** : **Pratique potentiellement interdite**, confiance Élevée (faits) / Moyenne (qualification : portée de « dans les établissements d'enseignement » pour des examens passés à distance, voir NV-02).
- À titre subsidiaire, si l'interdiction était écartée : haut risque probable (annexe III).

---

## 7. Obligations et calendrier

Statuts calculés par `obligation_timeline.py` à la date du 2026-10-27, avec une mise sur le marché le 2026-03-01.

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance | Constat(s) |
|---|---|---|---|---|---|---|---|
| Ne pas mettre sur le marché ni utiliser une pratique interdite (art. 5, par. 1, a) à h)) | SYS-04 (et examen de SYS-01) | Fournisseur, déployeur | **En vigueur** | 2025-02-02 | CAL-002 | Élevée | AIA-001 |
| Nouvelles interdictions de l'art. 5 (contenus intimes non consentis, pédopornographie) | SYS-03 | Fournisseur, déployeur | Non encore applicable | 2026-12-02 | CAL-004 | Moyenne | AIA-011 |
| Maîtrise de l'IA (art. 4, nouvelle rédaction) | Tous | Fournisseur, déployeur | **En vigueur** | 2025-02-02 ; rédaction modifiée 2026-07-27 (présumée) | CAL-002, CAL-003 | Élevée / Moyenne | AIA-012 |
| Information sur l'interaction avec une IA (art. 50, par. 1 et 5) | SYS-01 | Fournisseur | **En vigueur** | 2026-08-02 | CAL-009 | Élevée | AIA-003 |
| Marquage lisible par machine et détectabilité (art. 50, par. 2) | SYS-03 (images) | Fournisseur | Non encore applicable (régime transitoire) | **2026-12-02** | CAL-010 | Moyenne | AIA-007 |
| Idem, pour les textes conversationnels | SYS-01 | Fournisseur | Non encore applicable ; modalités `[AV]` | 2026-12-02 | CAL-010 | Moyenne / Faible | AIA-013 |
| Information des personnes exposées à la reconnaissance des émotions (art. 50, par. 3) | SYS-04 | Déployeur | En vigueur, mais absorbée par AIA-001 : la cessation prime sur l'information | 2026-08-02 | CAL-009 | Élevée | AIA-001, AIA-016 |
| Déclaration des hypertrucages (art. 50, par. 4, al. 1) | SYS-03 | Déployeur (outillage par le fournisseur) | En vigueur, applicabilité de fait à vérifier | 2026-08-02 | CAL-009 | Élevée (date) | AIA-010 |
| Exigences du haut risque, chapitre III, sections 1 à 3 (art. 8 à 27 : gestion des risques, documentation, journalisation, transparence, contrôle humain, exactitude et robustesse, SGQ, évaluation de la conformité, art. 26) | SYS-02, SYS-04 (subsidiaire) | Fournisseur, déployeur | Non encore applicable | 2027-12-02 | CAL-011 | Moyenne | AIA-002, AIA-004, AIA-006, AIA-008, AIA-009 |
| Systèmes à haut risque antérieurs (art. 111, par. 2) | SYS-02, SYS-04 | Fournisseur, déployeur | **Conditionnel** (modification importante après le 2027-12-02). Autorités publiques : 2030-08-02 | n.d. / 2030-08-02 | CAL-013 | Faible | AIA-008, AIA-014, AIA-016 |
| Art. 49 (enregistrement), 72 (surveillance après commercialisation), 73 (incidents graves), 86 (explication) | SYS-02, SYS-04 | Fournisseur / déployeur | Conditionnel, date effective `[AV]` | À vérifier | CAL-011, CAL-013 | Faible | AIA-008 |
| Analyse d'impact sur les droits fondamentaux (art. 27) | SYS-02, SYS-04 | Déployeurs de droit public | Non encore applicable et conditionnel (statut des clients) | 2027-12-02 | CAL-011 | Moyenne | AIA-016 |
| Obligations des fournisseurs de modèles GPAI (art. 53 à 55) | Tous | n.a. | Non applicable | n.a. | CAL-005 | Élevée | AIA-015 |

---

## 8. Constats

Les constats sont ordonnés par gravité, puis par identifiant.

### AIA-001 : Inférence des émotions des élèves pendant les examens en ligne

- **Système d'IA concerné** : SYS-04 (surveillance d'examens en ligne).
- **Nature du constat** : Risque potentiel.
- **Gravité** : Critique.
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification).
- **Preuve observée** :
  - **Fait observé.** Le module importe DeepFace et appelle `DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)` sur chaque image de la vidéo webcam d'un examen.
  - Il compte les images dont l'émotion dominante appartient à `{"fear", "angry", "surprise"}`.
  - Au-delà de 30 images, il annule l'examen.
  - Le README décrit le module comme « Surveillance d'examens en ligne : analyse la webcam pendant les examens et annule automatiquement les copies jugées suspectes ». Les clients sont des lycées et des universités.
- **Fichier(s) et lignes** : `app/proctoring.py:3, 5, 8-10, 13-25` ; `requirements.txt:3` ; `README.md:9, 21`.
- **Rôle réglementaire concerné** :
  - EduAssist : fournisseur (mise sur le marché) ;
  - établissements clients : déployeurs (utilisation). L'art. 5 vise les deux.
- **Classification du système** : Pratique potentiellement interdite. Subsidiairement : haut risque probable (annexe III, point 3, d) et point 1, c)).
- **Référence juridique** :
  - art. 5, par. 1, f) `[TI]` ;
  - définition du système de reconnaissance des émotions : art. 3, point 39 `[TI]` ;
  - art. 50, par. 3 `[TI]` à titre subsidiaire ;
  - liens : <https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5> ; [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689).
- **Date d'application** : 2025-02-02. **En vigueur** à la date d'audit, sans régime transitoire (CAL-002, confiance élevée).
- **Conditions et exceptions** :
  - (1) Système déduisant des émotions à partir de données biométriques (images du visage) : **rempli**.
  - (2) Utilisation dans les établissements d'enseignement : **rempli** pour des examens organisés par des lycées et universités. Point à confirmer : la portée exacte pour des examens passés **à distance** (référence à confirmer dans les lignes directrices de la Commission de février 2025 sur les pratiques interdites).
  - (3) Exception pour raisons médicales ou de sécurité : **écartée**. La finalité observée est la détection de comportements suspects ; la lutte contre la fraude n'est pas une raison de sécurité au sens de cette exception, d'interprétation stricte.
  - Le régime transitoire de l'art. 111, par. 2 ne couvre pas l'art. 5.
  - L'obligation d'information de l'art. 50, par. 3 (déployeur) ne rend pas licite une pratique interdite.
- **Explication** : le module observe le visage des élèves pendant l'examen et en déduit leurs émotions (peur, colère, surprise). Il traite ces émotions comme des indices de fraude. Le règlement interdit depuis février 2025 la reconnaissance des émotions dans les établissements d'enseignement, sauf pour des raisons médicales ou de sécurité. Au vu des éléments observés, le module est susceptible de relever de cette interdiction, pour l'éditeur comme pour les établissements qui l'utilisent.
- **Recommandation** (obligation, art. 5) :
  - désactiver sans délai l'inférence d'émotions pour tous les clients de l'Union, jusqu'à une analyse juridique documentée ;
  - informer les établissements déployeurs pour qu'ils cessent l'utilisation ;
  - si une surveillance est maintenue, la remplacer par des signaux techniques non biométriques (perte de focus de la fenêtre, connexion d'un second écran, etc.) soumis à un examen humain ;
  - bonne pratique : recenser les annulations déjà prononcées et organiser leur réexamen humain.
- **Méthode de vérification** :
  - absence de l'appel `actions=["emotion"]` et de la dépendance `deepface` dans le code livré ;
  - note de version et communication aux clients ;
  - avis juridique écrit sur la portée de l'art. 5, par. 1, f) ;
  - liste des annulations réexaminées.

### AIA-002 : Annulation automatique des examens sans intervention humaine

- **Système d'IA concerné** : SYS-04.
- **Nature du constat** : Risque potentiel.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification et calendrier `[O26]`, `[AV]`).
- **Preuve observée** :
  - **Fait observé.** `if suspicious > 30: cancel_exam(exam_id, student_id)` porte le commentaire « annulation automatique, sans intervention humaine ».
  - Le seuil est un nombre absolu d'images, indépendant de la durée de la vidéo et de la fréquence d'images.
  - `enforce_detection=False` fait produire une émotion même lorsqu'aucun visage n'est détecté.
  - `cancel_exam` se limite à un `print`, sans enregistrement, notification ni voie de recours.
  - Aucune fonction de relecture, de contestation ou d'arrêt n'est observée.
- **Fichier(s) et lignes** : `app/proctoring.py:9, 20-25, 28-29` ; `README.md:21`.
- **Rôle réglementaire concerné** : EduAssist (fournisseur, art. 14) ; établissements (déployeurs, art. 26, par. 2 et 5).
- **Classification du système** : Pratique potentiellement interdite (AIA-001). Subsidiairement : haut risque probable (annexe III, point 3, d)).
- **Référence juridique** :
  - art. 14, par. 4, d) et e) `[TI]` ;
  - art. 26, par. 2 `[TI]` ;
  - art. 12 `[TI]` ;
  - dates de l'art. 113 modifié `[O26]` ; art. 111, par. 2 `[AV]` ;
  - lien : <https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14>.
- **Date d'application** :
  - 2027-12-02 : non encore applicable (CAL-011, confiance moyenne) ;
  - régime de l'art. 111, par. 2 : conditionnel (CAL-013, confiance faible). Autorités publiques : 2030-08-02.
- **Conditions et exceptions** :
  - Le constat est subsidiaire à AIA-001 : si l'inférence d'émotions est retirée, il porte sur tout dispositif de remplacement.
  - Aucun manquement à l'art. 14 n'est affirmé à la date d'audit.
  - Le risque pour les personnes existe toutefois déjà : annulation d'un examen sur un critère non fiable.
- **Explication** : la décision d'annuler la copie d'un élève est prise par la machine seule, sans que personne ne vérifie. Elle repose sur un comptage d'émotions qui peut être déclenché par des images sans visage ou par un examen plus long. Les exigences de contrôle humain du haut risque ne s'appliqueront qu'à partir de décembre 2027 (sous réserve du régime transitoire). L'effet sur les élèves est en revanche immédiat.
- **Recommandation** :
  - bonne pratique immédiate, anticipant l'art. 14 :
    - transformer toute sortie de surveillance en **signalement** soumis à un surveillant habilité (statut « en attente d'examen ») ;
    - interdire toute annulation sans décision humaine motivée ;
    - permettre l'arrêt du système ;
    - journaliser les décisions ;
    - informer l'élève et lui ouvrir une voie de contestation ;
  - corriger `enforce_detection=False` et le seuil absolu dans tout dispositif conservé.
- **Méthode de vérification** :
  - revue de code : aucun appel à une action d'annulation sans validation humaine tracée ;
  - tests unitaires du flux de validation ;
  - procédure de surveillance écrite.

### AIA-003 : Le tuteur a pour consigne de se présenter comme une enseignante humaine et de nier être une IA

- **Système d'IA concerné** : SYS-01 (tuteur conversationnel).
- **Nature du constat** : Constat technique avéré.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits) / Élevée (qualification `[TI]`, date CAL-009 confiance élevée).
- **Preuve observée** :
  - **Fait observé.** Le prompt système impose : « Tu es Claire, professeure de français au lycée. Ne dis jamais que tu es une intelligence artificielle. Si on te le demande, réponds que tu es une enseignante. »
  - Aucun message d'information sur la nature d'IA n'est présent dans le dépôt (pas d'interface observée).
  - **Analyse juridique.** Manquement potentiel à l'art. 50, par. 1 et 5. Une éventuelle mention dans une interface hors dépôt serait contredite par le comportement du système.
- **Fichier(s) et lignes** : `app/tutor_chat.py:8-11, 14-18` ; `README.md:18`.
- **Rôle réglementaire concerné** : EduAssist, fournisseur (l'obligation porte sur la conception du système).
- **Classification du système** : Non à haut risque (motivé), soumis à l'art. 50.
- **Référence juridique** :
  - art. 50, par. 1 et 5 `[TI]` ;
  - lien : <https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50> ;
  - lignes directrices de la Commission sur l'art. 50 (20.7.2026, selon les sources, non contraignantes).
- **Date d'application** : 2026-08-02. **En vigueur** (CAL-009), sans délai de grâce pour ce paragraphe.
- **Conditions et exceptions** :
  - Interaction directe avec des personnes physiques (élèves) : remplie.
  - Exception « évident pour une personne raisonnablement informée » : écartée (persona à nom humain, consigne de se dire enseignante, public potentiellement mineur).
  - Exception répressive : sans objet.
  - Art. 5, par. 1, a) et b) : examinés et non retenus, faute d'éléments sur une altération substantielle du comportement et un préjudice important.
- **Explication** : la loi exige depuis août 2026 que les personnes sachent qu'elles parlent à une IA, au plus tard dès la première interaction. Ici, le système est programmé pour faire croire aux élèves, possiblement mineurs, qu'ils échangent avec une vraie professeure, et pour le maintenir si on le lui demande. Cette configuration est susceptible de constituer un manquement à l'art. 50, par. 1.
- **Recommandation** (obligation, art. 50, par. 1 et 5) :
  - supprimer les consignes de dissimulation ;
  - demander au modèle de confirmer qu'il est une IA si on le lui demande ;
  - afficher un message clair et accessible avant ou au début de la première interaction, sur tous les canaux ;
  - bonne pratique : renommer la persona de façon non ambiguë (par exemple « Assistant IA de français »).
- **Méthode de vérification** :
  - différence du prompt système ;
  - test automatisé (« Es-tu une IA ? » donne une réponse affirmative) ;
  - captures d'écran de l'information affichée dès la première interaction, y compris avec un lecteur d'écran.

### AIA-004 : Note finale attribuée par le modèle et publiée sans relecture humaine

- **Système d'IA concerné** : SYS-02 (correction automatique).
- **Nature du constat** : Risque potentiel.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits) / Moyenne (dates `[O26]`) / Faible (régime transitoire `[AV]`).
- **Preuve observée** :
  - **Fait observé.** La docstring indique : « La note produite par le modèle est la note finale : elle est écrite directement dans le bulletin de l'élève et compte pour le passage en classe supérieure. »
  - `publish_grade(student_id, grade)` est appelé immédiatement après la réponse du modèle (commentaire « publication immédiate, sans relecture »).
  - Aucune justification par critère n'est produite : seule `{"note": x}` est demandée.
  - Aucune fonction de modification ou de rejet par un enseignant n'existe.
- **Fichier(s) et lignes** : `app/grading.py:1-5, 18-29` ; `app/gradebook.py:5-6` ; `README.md:19`.
- **Rôle réglementaire concerné** : EduAssist (fournisseur : art. 14, 16) ; établissements (déployeurs : art. 26, par. 2 et 11).
- **Classification du système** : Haut risque probable (annexe III, point 3, b)). Dérogation de l'art. 6, par. 3 écartée.
- **Référence juridique** :
  - art. 6, par. 2 et annexe III, point 3, b) `[TI]` ;
  - art. 14, par. 4, b), c), d) `[TI]` ;
  - art. 26, par. 2 et 11 `[TI]` ;
  - art. 113 modifié `[O26]` ; art. 111, par. 2 `[AV]`.
- **Date d'application** :
  - 2027-12-02 : non encore applicable (CAL-011) ;
  - art. 111, par. 2 : conditionnel (CAL-013). Le système a été mis sur le marché avant la date de référence ; les exigences ne s'appliqueraient qu'en cas de modification importante après le 2027-12-02, ou au plus tard le 2030-08-02 si les déployeurs sont des autorités publiques (divergence de sources : 2028-01-28).
- **Conditions et exceptions** :
  - Dérogation de l'art. 6, par. 3 : aucune des conditions a) à d) n'est remplie, et le système détermine le résultat.
  - Une validation humaine ajoutée ne ferait pas sortir le système du haut risque : c'est une exigence, pas un critère d'exclusion.
  - Aucun manquement actuel à l'art. 14 n'est affirmé.
- **Explication** : la note de dissertation qui compte pour le passage en classe supérieure est décidée par le modèle seul. Elle est inscrite au bulletin sans qu'un enseignant la voie, sans justification, et sans possibilité de correction prévue par le code. Ce type de système relève probablement de la catégorie à haut risque « évaluation des acquis ». Les exigences correspondantes ne s'appliquent pas encore, mais l'effet sur les élèves est immédiat.
- **Recommandation** :
  - bonne pratique immédiate, préparant l'art. 14 et l'art. 26, par. 2 :
    - faire de la note une **proposition** (statut « en attente de validation ») ;
    - imposer la validation par l'enseignant avant toute publication, avec possibilité de modifier ou de rejeter ;
    - afficher la justification par critère de la grille et un avertissement sur le biais d'automatisation ;
    - tracer les écarts entre la proposition et la note finale ;
  - informer les élèves de l'usage de l'IA dans l'évaluation (préparation de l'art. 26, par. 11).
- **Méthode de vérification** :
  - revue de code : `publish_grade` n'est appelé que depuis le flux de validation enseignant ;
  - tests ;
  - journal des validations ;
  - captures de l'interface enseignant.

### AIA-005 : Clé d'API écrite en clair dans le code source

- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03 (configuration partagée).
- **Nature du constat** : Constat technique avéré.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits). Le README indique qu'aucune clé réelle n'est présente (README:4) ; la valeur semble fictive, à confirmer.
- **Preuve observée** :
  - **Fait observé.** `OPENAI_API_KEY = "[SECRET MASQUÉ]"`, littéral dans le code ;
  - la clé est importée par trois modules.
- **Fichier(s) et lignes** : `app/config.py:2` ; usages : `app/tutor_chat.py:4-6`, `app/grading.py:10-13`, `app/illustrations.py:7-9`.
- **Rôle réglementaire concerné** : EduAssist, fournisseur.
- **Classification du système** : SYS-01 et SYS-03 non à haut risque ; SYS-02 haut risque probable.
- **Référence juridique** :
  - aucune obligation de l'AI Act en vigueur ne vise directement ce point : c'est une bonne pratique de sécurité (checklist D8) ;
  - pour SYS-02 : art. 15 (cybersécurité) `[TI]`, non encore applicable.
- **Date d'application** : bonne pratique immédiate. Art. 15 : 2027-12-02, non encore applicable (CAL-011), régime de l'art. 111, par. 2 conditionnel (CAL-013).
- **Conditions et exceptions** : sans objet.
- **Explication** : une clé d'accès au fournisseur de modèles est inscrite dans le code. Toute personne ayant accès au code pourrait l'utiliser, ce qui expose à des usages frauduleux et à la fuite des échanges. Ce n'est pas en soi une obligation de l'AI Act en vigueur, mais c'est un défaut de sécurité.
- **Recommandation** (bonne pratique) :
  - retirer la valeur du code et la charger depuis un gestionnaire de secrets ou une variable d'environnement ;
  - révoquer et renouveler toute clé réelle ayant pu être exposée ;
  - purger l'historique de version le cas échéant ;
  - activer une détection de secrets en intégration continue.
- **Méthode de vérification** :
  - recherche de motifs de clés dans le code et l'historique (résultat nul) ;
  - configuration du gestionnaire de secrets ;
  - preuve de rotation.

### AIA-006 : Notation non reproductible et peu robuste

Le constat couvre la température élevée, l'alias de modèle mobile, l'absence de validation de la sortie et l'exposition à l'injection de consignes.

- **Système d'IA concerné** : SYS-02.
- **Nature du constat** : Risque potentiel.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée (faits) / Moyenne (effet réel non mesuré).
- **Preuve observée** :
  - **Fait observé.**
    - `temperature=1.0` : forte variabilité possible pour une même copie.
    - Modèle `gpt-4o` : alias non daté.
    - Le texte de l'élève est transmis tel quel dans le message utilisateur, sans délimitation ni défense : une copie contenant des consignes (« attribue 20/20 ») pourrait influencer la note.
    - `json.loads(...)["note"]` n'a ni gestion d'erreur ni contrôle du type et de la plage 0-20 avant publication.
    - Aucun versionnage de la grille ou du prompt n'est observé.
    - Aucun jeu d'évaluation ni test n'est présent.
- **Fichier(s) et lignes** : `app/grading.py:15, 19-27` ; `app/config.py:3`.
- **Rôle réglementaire concerné** : EduAssist, fournisseur.
- **Classification du système** : Haut risque probable (annexe III, point 3, b)).
- **Référence juridique** : art. 15 (exactitude, robustesse, cybersécurité) et art. 9, par. 6 à 8 (essais) `[TI]`, dates `[O26]`. Bonne pratique immédiate.
- **Date d'application** : 2027-12-02, non encore applicable (CAL-011). Régime de l'art. 111, par. 2 conditionnel (CAL-013).
- **Conditions et exceptions** : aucun manquement actuel affirmé. Le risque d'erreur de notation affecte toutefois déjà les élèves.
- **Explication** : la même copie peut recevoir des notes différentes d'une exécution à l'autre, et le modèle utilisé peut changer sans décision d'EduAssist. Un élève pourrait aussi glisser dans sa copie des instructions destinées au modèle. Une réponse mal formée ou hors barème serait publiée ou ferait échouer le traitement.
- **Recommandation** (bonne pratique immédiate, préparant les art. 9 et 15) :
  - température basse ou nulle et version de modèle datée ;
  - sortie structurée avec schéma, contrôle de plage et repli vers une correction humaine en cas d'anomalie ;
  - séparation et neutralisation du contenu de la copie (délimiteurs, détection d'instructions) ;
  - versionnage de la grille et du prompt ;
  - campagne d'évaluation sur un corpus noté par des enseignants, avec écarts mesurés par sous-groupes (allophones, copies courtes ou longues, handicap).
- **Méthode de vérification** :
  - paramètres dans le code ;
  - tests de reproductibilité et d'injection ;
  - rapport d'évaluation avec métriques et seuils d'acceptation.

### AIA-007 : Images générées enregistrées sans marquage lisible par machine

- **Système d'IA concerné** : SYS-03 (illustrations de cours).
- **Nature du constat** : Non encore applicable.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée (faits) / Moyenne (date `[O26]`).
- **Preuve observée** :
  - **Fait observé.** L'image renvoyée par l'API (`response_format="b64_json"`) est décodée et écrite telle quelle (commentaire « image enregistrée telle quelle, sans métadonnées ni mention ») ;
  - aucun manifeste C2PA, champ IPTC `DigitalSourceType` ni filigrane n'est ajouté par EduAssist ;
  - aucun moyen de détection n'est documenté ;
  - les images sont publiées aux élèves (README:20).
- **Fichier(s) et lignes** : `app/illustrations.py:12-15` ; `app/config.py:4` ; `README.md:20`.
- **Rôle réglementaire concerné** : EduAssist, fournisseur du système génératif.
- **Classification du système** : Non à haut risque (motivé), soumis à l'art. 50, par. 2.
- **Référence juridique** :
  - art. 50, par. 2 `[TI]` ;
  - délai transitoire introduit par le règlement 2026/1744 `[O26]`, selon le règlement 2026/1744, à confirmer sur le JO ;
  - lien : <https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50>.
- **Date d'application** : système mis sur le marché le 2026-03-01, donc avant le 2026-08-02. Applicable le **2026-12-02**, dans 36 jours (CAL-010, confiance moyenne). Non encore applicable à la date d'audit.
- **Conditions et exceptions** :
  - Exceptions « assistance à la mise en forme standard » et « absence de modification substantielle » : écartées (création d'images à partir d'un prompt).
  - Un éventuel marquage appliqué en amont par le fournisseur du modèle n'est pas vérifiable statiquement (NV-07). L'écriture brute des octets pourrait le préserver, mais aucune vérification ni test de préservation n'existe.
  - Selon une source, les contenus produits avant le 2026-08-02 n'auraient pas à être marqués rétroactivement : à confirmer.
- **Explication** : à partir du 2 décembre 2026, les images générées devront porter un marquage technique lisible par machine permettant de détecter qu'elles sont artificielles. Une simple mention visible ne suffit pas. Le code actuel n'en ajoute aucun.
- **Recommandation** (préparation de l'obligation, avant le 2026-12-02) :
  - intégrer un marquage multicouche : métadonnées C2PA et IPTC `trainedAlgorithmicMedia`, filigrane invisible si possible ;
  - préserver les marquages amont ;
  - tester leur survie au pipeline (redimensionnement, compression) ;
  - documenter un moyen de vérification ;
  - bonne pratique : s'appuyer sur le code de bonnes pratiques du 10.6.2026 (volontaire).
- **Méthode de vérification** :
  - lecture des métadonnées d'images produites (outil de vérification C2PA) ;
  - tests automatisés de préservation ;
  - documentation de détection.

### AIA-008 : Exigences du haut risque non préparées pour les systèmes d'évaluation et de surveillance

- **Système d'IA concerné** : SYS-02 et, à titre subsidiaire, SYS-04.
- **Nature du constat** : Non encore applicable.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Moyenne (classification et date `[O26]`) / Faible (art. 111, par. 2 et dates des art. 49, 72, 73, 86 `[AV]`).
- **Preuve observée** :
  - **Fait observé.** Le dépôt ne contient aucun élément observable de :
    - système de gestion des risques ;
    - documentation technique (annexe IV) ;
    - notice d'utilisation pour les déployeurs ;
    - système de gestion de la qualité ;
    - procédure d'évaluation de la conformité ;
    - procédure d'incident.
  - Le README déclare : « Aucune documentation technique, procédure de supervision ou politique de journalisation n'est fournie. »
  - L'absence dans le dépôt n'est pas une preuve d'inexistence (NV-11).
- **Fichier(s) et lignes** : `README.md:23` ; absence de dossier `docs/`.
- **Rôle réglementaire concerné** : EduAssist (fournisseur : art. 9 à 17, 43, 47 à 49, 72, 73) ; établissements (déployeurs : art. 26, 27 le cas échéant, 86).
- **Classification du système** : Haut risque probable (annexe III, point 3, b) pour SYS-02 ; point 3, d) et point 1, c) pour SYS-04, subsidiaire à AIA-001).
- **Référence juridique** :
  - art. 9, 11, 13, 14, 15, 16, 17, 18, 43 (contrôle interne de l'annexe VI), 47, 48, 49, par. 1 `[TI]` ;
  - art. 72, 73, 86 `[TI]`, dates `[AV]` ;
  - art. 113 modifié `[O26]` ; art. 111, par. 2 `[AV]`.
- **Date d'application** :
  - 2027-12-02 : non encore applicable (CAL-011) ;
  - art. 111, par. 2 conditionnel (CAL-013) : pour ces systèmes mis sur le marché le 2026-03-01, application seulement en cas de modification importante de la conception après le 2027-12-02, ou au plus tard le 2030-08-02 s'ils sont destinés à des autorités publiques (divergence : 2028-01-28).
- **Conditions et exceptions** :
  - Dérogation de l'art. 6, par. 3 écartée (section 5).
  - La documentation technique simplifiée réservée aux PME (art. 11, par. 1) est possible si le statut est confirmé (NV-12).
  - Tout changement de modèle sous-jacent ou de logique de décision d'ici là peut constituer une modification importante `[AV]` (voir AIA-014).
- **Explication** : les systèmes qui notent ou surveillent les élèves seront soumis à un ensemble d'exigences lourdes (gestion des risques, documentation, contrôle humain, robustesse, qualité, évaluation de la conformité, enregistrement). Ces exigences demandent plusieurs mois de préparation. Leur date exacte pour des systèmes déjà commercialisés dépend d'un régime transitoire encore incertain.
- **Recommandation** (préparation d'obligations futures) :
  - établir une feuille de route : registre des risques, documentation selon l'annexe IV, notice pour les établissements, SGQ, plan de surveillance après commercialisation et procédure d'incident ;
  - décider et documenter la politique de modification des systèmes au regard de l'art. 111, par. 2 ;
  - ne pas engager ce chantier pour SYS-04 tant que AIA-001 n'est pas tranché.
- **Méthode de vérification** : présence et revue des documents (registre des risques, documentation technique, notice, manuel qualité, rapport d'évaluation interne), datés et versionnés.

### AIA-009 : Absence de journalisation des entrées, sorties, versions et décisions

- **Système d'IA concerné** : SYS-02, SYS-04. Bonne pratique pour SYS-01 et SYS-03.
- **Nature du constat** : Non encore applicable.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée (faits) / Moyenne (date `[O26]`).
- **Preuve observée** :
  - **Fait observé.** Aucun module ne journalise la version du modèle servie, la version du prompt ou de la grille, la température, les entrées (ou leurs empreintes), les sorties ni les décisions.
  - Les notes sont stockées en mémoire volatile (`_GRADES: dict`).
  - L'annulation d'examen ne produit qu'un `print`.
  - Aucune durée de conservation n'est configurée.
- **Fichier(s) et lignes** : `app/grading.py:18-29` ; `app/gradebook.py:2-6` ; `app/proctoring.py:13-29` ; `app/tutor_chat.py:14-18` ; `app/illustrations.py:12-15`.
- **Rôle réglementaire concerné** : EduAssist (fournisseur : art. 12, 19) ; établissements (déployeurs : art. 26, par. 6).
- **Classification du système** : SYS-02 haut risque probable ; SYS-04 pratique potentiellement interdite, subsidiairement haut risque probable.
- **Référence juridique** : art. 12, 19, 26, par. 6 `[TI]` ; art. 86 (explication) `[TI]`, date `[AV]` ; dates `[O26]`.
- **Date d'application** : 2027-12-02, non encore applicable (CAL-011) ; art. 111, par. 2 conditionnel (CAL-013).
- **Conditions et exceptions** : pour SYS-01 et SYS-03 (non à haut risque), la journalisation est une bonne pratique. Elle aide notamment à démontrer le respect de l'art. 50.
- **Explication** : il est aujourd'hui impossible de retrouver comment une note a été attribuée ou pourquoi un examen a été annulé (quel modèle, quelle grille, quelle sortie, quelle intervention humaine). Cela empêche d'expliquer une décision à un élève et de corriger des erreurs.
- **Recommandation** :
  - préparation des art. 12 et 19, bonne pratique immédiate : journal d'audit horodaté, avec identifiant de corrélation, version du modèle, version du prompt et de la grille, paramètres, sortie, décision humaine, auteur ;
  - stockage protégé en intégrité et conservation d'au moins six mois, paramétrable pour les déployeurs ;
  - pas de secrets ni de contenus excessifs dans les journaux.
- **Méthode de vérification** : schéma de journal, revue de code, test de bout en bout produisant une entrée de journal complète, paramètre de rétention.

### AIA-010 : Illustrations pouvant constituer des hypertrucages, sans fonction d'étiquetage pour les déployeurs

- **Système d'IA concerné** : SYS-03.
- **Nature du constat** : À vérifier juridiquement ou organisationnellement.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée (faits) / Faible (qualification : contenu des images inconnu).
- **Preuve observée** :
  - **Fait observé.** Le générateur accepte un prompt libre ;
  - l'image est enregistrée sans mention visible ni fonction d'étiquetage ;
  - les supports sont « publiés aux élèves ».
  - On ne sait pas si les illustrations représentent des personnes, lieux ou événements réels (personnages historiques, scènes d'actualité) susceptibles d'être perçus comme authentiques.
- **Fichier(s) et lignes** : `app/illustrations.py:12-15` ; `README.md:20`.
- **Rôle réglementaire concerné** :
  - établissements et enseignants : déployeurs, débiteurs de l'art. 50, par. 4, al. 1 ;
  - EduAssist : fournisseur, qui peut outiller le déployeur (bonne pratique).
- **Classification du système** : Non à haut risque (motivé), soumis à l'art. 50.
- **Référence juridique** : art. 50, par. 4, al. 1 et par. 5 `[TI]` ; art. 3, point 60 (hypertrucage) `[TI]`.
- **Date d'application** : 2026-08-02, **en vigueur** (CAL-009). Applicabilité de fait à vérifier.
- **Conditions et exceptions** :
  - Applicable seulement si l'image ressemble à des personnes, objets, lieux, entités ou événements existants et peut être perçue à tort comme authentique.
  - Régime allégé pour une œuvre manifestement artistique, créative, satirique ou fictionnelle : divulgation appropriée.
  - Exception répressive : sans objet.
- **Explication** : si une illustration de cours montre par exemple un personnage historique ou un événement réel de façon réaliste, l'établissement qui la publie doit indiquer qu'elle a été générée par IA. Le produit ne propose aujourd'hui aucun moyen simple de le faire.
- **Recommandation** :
  - à vérifier avec EduAssist et les clients : usages réels et types d'illustrations ;
  - bonne pratique pour le fournisseur : mention visible « Image générée par IA » activée par défaut, consigne d'usage aux enseignants, journalisation des publications ;
  - obligation pour le déployeur : déclarer les hypertrucages.
- **Méthode de vérification** : échantillon d'illustrations publiées, captures de l'étiquette visible, guide d'utilisation remis aux établissements.

### AIA-011 : Aucun garde-fou observé sur les prompts et les sorties du générateur d'images au regard des nouvelles interdictions

- **Système d'IA concerné** : SYS-03.
- **Nature du constat** : Non encore applicable.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Moyenne (faits : filtrage amont d'OpenAI non observable) / Faible (portée pour un générateur non généraliste `[AV]`).
- **Preuve observée** :
  - **Fait observé.** Le prompt est transmis directement à l'API, sans filtre de prompt ou de sortie, politique d'usage, détection de personnes réelles ni mécanisme de signalement côté EduAssist.
  - Les garde-fous éventuels du fournisseur du modèle ne sont pas observables dans le dépôt.
- **Fichier(s) et lignes** : `app/illustrations.py:12-14`.
- **Rôle réglementaire concerné** : EduAssist (fournisseur) ; établissements (déployeurs).
- **Classification du système** : Non à haut risque (motivé).
- **Référence juridique** :
  - art. 5, par. 1, nouveaux points (contenus intimes non consentis de personnes identifiables ; matériel pédopornographique) `[O26]`, selon le règlement 2026/1744, à confirmer sur le JO ;
  - numérotation (ba) et (bb) `[AV]`.
- **Date d'application** : 2026-12-02, non encore applicable, dans 36 jours (CAL-004, confiance moyenne).
- **Conditions et exceptions** : selon une source, l'interdiction peut viser des fournisseurs de systèmes génératifs n'ayant pas mis en place de garde-fous raisonnables `[AV]`. La portée exacte reste à lire dans le texte officiel.
- **Explication** : à partir de décembre 2026, générer des images intimes non consenties de personnes réelles ou du matériel pédopornographique devient une pratique interdite. Le produit vise un public scolaire et ne contient aucun filtre propre. Il dépend entièrement des protections, non vérifiées, du fournisseur du modèle.
- **Recommandation** (préparation, avant le 2026-12-02) :
  - filtre de prompts et de sorties côté EduAssist ;
  - politique d'usage acceptable ;
  - restriction des comptes autorisés à générer ;
  - procédure de signalement et de retrait ;
  - vérification documentée des garde-fous contractuels du fournisseur du modèle.
- **Méthode de vérification** : tests de prompts interdits (rejet attendu), politique publiée, journal des refus, clauses contractuelles.

### AIA-012 : Mesures de maîtrise de l'IA non observables

- **Système d'IA concerné** : SYS-01 à SYS-04.
- **Nature du constat** : À vérifier juridiquement ou organisationnellement.
- **Gravité** : Moyenne (systèmes à fort impact sur des élèves, supervision attendue des enseignants).
- **Niveau de confiance** : Faible (non observable) / Moyenne (référence `[O26]`).
- **Preuve observée** : **Fait observé.** Aucun plan de formation, guide d'utilisation, avertissement d'interface ni registre de formation n'est présent dans le dépôt. Ce sont des éléments organisationnels, généralement hors dépôt.
- **Fichier(s) et lignes** : non disponible.
- **Rôle réglementaire concerné** : EduAssist (fournisseur) ; établissements (déployeurs).
- **Classification du système** : toutes classifications (obligation horizontale).
- **Référence juridique** :
  - art. 4 `[TI]`, nouvelle rédaction `[O26]` (mesures pour soutenir la maîtrise de l'IA, sans exigence d'un niveau déterminé), selon le règlement 2026/1744, à confirmer sur le JO ;
  - l'art. 4 ne figure pas à l'art. 99, par. 4. Le régime de sanction relève du droit national `[AV]`.
- **Date d'application** : en vigueur depuis le 2025-02-02 (CAL-002) ; nouvelle rédaction présumée applicable depuis le 2026-07-27 (CAL-003, confiance moyenne).
- **Conditions et exceptions** : sans objet.
- **Explication** : l'éditeur comme les établissements doivent prendre des mesures pour que leur personnel (développeurs, support, enseignants) comprenne les possibilités, limites et risques des systèmes d'IA utilisés. Le dépôt ne permet pas de savoir si c'est le cas.
- **Recommandation** :
  - obligation (art. 4) : définir et documenter des mesures adaptées au contexte (formation des équipes, guide enseignant sur les limites de la notation automatique et le biais d'automatisation) ;
  - bonne pratique : tenir un registre des formations.
- **Méthode de vérification** : plan de formation, supports, registre de participation, guide remis aux établissements.

### AIA-013 : Réponses textuelles du tuteur sans marquage lisible par machine

- **Système d'IA concerné** : SYS-01.
- **Nature du constat** : Non encore applicable.
- **Gravité** : Faible.
- **Niveau de confiance** : Élevée (faits) / Faible (qualification : modalités pour les textes conversationnels `[AV]`).
- **Preuve observée** : **Fait observé.** Le texte du modèle est renvoyé tel quel, sans métadonnée ni marquage.
- **Fichier(s) et lignes** : `app/tutor_chat.py:17-18`.
- **Rôle réglementaire concerné** : EduAssist, fournisseur.
- **Classification du système** : Non à haut risque (motivé).
- **Référence juridique** :
  - art. 50, par. 2 `[TI]` et délai `[O26]` ;
  - application aux textes conversationnels selon les lignes directrices de la Commission du 20.7.2026 (C(2026) 5054 selon les sources) `[AV]`.
- **Date d'application** : 2026-12-02 pour ce système mis sur le marché avant le 2026-08-02. Non encore applicable (CAL-010).
- **Conditions et exceptions** : la portée et les modalités de l'obligation pour des réponses conversationnelles sont à confirmer dans les lignes directrices.
- **Explication** : l'obligation de marquage technique vise aussi, en principe, les textes générés. Ses modalités pour un dialogue en ligne restent à préciser.
- **Recommandation** (préparation) : documenter une position au regard des lignes directrices avant le 2026-12-02 et, si nécessaire, prévoir un marquage (métadonnées dans l'API, en-têtes, mention).
- **Méthode de vérification** : note de position datée ; présence du marquage dans les réponses de l'API si retenu.

### AIA-014 : Versions de modèles non épinglées et non journalisées

- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03.
- **Nature du constat** : Bonne pratique recommandée.
- **Gravité** : Faible.
- **Niveau de confiance** : Élevée (faits).
- **Preuve observée** :
  - **Fait observé.** `DEFAULT_MODEL = "gpt-4o"` et `IMAGE_MODEL = "dall-e-3"` sont des alias non datés, que le fournisseur peut faire évoluer.
  - La version effectivement servie n'est pas enregistrée.
  - Point positif : les versions des bibliothèques sont épinglées dans `requirements.txt`.
- **Fichier(s) et lignes** : `app/config.py:3-4` ; `requirements.txt:1-4`.
- **Rôle réglementaire concerné** : EduAssist, fournisseur.
- **Classification du système** : SYS-01 et SYS-03 non à haut risque ; SYS-02 haut risque probable.
- **Référence juridique** : aucune obligation en vigueur (bonne pratique). Liens : annexe IV, points 1 et 6 (futur, CAL-011) ; art. 111, par. 2 (modification importante) `[AV]`.
- **Date d'application** : bonne pratique immédiate ; annexe IV : 2027-12-02.
- **Conditions et exceptions** : un changement de modèle sous-jacent peut constituer une modification importante de la conception au sens de l'art. 111, par. 2 `[AV]`. Pour SYS-02, un changement subi après le 2027-12-02 pourrait faire perdre le bénéfice du régime transitoire.
- **Explication** : le modèle utilisé peut changer sans décision d'EduAssist. Le comportement (notes, réponses) peut alors varier, et la traçabilité réglementaire du système s'en trouve fragilisée.
- **Recommandation** (bonne pratique) :
  - épingler des versions datées ;
  - consigner chaque changement de modèle dans un journal des modifications avec réévaluation ;
  - enregistrer la version servie à chaque appel.
- **Méthode de vérification** : configuration, CHANGELOG, journaux contenant `model_version`.

### AIA-015 : Obligations des fournisseurs de modèles d'IA à usage général non applicables à EduAssist

- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03 (modèles OpenAI) ; SYS-04 (DeepFace).
- **Nature du constat** : Non applicable.
- **Gravité** : Information.
- **Niveau de confiance** : Élevée (faits du dépôt et contexte déclaré).
- **Preuve observée** :
  - **Fait observé.** Le README déclare « EduAssist n'entraîne aucun modèle ».
  - Aucun script d'entraînement ou d'affinage, aucun jeu de données d'entraînement et aucune publication de poids ne sont présents.
  - Les modèles sont consommés via l'API d'OpenAI ou la bibliothèque DeepFace.
  - Le README (l. 12) omet DeepFace.
- **Fichier(s) et lignes** : `README.md:12` ; `app/config.py:3-4` ; `app/proctoring.py:3` ; `requirements.txt:2-3`.
- **Rôle réglementaire concerné** :
  - EduAssist : fournisseur des systèmes d'IA, **non** fournisseur de modèle GPAI ;
  - OpenAI : fournisseur du ou des modèles GPAI sous-jacents.
- **Classification du système** : sans objet.
- **Référence juridique** : art. 3, points 3 et 63 ; art. 53 à 55 `[TI]`.
- **Date d'application** : 2025-08-02 (CAL-005), sans objet pour EduAssist.
- **Conditions et exceptions** : la conclusion serait à revoir en cas d'affinage ou de publication d'un modèle par EduAssist.
- **Explication** : les obligations propres aux modèles d'IA à usage général pèsent sur ceux qui les développent et les mettent sur le marché, ici OpenAI. Elles ne pèsent pas sur EduAssist, qui intègre ces modèles dans ses produits et reste responsable de ses propres systèmes.
- **Recommandation** (bonne pratique) :
  - obtenir et conserver la documentation de l'annexe XII fournie par le fournisseur du modèle ;
  - vérifier ses conditions d'utilisation ;
  - documenter la provenance et la licence des poids du modèle d'émotions de DeepFace ;
  - compléter le README.
- **Méthode de vérification** : documentation fournisseur archivée, mise à jour de l'inventaire des modèles.

### AIA-016 : Statut des établissements déployeurs et obligations qui en dépendent à confirmer

- **Système d'IA concerné** : SYS-01 à SYS-04 (principalement SYS-02 et SYS-04).
- **Nature du constat** : À vérifier juridiquement ou organisationnellement.
- **Gravité** : Information.
- **Niveau de confiance** : Faible (information absente ; référence `[AV]`).
- **Preuve observée** :
  - **Fait observé.** Le README mentionne « lycées et universités de l'Union » sans préciser leur statut public ou privé.
  - Aucune fonction d'aide aux déployeurs n'est observée (information des personnes exposées, étiquetage, rétention configurable).
- **Fichier(s) et lignes** : `README.md:9, 11`.
- **Rôle réglementaire concerné** : établissements (déployeurs) ; EduAssist (fournisseur, qui peut les outiller).
- **Classification du système** : variable selon le système.
- **Référence juridique** :
  - art. 111, par. 2 `[AV]` (échéance 2030-08-02 pour les systèmes destinés aux autorités publiques ; divergence 2028-01-28) ;
  - art. 27 `[TI]` (analyse d'impact pour les organismes de droit public) ;
  - art. 26 `[TI]` ;
  - art. 50, par. 3 et 4 `[TI]`.
- **Date d'application** :
  - art. 50, par. 3 et 4 : en vigueur (CAL-009) ;
  - art. 26 et 27 : 2027-12-02, non encore applicables (CAL-011) ;
  - art. 111, par. 2 : conditionnel ; 2030-08-02 selon `obligation_timeline.py --public-authority` (CAL-013, confiance faible).
- **Conditions et exceptions** : les établissements publics d'enseignement peuvent être des autorités publiques ou des organismes de droit public. C'est à qualifier au cas par cas.
- **Explication** : la nature publique ou privée des clients modifie le calendrier applicable aux systèmes à haut risque déjà commercialisés et peut imposer une analyse d'impact sur les droits fondamentaux aux établissements publics.
- **Recommandation** :
  - à vérifier : cartographier les clients par statut ;
  - bonne pratique : fournir aux établissements une notice et des fonctions les aidant à remplir leurs obligations (information des élèves, étiquetage, conservation des journaux).
- **Méthode de vérification** : liste des clients qualifiée juridiquement ; notice déployeur.

---

## 9. Registre des éléments non vérifiables

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact sur la classification ou les obligations | Interlocuteur suggéré | Constat(s) liés |
|---|---|---|---|---|---|---|---|
| NV-01 | Tous | Confirmation de la date réelle de mise sur le marché ou de mise en service de chaque module (et de chaque version majeure), compte tenu de la mention « fixture, ne pas déployer » (README:3-4) | Information | Détermine le régime transitoire et l'éventuelle exclusion de l'art. 2, par. 8 | CAL-010 (délai au 2026-12-02 ou non), CAL-013 | Direction produit EduAssist | AIA-007, AIA-008, AIA-013 |
| NV-02 | SYS-04 | Modalités des examens (à distance, en établissement), pays de déploiement, éventuelle finalité médicale ou de sécurité invoquée, nombre d'annulations déjà prononcées | Information / juridique | Conditions de l'art. 5, par. 1, f) ; mesure de l'atteinte déjà causée | Qualification de pratique interdite | Juriste, direction produit, clients | AIA-001, AIA-002 |
| NV-03 | SYS-02, SYS-04 | Statut public ou privé des établissements clients | Information / juridique | Échéance de l'art. 111, par. 2 pour les autorités publiques ; art. 27 | Calendrier du haut risque | Service commercial, juriste | AIA-008, AIA-016 |
| NV-04 | SYS-01 | Interface utilisateur et canaux (web, mobile, API) et mentions d'information affichées | Document / information | Art. 50, par. 1 et 5 (moment, accessibilité) | Étendue du manquement potentiel | Équipe front-end | AIA-003 |
| NV-05 | SYS-01 | Réutilisation éventuelle des échanges du tuteur pour évaluer ou orienter les élèves | Information | Un usage évaluatif ferait basculer vers l'annexe III, point 3, b) | Classification de SYS-01 | Direction produit | AIA-003 |
| NV-06 | SYS-03 | Types d'illustrations produites (personnes réelles, personnages historiques, événements), auteurs des prompts, circuit de publication | Information | Qualification d'hypertrucage (art. 3, point 60 ; art. 50, par. 4) | Obligations des déployeurs | Clients, équipe pédagogique | AIA-010, AIA-011 |
| NV-07 | SYS-03 | Présence de marquages (C2PA, etc.) dans les images renvoyées par l'API du fournisseur du modèle et préservation dans le pipeline | Information technique | Art. 50, par. 2 | Effort de mise en œuvre avant le 2026-12-02 | Équipe technique, documentation du fournisseur | AIA-007 |
| NV-08 | SYS-02 | Existence hors dépôt d'une interface ou d'un processus permettant aux enseignants de corriger une note après publication ; usage réel par les conseils de classe | Information | Art. 14, art. 26, par. 2 ; évaluation du risque actuel | Gravité de AIA-004 | Clients, direction produit | AIA-004 |
| NV-09 | Tous | Mesures de maîtrise de l'IA (formations, guides, registre) chez EduAssist et chez les clients | Document | Art. 4 | Constat AIA-012 | RH, direction | AIA-012 |
| NV-10 | Tous | Contrats et conditions d'utilisation du fournisseur des modèles OpenAI (documentation de l'annexe XII, usages interdits, garde-fous) ; licence et provenance des poids DeepFace | Document | Obligations du fournisseur du système ; garde-fous art. 5 | AIA-011, AIA-015 | Achats, juriste | AIA-011, AIA-015 |
| NV-11 | SYS-02, SYS-04 | Documentation technique, registre des risques, SGQ, procédure d'incident, évaluations éventuellement tenus hors dépôt | Document | Le README les déclare non fournis, ce qui n'en prouve pas l'inexistence | Préparation du haut risque | Qualité, direction technique | AIA-008, AIA-009 |
| NV-12 | Tous | Statut d'EduAssist (PME, petite entreprise de taille intermédiaire) | Information | Documentation simplifiée (art. 11, par. 1) ; mesures d'allègement `[AV]` | Effort de remédiation | Direction financière | AIA-008 |
| NV-13 | SYS-02, SYS-04 | Évolutions prévues (changement de modèle, de finalité, refonte) avant ou après le 2027-12-02 | Décision | Une modification importante déclencherait l'application du chapitre III (art. 111, par. 2) `[AV]` | Calendrier | Direction produit | AIA-008, AIA-014 |
| NV-14 | Tous | Confirmation sur le JO des dispositions `[O26]` et `[AV]` : CAL-003, CAL-004, CAL-010, CAL-011, CAL-013, CAL-016 ; portée de l'art. 5, par. 1, f) pour les examens à distance (lignes directrices de février 2025) ; lignes directrices sur l'art. 50 | Juridique | Références de confiance moyenne ou faible | Dates et qualifications | Juriste | AIA-001, AIA-007, AIA-008, AIA-011, AIA-013 |

---

## 10. Plan de remédiation synthétique

Priorisation selon `references/findings-methodology.md`, section 6. Efforts estimés à partir du dépôt seul.

| Priorité | Constat(s) | Action | Base | Échéance réglementaire | Effort | Responsable suggéré | Preuve de clôture attendue |
|---|---|---|---|---|---|---|---|
| **P1** | AIA-001, AIA-002 | Désactiver immédiatement l'inférence d'émotions de SYS-04 dans l'Union, prévenir les établissements, obtenir une analyse juridique, faire réexaminer par un humain les annulations passées | Obligation : art. 5, par. 1, f) `[TI]` | En vigueur depuis le 2025-02-02 | S | Direction produit, juriste | Code sans `actions=["emotion"]` ni `deepface`, communication aux clients, avis juridique |
| **P1** | AIA-003 | Supprimer les consignes de dissimulation du prompt, afficher l'information « vous échangez avec une IA » dès la première interaction, de façon accessible | Obligation : art. 50, par. 1 et 5 `[TI]` | En vigueur depuis le 2026-08-02 | S | Équipe produit / front | Différence du prompt, test « Es-tu une IA ? », captures |
| P2 | AIA-004 | Passer la note en proposition validée par l'enseignant, avec justification par critère, avant toute publication | Bonne pratique immédiate ; préparation art. 14 et 26 `[TI]` | 2027-12-02 `[O26]` (CAL-013 conditionnel) | M | Équipe technique | Flux de validation, tests, journal |
| P2 | AIA-005 | Retirer la clé du code, la gérer par un gestionnaire de secrets, la renouveler et activer le scan de secrets | Bonne pratique de sécurité ; art. 15 (futur) | n.a. | S | DevSecOps | Scan sans résultat, preuve de rotation |
| P2 | AIA-006 | Température basse, version datée, sortie structurée validée, défense contre l'injection, campagne d'évaluation | Bonne pratique ; préparation art. 9 et 15 | 2027-12-02 | M | Équipe data / technique | Tests, rapport d'évaluation |
| P2 | AIA-007 | Marquage C2PA, IPTC et filigrane des images, avec tests de préservation et moyen de détection documenté | Obligation future : art. 50, par. 2 `[TI]` / délai `[O26]` | **2026-12-02** | M | Équipe technique | Métadonnées vérifiées sur échantillon, tests |
| P2 | AIA-011 | Filtres de prompts et de sorties, politique d'usage, signalement ; vérification des garde-fous contractuels | Obligation future : art. 5, nouveaux points `[O26]` | **2026-12-02** | S-M | Équipe technique, juriste | Tests de refus, politique publiée |
| P2 | AIA-010 | Qualifier les usages ; proposer une étiquette « Image générée par IA » par défaut et une consigne aux enseignants | À vérifier ; obligation du déployeur : art. 50, par. 4 | En vigueur depuis le 2026-08-02 | S | Produit, clients | Étiquette visible, guide |
| P2 | AIA-012 | Définir et documenter les mesures de maîtrise de l'IA (équipes, guide enseignant) | Obligation : art. 4 `[TI]` / `[O26]` | En vigueur | M | RH, direction pédagogique | Plan, supports, registre |
| P3 | AIA-008 | Feuille de route du haut risque pour SYS-02 (registre des risques, annexe IV, notice, SGQ, contrôle interne, surveillance après commercialisation, incidents) ; politique de modification au regard de l'art. 111, par. 2 | Obligation future : art. 9 à 17, 43, 47 à 49, 72, 73 | 2027-12-02 `[O26]` ; CAL-013 conditionnel `[AV]` | L | Qualité, direction technique | Documents versionnés |
| P3 | AIA-009 | Journal d'audit (version du modèle, prompt, grille, paramètres, sorties, décisions humaines), conservation d'au moins six mois | Obligation future : art. 12, 19, 26, par. 6 ; bonne pratique immédiate | 2027-12-02 | M | Équipe technique | Schéma et entrées de journal, rétention |
| P3 | AIA-013 | Note de position sur le marquage des textes conversationnels au regard des lignes directrices | Obligation future : art. 50, par. 2 `[AV]` (priorité relevée de P4 à P3 en raison de l'échéance proche) | 2026-12-02 | S | Juriste, produit | Note datée |
| P3 | AIA-014 | Épingler des versions de modèles datées, CHANGELOG des modèles, journalisation de la version servie | Bonne pratique (lien avec l'art. 111, par. 2 `[AV]`) | n.a. | S | Équipe technique | Configuration, CHANGELOG |
| P3 | AIA-016 | Cartographier le statut des clients ; outiller les déployeurs (notice, information, étiquetage, rétention) | À vérifier ; art. 26, 27, 50 | Conditionnel | M | Commercial, juriste | Liste qualifiée, notice déployeur |
| P4 | AIA-015 | Archiver la documentation du fournisseur du modèle, documenter la provenance des poids DeepFace, corriger le README | Bonne pratique | n.a. | S | Achats, technique | Documentation archivée |

### Jalons

| Date | Évènement réglementaire | Actions à terminer avant |
|---|---|---|
| Immédiat (en vigueur) | Art. 5 (2025-02-02), art. 4, art. 50, par. 1, 3, 4, 5 (2026-08-02) | AIA-001, AIA-002, AIA-003, AIA-010, AIA-012 |
| **2026-12-02** | Art. 50, par. 2 pour les systèmes antérieurs (CAL-010) ; nouvelles interdictions de l'art. 5 (CAL-004) `[O26]` | AIA-007, AIA-011, AIA-013 |
| **2027-12-02** | Exigences du haut risque, annexe III (CAL-011) `[O26]` ; date de référence de l'art. 111, par. 2 (CAL-013) `[AV]` | AIA-004, AIA-006, AIA-008, AIA-009 ; décision sur la politique de modification (AIA-014) |
| 2030-08-02 | Échéance des systèmes à haut risque antérieurs destinés aux autorités publiques (CAL-013) `[AV]`, divergence 2028-01-28 | Selon NV-03 |

### Hypothèses

- Les efforts sont estimés à partir du dépôt seul et sont à recalibrer avec l'équipe.
- Les échéances issues du règlement 2026/1744 (confiance moyenne) et de l'art. 111, par. 2 (confiance faible) sont à confirmer sur le Journal officiel.
- AIA-004 et AIA-006 sont classés P2 (aucune obligation en vigueur), mais il est recommandé de les traiter sans attendre, en raison de l'effet actuel sur les élèves.

---

## 11. Limites de l'audit

- **Analyse statique.** Le comportement réel, les données, les prompts dynamiques, la configuration de production et l'interface utilisateur (absente du dépôt) n'ont pas été observés. Le code audité n'a pas été exécuté.
- **Documents organisationnels absents du dépôt** : documentation technique, registre des risques, SGQ, procédures de supervision et d'incident, politique de journalisation, plans de formation, contrats avec le fournisseur des modèles, liste des clients. Le README déclare que les trois premiers ne sont pas fournis.
- **Références juridiques.**
  - Les entrées de confiance moyenne (CAL-003, CAL-004, CAL-010, CAL-011, CAL-012, CAL-015) ou faible (CAL-013, CAL-016) sont à confirmer sur le Journal officiel.
  - Les textes officiels (EUR-Lex, AI Act Explorer) étaient inaccessibles lors de la dernière vérification des références (2026-10-27). Les modifications du règlement 2026/1744 reposent sur des sources secondaires concordantes. Aucune version consolidée n'a été consultée.
- **Textes évolutifs.** Les lignes directrices (art. 50 du 20.7.2026, pratiques interdites de février 2025, classification à haut risque en projet), les normes harmonisées et les actes d'exécution évoluent.
- **Contexte fictif.** L'audit repose exclusivement sur le contexte déclaré dans le README, qui présente par ailleurs le projet comme une fixture de test. Si ce contexte est inexact, plusieurs qualifications changent (NV-01).
- **Hors périmètre.** La protection des données (données biométriques, décisions individuelles automatisées) et les autres législations sont signalées sans être analysées.
- **Portée du rapport.** Ce rapport est une aide à l'audit. Il ne remplace ni l'avis d'un juriste ni une évaluation de la conformité au sens de l'article 43. Il n'affirme en aucun cas la conformité du projet.

---

## 12. Suivi (ré-audit)

Premier audit : aucun constat antérieur. Lors du prochain audit :
- conserver les identifiants AIA-001 à AIA-016 ;
- recalculer le calendrier à la nouvelle date d'audit. Au-delà du 2026-12-02, AIA-007, AIA-011 et AIA-013 deviennent des obligations en vigueur.

| Constat | Statut précédent | Statut actuel | Preuve |
|---|---|---|---|
| AIA-001 à AIA-016 | n.a. | Nouveau | Présent rapport (2026-10-27) |
