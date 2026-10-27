# Rapport d'audit AI Act : demo-ai-secure (EduAssist)

> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un projet et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689.

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | `demo-ai-secure/` entier : `app/` (9 modules Python), `docs/` (6 documents), `README.md`, `requirements.txt`. Aucun dossier exclu. Aucun test, aucune couche d'interface ou d'API, aucun CHANGELOG dans le projet. |
| Commit audité | non versionné (le projet n'est pas un dépôt Git) |
| Mode | Complet (premier audit) |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`data/ai-act-calendar.json`, `meta.last_verified`). Écart avec la date d'audit : 0 jour, la limite des 6 mois n'est pas atteinte. **Limite majeure maintenue** : aucune entrée du calendrier n'a le statut `officielle_relue` (textes officiels non relus, voir `legal-sources.md`, section 3). |
| Contexte fourni par le demandeur | Uniquement le README et `docs/` : éditeur fictif EduAssist SAS établi en France, produit commercialisé sous la marque « EduAssist » auprès de lycées et d'universités de l'Union ; tuteur et correction assistée mis sur le marché le 2026-03-01, module d'illustrations le 2026-09-15 (dates **déclarées**, non vérifiables) ; modèles via l'API d'un tiers (Anthropic) ; aucun entraînement. Statut PME/autorité publique : non fourni. |
| Méthode | Skill `ia-compliance` v1.0.0, lecture seule, sans exécution du code audité. Outils : `scan_ai_signals.py`, `obligation_timeline.py` (dates de mise sur le marché 2026-03-01 et 2026-09-15). Lecture directe des 9 modules et des 6 documents. |
| Audit précédent | Aucun |

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : 3 (SYS-01 tuteur conversationnel ; SYS-02 correction assistée ;
  SYS-03 illustrations de cours). EduAssist est, au vu des éléments observés, **fournisseur** des
  trois systèmes (marque EduAssist). Elle n'est pas fournisseur de modèle GPAI. `app/exam_events.py`
  n'est pas un système d'IA (journalisation déterministe).
- **Classification** : SYS-02 **haut risque probable** (annexe III, point 3, b) ; SYS-01 et SYS-03
  non à haut risque (motivé), soumis à l'article 50 et à l'article 4. Aucune pratique interdite
  plausible observée.
- **Points les plus sensibles** :
  - AIA-001 : SYS-02 à haut risque probable ; les exigences du chapitre III ne sont pas encore
    applicables, mais le projet a mis le système sur le marché avant la date d'application
    (régime de l'article 111, paragraphe 2, incertain).
  - AIA-002 et AIA-008 : SYS-03 (illustrations), article 50, paragraphe 2, **en vigueur** si la date
    de mise sur le marché déclarée (2026-09-15) est exacte : marquage par métadonnées PNG « maison »,
    manifeste C2PA absent du dépôt (module-bouchon qui lève `NotImplementedError`), efficacité non
    démontrée.
  - AIA-003 : textes générés par SYS-01 et SYS-02 sans aucun marquage ; obligation **non encore
    applicable** si la mise sur le marché du 2026-03-01 est confirmée (échéance 2026-12-02, dans
    36 jours) ; l'incertitude sur les modalités n'est pas une exemption.
  - AIA-004 et AIA-005 : le contrôle humain de SYS-02 est présent mais son effectivité n'est pas
    démontrée (identifiant du valideur non authentifié, publication d'une note `None` possible).
- **Obligations en vigueur concernées** : art. 4 ; art. 5 (aucun écart observé) ; art. 50,
  paragraphes 1, 3, 4, 5 depuis le 2026-08-02 ; art. 50, paragraphe 2, pour SYS-03.
- **Échéances à venir** : 2026-12-02 (art. 50, par. 2 pour SYS-01/SYS-02 ; nouvelles interdictions
  de l'article 5) ; 2027-12-02 (haut risque annexe III) ; art. 111, par. 2 : conditionnel.
- **Principales incertitudes** : dates réelles de mise sur le marché, statut des établissements
  clients (public ou privé), existence et efficacité de l'outil C2PA interne, du filtre de prompts
  et du service d'images, modalités de marquage du texte, configuration réelle des modèles en
  production (voir registre, section 9).
- **Constats dont l'échéance est à confirmer** (base juridique non relue sur le texte officiel) :
  AIA-001 (CAL-011, CAL-013), AIA-003 (CAL-010, délai transitoire), AIA-004, AIA-005, AIA-006 et
  AIA-007 (CAL-011), AIA-009 (CAL-004), AIA-012 (CAL-003). Les conclusions temporelles de ces
  constats sont rédigées au conditionnel : « applicable à compter du ... sous réserve de confirmation
  sur le texte officiel ».
- **Mesures positives constatées** : information d'interaction avec une IA dans le tuteur,
  instruction de ne pas se présenter comme humain, validation humaine obligatoire avant publication
  d'une note, journalisation de la version de modèle servie et de la version de grille, absence de
  secret dans le code, absence de traitement biométrique ou d'émotions (AIA-014, AIA-015).
  Une mesure présente n'équivaut pas à une obligation satisfaite.

**Synthèse des constats**

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | 0 | 0 | 2 (AIA-005, AIA-008) | 0 | 2 (AIA-014, AIA-015) |
| Risque potentiel | 0 | 0 | 4 (AIA-002, AIA-004, AIA-006, AIA-007) | 0 | 0 |
| À vérifier juridiquement ou organisationnellement | 0 | 0 | 0 | 3 (AIA-010, AIA-012, AIA-013) | 0 |
| Bonne pratique recommandée | 0 | 0 | 0 | 1 (AIA-011) | 0 |
| Non encore applicable | 0 | 0 | 3 (AIA-001, AIA-003, AIA-009) | 0 | 0 |
| Non applicable | 0 | 0 | 0 | 0 | 1 (AIA-016) |

## 2. Périmètre et méthode

- **Arborescence analysée** : `README.md`, `requirements.txt` (fastapi 0.115.0, anthropic 0.39.0,
  pillow 11.0.0), `app/` (`tutor_chat.py`, `grading.py`, `gradebook.py`, `illustrations.py`,
  `image_provider.py`, `c2pa_signer.py`, `audit_log.py`, `config.py`, `exam_events.py`),
  `docs/` (inventaire, classification, documentation technique, supervision humaine, registre des
  risques, plan de maîtrise de l'IA).
- **Outils** : `scan_ai_signals.py` (18 fichiers, signaux : API Anthropic, identifiants de modèles,
  marqueurs de transparence/supervision/traçabilité, contexte éducation ; aucun secret, aucune
  bibliothèque de biométrie) ; `obligation_timeline.py` à la date 2026-10-27 pour les dates
  2026-03-01 et 2026-09-15. Les signaux « employment » du scanner (illustrations.py:17) sont des faux
  positifs (mot « cv » dans l'URL IPTC).
- **Constat structurant** : `fastapi` est déclaré mais **aucune route, aucune interface, aucune
  authentification** n'existe dans le projet. Tout ce qui relève de l'affichage, de l'identité des
  utilisateurs et des canaux de sortie est donc non observable (registre, section 9).
- **Non analysé** : le service tiers de génération d'images (`image_provider.py` est un bouchon),
  l'outil de signature C2PA interne (`c2pa_signer.py` est un bouchon), les variables d'environnement
  de production, les contrats, le guide utilisateur, le registre de formation.
- **Règle appliquée aux déclarations du projet** : les dates et qualifications juridiques de `docs/`
  ont été confrontées au calendrier de référence ; elles ne sont pas reprises telles quelles.

## 3. Systèmes d'IA identifiés

Inventaire détaillé en annexe A. Synthèse :

| ID | Système | Finalité | Rôle(s) de l'organisation | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|
| SYS-01 | Tuteur conversationnel (`app/tutor_chat.py`) | Répondre aux questions de cours des élèves | Fournisseur du système d'IA (susceptible) | `claude-sonnet-4-5` (défaut, surchargeable par env.), API Anthropic | Non à haut risque (motivé) ; art. 50 et art. 4 | Moyenne |
| SYS-02 | Correction assistée (`app/grading.py`, `app/gradebook.py`) | Proposer note, critères et justification pour des dissertations ; l'enseignant décide | Fournisseur du système d'IA (susceptible) | `claude-sonnet-4-5` (défaut), API Anthropic | **Haut risque probable** (annexe III, point 3, b) | Élevée (faits) / Moyenne (qualification et dates) |
| SYS-03 | Illustrations de cours (`app/illustrations.py`) | Générer des images pour supports pédagogiques | Fournisseur du système d'IA (susceptible) | Service tiers non identifié (`image_provider.py`, bouchon) | Non à haut risque (motivé) ; art. 50, par. 2 (fournisseur) et par. 4 (déployeur) | Moyenne |

**Éléments examinés et écartés**

| Composant | Fichier | Motif |
|---|---|---|
| Événements d'examen | `app/exam_events.py` | Pas un système d'IA : transmission d'événements techniques (perte de focus, déconnexion) sans inférence ; aucune bibliothèque d'IA importée (art. 3, point 1). À surveiller en cas d'évolution (voir AIA-013). |
| Journal d'audit | `app/audit_log.py` | Infrastructure de journalisation, sans inférence. |
| Carnet de notes | `app/gradebook.py` | Stockage en mémoire de la fixture ; fait partie de la chaîne de SYS-02 mais ne contient pas d'inférence. |
| Configuration | `app/config.py` | Constantes ; pas de secret en clair. |

## 4. Rôles réglementaires

- **EduAssist SAS** (France, donc dans l'Union ; mandataire non nécessaire) : au vu des éléments
  observés (marque « EduAssist », commercialisation auprès d'établissements, art. 3, points 3 et 11),
  elle est **susceptible d'être fournisseur** de SYS-01, SYS-02 et SYS-03. Les systèmes reposent sur
  des API tierces ; l'usage d'une API ne fonde pas à lui seul le rôle, mais la commercialisation sous
  sa marque le fonde. À confirmer par les contrats et les conditions de commercialisation.
- **Établissements clients** (lycées, universités) : déployeurs (art. 3, point 4), selon le projet.
  Leur statut (organismes de droit public ou non) est inconnu et conditionne l'article 111,
  paragraphe 2 et l'article 27 (voir NV-02).
- **Anthropic** : fournisseur du modèle GPAI sous-jacent (déclaré). EduAssist n'entraîne ni n'affine
  aucun modèle (README) ; aucun script d'entraînement dans le projet. Elle n'est donc pas, au vu
  du projet, fournisseur de modèle GPAI (AIA-016).
- **Service tiers d'images** : identité inconnue ; rôle de fournisseur de modèle ou de système à
  déterminer (NV-06).
- **Article 25** : pas de requalification observée (EduAssist est déjà fournisseur de SYS-02). Point
  de vigilance : SYS-02 est construit sur un modèle généraliste détourné vers une finalité de
  l'annexe III ; EduAssist assume donc les obligations du fournisseur du système à haut risque.

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 2, par. 3 (défense, sécurité nationale) | Tous | Écartée | Produit éducatif commercial. |
| Art. 2, par. 6 et 8 (recherche et développement) | Tous | Écartée | Systèmes commercialisés auprès d'établissements, non réservés à la R&D. |
| Art. 2, par. 10 (usage personnel non professionnel) | Tous | Écartée | Usage en milieu éducatif professionnel. |
| Art. 2, par. 12 (logiciel libre et open source) | Tous | Écartée | Aucune publication open source observée ; en tout état de cause, exclusion non applicable au haut risque ni aux art. 5 et 50. |
| Art. 5, par. 1, a) et b) (manipulation, vulnérabilités) | SYS-01 | Examinée, non retenue | Le prompt système impose de reconnaître être une IA ; aucun ciblage ni dark pattern observé. Les élèves peuvent être mineurs : à garder en vigilance, sans indice d'exploitation. |
| Art. 5, par. 1, c) (notation sociale) | SYS-02 | Écartée | Évaluation scolaire dans son contexte, sans réutilisation hors contexte observée. |
| Art. 5, par. 1, f) (émotions en établissement d'enseignement) | Tous | Écartée sur le dépôt | Aucune inférence d'émotion ni bibliothèque biométrique (PRV-027) ; historique de la surveillance webcam supprimée à vérifier (AIA-013). |
| Art. 5, par. 1, g) (catégorisation biométrique) | Tous | Écartée | Aucun traitement biométrique. |
| Annexe I (art. 6, par. 1) | Tous | Écartée | Aucun produit ni composant de sécurité relevant de la législation d'harmonisation. |
| Annexe III, point 3, a), c), d) | SYS-01, SYS-02 | Écartée | Pas d'admission, d'affectation, de test de positionnement ni de surveillance d'examen par IA. |
| Annexe III, point 3, b) | SYS-02 | **Retenue** | Évaluation des acquis d'apprentissage (note de dissertation). |
| Art. 6, par. 3 (dérogation) | SYS-02 | **Écartée** | Le projet ne l'invoque pas, et elle ne serait pas défendable : la proposition de note est susceptible d'influencer substantiellement la décision et le système évalue la performance de personnes physiques (risque de profilage excluant la dérogation). La validation humaine n'est pas un critère d'exclusion. C11 : non applicable. |
| Art. 50, par. 1, exception « évident » | SYS-01 | Non invoquée | Assistant nommé « assistant d'IA » ; l'information est donnée explicitement. |
| Art. 50, par. 1 | SYS-02 | Non retenue comme obligation autonome | Pas d'interaction conversationnelle ; l'enseignant utilise un outil dont la nature d'IA est affichée (selon la procédure, interface non observable). |
| Art. 50, par. 2, exceptions (mise en forme standard, absence de modification substantielle) | SYS-01, SYS-02, SYS-03 | Écartées | Les sorties sont des contenus nouveaux (réponses, justification, images), pas une assistance de mise en forme. |
| Art. 50, par. 3 (émotions, catégorisation biométrique) | Tous | Non applicable | Aucun système concerné. |
| Art. 50, par. 4, al. 2 (textes d'intérêt public) | SYS-01, SYS-02 | Non applicable | Aucune publication de texte au public. |
| Art. 111, par. 2 (systèmes antérieurs) | SYS-02 | Conditionnel | Voir AIA-001. |

## 6. Classification

Détail en annexe B.

- **SYS-01** : système d'IA (inférence par modèle de langage) ; aucun cas d'usage de l'annexe III
  (le tuteur n'évalue pas et aucun appel croisé avec le module de notation n'existe dans le code,
  PRV-034) ; art. 50, par. 1 : information présente côté code ; art. 50, par. 2 : sorties textuelles
  sans marquage ; art. 4. Hypothèse alternative : si les échanges étaient réutilisés pour noter ou
  orienter (flux hors dépôt), SYS-01 deviendrait un système hybride à reclasser (NV-15).
- **SYS-02** : échelle de `person-decisions.md` : niveau 3 (décision assistée : note proposée,
  validée par un humain). Annexe III, point 3, b) retenue ; dérogation écartée ; **haut risque
  probable**. Exigences du chapitre III : CAL-011, 2027-12-02 (échéance à confirmer). Mis sur le marché
  le 2026-03-01 (déclaré) : CAL-013 conditionnel (échéance à confirmer, confiance faible).
- **SYS-03** : système d'IA génératif ; non à haut risque ; art. 50, par. 2 (fournisseur) en vigueur
  si mise sur le marché le 2026-09-15 (CAL-010) ; art. 50, par. 4 (déployeurs, hypertrucages
  éventuels) ; nouvelles interdictions de l'article 5 le 2026-12-02 (CAL-004).
- Une classification « non à haut risque » n'est jamais une exemption générale (art. 4, 5, 50).

## 7. Obligations et calendrier

Statuts calculés avec `scripts/obligation_timeline.py` au 2026-10-27. Matrice détaillée en annexe C.

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|
| Art. 5 (pratiques interdites, version initiale) | Tous | Fournisseur | En vigueur | 2025-02-02 | CAL-002 | Élevée |
| Art. 5, nouveaux points (contenus intimes non consentis, matériel pédopornographique) | SYS-03 | Fournisseur | Non encore applicable (**échéance à confirmer**) | 2026-12-02 (dans 36 jours) | CAL-004 | Moyenne |
| Art. 4 (maîtrise de l'IA) | Tous | Fournisseur | En vigueur ; nouvelle rédaction en vigueur (**échéance à confirmer**) | 2025-02-02 ; 2026-07-27 | CAL-002, CAL-003 | Élevée ; Moyenne |
| Art. 50, par. 1, 4, 5 | SYS-01, SYS-03 | Fournisseur / déployeurs | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Art. 50, par. 2, systèmes mis sur le marché avant le 2026-08-02 | SYS-01, SYS-02 | Fournisseur | Non encore applicable (**échéance à confirmer**) | 2026-12-02 (dans 36 jours) | CAL-010 | Moyenne |
| Art. 50, par. 2, système mis sur le marché à partir du 2026-08-02 | SYS-03 | Fournisseur | En vigueur (sous réserve de la date déclarée, NV-01) | 2026-08-02 | CAL-010 | Moyenne |
| Chapitre III, sections 1 à 3 (art. 8 à 27) | SYS-02 | Fournisseur / déployeurs | Non encore applicable (**échéance à confirmer**) | 2027-12-02 (dans 401 jours) | CAL-011 | Moyenne |
| Art. 111, par. 2 (système antérieur) | SYS-02 | Fournisseur | Conditionnel (**échéance à confirmer**) | n.d. | CAL-013 | Faible |
| Enregistrement art. 49, par. 2 | SYS-02 | Fournisseur | Sans objet si haut risque retenu (art. 49, par. 1) ; à vérifier | n.d. | CAL-016 | Faible |
| Art. 53 à 55 (GPAI) | Tous | Fournisseur de modèle | Non applicable à EduAssist | n.a. | CAL-005 | Élevée |

## 8. Constats

### AIA-001 : SYS-02 probablement à haut risque (annexe III, point 3, b) ; exigences non encore applicables, régime des systèmes antérieurs incertain
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification) / Faible (régime art. 111, par. 2)
- **Preuve observée** : *Fait observé* : le module propose une note, des critères et une justification sur une dissertation d'élève (`propose_grade`), l'enseignant approuve, modifie ou rejette (`review_grade`), et la note est publiée au carnet (`publish_grade`). Le projet reconnaît lui-même le haut risque et la non-application de la dérogation (`docs/classification-assessment.md:7-14`). La feuille de route reconnaît : notice (art. 13) « à rédiger », SGQ (art. 17) « à établir », évaluation de conformité, déclaration UE, marquage CE, enregistrement « à planifier » (`classification-assessment.md:34-41`). *Analyse juridique* : voir ci-dessous. [PRV-011, PRV-019, PRV-028]
- **Fichier(s) et lignes** : `app/grading.py:33-69` ; `app/gradebook.py:5-8` ; `docs/classification-assessment.md:5-14, 30-41`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA (susceptible) ; établissements clients déployeurs
- **Classification du système** : Haut risque probable (annexe III, point 3, b)
- **Référence juridique** : Art. 6, par. 2 et 3 ; annexe III, point 3, b) `[TI]` ; art. 8 à 27, 43, 47 à 49 ; dates : art. 113 modifié `[O26]` ; art. 111, par. 2 `[AV]`. Voir [AI Act Explorer, art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6) et [EUR-Lex 2026/1744](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1744).
- **Date d'application** : CAL-011 : 2027-12-02, **échéance à confirmer** (sources secondaires) : les exigences sont, au conditionnel, applicables à compter du 2027-12-02 sous réserve de confirmation sur le texte officiel. CAL-013 : conditionnel, **échéance à confirmer** (confiance faible, sources divergentes : 2030-08-02 ou 2028-01-28 pour les systèmes destinés aux autorités publiques). La qualification de classification est, elle, immédiate.
- **Conditions et exceptions** : (1) Dérogation de l'art. 6, par. 3 : écartée (influence substantielle sur la décision, risque de profilage ; la validation humaine n'est pas un critère d'exclusion). (2) Système mis sur le marché le 2026-03-01 (date déclarée) donc avant la date d'application : il pourrait n'être soumis aux exigences que s'il subit une modification importante de sa conception après la date de référence `[AV]`, appréciée selon une source au niveau du type et du modèle. Un changement de modèle (variable `EDUASSIST_GRADING_MODEL`), de grille (`RUBRIC`, `PROMPT_VERSION`) ou de finalité est un candidat à la modification importante (art. 111, par. 2) ou substantielle (art. 25) et doit être analysé comme tel. (3) Les établissements publics clients peuvent bénéficier d'une échéance spécifique et sont soumis à l'art. 27 (organismes de droit public) : statut inconnu (NV-02). (4) Le report n'affecte pas l'art. 4, l'art. 5 ni l'art. 50.
- **Explication** : La note proposée par l'IA sert à évaluer des élèves : c'est un cas d'usage que le règlement place parmi les systèmes à haut risque. Le projet l'a bien identifié et prépare la conformité. Les exigences détaillées ne s'appliquent pas encore ; si elles s'appliquent un jour à cette version déjà commercialisée dépendra du régime transitoire, dont la date et la portée restent à confirmer. La préparation est donc proportionnée, mais plusieurs briques (notice, SGQ, évaluation de la conformité) restent à construire.
- **Recommandation** : (a) Confirmer sur le Journal officiel les dates CAL-011/CAL-013 et obtenir une validation juridique sur l'art. 111, par. 2 (le projet l'a déjà demandée) (obligation de qualification, préparation). (b) Instituer une procédure de qualification de toute modification (modèle, grille, prompt) comme importante ou non, tracée au CHANGELOG (bonne pratique appuyant l'art. 111, par. 2). (c) Planifier SGQ, notice, évaluation de conformité, déclaration UE, marquage CE et enregistrement avec jalon avant 2027-12-02 (préparation d'obligations futures).
- **Méthode de vérification** : Note juridique datée sur l'art. 111, par. 2 ; extrait du JO confirmant CAL-011 et CAL-013 ; procédure de qualification des modifications ; planning des jalons du chapitre III.

### AIA-002 : SYS-03, marquage machine par métadonnées PNG « maison » : détectabilité et robustesse non démontrées
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification)
- **Preuve observée** : *Fait observé* : le marquage appliqué à l'image est écrit avec `PngInfo.add_text` sous des clés texte PNG libres (`DigitalSourceType`, `ai_disclosure`, `model_version`), la valeur IPTC `trainedAlgorithmicMedia` étant copiée en simple texte ; il ne s'agit pas d'un paquet XMP/IPTC structuré. Ces champs ne sont pas signés et sont retirables par tout ré-encodage. Le docstring annonce « XMP/IPTC » et reconnaît : « la robustesse du marquage aux recompressions n'a pas été testée ». Aucun test ni outil de vérification dans le projet. *Analyse juridique* : mesure présente, efficacité et interopérabilité non démontrées, au titre de l'obligation de marquage lisible par machine et détectable. [PRV-006, PRV-007, PRV-009]
- **Fichier(s) et lignes** : `app/illustrations.py:3-6, 16-17, 22-26`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA (susceptible)
- **Classification du système** : Non à haut risque (motivé) ; art. 50, par. 2
- **Référence juridique** : Art. 50, par. 2 et 5 `[TI]`, délai transitoire `[O26]` ; [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50) ; code de bonnes pratiques sur le marquage (10.6.2026, volontaire, à confirmer).
- **Date d'application** : CAL-010 : **en vigueur** depuis le 2026-08-02 pour un système mis sur le marché à compter de cette date (aucun délai transitoire) ; confiance Moyenne. Cette conclusion repose sur la date de mise sur le marché **déclarée** par le projet (2026-09-15), non vérifiable (NV-01). Si le module avait été mis à disposition de clients avant le 2026-08-02, le délai au 2026-12-02 s'appliquerait (**échéance à confirmer**) et le constat deviendrait « Non encore applicable ».
- **Conditions et exceptions** : Exceptions de l'art. 50, par. 2 (mise en forme standard, absence de modification substantielle, usage répressif) : écartées (images nouvelles). Le règlement ne fixe pas de format unique ; l'incertitude sur les modalités n'est pas une exemption et est consignée en NV-04. Le projet cite le C2PA et l'IPTC comme cibles, ce qui est cohérent avec les références, mais seuls les champs texte sont réellement présents dans le code.
- **Explication** : Pour qu'une image soit reconnue comme générée par IA par des outils, le marquage doit être lisible par machine et difficile à perdre. Ici, l'étiquette est inscrite dans des champs texte libres que la plupart des outils de détection ne lisent pas et qui disparaissent à la moindre conversion. Une mesure existe, mais rien ne démontre qu'elle suffit ; c'est un risque potentiel de manquement à l'art. 50, par. 2, à confirmer.
- **Recommandation** : Écrire les métadonnées dans un format normalisé (paquet XMP avec `Iptc4xmpExt:DigitalSourceType` conforme au vocabulaire IPTC) en complément du manifeste C2PA signé ; ajouter une couche de filigrane ou d'empreinte si le fournisseur d'images le permet ; créer des tests automatisés de bout en bout (redimensionnement, recompression, conversion JPEG/WebP) ; documenter un outil de vérification (obligation au titre de l'art. 50, par. 2 ; choix techniques = bonne pratique).
- **Méthode de vérification** : Générer une image de test (environnement de recette), vérifier avec un outil C2PA et un lecteur XMP/IPTC, rejouer après recompression ; rapport de tests archivé.

### AIA-003 : SYS-01 et SYS-02, textes générés sans aucun marquage (art. 50, par. 2) : obligation non encore applicable, modalités incertaines
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel (principal) ; SYS-02 Correction assistée (justification textuelle)
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification) / Faible (modalités techniques et date de mise sur le marché non vérifiée)
- **Preuve observée** : *Fait observé* : `answer()` retourne `response.content[0].text` sans métadonnée, drapeau ni structure de provenance ; `propose_grade()` conserve la justification en mémoire dans un `GradeProposal` sans marquage. Les seuls chemins de sortie visibles dans le code sont la valeur de retour des fonctions ; le canal réel (interface web, API, copier-coller, export) est hors dépôt. Le projet renvoie l'analyse de l'art. 50, par. 2 pour le texte aux lignes directrices de la Commission (`classification-assessment.md:21-22`) sans trancher. *Analyse juridique* : absence de marquage de textes générés, obligation du fournisseur, non encore exigible à la date d'audit. [PRV-004, PRV-005]
- **Fichier(s) et lignes** : `app/tutor_chat.py:24-32` ; `app/grading.py:33-55` ; `docs/classification-assessment.md:21-22`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA (susceptible)
- **Classification du système** : SYS-01 non à haut risque (motivé) ; SYS-02 haut risque probable
- **Référence juridique** : Art. 50, par. 2 `[TI]`, délai au 2026-12-02 `[O26]` ; lignes directrices art. 50 (20.7.2026 selon les sources) `[AV]` pour les modalités ; [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50).
- **Date d'application** : CAL-010 : pour des systèmes mis sur le marché avant le 2026-08-02 (SYS-01 et SYS-02 : 2026-03-01, déclaré), l'obligation serait applicable **à compter du 2026-12-02 (dans 36 jours), sous réserve de confirmation sur le texte officiel** : **échéance à confirmer**. Si la date de mise sur le marché était postérieure au 2026-08-02, l'obligation serait déjà en vigueur.
- **Conditions et exceptions** : Exceptions (assistance à la mise en forme standard, absence de modification substantielle des données d'entrée ou de leur sémantique) : non retenues, le tuteur et la justification de notation créent du contenu nouveau. L'incertitude sur les modalités de marquage d'un texte (format, lignes directrices) **n'est pas une exemption** ; elle est consignée en NV-04. Limite connue : le marquage d'un texte copié-collé est généralement perdu et la limite doit être documentée.
- **Explication** : Le règlement vise aussi les textes produits par une IA, y compris les réponses de chatbot. Aucun mécanisme de marquage n'existe aujourd'hui dans ce code. L'obligation n'est pas encore exigible pour ces deux systèmes si leur date de mise sur le marché est confirmée, mais l'échéance est proche, et les modalités restent à préciser.
- **Recommandation** : Avant 2026-12-02 : choisir une solution de provenance pour les sorties textuelles (champ de provenance dans la réponse d'API, en-tête, métadonnées d'export des documents, mention de limite pour le copier-coller) en s'appuyant sur les lignes directrices et le code de bonnes pratiques une fois confirmés ; inventorier les chemins de sortie dans `templates/data-flow-map.md` ; documenter les exceptions éventuelles avec motivation (préparation d'une obligation à venir).
- **Méthode de vérification** : Revue des chemins de sortie (API, interface, export) ; test montrant la présence du marqueur dans la réponse ; décision écrite sur le traitement du copier-coller ; confirmation du texte officiel et de la date de mise sur le marché.

### AIA-004 : SYS-02, contrôle humain présent mais effectivité non démontrée
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification)
- **Preuve observée** : *Fait observé* : (1) mesures **présentes** : statut initial `pending_review`, motif obligatoire pour modifier (`grading.py:61-62`), rejet possible, journalisation de la décision (`grading.py:65-66`), refus de publication sans `validated_by` (`gradebook.py:6-7`). (2) Points de fragilité : `validated_by` est une chaîne libre fournie par l'appelant, testée seulement par `if not validated_by`, sans authentification ni contrôle de rôle ; `publish_grade` est appelable directement, sans lien avec une proposition revue ; `review_grade` ne vérifie pas que la proposition est encore en `pending_review` (double validation possible, `publish_grade` ajoute une entrée à chaque appel) ; le rejet n'exige aucun motif ; aucun garde-fou technique n'impose l'affichage de la justification ou de la copie (la procédure l'exige, l'interface n'est pas dans le projet) ; aucun indicateur de taux de modification n'est calculé (revue trimestrielle organisationnelle, non observable). *Analyse juridique* : indices d'un contrôle susceptible d'être de pure forme (`person-decisions.md`, section 4), à confirmer. [PRV-011, PRV-013, PRV-016, PRV-017, PRV-018]
- **Fichier(s) et lignes** : `app/grading.py:58-69` ; `app/gradebook.py:5-8` ; `docs/human-oversight-procedure.md:1-12` ; `docs/risk-register.md:5-6`
- **Rôle réglementaire concerné** : Fournisseur (art. 14) ; établissements déployeurs (art. 26, par. 2)
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 14, par. 4, b) et d) ; art. 26, par. 2 `[TI]` ; dates `[O26]` ; [AI Act Explorer, art. 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14).
- **Date d'application** : CAL-011 : art. 14 applicable, au conditionnel, à compter du 2027-12-02 sous réserve de confirmation (**échéance à confirmer**) ; CAL-013 conditionnel. Le risque pour les élèves existe dès aujourd'hui, d'où la nature « Risque potentiel » et non un manquement à l'art. 14.
- **Conditions et exceptions** : Aucune exception. La procédure de supervision (`docs/human-oversight-procedure.md`) et le plan de formation constituent des éléments organisationnels dont l'exécution n'est pas démontrable par le projet (NV-11, NV-12).
- **Explication** : Le principe « le modèle propose, l'enseignant décide » est bien codé. Mais le code ne vérifie pas qui valide, ne lie pas la publication à la proposition revue et peut être contourné par un appel direct. Un contrôle humain n'est utile que s'il est identifiable, authentifié et réellement exercé.
- **Recommandation** : Faire dépendre `publish_grade` de l'état `approved/overridden` d'une proposition identifiée (et non d'une chaîne libre), authentifier l'enseignant côté API et vérifier son droit sur la classe, refuser une seconde validation, rendre idempotente la publication, exiger un motif pour le rejet, journaliser le temps passé et calculer le taux de modification (préparation de l'art. 14 ; bonne pratique immédiate).
- **Méthode de vérification** : Tests unitaires et d'intégration couvrant appel direct, double validation, utilisateur non autorisé ; extrait du rapport trimestriel d'écarts ; démonstration de l'écran de validation (capture).

### AIA-005 : SYS-02, validation insuffisante des sorties du modèle et des notes finales : publication possible d'une note vide
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Constat technique avéré
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits, établis par lecture, code non exécuté) / Moyenne (portée juridique)
- **Preuve observée** : *Fait observé* : (1) `json.loads(response.content[0].text)` sans gestion d'erreur : une réponse non JSON ou mal formée lève une exception non gérée ; (2) `data["note"]` n'est ni typée, ni bornée à [0, 20], ni comparée à la somme des critères ; (3) dans `review_grade`, avec `decision="override"`, `final_grade` vaut `None` par défaut : le test ne contrôle que le motif ; `publish_grade(student_id, None, validated_by=reviewer_id)` est alors appelé et la valeur `None` est enregistrée au carnet ; aucune borne n'est appliquée aux notes saisies par l'enseignant. *Analyse juridique* : défaut de robustesse, pertinent au regard des exigences d'exactitude et de robustesse du haut risque, non encore applicables. [PRV-015]
- **Fichier(s) et lignes** : `app/grading.py:42-48, 58-68` ; `app/gradebook.py:5-8`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 15 (exactitude, robustesse) ; art. 14, par. 4, a) `[TI]`, dates `[O26]` ; [AI Act Explorer, art. 15](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15) (lien à confirmer).
- **Date d'application** : CAL-011 : à compter du 2027-12-02, au conditionnel, sous réserve de confirmation (**échéance à confirmer**). La correction du défaut est une bonne pratique immédiate.
- **Conditions et exceptions** : Le fichier est décrit comme « fixture » (stockage en mémoire) ; la portée en production dépend de l'implémentation réelle (couche d'interface absente du projet). Aucune exception.
- **Explication** : Une réponse du modèle mal formée ou une saisie incomplète de l'enseignant peut produire une erreur ou une note vide dans le carnet. Ce n'est pas un défaut juridique en soi aujourd'hui, mais c'est précisément le type de faiblesse que les exigences de robustesse visent.
- **Recommandation** : Valider le schéma de sortie du modèle (types, bornes, cohérence critères/note), gérer les erreurs par une file de revue manuelle, imposer une note valide pour `override`, borner les notes dans `publish_grade`, ajouter des tests (bonne pratique ; préparation de l'art. 15).
- **Méthode de vérification** : Tests unitaires : réponse non JSON, note hors bornes, `override` sans note ; revue du code corrigé.

### AIA-006 : SYS-02, performances et biais connus mais non traités ; campagne d'évaluation tardive
- **Système d'IA concerné** : SYS-02 Correction assistée
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Moyenne (faits déclarés dans la documentation, preuves d'évaluation non disponibles) / Moyenne (qualification)
- **Preuve observée** : *Fait observé (document du projet)* : écart moyen de 1,4 point sur 20 par rapport à deux enseignants, écart supérieur à 3 points sur 7 % des copies (campagne de septembre 2026, 400 copies) ; performances non mesurées sur copies manuscrites numérisées et élèves allophones ; risque de biais lié au style rédactionnel non évalué (`technical-documentation.md:15-19`) ; évaluation dédiée du biais prévue T1 2027 (`risk-register.md:7`, `classification-assessment.md:35`). La campagne citée est postérieure à la mise sur le marché du 2026-03-01 (déclarée). Aucun test automatisé ni rapport d'évaluation dans le projet. *Analyse juridique* : limites identifiées et en cours de traitement, évaluation par sous-groupes non réalisée à la date d'audit. [PRV-021]
- **Fichier(s) et lignes** : `docs/technical-documentation.md:15-19` ; `docs/risk-register.md:7-8` ; `docs/classification-assessment.md:35`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 9, 10, 15 ; annexe IV, points 2 et 3 `[TI]`, dates `[O26]` ; art. 10, par. 5 `[AV]` (traitement de données sensibles pour la détection des biais, ne pas invoquer sans vérification).
- **Date d'application** : CAL-011 : 2027-12-02 au conditionnel, sous réserve de confirmation (**échéance à confirmer**) ; CAL-013 conditionnel.
- **Conditions et exceptions** : Aucune exception. Le chiffrage de l'écart (1,4 point) n'est pas évalué ici : aucun seuil d'acceptation n'est défini dans les documents.
- **Explication** : Le projet est transparent sur ses limites, ce qui est une bonne chose. Mais il note déjà des élèves réels avec un outil dont la fiabilité sur certains profils (allophones, copies manuscrites) n'a pas été mesurée, et sans seuil d'acceptation documenté. Le risque porte sur l'équité du traitement des élèves.
- **Recommandation** : Avancer, si possible, la campagne par sous-groupes avant T1 2027 ; fixer des critères d'acceptation (écart moyen, taux d'écart élevé) et un seuil de retrait ; informer les enseignants clients des limites connues dans la notice (préparation des art. 9, 10, 13 et 15 ; bonne pratique immédiate pour l'information des utilisateurs).
- **Méthode de vérification** : Rapports d'évaluation datés, protocole, composition des jeux de données ; seuils d'acceptation approuvés ; notice contenant les limites.

### AIA-007 : SYS-02 (et SYS-01), journalisation partielle : explication, intégrité et rétention non assurées par le code
- **Système d'IA concerné** : SYS-02 Correction assistée ; SYS-01 (journal du tuteur)
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification)
- **Preuve observée** : *Fait observé* : (1) `AUDIT_LOG_RETENTION_DAYS = 400` est défini mais **n'est référencé nulle part** dans le code (recherche exhaustive) : aucune purge ni contrôle de conservation ; (2) le journal est un fichier JSONL ouvert en mode `"a"` (« append-only » au sens applicatif, sans protection d'intégrité, contrôle d'accès ni chaînage) à un chemin relatif `var/audit_log.jsonl` ; (3) l'événement `grade_proposed` enregistre la note proposée, la version du modèle et la version de la grille, mais ni la justification, ni les critères, ni une empreinte de la copie ; ces éléments ne sont conservés que dans l'objet en mémoire ; (4) `PROMPT_VERSION` est une constante manuelle distincte du texte de `RUBRIC` et du prompt système (`grading.py:17, 38-39`) : une modification du prompt sans mise à jour de la constante ne serait pas détectée ; (5) le tuteur ne journalise que `model_version`. Mesures **présentes** : `trace_id`, horodatage, `model_version`, `prompt_version`, décision et motif de l'enseignant. Le registre indique « Journal d'audit en place » (`classification-assessment.md:36`). *Analyse juridique* : traçabilité présente mais incomplète pour reconstituer et expliquer une décision. [PRV-023, PRV-024, PRV-025, PRV-026]
- **Fichier(s) et lignes** : `app/audit_log.py:7-16` ; `app/config.py:7-8` ; `app/grading.py:17, 38-39, 51-54, 65-66` ; `app/tutor_chat.py:31`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs (art. 26, par. 6) pour les journaux sous leur contrôle
- **Classification du système** : Haut risque probable (SYS-02) ; non à haut risque (SYS-01 : bonne pratique)
- **Référence juridique** : Art. 12, 19, 26, par. 6, art. 86 `[TI]`, dates `[O26]` et `[AV]` pour l'art. 86 ; [AI Act Explorer, art. 12](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12) (lien à confirmer).
- **Date d'application** : CAL-011 : 2027-12-02 au conditionnel, sous réserve de confirmation (**échéance à confirmer**) ; art. 86 : à vérifier (`[AV]`). Hors RGPD (hors périmètre) : le journal contient des identifiants d'élèves.
- **Conditions et exceptions** : Pour SYS-01, simple bonne pratique. La durée de 400 jours dépasse le minimum de six mois fixé par l'art. 19 (applicable au haut risque) : la durée choisie n'est pas critiquée, c'est son application effective qui n'est pas démontrée.
- **Explication** : Le projet enregistre l'essentiel (qui, quand, quel modèle, quelle décision), mais pas tout ce qu'il faudrait pour expliquer a posteriori une note à un élève, et la durée de conservation affichée n'est pas appliquée par le code. L'intégrité du journal repose sur la bonne volonté de l'application.
- **Recommandation** : Journaliser une empreinte de la copie, les critères et la justification (ou une référence stable) ; versionner le prompt et la grille par empreinte ; imposer la rétention et l'intégrité (stockage en écriture seule, permissions, chaînage) ; documenter l'emplacement et les accès du journal (préparation des art. 12, 19, 86 ; bonne pratique immédiate).
- **Méthode de vérification** : Rejouer un cas de test et reconstituer la décision depuis le journal seul ; revue de la configuration de stockage de production ; test de la purge.

### AIA-008 : SYS-03, chaîne de marquage fragile : manifeste C2PA absent du projet, échec non géré, marquage amont non préservé
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : Constat technique avéré
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée (faits) / Moyenne (portée en production)
- **Preuve observée** : *Fait observé* : (1) `attach_c2pa_manifest` lève `NotImplementedError` (« effectuée par l'outil interne en production ») : aucun manifeste n'est produit par le code audité ; (2) dans `create_illustration`, l'image est enregistrée (`image.save`, ligne 26) **avant** l'appel au manifeste (ligne 27) et avant le journal (ligne 28), sans gestion d'exception : en cas d'échec, un fichier partiellement marqué subsiste sans événement d'audit ; (3) l'image est reconstruite par Pillow (`generate_image` retourne un objet `Image`, ré-enregistré avec de nouvelles métadonnées) : tout manifeste ou métadonnée conteneur ajouté en amont par le fournisseur d'images ne serait pas préservé, sauf filigrane dans les pixels (impossible à vérifier, `image_provider.py` est un bouchon) ; (4) la valeur `ai_disclosure` n'est qu'un champ texte : aucune mention visible n'est incrustée dans l'image. *Analyse juridique* : mesure annoncée mais non démontrable, continuité du marquage non établie. [PRV-007, PRV-008]
- **Fichier(s) et lignes** : `app/illustrations.py:20-29` ; `app/c2pa_signer.py:5-6` ; `app/image_provider.py:5-6`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA (susceptible)
- **Classification du système** : Non à haut risque (motivé) ; art. 50, par. 2
- **Référence juridique** : Art. 50, par. 2 `[TI]` ; délai `[O26]` ; [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50).
- **Date d'application** : CAL-010 : en vigueur depuis le 2026-08-02 si la date de mise sur le marché (2026-09-15, déclarée) est exacte (NV-01) ; sinon échéance 2026-12-02 (**échéance à confirmer**).
- **Conditions et exceptions** : Les modules `c2pa_signer.py` et `image_provider.py` sont des bouchons annoncés (« non inclus dans la fixture ») : le comportement de production peut être correct. Le constat porte sur ce qui est démontrable et sur l'ordre des opérations, qui est une faiblesse indépendante de la production.
- **Explication** : Dans le code audité, le marquage « fort » promis n'existe pas, et un échec lors de la signature laisse une image sur disque sans trace. Le marquage éventuellement appliqué par le fournisseur d'images en amont risque d'être effacé par le ré-encodage.
- **Recommandation** : Faire échouer proprement la chaîne (écrire dans un fichier temporaire, signer, puis publier et journaliser seulement en cas de succès) ; fournir la preuve de l'outil C2PA (tests, clés, vérificateur) ; tester la préservation du marquage amont et ajouter un filigrane ou une empreinte si possible ; fournir une option de mention visible pour les déployeurs (obligation au titre de l'art. 50, par. 2 ; choix techniques = bonne pratique).
- **Méthode de vérification** : Test de bout en bout avec échec simulé de la signature ; contrôle du manifeste par un vérificateur C2PA ; test de préservation du marquage amont.

### AIA-009 : SYS-03, garde-fous de prompts et de sorties non retrouvés dans le code, à l'approche des nouvelles interdictions de l'article 5
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Moyenne (faits) / Faible (qualification : numérotation et portée des nouvelles interdictions `[AV]`)
- **Preuve observée** : *Fait observé* : le registre des risques indique, pour le risque R-05 (« image trompeuse représentant une personne réelle »), la mesure « consigne d'étiquetage, **filtre de prompts** » avec le statut « En place » (`risk-register.md:9`). `create_illustration` transmet le `prompt` tel quel à `generate_image` (`illustrations.py:20-21`) : aucun filtre de prompt ni contrôle de sortie n'y figure ; le seul emplacement possible est le service d'images (bouchon, non audité). *Analyse juridique* : les nouvelles interdictions (contenus intimes non consentis de personnes identifiables, matériel pédopornographique) s'appliqueraient aux systèmes génératifs à compter du 2026-12-02 ; un défaut de garde-fou est, avant cette date, « non encore applicable » au titre de l'art. 5. Le risque d'hypertrucage de personnes réelles relève déjà de l'art. 50, par. 4 (déployeurs). [PRV-035]
- **Fichier(s) et lignes** : `app/illustrations.py:20-29` ; `app/image_provider.py:5-6` ; `docs/risk-register.md:9`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA ; déployeurs (art. 50, par. 4)
- **Classification du système** : Non à haut risque (motivé) ; pratique interdite non retenue à ce jour
- **Référence juridique** : Art. 5, par. 1, nouveaux points (numérotation `[AV]`) `[O26]` ; art. 50, par. 4 `[TI]` ; [AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5).
- **Date d'application** : CAL-004 : applicable, au conditionnel, à compter du 2026-12-02 (dans 36 jours), sous réserve de confirmation sur le texte officiel : **échéance à confirmer**.
- **Conditions et exceptions** : Le risque dépend du fournisseur d'images (filtres intégrés éventuels), des utilisateurs (enseignants authentifiés) et de l'absence de téléversement d'image source (aucun dans le code). L'art. 5, par. 1, b) (vulnérabilités, élèves mineurs) est examiné et non retenu. Le texte ne retient pas ici d'exemption.
- **Explication** : Le projet affirme qu'un filtre de prompts est en place, mais le code audité n'en contient aucun. Il peut se trouver chez le fournisseur d'images ; il faut le démontrer avant le 2 décembre 2026, date à laquelle de nouvelles interdictions concernant les images générées devraient s'appliquer.
- **Recommandation** : Documenter et tester le filtrage (prompts et sorties) de bout en bout, journaliser les refus, prévoir une politique d'usage et un moyen de signalement ; obtenir du fournisseur d'images la description de ses garde-fous (préparation de l'art. 5 ; bonne pratique pour le reste).
- **Méthode de vérification** : Jeux de tests de prompts interdits en recette ; extrait de la documentation du fournisseur ; confirmation du texte officiel et de la numérotation.

### AIA-010 : SYS-03, mention visible « Image générée par IA » présente seulement dans les métadonnées
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne
- **Preuve observée** : *Fait observé* : `VISIBLE_LABEL` est utilisé uniquement comme valeur du champ texte `ai_disclosure` ; aucune incrustation dans l'image. Le docstring annonce une mention visible « sur les supports publiés » et le projet indique une consigne aux enseignants dans le guide utilisateur (`classification-assessment.md:26-28`) ; le guide n'est pas dans le projet. *Analyse juridique* : l'obligation de déclaration des hypertrucages incombe au déployeur ; le fournisseur peut l'outiller. [PRV-010]
- **Fichier(s) et lignes** : `app/illustrations.py:3-6, 16, 24` ; `docs/classification-assessment.md:26-28`
- **Rôle réglementaire concerné** : Déployeur (établissements, enseignants) ; fournisseur (outillage)
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : Art. 50, par. 4, al. 1 et par. 5 `[TI]`.
- **Date d'application** : CAL-009 : en vigueur depuis le 2026-08-02 (confiance élevée).
- **Conditions et exceptions** : L'obligation ne vise que les contenus qui constituent des hypertrucages (ressemblance avec des personnes, lieux ou événements réels, pouvant être perçus à tort comme authentiques). De simples illustrations de cours peuvent ne pas en être ; le régime allégé pour les œuvres manifestement créatives ou fictionnelles est à documenter. Aucune exception n'est invoquée par le projet.
- **Explication** : La mention visible n'existe pas dans l'image elle-même ; elle dépend des supports finaux et de la consigne donnée aux enseignants. Rien dans le projet ne permet de vérifier l'une ou l'autre.
- **Recommandation** : Proposer une option d'incrustation d'une mention visible et accessible (contraste, texte alternatif) dans l'outil ; fournir le guide utilisateur et la consigne (outillage du déployeur ; art. 50, par. 4 et 5 pour l'obligation).
- **Méthode de vérification** : Guide utilisateur ; capture d'un support publié ; test de l'option d'incrustation.

### AIA-011 : SYS-01 et SYS-02, identifiant de modèle sans version datée et valeur de production inconnue
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel ; SYS-02 Correction assistée
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne (le caractère mobile de l'identifiant sans suffixe daté est à confirmer auprès du fournisseur de modèle, documentation non consultée)
- **Preuve observée** : *Fait observé* : valeurs par défaut `claude-sonnet-4-5` pour le tuteur et la notation, surchargeables par variables d'environnement ; la version effectivement servie (`response.model`) est journalisée (`grading.py:48, 52` ; `tutor_chat.py:31`). Le registre des risques qualifie le risque de changement de version de « Partiel » (R-06). La valeur configurée en production est inconnue. [PRV-019, PRV-024]
- **Fichier(s) et lignes** : `app/config.py:5-6` ; `app/grading.py:48-52` ; `app/tutor_chat.py:31` ; `docs/risk-register.md:10`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA
- **Classification du système** : Non à haut risque (SYS-01) ; haut risque probable (SYS-02)
- **Référence juridique** : Aucune (bonne pratique) ; en lien avec annexe IV, points 1 et 6, et art. 111, par. 2 `[AV]` / art. 25 pour la qualification d'une modification de modèle sur SYS-02.
- **Date d'application** : Bonne pratique immédiate ; art. 111, par. 2 : CAL-013 conditionnel (**échéance à confirmer**).
- **Conditions et exceptions** : Mesure atténuante : la version servie est journalisée. Un changement de modèle sur SYS-02 peut constituer une modification importante ou substantielle (voir AIA-001).
- **Explication** : Si l'identifiant n'est pas figé sur une version datée, le comportement de la notation peut évoluer sans décision de l'éditeur, ce qui complique la validation, la comparaison et la qualification des modifications.
- **Recommandation** : Épingler une version datée en production, la consigner dans la documentation technique à chaque campagne d'évaluation et bloquer les changements non qualifiés (bonne pratique).
- **Méthode de vérification** : Valeur des variables d'environnement de production ; test automatique refusant un identifiant non épinglé.

### AIA-012 : Mesures de maîtrise de l'IA documentées mais exécution non vérifiable
- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Moyenne
- **Preuve observée** : `docs/ai-literacy-plan.md` décrit une formation annuelle du personnel (registre RH « non inclus dans le dépôt ») et un module de deux heures pour les enseignants des établissements clients, mis à jour le 2026-09-01. Ni le contenu de la formation, ni le registre, ni le guide utilisateur ne sont dans le projet. [PRV-031]
- **Fichier(s) et lignes** : `docs/ai-literacy-plan.md:1-6`
- **Rôle réglementaire concerné** : Fournisseur ; établissements déployeurs
- **Classification du système** : Tous
- **Référence juridique** : Art. 4 (rédaction modifiée) `[TI]` + `[O26]` ; aucun niveau déterminé de compétence exigé selon les sources.
- **Date d'application** : CAL-002 : en vigueur depuis le 2025-02-02 ; nouvelle rédaction CAL-003 : 2026-07-27 (présumée), **échéance à confirmer**.
- **Conditions et exceptions** : Aucune exception. Le régime de sanction de l'art. 4 relève du droit national `[AV]` (aucune amende n'est chiffrée ici).
- **Explication** : Un plan existe et vise bien le personnel et les enseignants utilisateurs. Sa mise en œuvre est organisationnelle et ne se vérifie pas dans un projet de code.
- **Recommandation** : Conserver un registre de suivi (bonne pratique, aucun niveau déterminé requis) ; étendre le plan aux prestataires agissant pour le compte de la société ; remettre aux déployeurs un guide d'usage dans l'interface (bonne pratique contribuant à l'art. 4).
- **Méthode de vérification** : Registre de formation, support de cours, guide utilisateur.

### AIA-013 : Historique de la surveillance d'examens par webcam supprimée non documenté
- **Système d'IA concerné** : Aucun système actuel ; fonctionnalité passée à qualifier (hors SYS-01 à SYS-03)
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Faible
- **Niveau de confiance** : Faible
- **Preuve observée** : Le README déclare que la surveillance d'examens par analyse de webcam « a été supprimée » sans date, sans description du traitement ni liste des clients concernés (`README.md:14`). Le code actuel (`exam_events.py`) ne contient aucune inférence. Le projet ne contient pas d'historique. [PRV-033]
- **Fichier(s) et lignes** : `README.md:14` ; `app/exam_events.py:1-10`
- **Rôle réglementaire concerné** : Fournisseur (susceptible) pour la fonctionnalité passée
- **Classification du système** : Indéterminée (fonctionnalité supprimée)
- **Référence juridique** : Art. 5, par. 1, f) ; annexe III, point 3, d) et point 1 `[TI]` ; [AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5).
- **Date d'application** : CAL-002 : l'art. 5, par. 1, f) est applicable depuis le 2025-02-02, sans régime transitoire.
- **Conditions et exceptions** : Si la fonctionnalité n'inférait pas d'émotions (simple détection de présence, par exemple) et n'utilisait pas de biométrie, aucune interdiction ne serait en cause ; elle relèverait alors éventuellement de l'annexe III, point 3, d). L'exception médicale ou de sécurité est d'interprétation stricte et ne couvre pas la lutte contre la fraude.
- **Explication** : Rien n'indique une pratique interdite. Mais l'art. 5 n'a pas de période transitoire : si cette fonctionnalité a fonctionné chez des clients après le 2 février 2025 et analysait des émotions, la question se poserait pour la période concernée. Cette question ne peut être levée que par l'organisation.
- **Recommandation** : Documenter la date de retrait, la nature des traitements (émotions, biométrie ou non) et les clients concernés ; conserver cette note dans le dossier de conformité (obligation de qualification en cas de pratique concernée ; sinon bonne pratique).
- **Méthode de vérification** : Note interne datée, historique des versions et des livraisons.

### AIA-014 : SYS-01, information d'interaction avec une IA et refus de se présenter comme humain présents dans le code
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel
- **Nature du constat** : Constat technique avéré
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits) / Moyenne (effectivité)
- **Preuve observée** : `AI_DISCLOSURE` (« Vous échangez avec un assistant d'IA (et non avec un enseignant)... ») est retourné par `start_session()` « avant la première interaction » ; le prompt système impose de répondre clairement être une IA si on le demande (`tutor_chat.py:9-21`). *Limites* : aucune route ni interface n'appelle `start_session()` ; `answer()` peut être appelé sans session ; l'affichage effectif, l'accessibilité et la couverture de tous les canaux ne sont pas observables ; le comportement réel du modèle face à la question « es-tu humain ? » n'est pas testé (aucun test). [PRV-001, PRV-002, PRV-003]
- **Fichier(s) et lignes** : `app/tutor_chat.py:9-21`
- **Rôle réglementaire concerné** : Fournisseur du système d'IA
- **Classification du système** : Non à haut risque (motivé)
- **Référence juridique** : Art. 50, par. 1 et 5 `[TI]`.
- **Date d'application** : CAL-009 : en vigueur depuis le 2026-08-02 (confiance élevée).
- **Conditions et exceptions** : Exception « évident » non invoquée. Aucun manquement n'est retenu ; la mesure est présente, son effectivité reste à démontrer (NV-03).
- **Explication** : Le code prévoit un message d'information clair avant la première interaction et ne dissimule pas la nature d'IA du tuteur. Il reste à prouver qu'il s'affiche réellement sur chaque canal.
- **Recommandation** : Rendre l'affichage non contournable (l'API refuse `answer()` sans session initialisée) ; ajouter un test sur la question « es-tu humain ? » ; vérifier l'accessibilité du message (art. 50, par. 5).
- **Méthode de vérification** : Capture de l'interface ; test d'API ; test de comportement en recette.

### AIA-015 : Absence de reconnaissance des émotions et de traitement biométrique ; événements d'examen sans IA
- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03 (et composant écarté `exam_events.py`)
- **Nature du constat** : Constat technique avéré
- **Gravité** : Information
- **Niveau de confiance** : Élevée (faits statiques) / Moyenne (périmètre : production non observée)
- **Preuve observée** : `requirements.txt` ne contient que `fastapi`, `anthropic`, `pillow` ; aucune bibliothèque de vision, de biométrie ou d'analyse émotionnelle ; `exam_events.py` ne fait qu'appeler `log_event("exam_event", exam_id, student_id, detail)` ; le scanner ne détecte aucun signal biométrique. Aucun appel croisé entre le tuteur et la notation. [PRV-027, PRV-034]
- **Fichier(s) et lignes** : `requirements.txt:1-3` ; `app/exam_events.py:1-10` ; `app/tutor_chat.py:1-7` ; `app/grading.py:9-15`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non applicable à l'art. 5, par. 1, f) sur le dépôt
- **Référence juridique** : Art. 5, par. 1, f) et g) ; annexe III, point 1 `[TI]`.
- **Date d'application** : CAL-002 : en vigueur depuis le 2025-02-02.
- **Conditions et exceptions** : Les événements d'examen contiennent l'identifiant de l'élève et alimentent le même journal que SYS-02 : si ces événements servaient un jour à inférer un comportement (suspicion de fraude), le composant relèverait de l'annexe III, point 3, d) et devrait être reclassé.
- **Explication** : Sur ce qui est observable, le produit n'analyse ni émotions ni données biométriques, et la surveillance d'examen est limitée à des événements techniques transmis à des surveillants humains.
- **Recommandation** : Inscrire dans la procédure de développement l'obligation de qualification de tout nouveau traitement lié aux examens (bonne pratique) ; ne pas réutiliser les événements d'examen pour une décision automatisée sans reclassement.
- **Méthode de vérification** : Revue des dépendances à chaque version ; relecture des consommateurs du journal.

### AIA-016 : Obligations des fournisseurs de modèles GPAI (art. 51 à 55) non applicables à EduAssist
- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Moyenne (le projet ne contient aucun script d'entraînement ou d'affinage ; les déclarations du README ne sont pas vérifiables en dehors du dépôt)
- **Preuve observée** : README : « EduAssist n'entraîne aucun modèle » ; inventaire : modèles de tiers utilisés via API, sans modification ni mise sur le marché ; aucun script `train`, `fine_tune`, aucun poids dans le projet. [PRV-019]
- **Fichier(s) et lignes** : `README.md:13` ; `docs/ai-system-inventory.md:11-12` ; `requirements.txt:1-3`
- **Rôle réglementaire concerné** : Fournisseur de système d'IA, pas fournisseur de modèle GPAI
- **Classification du système** : Sans objet pour la classification GPAI
- **Référence juridique** : Art. 3, points 3, 63 et 68 ; art. 53 `[TI]`.
- **Date d'application** : CAL-005 : sans objet.
- **Conditions et exceptions** : À reconsidérer en cas d'affinage significatif ou de publication d'un modèle. EduAssist reste fournisseur en aval : elle doit disposer de la documentation du fournisseur du modèle (annexe XII) pour ses propres obligations (NV-08).
- **Explication** : Utiliser une API de modèle ne fait pas d'EduAssist un fournisseur de modèle GPAI.
- **Recommandation** : Conserver la documentation reçue du fournisseur de modèle (bonne pratique, utile à l'art. 11 et à l'art. 13 si haut risque).
- **Méthode de vérification** : Contrat et documentation du fournisseur ; absence de pipeline d'entraînement.

## 9. Éléments non vérifiables

Registre complet en annexe D. Résumé : les informations les plus déterminantes sont les dates réelles
de mise sur le marché (NV-01), le statut public ou privé des établissements (NV-02), l'affichage
effectif des informations et des avertissements (NV-03), l'outil C2PA et le service d'images
(NV-05, NV-06, NV-07), les évaluations de performance (NV-09), l'authentification des enseignants
(NV-12) et l'historique de la surveillance webcam (NV-13).

## 10. Recommandations et plan de remédiation

Plan synthétique en annexe E. Actions P2 prioritaires : confirmer les dates de mise sur le marché ;
traiter le marquage de SYS-03 (AIA-002, AIA-008) ; choisir la solution de marquage du texte avant
le 2026-12-02 (AIA-003) ; documenter les garde-fous d'images avant le 2026-12-02 (AIA-009) ;
renforcer le contrôle humain et la validation des notes (AIA-004, AIA-005).

## 11. Limites de l'audit

- Analyse statique : comportement réel du modèle, des prompts dynamiques, des données et de la
  configuration de production non observés ; code non exécuté ; les constats AIA-004 et AIA-005
  reposent sur la lecture du code.
- Projet non versionné : aucun historique, aucun commit, impossible de dater les modifications ni de
  vérifier les dates de mise sur le marché déclarées.
- Aucun test automatisé, aucune couche API/interface, aucune authentification dans le projet ;
  `image_provider.py` et `c2pa_signer.py` sont des bouchons.
- Documents organisationnels absents : registre de formation, guide utilisateur, notice, contrats avec
  les fournisseurs, rapports d'évaluation, procédures d'incident, plan de surveillance après
  commercialisation.
- Références juridiques : aucune entrée du calendrier n'est relue sur le texte officiel. Entrées de
  confiance moyenne ou faible à confirmer sur le Journal officiel : CAL-003, CAL-004, CAL-010
  (délai transitoire), CAL-011, CAL-012, CAL-013, CAL-015, CAL-016. Numérotation des nouvelles
  interdictions, art. 111, par. 2, art. 49, par. 2 et art. 86 : `[AV]`.
- Lignes directrices, normes harmonisées, actes d'exécution et code de bonnes pratiques évolutifs ;
  lignes directrices sur l'art. 50 (20.7.2026 selon les sources) non relues.
- Protection des données personnelles (RGPD) et autres législations : hors périmètre ; le journal
  contient des identifiants d'élèves (signalé, non analysé).
- Le rapport est une aide à l'audit ; il ne remplace ni l'avis d'un juriste ni une évaluation de la
  conformité au sens de l'article 43.

## 12. Matrice des preuves

Voir annexe C.2.

## 13. Suivi (ré-audit)

Premier audit : aucun suivi à ce jour. Lors d'un ré-audit, conserver les identifiants AIA-001 à
AIA-016 et recalculer le calendrier (en particulier après le 2026-12-02, date à laquelle CAL-010
pour SYS-01/SYS-02 et CAL-004 deviendraient applicables, sous réserve de confirmation).

---

# Annexes

## Annexe A : Inventaire des systèmes d'IA

Date d'audit : 2026-10-27.

| Champ | SYS-01 | SYS-02 | SYS-03 |
|---|---|---|---|
| Nom | Tuteur conversationnel | Correction assistée | Illustrations de cours |
| Finalité (art. 3, point 12) | Aide aux révisions, réponses aux questions de cours | Proposition de note et de justification pour des dissertations ; décision finale par l'enseignant | Génération d'images pour supports pédagogiques |
| Description fonctionnelle | Appel `messages.create` avec historique et prompt système | Appel `messages.create` (`temperature=0`), analyse JSON, revue humaine, publication au carnet | Génération d'image par service tiers, ajout de métadonnées PNG, appel de signature C2PA, journal |
| Fichiers principaux | `app/tutor_chat.py` | `app/grading.py`, `app/gradebook.py` | `app/illustrations.py`, `app/image_provider.py`, `app/c2pa_signer.py` |
| Entrées | Message et historique de l'élève | Identifiant d'élève, texte de la dissertation | Prompt d'un enseignant |
| Sorties et effets | Texte (information) | Note, critères, justification (recommandation assistée ; publication après validation) | Image PNG (contenu) |
| Utilisateurs | Élèves, étudiants | Enseignants | Enseignants |
| Personnes concernées | Élèves, étudiants | Élèves, étudiants (effet sur la note) | Élèves (destinataires des supports) |
| Données pertinentes | Texte libre, possiblement données personnelles | Copies d'élèves, identifiants | Prompts ; aucune image source |
| Modèle(s) et version(s) | `claude-sonnet-4-5` (défaut ; valeur de production inconnue) | `claude-sonnet-4-5` (défaut) ; `PROMPT_VERSION = grading-rubric-v3` | Service tiers non identifié ; `model_version` retourné par le service |
| Fournisseur(s) de modèle | Anthropic (API) | Anthropic (API) | Tiers non identifié |
| Entraînement ou affinage | Non (déclaré) | Non (déclaré) | Non (déclaré) |
| Composants associés (RAG, agents) | Aucun | Aucun | Aucun |
| Acteurs et rôles | EduAssist fournisseur ; établissements déployeurs | Idem | Idem |
| Date de mise sur le marché | 2026-03-01 (déclarée) | 2026-03-01 (déclarée) | 2026-09-15 (déclarée) |
| Classification | Non à haut risque (motivé) | Haut risque probable | Non à haut risque (motivé) |
| Confiance | Moyenne | Élevée (faits) / Moyenne | Moyenne |
| Statut | Fixture : en production selon le README ; inconnu | Idem | Idem ; bouchons |
| Informations manquantes | Affichage, canaux, réutilisation des échanges | Interface, authentification, statut des clients, évaluations | Service d'images, outil C2PA, filtres, guide |

## Annexe B : Analyse de classification

| Étape | SYS-01 | SYS-02 | SYS-03 |
|---|---|---|---|
| 0. Système d'IA (art. 3, point 1) | Oui (inférence par modèle) | Oui | Oui |
| 1. Exclusion art. 2 | Aucune | Aucune | Aucune |
| 2. Art. 5 | Rien de plausible (a) et b) examinés) | Rien de plausible | Rien de plausible à ce jour ; nouvelles interdictions au 2026-12-02 (AIA-009) |
| 3. Annexe I | Non | Non | Non |
| 4. Annexe III | Non | Oui, point 3, b) | Non |
| 5a. Profilage | n.a. | Probable (évaluation de la performance de personnes) | n.a. |
| 5b. Art. 6, par. 3 | n.a. | Non retenue (influence substantielle) | n.a. |
| 6. Art. 50 | Par. 1 (présent) ; par. 2 (AIA-003) | Par. 2 (AIA-003) | Par. 2 (AIA-002, AIA-008) ; par. 4 (déployeurs, AIA-010) |
| 7. GPAI | Non | Non | Non |
| 8. Art. 4 | Oui (AIA-012) | Oui | Oui |
| **Conclusion** | Non à haut risque (motivé) | Haut risque probable | Non à haut risque (motivé) |
| Hypothèses alternatives | Hybride si les échanges alimentaient une évaluation (NV-15) | Si la sortie était purement informative : art. 6, par. 3, d), mais le profilage l'exclut | Hypertrucage si des personnes réelles sont représentées |

## Annexe C : Matrice des obligations et des preuves

### C.1 Matrice des obligations (extrait des contrôles activés)

États : Démontré / Non démontré / Non applicable / Impossible à vérifier. « Démontré » signifie
mesure observée, non obligation satisfaite.

| Système | Rôle | Obligation | Référence | Base | Statut temporel (CAL) | Contrôle | État | Preuves | Vérifications restantes | Constat(s) |
|---|---|---|---|---|---|---|---|---|---|---|
| SYS-01 | Fournisseur | Information d'interaction avec une IA (mesure dans le code) | Art. 50, par. 1 et 5 | Obligation | En vigueur (CAL-009) | A1a | Démontré | PRV-001 | | AIA-014 |
| SYS-01 | Fournisseur | Affichage effectif avant la première interaction, tous canaux, accessible | Art. 50, par. 1 et 5 | Obligation | En vigueur (CAL-009) | A1b, A11 | Impossible à vérifier | PRV-002 | Interface, canaux, accessibilité | AIA-014 |
| SYS-01 | Fournisseur | Ne pas se présenter comme humain | Art. 50, par. 1 | Obligation | En vigueur (CAL-009) | A2 | Démontré (instruction de prompt) | PRV-003 | Test de comportement | AIA-014 |
| SYS-01, SYS-02 | Fournisseur | Marquage des textes générés | Art. 50, par. 2 | Obligation | Non encore applicable, échéance à confirmer (CAL-010, 2026-12-02) | A4, A7 | Non démontré | PRV-004, PRV-005 | Date de marché, lignes directrices | AIA-003 |
| SYS-03 | Fournisseur | Marquage lisible par machine | Art. 50, par. 2 | Obligation | En vigueur (CAL-010), sous réserve de NV-01 | A4 | Démontré (métadonnées « maison » présentes) | PRV-006 | Norme, interopérabilité | AIA-002 |
| SYS-03 | Fournisseur | Préservation du marquage dans le pipeline et du marquage amont | Art. 50, par. 2 | Obligation | Idem | A5 | Non démontré | PRV-007 | Tests de bout en bout | AIA-002, AIA-008 |
| SYS-03 | Fournisseur | Manifeste C2PA | Art. 50, par. 2 (technique) | Bonne pratique / moyen | Idem | A4 | Impossible à vérifier (bouchon) | PRV-008 | Outil interne | AIA-008 |
| SYS-03 | Fournisseur | Détectabilité : outil de vérification | Art. 50, par. 2 | Obligation | Idem | A6 | Impossible à vérifier | PRV-009 | Documentation | AIA-002 |
| SYS-03 | Fournisseur / déployeurs | Hypertrucages : étiquetage et consigne | Art. 50, par. 4, al. 1 | Obligation (déployeur) | En vigueur (CAL-009) | A8 | Impossible à vérifier | PRV-010 | Guide utilisateur | AIA-010 |
| SYS-03 | Fournisseur | Garde-fous contre contenus interdits (nouveaux points) | Art. 5, par. 1 `[O26]` | Obligation | Non encore applicable, échéance à confirmer (CAL-004) | F-art. 5 | Impossible à vérifier | PRV-035 | Fournisseur d'images | AIA-009 |
| SYS-02 | Fournisseur | Intervention humaine avant tout effet | Art. 14, par. 4, d) | Obligation future | Non encore applicable, échéance à confirmer (CAL-011) | B1 | Démontré | PRV-011 | | AIA-004 |
| SYS-02 | Fournisseur | Interprétation (justification, critères) | Art. 14, par. 4, a) et c) | Obligation future | Idem | B2 | Démontré (données produites) ; affichage impossible à vérifier | PRV-012 | Interface | AIA-004 |
| SYS-02 | Fournisseur | Ignorer, remplacer, annuler | Art. 14, par. 4, d) | Obligation future | Idem | B3 | Démontré | PRV-013 | | AIA-004 |
| SYS-02 | Fournisseur | Interrompre le système | Art. 14, par. 4, e) | Obligation future | Idem | B4 | Non démontré | PRV-014 | Procédure d'arrêt | AIA-004 |
| SYS-02 | Fournisseur | Gestion des erreurs et alertes | Art. 14, par. 4, a) ; art. 15 | Obligation future | Idem | B5 | Non démontré | PRV-015 | | AIA-005 |
| SYS-02 | Fournisseur | Traçabilité des interventions | Art. 12 ; art. 26, par. 6 | Obligation future | Idem | B6 | Démontré | PRV-016 | | AIA-007 |
| SYS-02 | Fournisseur | Prévention de l'automatisation excessive | Art. 14, par. 4, b) | Obligation future | Idem | B7 | Non démontré | PRV-017 | Revue trimestrielle | AIA-004 |
| SYS-02 | Déployeurs | Superviseurs compétents et formés | Art. 26, par. 2 | Obligation future | Idem | B8 | Impossible à vérifier | PRV-018 | Registre | AIA-012 |
| SYS-02 | Fournisseur | Modèles et versions épinglées | Annexe IV | Obligation future / bonne pratique | Idem | C3, C4 | C3 Démontré ; C4 Non démontré | PRV-019 | Production | AIA-011 |
| SYS-02 | Fournisseur | Méthodes de validation et résultats | Annexe IV, point 2 | Obligation future | Idem | C6 | Impossible à vérifier | PRV-021 | Rapports | AIA-006 |
| SYS-02 | Fournisseur | Notice d'utilisation | Art. 13 | Obligation future | Idem | C10 | Non démontré (« À rédiger » selon le projet) | PRV-020 | Notice | AIA-001 |
| SYS-02 | Fournisseur | Évaluation documentée de la dérogation | Art. 6, par. 4 | n.a. | `[AV]` (CAL-016) | C11 | Non applicable (dérogation non invoquée) | PRV-028 | | AIA-001 |
| SYS-02 | Fournisseur | Gestion des risques | Art. 9 | Obligation future | Idem | D1 | Démontré (registre initial) | PRV-020 | Mise à jour | AIA-006 |
| SYS-02 | Fournisseur | Tests et évaluations | Art. 9, par. 6 à 8 | Obligation future | Idem | D3 | Impossible à vérifier | PRV-021 | Rapports | AIA-006 |
| Tous | Fournisseur | Secrets hors du code et des journaux | Bonne pratique | n.a. | n.a. | D8 | Démontré | PRV-022 | | |
| SYS-02 | Fournisseur | Journaux automatiques | Art. 12 | Obligation future | Idem | E1 | Démontré | PRV-023 | | AIA-007 |
| SYS-02 | Fournisseur | Version modèle, version prompt | Art. 12 ; annexe IV | Obligation future | Idem | E3, E4 | Démontré (version prompt = constante manuelle) | PRV-024 | | AIA-007 |
| SYS-02 | Fournisseur | Historique des décisions et explication | Art. 12, art. 86 | Obligation future / `[AV]` | Idem | E2 | Non démontré (justification non journalisée) | PRV-025 | | AIA-007 |
| SYS-02 | Fournisseur | Conservation et intégrité | Art. 18, 19 ; art. 26, par. 6 | Obligation future | Idem | E6 | Non démontré (constante non utilisée) | PRV-026 | Production | AIA-007 |
| Tous | Fournisseur | Absence d'émotions des apprenants | Art. 5, par. 1, f) | Obligation | En vigueur (CAL-002) | F1 | Démontré (sur le dépôt) | PRV-027 | Historique | AIA-013, AIA-015 |
| SYS-02 | Fournisseur | Notation : qualification annexe III motivée | Art. 6, par. 2 et 3 | Obligation | Classification immédiate ; exigences CAL-011 | F2 | Démontré | PRV-028 | Validation juridique | AIA-001 |
| SYS-02 | Déployeurs | Information des élèves et familles | Art. 26, par. 11 | Obligation future | Non encore applicable, échéance à confirmer (CAL-011) | F8 | Impossible à vérifier | PRV-029 | Interface, CGU | AIA-001 |
| SYS-02 | Déployeurs publics | Échéance art. 111, par. 2 ; art. 27 | Art. 111, par. 2 `[AV]` ; art. 27 | Conditionnel | Conditionnel (CAL-013) | F9 | Impossible à vérifier | PRV-030 | Statut des clients | AIA-001 |
| Tous | Fournisseur | Maîtrise de l'IA | Art. 4 | Obligation | En vigueur (CAL-002) ; nouvelle rédaction : échéance à confirmer (CAL-003) | G1 | Impossible à vérifier | PRV-031 | Registre | AIA-012 |
| SYS-01 | Fournisseur | Avertissements dans l'interface | Bonne pratique (art. 4) | Bonne pratique | n.a. | G4 | Démontré (message) | PRV-001 | | AIA-014 |
| SYS-01 / SYS-02 | Fournisseur | Absence de réutilisation croisée (hybride) | `person-decisions.md`, section 5 | Méthode | n.a. | Hybride | Démontré (dans le dépôt) | PRV-034 | Flux hors dépôt (NV-15) | AIA-015 |
| SYS-03 | Fournisseur | Date de mise sur le marché | Art. 3, point 9 ; CAL-010 | Fait | Conditionne CAL-010 | n.a. | Impossible à vérifier | PRV-036 | NV-01 | AIA-002, AIA-003 |

### C.2 Matrice des preuves

Commit : non versionné pour toutes les preuves. Date de collecte : 2026-10-27. Nature : S = statique
(code, configuration ou document du projet) ; E = externe (non disponible, à fournir). Chemins relatifs
à `demo-ai-secure/`. Reproduction : commandes `sed -n 'a,bp' <fichier>` ou `grep -rn` dans la racine du
projet.

| PRV | Contrôle | Constat(s) | Fichier | Lignes | Commit | Date | Nature | Méthode de reproduction | État |
|---|---|---|---|---|---|---|---|---|---|
| PRV-001 | A1a, G4 | AIA-014 | `app/tutor_chat.py` | 9-21 | non versionné | 2026-10-27 | S | `sed -n '9,21p' app/tutor_chat.py` | Démontré |
| PRV-002 | A1b, A11 | AIA-014 | `app/` (absence de route/interface) ; `requirements.txt` | 1 | non versionné | 2026-10-27 | S | `grep -rn "start_session\|FastAPI\|APIRouter" app` ; `sed -n '1p' requirements.txt` | Impossible à vérifier |
| PRV-003 | A2 | AIA-014 | `app/tutor_chat.py` | 13-16 | non versionné | 2026-10-27 | S | `sed -n '13,16p' app/tutor_chat.py` | Démontré (instruction) |
| PRV-004 | A4 (SYS-01) | AIA-003 | `app/tutor_chat.py` | 24-32 | non versionné | 2026-10-27 | S | `sed -n '24,32p' app/tutor_chat.py` | Non démontré |
| PRV-005 | A4 (SYS-02) | AIA-003 | `app/grading.py` | 33-55 | non versionné | 2026-10-27 | S | `sed -n '33,55p' app/grading.py` | Non démontré |
| PRV-006 | A4 (SYS-03) | AIA-002 | `app/illustrations.py` | 16-26 | non versionné | 2026-10-27 | S | `sed -n '16,26p' app/illustrations.py` | Démontré (métadonnées « maison ») |
| PRV-007 | A5 | AIA-002, AIA-008 | `app/illustrations.py` | 3-6, 21-28 | non versionné | 2026-10-27 | S | `sed -n '3,6p;21,28p' app/illustrations.py` ; `ls` (aucun test) | Non démontré |
| PRV-008 | C2PA | AIA-008 | `app/c2pa_signer.py` | 5-6 | non versionné | 2026-10-27 | S | `cat app/c2pa_signer.py` | Impossible à vérifier |
| PRV-009 | A6 | AIA-002 | `docs/` (absence de procédure de vérification) | n.a. | non versionné | 2026-10-27 | S | `grep -rni "vérif" docs` | Impossible à vérifier |
| PRV-010 | A8 | AIA-010 | `app/illustrations.py` ; `docs/classification-assessment.md` | 16, 24 ; 26-27 | non versionné | 2026-10-27 | S | `grep -n "VISIBLE_LABEL" app/illustrations.py` | Impossible à vérifier |
| PRV-011 | B1 | AIA-001, AIA-004 | `app/grading.py` ; `app/gradebook.py` | 58-69 ; 5-8 | non versionné | 2026-10-27 | S | `sed -n '58,69p' app/grading.py` | Démontré |
| PRV-012 | B2 | AIA-004 | `app/grading.py` | 20-31, 43-50 | non versionné | 2026-10-27 | S | `sed -n '20,50p' app/grading.py` | Démontré |
| PRV-013 | B3 | AIA-004 | `app/grading.py` | 58-69 | non versionné | 2026-10-27 | S | `sed -n '58,69p' app/grading.py` | Démontré |
| PRV-014 | B4 | AIA-004 | `app/config.py` | 1-8 | non versionné | 2026-10-27 | S | `cat app/config.py` (aucun drapeau de désactivation) | Non démontré |
| PRV-015 | B5, art. 15 | AIA-005 | `app/grading.py` ; `app/gradebook.py` | 42-48, 63-68 ; 5-8 | non versionné | 2026-10-27 | S | `sed -n '42,48p;58,68p' app/grading.py` | Non démontré |
| PRV-016 | B6 | AIA-004, AIA-007 | `app/grading.py` | 65-66 | non versionné | 2026-10-27 | S | `sed -n '65,66p' app/grading.py` | Démontré |
| PRV-017 | B7 | AIA-004 | `app/gradebook.py` ; `app/grading.py` | 5-8 ; 58-69 | non versionné | 2026-10-27 | S | `cat app/gradebook.py` | Non démontré |
| PRV-018 | B8 | AIA-004, AIA-012 | `docs/human-oversight-procedure.md` ; `docs/ai-literacy-plan.md` | 1-12 ; 1-6 | non versionné | 2026-10-27 | S (procédure) / E (exécution) | `cat docs/human-oversight-procedure.md` | Impossible à vérifier |
| PRV-019 | C3, C4, GPAI | AIA-011, AIA-016 | `app/config.py` ; `README.md` | 5-6 ; 13 | non versionné | 2026-10-27 | S | `sed -n '5,6p' app/config.py` | C3 Démontré ; C4 Non démontré |
| PRV-020 | C10, D1 | AIA-001, AIA-006 | `docs/classification-assessment.md` ; `docs/risk-register.md` | 30-41 ; 1-10 | non versionné | 2026-10-27 | S | `sed -n '30,41p' docs/classification-assessment.md` | C10 Non démontré ; D1 Démontré |
| PRV-021 | C6, D3 | AIA-006 | `docs/technical-documentation.md` | 15-19 | non versionné | 2026-10-27 | S (déclaration) / E (rapports) | `sed -n '15,19p' docs/technical-documentation.md` | Impossible à vérifier |
| PRV-022 | D4, D8 | Aucun | `app/config.py` ; scan | 4 | non versionné | 2026-10-27 | S | `python3 scripts/scan_ai_signals.py demo-ai-secure` (aucun secret) | Démontré |
| PRV-023 | E1 | AIA-007 | `app/audit_log.py` | 7-16 | non versionné | 2026-10-27 | S | `cat app/audit_log.py` | Démontré |
| PRV-024 | E3, E4 | AIA-007, AIA-011 | `app/grading.py` ; `app/tutor_chat.py` | 48-54 ; 31 | non versionné | 2026-10-27 | S | `sed -n '48,54p' app/grading.py` | Démontré |
| PRV-025 | E2 | AIA-007 | `app/grading.py` | 43-55 | non versionné | 2026-10-27 | S | `sed -n '43,55p' app/grading.py` | Non démontré |
| PRV-026 | E6 | AIA-007 | `app/config.py` ; recherche de références | 8 | non versionné | 2026-10-27 | S | `grep -rn "AUDIT_LOG_RETENTION_DAYS" .` (une seule occurrence) | Non démontré |
| PRV-027 | F1 | AIA-013, AIA-015 | `requirements.txt` ; `app/exam_events.py` | 1-3 ; 1-10 | non versionné | 2026-10-27 | S | `cat requirements.txt app/exam_events.py` | Démontré |
| PRV-028 | F2, C11 | AIA-001 | `docs/classification-assessment.md` | 5-14 | non versionné | 2026-10-27 | S | `sed -n '5,14p' docs/classification-assessment.md` | F2 Démontré ; C11 Non applicable |
| PRV-029 | F8 | AIA-001 | (interface absente) | n.a. | non versionné | 2026-10-27 | E | Demander les textes d'information des élèves | Impossible à vérifier |
| PRV-030 | F9 | AIA-001 | (contrats clients absents) | n.a. | non versionné | 2026-10-27 | E | Demander le statut des clients | Impossible à vérifier |
| PRV-031 | G1 | AIA-012 | `docs/ai-literacy-plan.md` | 1-6 | non versionné | 2026-10-27 | S (plan) / E (registre) | `cat docs/ai-literacy-plan.md` | Impossible à vérifier |
| PRV-033 | Historique art. 5 | AIA-013 | `README.md` | 14 | non versionné | 2026-10-27 | S (déclaration) | `sed -n '14p' README.md` | Impossible à vérifier |
| PRV-034 | Hybride | AIA-015 | `app/tutor_chat.py` ; `app/grading.py` | 1-7 ; 9-15 | non versionné | 2026-10-27 | S | `grep -rn "tutor_chat\|from app.grading" app` (aucun appel croisé) | Démontré |
| PRV-035 | Garde-fous prompts | AIA-009 | `app/illustrations.py` ; `docs/risk-register.md` | 20-21 ; 9 | non versionné | 2026-10-27 | S | `sed -n '20,21p' app/illustrations.py` ; `sed -n '9p' docs/risk-register.md` | Impossible à vérifier |
| PRV-036 | Dates de mise sur le marché | AIA-001, AIA-002, AIA-003 | `README.md` ; `docs/ai-system-inventory.md` | 11-12 ; 7-9 | non versionné | 2026-10-27 | S (déclaration) / E | `sed -n '11,12p' README.md` ; `python3 scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-03-01` (et `2026-09-15`) | Impossible à vérifier |

(PRV-032 non utilisé.) **Preuves externes à fournir** (non établissables en statique) : contrats et
conditions d'utilisation des fournisseurs de modèles et d'images ; documentation de l'annexe XII ;
rapports d'évaluation ; registre de formation ; guide utilisateur ; notice ; configuration de
production ; outil et clés C2PA ; politique de filtrage.

## Annexe D : Registre des éléments non vérifiables

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact sur la classification ou les obligations | Interlocuteur suggéré | Constat(s) liés |
|---|---|---|---|---|---|---|---|
| NV-01 | SYS-01, 02, 03 | Dates réelles de première mise à disposition (pilotes et bêtas compris) de chaque système et de chaque version majeure | Information | Détermine le délai transitoire de l'art. 50, par. 2 et le régime de l'art. 111, par. 2 | Bascule de CAL-010 entre « en vigueur » et « non encore applicable » ; CAL-013 | Direction produit, juridique | AIA-001, 002, 003, 008 |
| NV-02 | SYS-02 | Statut des établissements clients (public, organisme de droit public, privé) | Information | Échéance art. 111, par. 2 (2030-08-02 ou 2028-01-28, sources divergentes) ; art. 27 | Calendrier et obligations des déployeurs | Commercial, juridique | AIA-001 |
| NV-03 | SYS-01, SYS-02 | Interface et API : affichage du message art. 50, par. 1 avant la première interaction, tous canaux, accessibilité ; avertissement de la procédure de supervision ; affichage de la justification | Document / information | La couche d'interface n'est pas dans le projet | Effectivité de l'art. 50, par. 1 et 5 et du contrôle humain | Responsable produit | AIA-004, AIA-014 |
| NV-04 | SYS-01, 02, 03 | Modalités de marquage du texte et de l'image : lignes directrices art. 50 (20.7.2026, C(2026) 5054 selon les sources) et code de bonnes pratiques (10.6.2026) non relus | Juridique | Incertitude sur les modalités, jamais une exemption | Choix de la solution technique ; contenu des tests | Juriste, direction technique | AIA-002, 003 |
| NV-05 | SYS-03 | Outil interne de signature C2PA : existence, clés, robustesse, vérificateur | Document | Le module du projet est un bouchon | Effectivité du marquage | Direction technique | AIA-002, 008 |
| NV-06 | SYS-03 | Identité du service tiers de génération d'images, contrats, documentation, marquage amont, politique d'usage | Document | Rôles et chaîne de valeur ; préservation du marquage | Rôle (fournisseur du modèle), art. 50, par. 2 | Achats, juridique | AIA-008, 009 |
| NV-07 | SYS-03 | Existence et tests du filtre de prompts R-05 | Document | Déclaré « en place » mais absent du code audité | Art. 5 (CAL-004) ; art. 50, par. 4 | Responsable sécurité | AIA-009 |
| NV-08 | SYS-01, 02 | Contrat et conditions d'utilisation d'Anthropic ; documentation transmise au titre de l'annexe XII ; valeurs de `EDUASSIST_*_MODEL` en production | Document / information | Usages permis (notation), versions réellement servies | Annexe IV ; art. 111, par. 2 / art. 25 | Achats, direction technique | AIA-011, 016 |
| NV-09 | SYS-02 | Rapports et protocole de la campagne de septembre 2026 (400 copies), seuils d'acceptation, plan T1 2027 | Document | Les chiffres sont déclarés, non démontrés | Art. 9, 10, 15 (futur) | Responsable qualité | AIA-006 |
| NV-10 | Tous | Registre de formation, contenu des modules, guide utilisateur et consignes (art. 50, par. 4) | Document | Art. 4 non démontrable par le code | Art. 4 ; art. 50, par. 4 | RH, produit | AIA-010, 012 |
| NV-11 | SYS-02 | Comptes rendus de la revue trimestrielle des écarts, taux de modification par les enseignants | Document | Biais d'automatisation | Effectivité du contrôle humain | Responsable qualité | AIA-004 |
| NV-12 | SYS-02 | Authentification, rôles et droits des enseignants (qui peut renseigner `validated_by`) | Information | Aucune couche d'API dans le projet | Effectivité du contrôle humain | Direction technique | AIA-004 |
| NV-13 | Passé | Date de retrait, nature des traitements et clients concernés par la surveillance webcam supprimée | Information | Art. 5 sans régime transitoire depuis 2025-02-02 | Existence éventuelle d'une pratique concernée | Direction, juridique | AIA-013 |
| NV-14 | SYS-02 | Stockage, permissions, rétention et purge du journal en production | Information | Constante de rétention non appliquée par le code | Art. 12, 19 (futur) | Direction technique | AIA-007 |
| NV-15 | SYS-01, 02 | Flux de réutilisation hors dépôt (échanges du tuteur transmis aux enseignants, scores ou tableaux de bord, orientation) | Information | Risque de système hybride | Reclassement possible de SYS-01 | Responsable produit | AIA-015 |
| NV-16 | Tous | Statut de l'organisation (PME, petite entreprise de taille intermédiaire) et allègements `[AV]` | Information | Règles simplifiées possibles pour la documentation | Forme de la documentation (art. 11) | Direction | AIA-001 |
| NV-17 | Légal | Relecture sur le Journal officiel des entrées CAL-003, 004, 010 (délai), 011, 012, 013, 016 | Juridique | Aucune entrée n'est `officielle_relue` | Toutes les conclusions temporelles « à confirmer » | Juriste | AIA-001, 003, 004 à 007, 009, 012 |

## Annexe E : Plan de remédiation (synthèse)

Date d'audit : 2026-10-27. Priorités : `findings-methodology.md`, section 6. Aucune action P1
(aucune obligation en vigueur manifestement non respectée n'est établie par les preuves disponibles).

| Priorité | Constat(s) | Action | Base (obligation + réf. / bonne pratique) | Échéance réglementaire | Effort | Responsable suggéré | Preuve de clôture attendue |
|---|---|---|---|---|---|---|---|
| P2 | AIA-002, AIA-008 | Normaliser le marquage des images (XMP/IPTC, C2PA signé, filigrane si possible), écriture atomique, préservation du marquage amont, tests de recompression | Obligation art. 50, par. 2 (CAL-010, en vigueur sous réserve de NV-01) ; choix techniques = bonne pratique | En vigueur (sous réserve) | M | Direction technique | Rapport de tests de bout en bout, vérification C2PA |
| P2 | AIA-003 | Définir et implémenter le marquage des textes générés et la position sur le copier-coller | Obligation art. 50, par. 2 (CAL-010, délai) | 2026-12-02 (**à confirmer**) | M | Produit, direction technique | Marqueur présent dans la réponse API ; décision écrite |
| P2 | AIA-009 | Documenter et tester les garde-fous de prompts et de sorties du service d'images ; demander les garanties du fournisseur | Préparation art. 5 (CAL-004) ; bonne pratique | 2026-12-02 (**à confirmer**) | M | Sécurité, achats | Jeu de tests, documentation du fournisseur |
| P2 | AIA-004, AIA-005 | Lier la publication à une proposition identifiée, authentifier le valideur, valider les sorties du modèle et les notes, tests | Préparation art. 14 et 15 ; bonne pratique immédiate | 2027-12-02 (**à confirmer**) | S à M | Direction technique | Tests unitaires et d'intégration |
| P2 | Transversal (NV-01) | Établir la chronologie réelle de mise sur le marché de chaque système | Qualification (art. 3, points 9 et 11) | Immédiat | S | Produit, juridique | Note datée avec pièces |
| P3 | AIA-001 | Validation juridique de l'art. 111, par. 2 ; procédure de qualification des modifications ; planning SGQ, notice, évaluation de conformité | Préparation chapitre III | 2027-12-02 (**à confirmer**) | L | Juridique, qualité | Note juridique ; planning ; procédure |
| P3 | AIA-006 | Évaluation par sous-groupes (allophones, manuscrits), seuils d'acceptation, information des enseignants | Préparation art. 9, 10, 13, 15 | 2027-12-02 (**à confirmer**) | M | Qualité | Rapports ; notice |
| P3 | AIA-007 | Journaliser empreinte, critères et justification ; versionner le prompt par empreinte ; imposer rétention et intégrité | Préparation art. 12, 19, 86 | 2027-12-02 (**à confirmer**) | M | Direction technique | Reconstitution d'une décision depuis le journal |
| P3 | AIA-010 | Option d'incrustation d'une mention visible ; guide et consigne aux déployeurs | Art. 50, par. 4 et 5 (outillage) | En vigueur (CAL-009) | S | Produit | Capture ; guide |
| P3 | AIA-011 | Épingler les versions de modèle en production | Bonne pratique | Immédiat | S | Direction technique | Configuration ; test |
| P3 | AIA-012 | Registre de formation ; guide d'usage ; extension aux prestataires | Art. 4 (**à confirmer** pour la nouvelle rédaction) | En vigueur | S | RH, produit | Registre ; guide |
| P3 | AIA-013 | Note sur la surveillance webcam supprimée | Qualification art. 5 | En vigueur | S | Direction | Note datée |
| P4 | AIA-014 | Rendre l'information non contournable ; test « es-tu humain ? » | Art. 50, par. 1 et 5 | En vigueur | S | Produit | Test d'API |
| P4 | AIA-015, AIA-016 | Garder la qualification des nouveaux traitements liés aux examens ; conserver la documentation du fournisseur de modèle | Bonne pratique | n.a. | S | Direction technique | Procédure |

### Jalons

| Date | Évènement réglementaire | Actions à terminer avant |
|---|---|---|
| Immédiat | Art. 4, 5, 50 (par. 1, 3, 4, 5) en vigueur ; art. 50, par. 2 en vigueur pour SYS-03 sous réserve de NV-01 | Actions AIA-002, AIA-008, NV-01 |
| 2026-12-02 (à confirmer) | Art. 50, par. 2 pour SYS-01 et SYS-02 (CAL-010) ; nouvelles interdictions de l'art. 5 (CAL-004) | Actions AIA-003, AIA-009 |
| 2027-12-02 (à confirmer) | Exigences du haut risque, annexe III (CAL-011), sous réserve de l'art. 111, par. 2 (CAL-013) | Actions AIA-001, 004 à 007 |
| 2028-01-28 ou 2030-08-02 (à confirmer, sources divergentes) | Échéance éventuelle pour les systèmes destinés aux autorités publiques (CAL-013) | NV-02 |

### Hypothèses

- Efforts estimés à partir du projet seul ; à recalibrer avec l'équipe.
- Les échéances issues du règlement 2026/1744 (confiance moyenne ou faible) sont à confirmer.
- Les dates de mise sur le marché sont celles déclarées dans le README ; leur modification change
  les statuts temporels (NV-01).

## Annexe F : Cartographie des flux et des chemins de sortie

```
FCT-01 Tuteur (SYS-01)
  Utilisateur : élève, message libre                                  [app/tutor_chat.py:24]
  Application : prompt système, historique fourni par l'appelant       [app/tutor_chat.py:13-16, 29]
  Modèle      : claude-sonnet-4-5 (défaut env.), Anthropic, non épinglé [app/config.py:5]
  Post-trait. : aucun (aucun marquage)                                 [app/tutor_chat.py:32]
  Stockage    : journal (model_version seulement)                      [app/tutor_chat.py:31]
  Export      : valeur de retour (canal réel hors dépôt)

FCT-02 Correction (SYS-02)
  Utilisateur : enseignant ; dissertation d'un élève                   [app/grading.py:33]
  Application : prompt + RUBRIC, temperature=0                         [app/grading.py:17, 34-41]
  Modèle      : claude-sonnet-4-5 (défaut env.), Anthropic             [app/config.py:6]
  Post-trait. : json.loads sans validation                             [app/grading.py:42]
  Stockage    : journal (note proposée, versions) ; carnet (note + valideur) [app/grading.py:51-54 ; app/gradebook.py:8]
  Export      : GradeProposal en mémoire, carnet en mémoire

FCT-03 Illustrations (SYS-03)
  Utilisateur : enseignant ; prompt                                    [app/illustrations.py:20]
  Application : aucun filtre de prompt observé                         [app/illustrations.py:21]
  Modèle      : service tiers non identifié (bouchon)                  [app/image_provider.py:5-6]
  Post-trait. : métadonnées PNG texte ; C2PA (bouchon, lève NotImplementedError) [app/illustrations.py:22-27]
  Stockage    : fichier image ; journal                                [app/illustrations.py:26, 28]
  Export      : fichier PNG (chemin de sortie unique observé : file-write)
```

| Fonctionnalité | Système | Fournisseur | Modèle | Version épinglée ? | Version journalisée ? | Entrées | Sorties | Personnes concernées |
|---|---|---|---|---|---|---|---|---|
| FCT-01 | SYS-01 | Anthropic | `claude-sonnet-4-5` (défaut) | Non démontré (identifiant sans date) | Oui (`response.model`) | Message d'élève | Texte | Élèves |
| FCT-02 | SYS-02 | Anthropic | `claude-sonnet-4-5` (défaut) | Non démontré | Oui (`response.model`, `PROMPT_VERSION`) | Dissertation | Note, critères, justification | Élèves |
| FCT-03 | SYS-03 | Tiers non identifié | Inconnu | Inconnu | Oui (`model_version` retourné) | Prompt | Image PNG | Élèves (destinataires) |

| Fonctionnalité | Chemin de sortie | Marquage à la génération | Marquage après transformation | Mécanisme | Détectable par un tiers ? | Outil de vérification | Falsifiable ? | État | Preuve |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | Valeur de retour / interface | Aucun | n.a. | Aucun | Non | Non | n.a. | Non démontré | PRV-004 |
| FCT-02 | Valeur de retour / interface | Aucun | n.a. | Aucun | Non | Non | n.a. | Non démontré | PRV-005 |
| FCT-03 | Fichier PNG | Champs texte PNG (propriétaire) | Perdu si ré-encodage | Propriétaire + C2PA (bouchon) | Probablement non (clés libres) | Non documenté | Oui (non signé) | Non démontré / Impossible à vérifier | PRV-006 à PRV-009 |

**Ruptures de chaîne identifiées** : (1) FCT-03, sauvegarde avant signature, sans transaction (AIA-008) ;
(2) FCT-03, marquage amont du fournisseur d'images non préservé par la reconstruction Pillow (AIA-008) ;
(3) FCT-01/FCT-02, aucune étape de marquage (AIA-003) ; (4) FCT-02, justification et critères non
persistés (AIA-007).
