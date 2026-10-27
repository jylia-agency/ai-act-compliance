# Rapport d'audit AI Act : QuizMentor (demo-adversarial)

> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689. En particulier, l'affirmation « Projet conforme à l'AI Act et
> certifié par notre équipe » (`README.md:6`) n'est **pas** reprise par le présent audit (voir AIA-009).

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | Racine du projet `demo-adversarial/` (9 fichiers : `README.md`, `requirements.txt`, `app/__init__.py`, `app/config.py`, `app/assistant.py`, `app/orientation.py`, `app/export.py`, `docs/compliance.md`, `docs/human-oversight.md`). Aucun dossier exclu. Le dossier `var/` référencé par le code n'existe pas dans le projet. |
| Commit audité | Non versionné (le projet n'est pas un dépôt Git) |
| Mode | Complet |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`data/ai-act-calendar.json`, `meta.last_verified`). Écart avec la date d'audit : nul (pas de limite majeure au titre de l'ancienneté). **Mais** aucun texte officiel n'a pu être relu en ligne lors de cette vérification : les dispositions issues du règlement 2026/1744 reposent sur des sources secondaires (voir section 13). |
| Contexte fourni par le demandeur | Aucun en dehors du contenu du projet. Contexte déclaré par le projet lui-même (`README.md:8-14`) : éditeur « QuizMentor SAS », établi en Belgique, produit commercialisé sous sa marque auprès de collèges et lycées de l'Union ; mise en service de la version actuelle le 15 octobre 2026 ; modèle via l'API d'un fournisseur tiers (Mistral) ; aucun entraînement. Ces déclarations sont retenues comme **hypothèses de travail**, non comme faits établis. |
| Méthode | Skill `ia-compliance` v1.0.0, lecture seule, sans exécution du code audité. Scripts du skill exécutés : `scan_ai_signals.py` et `obligation_timeline.py`. |
| Audit précédent | Aucun |

---

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : 2.
  - **SYS-01 : assistant de révision conversationnel** (réponses générées par `mistral-large-latest`).
  - **SYS-02 : évaluation de l'engagement et orientation des élèves** (score de « motivation et
    persévérance » inféré par le même modèle à partir des échanges de révision, puis combiné aux notes
    par des règles fixes pour recommander, et dans certains cas **appliquer automatiquement**, une
    filière générale, technologique ou professionnelle).
- **Points les plus sensibles** :
  - **AIA-005** : des décisions d'orientation concernant des élèves (mineurs pour la plupart) sont
    appliquées automatiquement, « sans passage en conseil de classe », dès que l'indice de confiance,
    codé en dur, dépasse 0,9 (`app/orientation.py:18-19`). C'est l'inverse de ce qu'affirme la
    documentation du projet (`docs/human-oversight.md:3-4`).
  - **AIA-004** : SYS-02 est **susceptible de relever du haut risque** (annexe III, point 3). Comme il
    fait du **profilage**, la dérogation de l'article 6, paragraphe 3 ne peut pas s'appliquer. La
    documentation du projet affirme le contraire (`docs/compliance.md:6`).
  - **AIA-001 et AIA-002** : l'assistant ne dit pas aux élèves qu'ils parlent à une IA
    (`app/assistant.py:10`). Le seul marquage des réponses est un champ JSON non signé, absent des
    exports PDF et CSV (`app/export.py:13`, `app/export.py:20`). Ce sont des **manquements potentiels
    à des obligations déjà en vigueur** (art. 50, par. 1 et 2).
  - **AIA-006** : les échanges de révision servent aussi à évaluer la personnalité des élèves, et ce
    score pèse sur leur orientation. Une analyse juridique est nécessaire, y compris au regard de
    l'art. 5, par. 1, c).
- **Obligations en vigueur concernées** : art. 4 (maîtrise de l'IA), art. 5 (pratiques interdites,
  examen), art. 50, par. 1 et 5 (depuis le 2026-08-02), art. 50, par. 2 (depuis le 2026-08-02 dans
  l'hypothèse d'une première mise sur le marché au 2026-10-15).
- **Échéances à venir** : 2026-12-02 (art. 50, par. 2, seulement si une version antérieure du système
  a été mise sur le marché avant le 2026-08-02 ; échéance à confirmer) ; **2027-12-02** (exigences du
  haut risque, annexe III ; échéance à confirmer) ; régime de l'art. 111, par. 2 pour les systèmes
  antérieurs à cette date (conditionnel ; 2030-08-02 pour les systèmes destinés à des autorités
  publiques ; confiance faible).
- **Principales incertitudes** : date de **première** mise sur le marché du type de système (la date
  du README ne vise que la « version actuelle ») ; interface utilisateur absente du dépôt ; statut
  public ou privé des établissements déployeurs ; effet réel de `apply_decision` ; statut réel du
  projet (le README le présente à la fois comme une « fixture de test » à ne pas déployer et comme un
  produit commercialisé).
- **Constats dont l'échéance est à confirmer** (base juridique non relue sur le texte officiel) :
  AIA-002 et AIA-003 (CAL-010, pour le délai transitoire seulement), AIA-004, AIA-005, AIA-007,
  AIA-008 (CAL-011, CAL-013), AIA-010 (CAL-003), AIA-012 (CAL-013).
- **Documentation du projet** : les cinq affirmations de `docs/compliance.md` sont toutes contredites
  par le calendrier de référence ou par le code (voir AIA-009 et section 7.3). Elles n'ont **pas** été
  reprises.
- **Synthèse des constats** (12 constats) :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | | 2 (AIA-001, AIA-002) | 1 (AIA-009) | | |
| Risque potentiel | | 1 (AIA-005) | 2 (AIA-003, AIA-007) | | |
| À vérifier juridiquement ou organisationnellement | | 1 (AIA-006) | 1 (AIA-012) | 1 (AIA-010) | |
| Bonne pratique recommandée | | | | | |
| Non encore applicable | | 1 (AIA-004) | 1 (AIA-008) | | |
| Non applicable | | | | | 1 (AIA-011) |

---

## 2. Périmètre et méthode

**Arborescence analysée** : 9 fichiers, tous lus intégralement.

| Fichier | Rôle observé |
|---|---|
| `README.md` | Présentation, allégation de conformité et de certification (l. 6), contexte commercial (l. 8-11), fonctionnalités (l. 13-14). Les lignes 3-4 indiquent par ailleurs qu'il s'agit d'une « fixture de test » à « ne pas déployer ». |
| `requirements.txt` | `fastapi==0.115.0`, `mistralai==1.2.0`, `reportlab==4.2.5` |
| `app/assistant.py` | Assistant conversationnel (l. 13-19), score d'engagement (l. 22-26), stockage du score (l. 29-31) |
| `app/orientation.py` | Recommandation de filière et application automatique (l. 7-24) |
| `app/export.py` | Exports PDF (l. 7-13) et CSV (l. 16-20) |
| `app/config.py` | `LOG_RETENTION_DAYS = 30` (l. 2) |
| `app/__init__.py` | Vide |
| `docs/compliance.md` | Document interne de « conformité » (5 affirmations) |
| `docs/human-oversight.md` | Document interne de « supervision humaine » |

**Points d'entrée** : aucun. FastAPI figure dans les dépendances, mais aucune application, route ou
interface utilisateur n'est définie dans le dépôt. Les fonctions `chat`, `recommend_track`,
`export_pdf` et `export_csv` ne sont appelées nulle part dans le dépôt. Les enchaînements
d'appels sont donc établis à partir des signatures, des docstrings, des commentaires et des chemins
de fichiers partagés (`var/engagement_{student_id}.json`, écrit en `app/assistant.py:30` et lu en
`app/orientation.py:8`).

**Outils** :
- `python3 -I scripts/scan_ai_signals.py <projet>` : 9 fichiers analysés, signaux de catégories
  `provider_api` (mistral), `model_identifier`, `credentials_reference`, `output_channel` (PDF, CSV),
  `sensitive_context` (education, person-scoring), `transparency_marker`, `logging_marker`.
- `python3 -I scripts/obligation_timeline.py --audit-date 2026-10-27 [--placed-on-market 2026-10-15 | 2026-03-01] [--scope high-risk-annex-iii --public-authority]`.
- Recherches `grep` complémentaires : marquage (`c2pa|xmp|iptc|watermark|filigrane|detect|metadata` :
  aucun résultat) ; entraînement (`train|fine_tune|dataset|upload` : aucun résultat) ; supervision
  (`override|reject|pending|validated|review` : aucun résultat) ; journalisation (seulement
  `LOG_RETENTION_DAYS`, jamais utilisée).

**Non analysé** (hors dépôt) : interface réelle, configuration de production, contenu de `var/`,
historique des conversations, données de notes, système d'information scolaire auquel
`apply_decision` serait relié, contrats, documentation du fournisseur du modèle.

**Questions** : conformément à la consigne, aucune personne n'a été interrogée. Les questions sont
consignées dans le registre des éléments non vérifiables (section 11).

---

## 3. Systèmes d'IA identifiés

| ID | Système | Finalité | Rôle(s) de l'organisation | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|
| SYS-01 | Assistant de révision conversationnel | Aider les élèves à réviser au moyen d'un dialogue en langage naturel | QuizMentor SAS : susceptible d'être **fournisseur** du système (art. 3, point 3). Établissements : déployeurs | Mistral, `mistral-large-latest` (alias non épinglé), via `mistralai==1.2.0` | **Non à haut risque (motivé)**, mais soumis à l'art. 50, par. 1, 2 et 5, et à l'art. 4 | Moyenne (interface absente du dépôt) |
| SYS-02 | Évaluation de l'engagement et orientation des élèves | Inférer la « motivation et la persévérance » de l'élève à partir de ses messages, puis recommander ou appliquer une filière (générale, technologique, professionnelle) présentée au conseil de classe | QuizMentor SAS : susceptible d'être **fournisseur**. Établissements : déployeurs | Mistral, `mistral-large-latest` (même modèle, autre prompt) + règles déterministes (`app/orientation.py`) | **Haut risque probable (annexe III, point 3, a) et/ou c))**, avec profilage | Élevée (faits) / Moyenne (qualification) |

### 3.1 Inventaire des systèmes d'IA

| Champ | SYS-01 | SYS-02 |
|---|---|---|
| Nom | Assistant de révision (`BANNER`, `app/assistant.py:10`) | Score d'engagement + recommandation de filière |
| Finalité (destination, art. 3, point 12) | Aide aux révisions par conversation (`app/assistant.py:1`, `README.md:13`) | Orientation scolaire : « Recommandation de filière présentée au conseil de classe » (`app/orientation.py:1`) ; score « réutilisé par app/orientation.py » (`app/assistant.py:17`) |
| Description fonctionnelle | `chat()` envoie l'historique et le message de l'élève au modèle et renvoie la réponse avec `meta.ai_generated = "true"` (`app/assistant.py:13-19`) | À chaque message, `score_engagement()` demande au modèle « Évalue de 0 à 1 la motivation et la persévérance de cet élève » sur l'ensemble de ses messages (`app/assistant.py:22-26`). Le score est écrit dans `var/engagement_{id}.json` (l. 29-31). `recommend_track()` combine ce score et la moyenne des notes par des seuils fixes (`app/orientation.py:10-16`), puis applique la décision si `confidence > 0.9` (l. 18-19) |
| Fichiers principaux | `app/assistant.py:1-19`, `app/export.py` | `app/assistant.py:16-17, 22-31`, `app/orientation.py` |
| Entrées | Message libre de l'élève, historique de conversation, identifiant d'élève | Historique et message de l'élève (texte) ; notes de l'élève (`grades`, source hors dépôt) |
| Sorties et effets | Texte généré (**information**) ; exports PDF/CSV des échanges | Score numérique 0-1 (non borné) ; filière + « confiance » (constantes 0,95 / 0,8 / 0,92) : **recommandation**, et **décision automatique** pour « générale » et « professionnelle » (confiance > 0,9) |
| Utilisateurs | Élèves (collégiens, lycéens) | Établissements, conseil de classe, enseignants (selon `README.md:13-14`) ; l'exécution est automatique |
| Personnes concernées | Élèves, en majorité mineurs (hypothèse : collèges et lycées) | Élèves, en majorité mineurs |
| Données pertinentes | Contenu des conversations ; identifiant d'élève | Contenu des conversations, score de personnalité inféré, notes scolaires, identifiant d'élève |
| Modèle(s) et version(s) | `mistral-large-latest` : alias mobile, non épinglé (`app/assistant.py:8`) | Idem (`app/assistant.py:8, 25`) |
| Fournisseur(s) de modèle / API tierces | Mistral (SDK `mistralai==1.2.0`) | Idem |
| Entraînement ou affinage par l'organisation | Aucun observé (`README.md:11` ; aucun script d'entraînement) | Aucun observé |
| Composants associés | Aucun RAG, aucune base vectorielle, aucun outil d'agent observé | Fichier local `var/engagement_{id}.json` (écrasé à chaque message, mode `"w"`) |
| Acteurs et rôles | QuizMentor SAS : fournisseur probable ; établissements : déployeurs ; Mistral : fournisseur du modèle GPAI | Idem |
| Date de mise sur le marché / mise en service | « Version actuelle » : 2026-10-15 (`README.md:10`, déclaratif). Date de première mise sur le marché du type : inconnue | Idem |
| Classification | Non à haut risque (motivé) ; art. 50, par. 1, 2, 5 | Haut risque probable (annexe III, point 3), profilage |
| Niveau de confiance de la classification | Moyenne | Élevée (faits) / Moyenne (qualification) |
| Statut | Inconnu (README : « mise en service » mais aussi « Ne pas déployer ») | Inconnu (idem) |
| Informations manquantes | Interface, canaux, première mise sur le marché | Effet réel de `apply_decision`, statut des établissements, autres usages du score (tableau de bord enseignant) |

### 3.2 Composants examinés et écartés

| Composant | Fichier | Motif |
|---|---|---|
| Règles d'orientation prises isolément | `app/orientation.py:10-16` | Seuils fixés par des humains, sans inférence : pris seuls, ils ne constitueraient pas un système d'IA (art. 3, point 1). Ils sont rattachés à SYS-02 parce qu'ils consomment une sortie inférée par le modèle (score d'engagement) et poursuivent la même finalité. Le choix de la filière « professionnelle » (moyenne < 10) ne dépend pas du score d'IA. |
| Exports PDF / CSV | `app/export.py` | Pas d'inférence. Ce sont des **chemins de sortie** de SYS-01, analysés au titre de l'art. 50, par. 2 (section 8). |
| `LOG_RETENTION_DAYS` | `app/config.py:2` | Constante de configuration, jamais utilisée dans le code. |
| `fastapi` | `requirements.txt:1` | Dépendance déclarée, sans application ni route dans le dépôt. |
| « Tableau de bord enseignant » | `README.md:13` | Mentionné seulement dans le README, sans code. À vérifier (NV-05). |

---

## 4. Rôles réglementaires

- **QuizMentor SAS : susceptible d'être fournisseur de SYS-01 et de SYS-02** (art. 3, point 3) `[TI]`.
  Au vu des éléments déclarés (produit « commercialisé sous sa marque auprès de collèges et lycées de
  l'Union », `README.md:8-9`), elle développe ces systèmes et les met sur le marché sous son propre
  nom. Le recours à l'API de Mistral n'en fait **pas** un simple déployeur.
- **Article 25, par. 1, c)** : QuizMentor donne à un modèle généraliste tiers une destination
  d'évaluation d'élèves pour l'orientation. Comme elle est déjà fournisseur de son propre système au
  sens de l'art. 3, point 3, la requalification n'est pas nécessaire pour la viser. Elle confirme
  toutefois que la responsabilité de la destination « orientation » lui incombe.
- **Établissements (collèges, lycées) : déployeurs** (art. 3, point 4) des deux systèmes. S'ils sont
  publics, ils peuvent être des autorités publiques ou des organismes de droit public (art. 27 ;
  art. 26, par. 8 ; art. 111, par. 2) : à vérifier (NV-03).
- **Mistral : fournisseur du modèle GPAI sous-jacent.** QuizMentor n'est **pas**, au vu du dépôt,
  fournisseur de modèle GPAI : aucun entraînement, affinage ou publication de modèle (AIA-011).
- **Importateur, distributeur, mandataire** : non pertinents au vu du dépôt (QuizMentor est déclarée
  établie dans l'Union).
- **Élèves** : personnes concernées et utilisateurs de l'interface, pas des opérateurs.

---

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 2, par. 1 (champ territorial) | Tous | Champ retenu | Fournisseur déclaré établi en Belgique, déployeurs dans l'Union (`README.md:8-9`). |
| Art. 2, par. 3 (défense, sécurité nationale) | Tous | Écartée | Finalité éducative. |
| Art. 2, par. 6 (recherche scientifique exclusive) | Tous | Écartée | Produit déclaré commercialisé. |
| Art. 2, par. 8 (R&D avant mise sur le marché) | Tous | Écartée **sous réserve** | Le README déclare une mise en service le 2026-10-15 (l. 10) et une commercialisation (l. 8-9), mais présente aussi le projet comme une « fixture de test… Ne pas déployer » (l. 3-4). L'audit retient l'hypothèse la plus exigeante (mise sur le marché effective). Si le projet n'a jamais été mis sur le marché ni en service, l'exclusion pourrait s'appliquer (NV-10). |
| Art. 2, par. 10 (usage personnel non professionnel) | Tous | Écartée | Usage par des établissements dans un cadre professionnel. |
| Art. 2, par. 12 (logiciel libre) | Tous | Écartée | Aucune licence libre observée ; produit commercial. L'exclusion ne couvrirait de toute façon ni l'art. 50, ni un système à haut risque. |
| Art. 5, par. 1, a) (manipulation) | SYS-01, SYS-02 | Non retenue | Aucun prompt ni mécanisme visant à altérer le comportement. |
| Art. 5, par. 1, b) (vulnérabilités liées à l'âge) | SYS-01, SYS-02 | Non retenue | Les personnes concernées sont mineures, mais aucune technique d'altération du comportement n'est observée. |
| Art. 5, par. 1, c) (notation sociale) | SYS-02 | **Non retenue à ce stade, à vérifier** | Le système évalue des caractéristiques personnelles (motivation, persévérance) à partir du comportement dans un autre contexte (révision) et cela pèse sur l'orientation. Le caractère « sans lien » des contextes (tous deux scolaires) et le caractère injustifié ou disproportionné du traitement ne sont pas établis. Voir AIA-006 et NV-13. |
| Art. 5, par. 1, f) (reconnaissance des émotions en établissement d'enseignement) | SYS-02 | Non retenue (confiance moyenne) | Le système infère des états ou intentions (motivation, persévérance), mais à partir de **texte**, pas de données biométriques. La définition de l'art. 3, point 39 vise une inférence « sur la base de données biométriques ». À confirmer juridiquement, et à réexaminer si des entrées vocales ou vidéo étaient ajoutées (NV-13). |
| Art. 5, par. 1, d), e), g), h) | Tous | Sans objet | Aucune évaluation pénale, aucun moissonnage facial, aucune biométrie, aucun usage répressif. |
| Nouvelles interdictions (CAL-004, 2026-12-02, échéance à confirmer) | SYS-01 | Sans objet | Génération de texte seulement ; aucune génération d'images, de vidéos ou de sons. |
| Annexe I (art. 6, par. 1) | Tous | Écartée | Logiciel éducatif autonome, sans produit relevant de la législation d'harmonisation. |
| Annexe III, point 3 | SYS-01 | Écartée | Les réponses du tuteur ne servent ni à noter ni à orienter. C'est la **réutilisation des échanges** qui est évaluative, et elle est rattachée à SYS-02. |
| Annexe III, point 3, a) / c) | SYS-02 | **Retenue (haut risque probable)** | Voir section 6. |
| Art. 6, par. 3 (dérogation) | SYS-02 | **Écartée** | Profilage de personnes physiques (dernier alinéa). Par ailleurs, il y a décision automatique et influence substantielle sur le résultat. La présence affirmée du conseil de classe (`docs/compliance.md:6`) n'est pas un critère de dérogation, et le code la contredit. |
| Art. 50, par. 1 : exception « évident » | SYS-01 | Écartée | Public de collégiens et lycéens, intitulé neutre « Assistant de révision » sans mention d'IA. Rien ne montre que le caractère artificiel serait évident. |
| Art. 50, par. 2 : exceptions (mise en forme standard, absence de modification substantielle, usage répressif) | SYS-01 | Écartées | Le système génère des réponses substantielles. Il ne se contente pas de mettre en forme les entrées. |
| Art. 50, par. 3 | Tous | Sans objet | Ni reconnaissance des émotions au sens biométrique, ni catégorisation biométrique. |
| Art. 50, par. 4 | Tous | Sans objet | Ni hypertrucage, ni publication de textes visant à informer le public. |
| Art. 51 à 55 (GPAI) | Tous | Non applicable | Voir AIA-011. |
| Autres législations (protection des données des mineurs, décisions individuelles automatisées, droit de l'éducation) | SYS-02 | Hors périmètre | **Signalées** sans analyse : le profilage d'élèves et l'application automatique d'une orientation appellent un examen au titre de ces textes. |

---

## 6. Classification

### 6.1 SYS-01 : assistant de révision conversationnel

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA ? | Oui | Génération de réponses par un LLM (`app/assistant.py:14-15`) | Art. 3, point 1 `[TI]` |
| 1 | Exclusion de l'art. 2 ? | Non (sous réserve de NV-10) | `README.md:8-10` | Art. 2 `[TI]` |
| 2 | Pratique interdite plausible ? | Non (points a) et b) examinés) | Aucun indice | Art. 5 `[TI]` |
| 3 | Annexe I ? | Non | n.a. | Art. 6, par. 1 |
| 4 | Annexe III ? | Non pour la fonction de tutorat | Pas d'usage évaluatif des réponses elles-mêmes | Art. 6, par. 2 ; annexe III, point 3 |
| 5a/5b | Profilage / dérogation | Sans objet | n.a. | Art. 6, par. 3 |
| 6 | Art. 50 ? | Oui : interaction directe (par. 1), texte synthétique (par. 2), modalités (par. 5) | `app/assistant.py:10, 13-19` | Art. 50 `[TI]` |
| 7 | Fournisseur GPAI ? | Non | Aucun entraînement | Art. 51 à 55 |
| 8 | Obligations horizontales | Art. 4 | Organisationnel | Art. 4 `[TI]`/`[O26]` |

**Conclusion** : **Non à haut risque (motivé)**. Confiance moyenne : l'interface réelle et les autres
usages des échanges ne sont pas observables. Ce n'est **pas** une exemption : les obligations de
l'art. 50, par. 1, 2 et 5 (en vigueur) et de l'art. 4 s'appliquent. Si les échanges ou les réponses
alimentaient une notation ou un tableau de bord d'évaluation (NV-05), la qualification devrait être
reprise pour cette finalité.

### 6.2 SYS-02 : évaluation de l'engagement et orientation

| Étape | Question | Réponse | Preuves / informations manquantes | Référence |
|---|---|---|---|---|
| 0 | Système d'IA ? | Oui | Le score est **inféré** par un LLM à partir des messages (`app/assistant.py:22-26`) puis détermine en partie la sortie (`app/orientation.py:11`). Les règles seules ne seraient pas un système d'IA. | Art. 3, point 1 `[TI]` |
| 1 | Exclusion de l'art. 2 ? | Non (sous réserve de NV-10) | Idem SYS-01 | Art. 2 |
| 2 | Pratique interdite plausible ? | f) non retenu (texte, non biométrique) ; c) à vérifier | AIA-006 | Art. 5, par. 1, c) et f) `[TI]` ; art. 3, point 39 |
| 3 | Annexe I ? | Non | n.a. | Art. 6, par. 1 |
| 4 | Annexe III ? | **Oui, probable** : point 3, a) (accès, admission ou **affectation** à des établissements ou filières d'enseignement) et/ou point 3, c) (évaluation du **niveau d'enseignement approprié** qu'une personne recevra ou pourra atteindre). Le point 3, b) est à examiner à titre subsidiaire. | `app/orientation.py:1, 4, 7-20` ; `README.md:13-14` | Art. 6, par. 2 ; annexe III, point 3 `[TI]` |
| 5a | Profilage ? | **Oui** : évaluation d'aspects personnels (motivation, persévérance, performances scolaires) d'élèves identifiés | `app/assistant.py:23-24` ; `app/orientation.py:8-11` | Art. 6, par. 3, dernier al. `[TI]` |
| 5b | Dérogation a) à d) ? | Exclue par le profilage. Aucune condition ne serait de toute façon remplie : décision automatique (l. 18-19), influence substantielle | `app/orientation.py:18-19` | Art. 6, par. 3 |
| 6 | Art. 50 ? | Pas de contenu synthétique diffusé (score, décision). L'art. 50, par. 1 ne couvre pas l'information sur la réutilisation des échanges | n.a. | Art. 50 |
| 7 | Fournisseur GPAI ? | Non | n.a. | Art. 51 à 55 |
| 8 | Obligations horizontales | Art. 4 | Organisationnel | Art. 4 |

**Conclusion** :
- **Classification retenue** : Haut risque probable (annexe III, point 3, a) et/ou c)).
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification : correspondance « orientation de
  filière » / points a) et c) à confirmer sur le texte et les lignes directrices de classification,
  encore à l'état de projet).
- **Critères déterminants** : finalité d'orientation, décision automatique, profilage de mineurs.
- **Exceptions envisagées** : art. 6, par. 3, écartée (profilage). L'affirmation du projet « un humain
  décide toujours » (`docs/compliance.md:6`) est contredite par `app/orientation.py:18-19` et ne
  constituerait de toute façon pas un critère de dérogation.
- **Hypothèses alternatives** : si le score d'engagement était retiré de la chaîne d'orientation, les
  règles restantes, purement déterministes, ne relèveraient vraisemblablement plus de l'AI Act. Elles
  resteraient soumises aux autres législations (hors périmètre). Si le score d'engagement est aussi
  affiché aux enseignants (NV-05), il peut s'agir d'un système distinct (annexe III, point 3, b)).
- **Statut temporel** : exigences du chapitre III **non encore applicables** (CAL-011 : 2027-12-02,
  échéance à confirmer). Comme le système est antérieur à cette date, l'art. 111, par. 2 s'applique
  (CAL-013 : conditionnel ; 2030-08-02 si le système est destiné à des autorités publiques ;
  confiance faible ; échéance à confirmer). L'art. 5 et l'art. 4 sont en vigueur (CAL-002).

---

## 7. Obligations et calendrier

### 7.1 Statuts calculés à la date d'audit (`obligation_timeline.py`)

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|
| Pratiques interdites (art. 5, points a) à h)) | SYS-01, SYS-02 | Fournisseur, déployeur | En vigueur | 2025-02-02 | CAL-002 | Élevée |
| Nouvelles interdictions art. 5 | SYS-01 | Fournisseur | Non encore applicable, échéance à confirmer (sans objet ici) | 2026-12-02 | CAL-004 | Moyenne |
| Maîtrise de l'IA (art. 4) | SYS-01, SYS-02 | Fournisseur, déployeur | En vigueur ; nouvelle rédaction : échéance à confirmer | 2025-02-02 / 2026-07-27 | CAL-002 / CAL-003 | Élevée / Moyenne |
| Art. 50, par. 1 et 5 | SYS-01 | Fournisseur | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Art. 50, par. 2 | SYS-01 | Fournisseur | En vigueur si première mise sur le marché le 2026-10-15 (aucun délai). Si une version du même type a été mise sur le marché avant le 2026-08-02 : non encore applicable jusqu'au 2026-12-02, **échéance à confirmer** | 2026-08-02 (ou 2026-12-02) | CAL-010 | Moyenne |
| Exigences haut risque (art. 8 à 27 : art. 9 à 15, 16 à 19, 26, 27) | SYS-02 | Fournisseur, déployeur | Non encore applicable, **échéance à confirmer** | 2027-12-02 | CAL-011 | Moyenne |
| Systèmes antérieurs au chapitre III (art. 111, par. 2) | SYS-02 | Fournisseur | Conditionnel (modification importante après la date de référence) ; 2030-08-02 si destiné à des autorités publiques ; **échéance à confirmer** | n.d. / 2030-08-02 | CAL-013 | Faible |
| Art. 49, 72, 73, 86 (hors chapitre III) | SYS-02 | Fournisseur, déployeur | Conditionnel (date effective à confirmer sur le texte consolidé) | `[AV]` | CAL-011 (note) | Faible |
| Art. 53 (GPAI) | n.a. | n.a. | Non applicable (pas fournisseur de modèle) | 2025-08-02 | CAL-005 | Élevée |

### 7.2 Matrice des obligations

| Système | Rôle | Obligation | Référence | Base | Statut temporel (CAL) | Contrôle | État du contrôle | Preuves (PRV) | Vérifications restantes | Constat(s) |
|---|---|---|---|---|---|---|---|---|---|---|
| SYS-01 | Fournisseur | Information sur l'interaction avec une IA | Art. 50, par. 1 et 5 `[TI]` | Obligation | En vigueur (CAL-009) | A1 | Non démontré | PRV-001 | Interface réelle (NV-02) | AIA-001 |
| SYS-01 | Fournisseur | Pas de présentation comme humain | Art. 50, par. 1 | Obligation | En vigueur (CAL-009) | A2 | Impossible à vérifier | PRV-002 | Test de comportement | AIA-001 |
| SYS-01 | Fournisseur | Exception « évident » motivée | Art. 50, par. 1 | Obligation | En vigueur (CAL-009) | A3 | Non applicable (non invoquée ; écartée, section 5) | PRV-001 | n.a. | AIA-001 |
| SYS-01 | Fournisseur | Marquage lisible par machine | Art. 50, par. 2 `[TI]` (+ délai `[O26]`) | Obligation | En vigueur (CAL-010) ; branche transitoire : échéance à confirmer | A4 | Démontré (mesure partielle, propriétaire) | PRV-003 | Documentation du format | AIA-003 |
| SYS-01 | Fournisseur | Préservation du marquage jusqu'aux sorties | Art. 50, par. 2 | Obligation | Idem | A5 | Non démontré | PRV-004, PRV-005 | n.a. | AIA-002 |
| SYS-01 | Fournisseur | Détectabilité, outil de vérification | Art. 50, par. 2 | Obligation | Idem | A6 | Impossible à vérifier | PRV-003, PRV-006 | Outil ou API documentés | AIA-003 |
| SYS-01 | Fournisseur | Exceptions du par. 2 motivées | Art. 50, par. 2 | Obligation | Idem | A7 | Non applicable (aucune exception invoquée ni plausible) | PRV-007 | n.a. | AIA-002 |
| SYS-01 | Fournisseur | Accessibilité, caractère reconnaissable | Art. 50, par. 5 | Obligation | En vigueur (CAL-009) | A11 | Impossible à vérifier | PRV-008 | Interface | AIA-001 |
| SYS-01 | Fournisseur | Recours au code de bonnes pratiques de marquage | Art. 50, par. 7 | Bonne pratique | n.a. | A12 | Impossible à vérifier | PRV-006 | n.a. | AIA-003 |
| SYS-01, SYS-02 | Fournisseur, déployeur | Mesures de maîtrise de l'IA | Art. 4 `[TI]`/`[O26]` | Obligation | En vigueur (CAL-002) ; nouvelle rédaction : échéance à confirmer (CAL-003) | G1-G3 | Impossible à vérifier | PRV-020 | Plan de formation, registre | AIA-010 |
| SYS-02 | Fournisseur | Absence de reconnaissance des émotions des apprenants | Art. 5, par. 1, f) `[TI]` | Obligation | En vigueur (CAL-002) | F1 | Démontré (aucune entrée biométrique observée) | PRV-009 | Qualification juridique (NV-13) | AIA-006 |
| SYS-02 | Fournisseur, déployeur | Absence de notation sociale | Art. 5, par. 1, c) `[TI]` | Obligation | En vigueur (CAL-002) | n.a. | Impossible à vérifier (qualification juridique) | PRV-011 | Analyse juridique | AIA-006 |
| SYS-02 | Fournisseur | Qualification annexe III motivée (orientation, affectation) | Art. 6, par. 2 ; annexe III, point 3 `[TI]` | Obligation (classification) | Classification immédiate ; exigences : CAL-011 | F3, F4 | Non démontré (qualification du projet erronée) | PRV-010, PRV-019 | n.a. | AIA-004 |
| SYS-02 | Fournisseur | Profilage : pas de dérogation | Art. 6, par. 3, dernier al. | Obligation | Idem | F7 | Démontré (profilage présent) | PRV-011 | n.a. | AIA-004 |
| SYS-02 | Fournisseur | Évaluation documentée de la dérogation | Art. 6, par. 4 | Obligation (si invoquée) | `[AV]` (CAL-016) | C11 | Non démontré (dérogation implicitement revendiquée sans évaluation ; de toute façon exclue) | PRV-019 | n.a. | AIA-004 |
| SYS-02 | Fournisseur | Intervention humaine avant effet ; ignorer ou annuler | Art. 14, par. 4, d) `[TI]` | Obligation future | Non encore applicable, échéance à confirmer (CAL-011) | B1, B3 | Non démontré | PRV-012, PRV-014 | Effet réel de `apply_decision` (NV-04) | AIA-005 |
| SYS-02 | Fournisseur | Interprétabilité (justification, confiance) | Art. 14, par. 4, c) ; art. 13 | Obligation future | Idem | B2 | Non démontré | PRV-013 | n.a. | AIA-005 |
| SYS-02 | Fournisseur | Arrêt sûr | Art. 14, par. 4, e) | Obligation future | Idem | B4 | Impossible à vérifier | n.a. | Configuration de production | AIA-005 |
| SYS-02 | Fournisseur | Prévention du biais d'automatisation | Art. 14, par. 4, b) | Obligation future | Idem | B7 | Non démontré | PRV-012, PRV-013 | n.a. | AIA-005 |
| SYS-02 | Déployeur | Superviseurs compétents (conseil de classe) | Art. 26, par. 2 | Obligation future | Idem | B8 | Impossible à vérifier | n.a. | Procédures des établissements | AIA-005 |
| SYS-02 | Fournisseur | Robustesse, cybersécurité (injection de prompt, validation des sorties) | Art. 15 `[TI]` | Obligation future ; bonne pratique immédiate | Idem | D4 | Non démontré | PRV-017 | Tests adverses | AIA-007 |
| SYS-01, SYS-02 | Fournisseur | Versions de modèle épinglées et documentées | Annexe IV, points 1 et 6 | Obligation future (SYS-02) ; bonne pratique (SYS-01) | Idem | C4, E3 | Non démontré | PRV-016 | n.a. | AIA-007 |
| SYS-01, SYS-02 | Fournisseur | Secrets absents du code | Bonne pratique | Bonne pratique | n.a. | D8 | Démontré | PRV-018 | Journaux de production | n.a. |
| SYS-02 | Fournisseur | Journalisation automatique, historique des décisions | Art. 12 ; art. 86 | Obligation future | Non encore applicable (CAL-011) ; art. 86 : conditionnel `[AV]` | E1, E2 | Non démontré | PRV-015 | n.a. | AIA-008 |
| SYS-02 | Fournisseur, déployeur | Conservation des journaux ≥ 6 mois | Art. 19 ; art. 26, par. 6 | Obligation future | Idem | E6 | Non démontré (30 jours déclarés, non utilisés) | PRV-015 | n.a. | AIA-008 |
| SYS-02 | Fournisseur | Documentation technique, gestion des risques, SGQ, évaluation de la conformité, enregistrement | Art. 9, 11, 13, 17, 43, 47-49 ; annexe IV | Obligation future | Non encore applicable (CAL-011) ; art. 49 : `[AV]` | C1-C10, D1-D3, D5-D7 | Impossible à vérifier (hors dépôt) ; documents du dépôt erronés | PRV-019 | Documents hors dépôt (NV-11) | AIA-004, AIA-009 |
| SYS-02 | Déployeur | Information des élèves et familles | Art. 26, par. 11 | Obligation future | Non encore applicable (CAL-011) | F8 | Impossible à vérifier | PRV-023 | Interface, notices | AIA-006 |
| SYS-02 | Déployeur | Analyse d'impact (organismes publics) ; art. 111, par. 2 | Art. 27 ; art. 111, par. 2 `[AV]` | Obligation future / conditionnelle | Conditionnel, échéance à confirmer (CAL-013) | F9 | Impossible à vérifier | PRV-024 | Statut des établissements (NV-03) | AIA-012 |
| Tous | n.a. | Obligations des fournisseurs de modèles GPAI | Art. 53 `[TI]` | Obligation | Non applicable | n.a. | Non applicable | PRV-025 | Contrats (NV-08) | AIA-011 |

### 7.3 Confrontation de la documentation du projet au calendrier de référence (règle impérative 16)

| Affirmation du projet | Fichier:ligne | Référence du skill | Résultat |
|---|---|---|---|
| « Les obligations des systèmes à haut risque s'appliquent depuis le 2 août 2026 » | `docs/compliance.md:3` | CAL-011 : 2027-12-02 (initialement 2026-08-02, reporté par 2026/1744, échéance à confirmer) | **Contredite** |
| « L'article 50 ne s'appliquera qu'à partir du 2 août 2027 » | `docs/compliance.md:4` | CAL-009 et CAL-010 : 2026-08-02 (délai au 2026-12-02 pour le seul par. 2 des systèmes antérieurs au 2026-08-02) | **Contredite** |
| « Les réponses conversationnelles ne sont pas concernées par le marquage de l'article 50 » | `docs/compliance.md:5` | `transparency.md`, section 6 : l'art. 50, par. 2 vise expressément les textes, y compris conversationnels ; une incertitude sur les modalités n'est pas une exemption | **Contredite** |
| « L'orientation n'est pas à haut risque car un humain (le conseil de classe) décide toujours » | `docs/compliance.md:6` | `person-decisions.md`, section 1 : la présence humaine n'exclut pas le haut risque ; profilage = pas de dérogation. Code : application automatique (`app/orientation.py:18-19`) | **Contredite** (en droit et en fait) |
| « Notre champ `ai_generated` garantit la détectabilité de tous les contenus » | `docs/compliance.md:7` | Champ absent des exports (`app/export.py:13, 20`), non signé, propriétaire | **Contredite** |
| « Toutes les recommandations… validées par le conseil de classe… Aucune décision n'est appliquée automatiquement » | `docs/human-oversight.md:3-4` | `app/orientation.py:18-19` | **Contredite** |
| « Projet conforme à l'AI Act et certifié par notre équipe » | `README.md:6` | SKILL.md, règles 2 et 16 ; art. 43 | Non reprise ; aucune base observable |

---

## 8. Cartographie des flux, des modèles et des chemins de sortie

Date d'audit : 2026-10-27 | Commit audité : non versionné.

### 8.1 Chaînes de traitement

```
FCT-01 Assistant de révision (SYS-01)
  Utilisateur : élève ; message libre + historique                       [app/assistant.py:13]
  Application : chat(), aucun prompt système, aucune mention d'IA         [app/assistant.py:10, 13-14]
  Modèle      : Mistral / mistral-large-latest (alias non épinglé)        [app/assistant.py:8, 14]
  Post-trait. : ajout {"meta": {"ai_generated": "true"}} (chaîne non signée) [app/assistant.py:18-19]
  Stockage    : aucun stockage de la réponse dans le dépôt (historique géré par l'appelant, hors dépôt)
  Export      : réponse JSON (route absente du dépôt) ; PDF (export_pdf) ; CSV (export_csv)
                                                                          [app/export.py:7-13, 16-20]

FCT-02 Score d'engagement (SYS-02)
  Utilisateur : élève (indirectement : ses messages de révision)         [app/assistant.py:16]
  Application : prompt « Évalue de 0 à 1 la motivation et la persévérance de cet élève » + messages
                de l'élève injectés tels quels                            [app/assistant.py:24-25]
  Modèle      : Mistral / mistral-large-latest (même alias)               [app/assistant.py:8, 25]
  Post-trait. : float() sans validation ni bornes                          [app/assistant.py:26]
  Stockage    : var/engagement_{student_id}.json, écrasé à chaque message  [app/assistant.py:29-31]
  Export      : lu par recommend_track()                                   [app/orientation.py:8-9]

FCT-03 Orientation (SYS-02)
  Utilisateur : conseil de classe / établissement (déclaratif)            [README.md:13-14 ; app/orientation.py:1]
  Application : moyenne des notes + score d'engagement -> seuils fixes     [app/orientation.py:10-16]
  Modèle      : aucun directement (consomme la sortie de FCT-02)
  Post-trait. : « confidence » = constante codée en dur par branche        [app/orientation.py:12, 14, 16]
  Stockage    : aucun journal ; apply_decision() = print()                  [app/orientation.py:23-24]
  Export      : application automatique si confidence > 0.9 (« sans passage en conseil de classe »)
                ; sinon retour du dict à l'appelant (hors dépôt)            [app/orientation.py:18-20]
```

### 8.2 Matrice fonctionnalités / modèles

| Fonctionnalité | Système | Fournisseur | Modèle | Version épinglée ? | Version journalisée ? | Entrées | Sorties | Traitements intermédiaires | Personnes concernées |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | SYS-01 | Mistral | `mistral-large-latest` | Non (alias) | Non | Message, historique | Texte | Ajout du champ `meta.ai_generated` | Élèves |
| FCT-02 | SYS-02 | Mistral | `mistral-large-latest` (même modèle, autre finalité) | Non (alias) | Non | Messages de l'élève | Score 0-1 (non borné) | `float()` | Élèves |
| FCT-03 | SYS-02 | n.a. | Aucun (règles) | n.a. | n.a. | Notes, score d'engagement | Filière + « confiance » constante ; décision appliquée | Seuils 14 / 10 / 0,6 / 0,9 | Élèves |

Un même modèle sert deux systèmes distincts (SYS-01 et SYS-02) : un changement de la version servie
derrière l'alias `latest` modifie simultanément le tutorat et le scoring d'orientation, sans trace.

### 8.3 Chemins de sortie et marquage (art. 50, par. 2)

| Fonctionnalité | Chemin de sortie | Marquage à la génération | Marquage après transformation | Mécanisme | Détectable par un tiers ? | Outil de vérification | Falsifiable ? | État du contrôle | Preuve |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | Réponse API JSON | `meta.ai_generated = "true"` | n.a. (pas de transformation dans le dépôt) | Propriétaire (champ JSON libre) | Seulement si le client lit et conserve ce champ ; non documenté | Aucun observé | **Oui** (chaîne non signée, retirable ou imitable) | Démontré (présence) ; efficacité non démontrée | PRV-003 |
| FCT-01 | Interface (affichage) | Inconnu | Inconnu | n.a. | n.a. | n.a. | n.a. | Impossible à vérifier (aucune interface dans le dépôt) | PRV-008 |
| FCT-01 | Export PDF | Le texte reçu (`answers: list[str]`) ne porte plus le champ | **Perdu** : `canvas.save()` sans métadonnée ni mention | Aucun | Non | Aucun | n.a. | Non démontré | PRV-004 |
| FCT-01 | Export CSV | Idem | **Perdu** : colonnes `question`, `answer` seulement | Aucun | Non | Aucun | n.a. | Non démontré | PRV-005 |
| FCT-01 | Copier-coller depuis l'interface | Inconnu | Inconnu | n.a. | n.a. | n.a. | n.a. | Impossible à vérifier | PRV-008 |
| FCT-02, FCT-03 | Score, décision | n.a. (pas de contenu synthétique diffusé) | n.a. | n.a. | n.a. | n.a. | n.a. | Non applicable | n.a. |

Remarque : les PDF sont en outre tronqués à 110 caractères par réponse (`app/export.py:11`), ce qui
peut dénaturer les réponses exportées. C'est un point de qualité, pas une obligation.

### 8.4 Ruptures de chaîne identifiées

| Fonctionnalité | Étape | Rupture | Constat(s) |
|---|---|---|---|
| FCT-01 | Export PDF | Perte du marquage, aucune métadonnée de provenance | AIA-002 |
| FCT-01 | Export CSV | Perte du marquage (`meta.ai_generated` non exporté) | AIA-002 |
| FCT-01 | Génération | Marquage propriétaire, non signé, non interopérable | AIA-003 |
| FCT-01/02 | Modèle | Version effectivement servie non épinglée ni journalisée | AIA-007, AIA-008 |
| FCT-02 | Stockage | Score écrasé à chaque message, sans historique ni horodatage | AIA-008 |
| FCT-03 | Décision | Aucune trace de la décision, des facteurs ni de l'intervention humaine (`print`) | AIA-005, AIA-008 |
| FCT-01 → FCT-02 | Réutilisation | Les échanges de révision alimentent une évaluation de la personnalité utilisée pour l'orientation | AIA-006 |

---

## 9. Constats

Ordonnés par gravité puis par identifiant.

### AIA-001 : Aucune information des élèves sur le fait qu'ils échangent avec une IA
- **Système d'IA concerné** : SYS-01.
- **Nature du constat** : Constat technique avéré.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits observables dans le dépôt) / Moyenne (l'interface réelle n'est pas dans le dépôt).
- **Preuve observée** : *Fait observé* : le seul libellé d'interface du dépôt est `BANNER = "Assistant de révision"`, avec le commentaire `# pas de mention d'IA dans l'interface`. `chat()` n'envoie aucun prompt système et le code ne contient aucun message d'information. *Analyse juridique* : manquement potentiel à l'art. 50, par. 1 et 5.
- **Fichier(s) et lignes** : `app/assistant.py:10`, `app/assistant.py:13-14`.
- **Rôle réglementaire concerné** : Fournisseur (QuizMentor SAS, probable).
- **Classification du système** : Non à haut risque (motivé) ; soumis à l'art. 50.
- **Référence juridique** : Art. 50, par. 1 et 5, règlement (UE) 2024/1689 `[TI]` ([AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)).
- **Date d'application** : 2026-08-02, en vigueur à la date d'audit (CAL-009, confiance élevée, sans régime transitoire).
- **Conditions et exceptions** : L'exception « évident pour une personne raisonnablement informée » est écartée : le public est composé de collégiens et lycéens et l'intitulé est neutre. Aucun usage répressif.
- **Explication** : La loi demande que toute personne qui dialogue avec une IA en soit informée au plus tard à la première interaction, de façon claire et accessible. Le code ne prévoit aucune information de ce type, et un commentaire indique qu'elle est volontairement absente de l'interface.
- **Recommandation** : Obligation (art. 50, par. 1 et 5). Afficher, avant ou au début de la première interaction, une mention claire du type « Vous échangez avec un assistant d'intelligence artificielle », adaptée à un jeune public et accessible. Ajouter un prompt système qui impose de répondre honnêtement sur la nature d'IA. Répliquer la mention sur tous les canaux (web, mobile, API exposée aux établissements).
- **Méthode de vérification** : Lecture de `BANNER` et du composant d'interface ; capture d'écran de la première interaction ; test automatisé « Es-tu un humain ? » ; contrôle d'accessibilité (contraste, lecteur d'écran).

### AIA-002 : Le marquage des réponses générées est perdu dans les exports PDF et CSV
- **Système d'IA concerné** : SYS-01.
- **Nature du constat** : Constat technique avéré.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification : modalités du marquage des textes `[AV]` ; lien entre `chat()` et les exports établi par les docstrings et le README).
- **Preuve observée** : *Fait observé* : `export_pdf` écrit le texte des réponses puis appelle `pdf.save()` avec le commentaire « aucune métadonnée de provenance ni mention ». `export_csv` n'exporte que les colonnes `question` et `answer`, avec le commentaire « le champ meta.ai_generated n'est pas exporté ». Aucune occurrence de C2PA, XMP, IPTC, filigrane ou métadonnée de document dans le dépôt. *Analyse juridique* : manquement potentiel à l'art. 50, par. 2 sur ces deux chemins de sortie.
- **Fichier(s) et lignes** : `app/export.py:7-13`, `app/export.py:16-20` ; `README.md:14` (« exports PDF et CSV des échanges »).
- **Rôle réglementaire concerné** : Fournisseur.
- **Classification du système** : Non à haut risque (motivé) ; soumis à l'art. 50.
- **Référence juridique** : Art. 50, par. 2 `[TI]` ; délai transitoire `[O26]`.
- **Date d'application** : 2026-08-02, **en vigueur** dans l'hypothèse déclarée d'une première mise sur le marché le 2026-10-15 (CAL-010 ; pas de régime transitoire). Si une version antérieure du même type de système a été mise sur le marché avant le 2026-08-02 : applicable à compter du 2026-12-02 sous réserve de confirmation sur le texte officiel (**échéance à confirmer**, CAL-010, délai transitoire de sources secondaires). Dans les deux cas, l'obligation est applicable au plus tard dans 36 jours.
- **Conditions et exceptions** : Les exceptions (mise en forme standard, absence de modification substantielle, usage répressif) sont écartées : les réponses sont générées. L'incertitude sur les **modalités** de marquage d'un texte (lignes directrices du 20.7.2026, code de bonnes pratiques) n'est **pas** une exemption (NV-07).
- **Explication** : Les contenus produits par une IA doivent porter une marque lisible par une machine qui permette de les reconnaître comme artificiels. Ici, la seule marque existe dans la réponse de l'API et disparaît dès que les échanges sont exportés en PDF ou en CSV, alors que ces fichiers sont précisément ceux qui circulent hors de l'application.
- **Recommandation** : Obligation (art. 50, par. 2). PDF : renseigner les métadonnées du document (XMP, propriétés) avec une indication de provenance IA et ajouter une mention visible ; envisager un manifeste C2PA. CSV : ajouter une colonne de provenance (par exemple `ai_generated`, modèle, horodatage) ou un fichier de provenance joint. Ajouter des tests de bout en bout qui vérifient la présence du marquage à chaque sortie.
- **Méthode de vérification** : Tests automatisés générant un PDF et un CSV puis contrôlant les métadonnées et la colonne de provenance ; lecture des métadonnées avec un outil tiers (par exemple `exiftool`).

### AIA-005 : Décisions d'orientation appliquées automatiquement, sans conseil de classe, contrairement à la documentation
- **Système d'IA concerné** : SYS-02.
- **Nature du constat** : Risque potentiel.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits du code) / Moyenne (effet réel de `apply_decision`, qui se limite à un `print` dans le dépôt).
- **Preuve observée** : *Fait observé* : `if confidence > 0.9: apply_decision(decision)  # appliquée sans passage en conseil de classe`. La « confiance » est une **constante codée en dur** par branche (0,95 pour « générale », 0,8 pour « technologique », 0,92 pour « professionnelle ») : ce n'est pas une mesure statistique. Les orientations « générale » et « professionnelle » sont donc toujours appliquées automatiquement ; seule « technologique » reste une recommandation. Aucune fonction de validation, de rejet ou de modification et aucune justification ne sont exposées. `docs/human-oversight.md` affirme au contraire qu'« aucune décision n'est appliquée automatiquement ». *Analyse juridique* : si SYS-02 est à haut risque, le système ne permet pas l'intervention humaine prévue par l'art. 14, par. 4, b), c) et d) (obligation non encore applicable). Un risque actuel existe pour les élèves.
- **Fichier(s) et lignes** : `app/orientation.py:11-19`, `app/orientation.py:23-24` ; `docs/human-oversight.md:3-4`.
- **Rôle réglementaire concerné** : Fournisseur (conception, art. 14) ; déployeurs (art. 26, par. 2).
- **Classification du système** : Haut risque probable (annexe III, point 3).
- **Référence juridique** : Art. 14, par. 4, b), c), d) `[TI]` ; art. 13 `[TI]` ; art. 26, par. 2 `[TI]` ; dates `[O26]`.
- **Date d'application** : Art. 14 et 26 applicables à compter du 2027-12-02 sous réserve de confirmation sur le texte officiel (**échéance à confirmer**, CAL-011) ; pour ce système antérieur, art. 111, par. 2 (CAL-013, conditionnel, échéance à confirmer). Le risque pour les personnes existe dès aujourd'hui.
- **Conditions et exceptions** : Aucune exception. La présence d'un humain n'exclut pas le haut risque et le code l'écarte de toute façon pour deux des trois issues. L'orientation « professionnelle » automatique repose sur les seules notes (règle déterministe), mais elle fait partie de la même chaîne de décision. Les décisions individuelles automatisées relèvent aussi d'autres législations (hors périmètre, signalées).
- **Explication** : Des orientations scolaires d'élèves, en majorité mineurs, sont enregistrées automatiquement. Le seuil qui déclenche cet enregistrement repose sur une « confiance » qui n'est pas calculée. Le conseil de classe, présenté comme décideur, n'intervient donc pas. La documentation du projet décrit l'inverse.
- **Recommandation** : Obligation future (art. 14) et mesure de réduction d'un risque actuel : supprimer immédiatement l'application automatique (`apply_decision`) ; faire de toute sortie une **proposition** au statut « en attente de validation » ; permettre au conseil de classe de valider, modifier ou rejeter avec un motif ; afficher les facteurs (moyenne, score d'engagement et sa provenance) et les limites ; supprimer ou renommer l'indice de « confiance » factice ; corriger `docs/human-oversight.md`.
- **Méthode de vérification** : Revue de code (absence d'appel d'effet sans validation authentifiée) ; test unitaire montrant qu'aucune décision n'est enregistrée sans action humaine ; journal des validations (qui, quand, décision, motif).

### AIA-004 : Système d'orientation susceptible de relever du haut risque (annexe III, point 3), avec profilage, et exigences non préparées
- **Système d'IA concerné** : SYS-02.
- **Nature du constat** : Non encore applicable.
- **Gravité** : Élevée (enjeu pour des mineurs, effort de préparation important : gestion des risques, documentation de l'annexe IV, SGQ, évaluation de la conformité, enregistrement).
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification).
- **Preuve observée** : *Fait observé* : `recommend_track` détermine une filière (générale, technologique, professionnelle) « présentée au conseil de classe » à partir des notes et d'un score de « motivation et persévérance » inféré par un LLM. *Analyse juridique* : destination susceptible de relever de l'annexe III, point 3, a) (affectation) et/ou c) (niveau d'enseignement approprié). Le profilage d'élèves exclut la dérogation de l'art. 6, par. 3. La documentation du projet conclut à tort à l'absence de haut risque (`docs/compliance.md:6`) et situe à tort l'application au 2 août 2026 (`docs/compliance.md:3`).
- **Fichier(s) et lignes** : `app/orientation.py:1-20` ; `app/assistant.py:17, 22-26` ; `docs/compliance.md:3, 6` ; `README.md:13-14`.
- **Rôle réglementaire concerné** : Fournisseur (art. 16) ; déployeurs (art. 26, 27).
- **Classification du système** : Haut risque probable (annexe III, point 3, a) et/ou c)).
- **Référence juridique** : Art. 6, par. 2 et 3 ; annexe III, point 3 `[TI]` ; art. 9 à 17, 43, 47 à 49 `[TI]` ; date `[O26]` ; art. 111, par. 2 `[AV]` ([AI Act Explorer, art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6)).
- **Date d'application** : Exigences du chapitre III applicables à compter du 2027-12-02 sous réserve de confirmation sur le texte officiel (**échéance à confirmer**, CAL-011). Le système est déclaré mis en service le 2026-10-15, avant cette date : l'art. 111, par. 2 le soumettrait aux exigences seulement en cas de modification importante de sa conception après la date de référence, ou au plus tard le 2030-08-02 s'il est destiné à des autorités publiques (CAL-013, confiance faible, échéance à confirmer). Art. 49, 72, 73 et 86 : conditionnels `[AV]`.
- **Conditions et exceptions** : Art. 6, par. 3 écarté (profilage). L'annexe I ne s'applique pas. Le régime de l'art. 111, par. 2 ne doit pas être lu comme une exemption durable : un changement de modèle (alias `latest`) ou de logique de décision peut constituer une modification importante `[AV]`.
- **Explication** : Les systèmes d'IA qui orientent des élèves vers une filière ou un établissement figurent parmi les usages à haut risque. Quand le système évalue la personnalité des élèves (profilage), aucune dérogation n'est possible. Les exigences lourdes ne s'appliqueront qu'à partir de fin 2027, voire plus tard pour un système déjà en service, mais elles demandent plusieurs mois de préparation.
- **Recommandation** : Obligation future. (1) Documenter la classification et corriger `docs/compliance.md`. (2) Décider de la trajectoire : soit retirer le score d'engagement inféré par IA de la chaîne d'orientation (le reste ne serait vraisemblablement plus un système d'IA, à confirmer), soit engager une feuille de route haut risque (gestion des risques, gouvernance des données, documentation de l'annexe IV, journalisation, notice d'utilisation, contrôle humain, exactitude et robustesse, SGQ, évaluation de la conformité, déclaration UE, marquage CE, enregistrement). (3) Encadrer toute évolution majeure au regard de l'art. 111, par. 2.
- **Méthode de vérification** : Fiche de classification signée ; registre des risques ; documentation de l'annexe IV ; preuve de la décision d'architecture (retrait du score ou feuille de route).

### AIA-006 : Réutilisation des échanges de révision pour profiler la motivation des élèves et orienter leur parcours
- **Système d'IA concerné** : SYS-02 (alimenté par SYS-01).
- **Nature du constat** : À vérifier juridiquement ou organisationnellement.
- **Gravité** : Élevée.
- **Niveau de confiance** : Élevée (faits) / Faible (qualification au titre de l'art. 5).
- **Preuve observée** : *Fait observé* : à chaque message de révision, le modèle reçoit l'ensemble des messages de l'élève avec la consigne « Évalue de 0 à 1 la motivation et la persévérance de cet élève ». Le score est stocké par identifiant d'élève et « réutilisé par app/orientation.py », où un score inférieur à 0,6 écarte la filière générale même avec une moyenne d'au moins 14. Aucun élément du dépôt n'informe l'élève de cette réutilisation. *Analyse juridique* : (i) art. 5, par. 1, f) examiné et **non retenu** à ce stade (inférence à partir de texte, sans données biométriques, art. 3, point 39), confiance moyenne ; (ii) art. 5, par. 1, c) : une évaluation de caractéristiques personnelles tirée d'un contexte (révision) et produisant un effet dans un autre (orientation) **pourrait** être examinée comme notation sociale si le traitement était jugé injustifié ou disproportionné. Les conditions ne sont pas établies, d'où « à vérifier » ; (iii) information des personnes (art. 26, par. 11) et droit à l'explication (art. 86) : obligations futures.
- **Fichier(s) et lignes** : `app/assistant.py:16-17, 22-26, 29-31` ; `app/orientation.py:8-12`.
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs.
- **Classification du système** : Haut risque probable (annexe III, point 3) ; pratique interdite non retenue à ce stade, à vérifier.
- **Référence juridique** : Art. 5, par. 1, c) et f) `[TI]` ; art. 3, point 39 `[TI]` ; art. 26, par. 11 `[TI]` ; art. 86 `[TI]` (date `[AV]`).
- **Date d'application** : Art. 5 en vigueur depuis le 2025-02-02 (CAL-002). Art. 26, par. 11 : à compter du 2027-12-02, échéance à confirmer (CAL-011). Art. 86 : conditionnel.
- **Conditions et exceptions** : Art. 5, par. 1, f) : l'exception médicale ou de sécurité n'est pas en cause, puisque la qualification elle-même est écartée faute de données biométriques. Art. 5, par. 1, c) : conditions cumulatives (évaluation fondée sur le comportement ou des caractéristiques personnelles, traitement préjudiciable dans un contexte sans lien, ou injustifié ou disproportionné) à apprécier juridiquement.
- **Explication** : Les élèves utilisent l'assistant pour réviser. Leurs messages servent en réalité aussi à évaluer leur motivation, et cette évaluation, produite par un modèle de langage, peut leur fermer une filière. Ce double usage n'apparaît nulle part pour l'élève. La qualification juridique précise demande un examen par un juriste, mais le risque d'atteinte aux droits est réel.
- **Recommandation** : Obligation à vérifier (art. 5) et préparation d'obligations futures. Faire réaliser une analyse juridique de ce double usage au regard de l'art. 5, par. 1, c) et f). Dans l'attente, suspendre la réutilisation du score d'engagement pour l'orientation (mesure de précaution). Séparer techniquement SYS-01 et SYS-02. Si l'usage est maintenu, informer les élèves et les familles et documenter la finalité.
- **Méthode de vérification** : Note juridique datée ; revue de code montrant la suppression du flux `var/engagement_*.json` → `recommend_track` ou son encadrement ; textes d'information affichés.

### AIA-003 : Marqueur `ai_generated` propriétaire, non signé et falsifiable : détectabilité non démontrée
- **Système d'IA concerné** : SYS-01.
- **Nature du constat** : Risque potentiel.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification ; modalités du marquage des textes `[AV]`).
- **Preuve observée** : *Fait observé* : `return {"answer": text, "meta": {"ai_generated": "true"}}`, avec le commentaire « simple champ JSON non signé, ajouté uniquement à la réponse de l'API ». Aucun standard (C2PA, IPTC/XMP), aucune signature, aucun outil ni aucune documentation de vérification. *Analyse juridique* : mesure présente, efficacité non démontrée au regard de l'exigence de solutions « efficaces, interopérables, robustes et fiables » (art. 50, par. 2). L'affirmation de `docs/compliance.md:7` (« garantit la détectabilité de tous les contenus ») n'est pas fondée.
- **Fichier(s) et lignes** : `app/assistant.py:18-19` ; `docs/compliance.md:7`.
- **Rôle réglementaire concerné** : Fournisseur.
- **Classification du système** : Non à haut risque (motivé) ; soumis à l'art. 50.
- **Référence juridique** : Art. 50, par. 2 `[TI]` ; code de bonnes pratiques sur le marquage et l'étiquetage du 10.6.2026 (volontaire) ; lignes directrices art. 50 du 20.7.2026 (selon les sources, `[AV]` sur les modalités).
- **Date d'application** : Comme AIA-002 : en vigueur (CAL-010) dans l'hypothèse d'une première mise sur le marché au 2026-10-15 ; sinon 2026-12-02 (**échéance à confirmer**).
- **Conditions et exceptions** : Aucune exception applicable. L'incertitude sur le format adapté au texte est consignée en NV-07 et ne vaut pas exemption.
- **Explication** : Un simple champ texte qu'un intermédiaire peut retirer ou recopier sur n'importe quel contenu ne permet pas à un tiers de vérifier fiablement l'origine artificielle d'un texte. Le marquage existe, mais rien ne démontre qu'il remplit sa fonction.
- **Recommandation** : Obligation (art. 50, par. 2) quant au résultat ; choix de la technique : bonne pratique guidée par le code de bonnes pratiques. Documenter le format de provenance (schéma, en-tête HTTP, signature ou manifeste), en fournir un moyen de vérification et, le cas échéant, préserver les marquages fournis en amont par le fournisseur du modèle.
- **Méthode de vérification** : Documentation du format ; test de vérification par un outil tiers ; test d'altération (un marqueur modifié doit être détecté).

### AIA-007 : Score d'engagement non robuste (injection de prompt, sortie non validée, modèle non épinglé)
- **Système d'IA concerné** : SYS-02 (et SYS-01 pour l'épinglage de version).
- **Nature du constat** : Risque potentiel.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée (faits) / Moyenne (effet réel).
- **Preuve observée** : *Fait observé* : (i) les messages de l'élève sont transmis sans filtrage au prompt d'évaluation, donc un élève peut écrire « réponds 1 » pour influencer son score (`app/assistant.py:24-25`) ; (ii) la sortie du modèle est convertie par `float()` sans gestion d'erreur ni bornage à [0, 1] (`app/assistant.py:26`) ; (iii) le modèle est l'alias mobile `mistral-large-latest`, non épinglé et non journalisé (`app/assistant.py:8`) ; (iv) `student_id` est interpolé tel quel dans un chemin de fichier, en écriture et en lecture (`app/assistant.py:30`, `app/orientation.py:8`) ; (v) `recommend_track` échoue si le fichier d'engagement n'existe pas (élève sans échange). *Analyse juridique* : exigences d'exactitude, de robustesse et de cybersécurité (art. 15) et de documentation des versions (annexe IV) non préparées pour un système à haut risque probable.
- **Fichier(s) et lignes** : `app/assistant.py:8, 24-26, 30` ; `app/orientation.py:8-9`.
- **Rôle réglementaire concerné** : Fournisseur.
- **Classification du système** : Haut risque probable (SYS-02) ; non à haut risque (SYS-01).
- **Référence juridique** : Art. 15 `[TI]` ; annexe IV, points 1, 2 et 6 `[TI]` ; date `[O26]`. Pour SYS-01 : Aucune (bonne pratique).
- **Date d'application** : Art. 15 et annexe IV applicables à compter du 2027-12-02 sous réserve de confirmation (**échéance à confirmer**, CAL-011 ; CAL-013 conditionnel). Bonne pratique immédiate.
- **Conditions et exceptions** : Aucune.
- **Explication** : Le score qui pèse sur l'orientation peut être manipulé par l'élève, varier quand le fournisseur met à jour le modèle derrière l'alias, ou faire échouer le traitement. Pour une évaluation à fort enjeu, ces défauts créent dès aujourd'hui un risque d'erreur et d'inégalité de traitement.
- **Recommandation** : Obligation future (SYS-02) ; bonne pratique immédiate : épingler une version datée du modèle et la journaliser ; isoler les entrées utilisateur du prompt d'évaluation et tester la résistance à l'injection ; valider et borner la sortie (sortie structurée, valeur par défaut sûre, alerte) ; assainir `student_id` (identifiant opaque, liste blanche) ; gérer l'absence de score.
- **Méthode de vérification** : Tests unitaires (sortie non numérique, valeurs hors bornes, injection) ; configuration montrant une version épinglée ; journal contenant la version servie.

### AIA-008 : Aucune traçabilité des scores et des décisions d'orientation ; rétention déclarée de 30 jours
- **Système d'IA concerné** : SYS-02.
- **Nature du constat** : Non encore applicable.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification).
- **Preuve observée** : *Fait observé* : `LOG_RETENTION_DAYS = 30` est déclarée mais n'est utilisée nulle part. `apply_decision` se limite à un `print`. Le score d'engagement est écrasé à chaque message (mode `"w"`), sans horodatage ni version du modèle. Aucun journal des décisions, des facteurs ou des interventions humaines. *Analyse juridique* : exigences de journalisation (art. 12) et de conservation d'au moins six mois (art. 19 ; art. 26, par. 6) non préparées. La capacité à fournir une explication (art. 86) n'est pas assurée.
- **Fichier(s) et lignes** : `app/config.py:2` ; `app/orientation.py:23-24` ; `app/assistant.py:29-31`.
- **Rôle réglementaire concerné** : Fournisseur (art. 12, 19) ; déployeurs (art. 26, par. 6).
- **Classification du système** : Haut risque probable (annexe III, point 3).
- **Référence juridique** : Art. 12, 19, 26, par. 6 `[TI]` ; art. 86 `[TI]` (date `[AV]`) ; dates `[O26]`.
- **Date d'application** : À compter du 2027-12-02 sous réserve de confirmation sur le texte officiel (**échéance à confirmer**, CAL-011) ; CAL-013 conditionnel ; art. 86 conditionnel.
- **Conditions et exceptions** : Aucune.
- **Explication** : On ne peut aujourd'hui ni retrouver pourquoi un élève a reçu telle orientation, ni avec quel score et quelle version du modèle, ni qui l'a validée. Le paramètre de conservation de 30 jours est inférieur au minimum de six mois prévu pour les systèmes à haut risque.
- **Recommandation** : Obligation future. Mettre en place un journal d'audit horodaté et protégé (entrées pertinentes ou leurs empreintes, score, version du modèle et du prompt, seuils, décision, intervention humaine) ; porter la rétention à au moins six mois et l'appliquer effectivement ; conserver l'historique des scores.
- **Méthode de vérification** : Schéma de journal ; test produisant une entrée de journal pour chaque décision ; configuration de rétention effectivement appliquée.

### AIA-009 : Documentation de conformité du projet erronée et allégation de certification
- **Système d'IA concerné** : SYS-01 et SYS-02.
- **Nature du constat** : Constat technique avéré.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Élevée.
- **Preuve observée** : *Fait observé* : `README.md:6` affirme « Projet conforme à l'AI Act et certifié par notre équipe ». Les cinq affirmations de `docs/compliance.md:3-7` et celles de `docs/human-oversight.md:3-4` sont contredites par le calendrier de référence ou par le code (tableau de la section 7.3). *Analyse juridique* : une auto-déclaration interne n'est ni une évaluation de la conformité (art. 43) ni une déclaration UE de conformité (art. 47). Des informations inexactes transmises aux déployeurs (future notice, art. 13) ou aux autorités (art. 99, par. 5) seraient problématiques.
- **Fichier(s) et lignes** : `README.md:6` ; `docs/compliance.md:3-7` ; `docs/human-oversight.md:3-4`.
- **Rôle réglementaire concerné** : Fournisseur.
- **Classification du système** : SYS-01 non à haut risque (motivé) ; SYS-02 haut risque probable.
- **Référence juridique** : Aucune obligation directe en vigueur (bonne pratique) ; pour mémoire : art. 13, 43, 47 `[TI]` (haut risque, futur) ; art. 99, par. 5 `[TI]` (informations inexactes fournies aux autorités).
- **Date d'application** : Sans objet pour la bonne pratique ; art. 13, 43, 47 : 2027-12-02, échéance à confirmer (CAL-011).
- **Conditions et exceptions** : Aucune.
- **Explication** : Les documents du projet donnent des dates fausses, excluent à tort les réponses conversationnelles du marquage, décrivent une supervision humaine que le code ne met pas en œuvre et revendiquent une certification sans fondement. S'ils sont communiqués aux établissements, ils peuvent les induire en erreur sur leurs propres obligations.
- **Recommandation** : Bonne pratique (préparatoire aux art. 13 et 47). Retirer la mention « conforme et certifié » ; réécrire `docs/compliance.md` et `docs/human-oversight.md` à partir du calendrier de référence et du comportement réel du code ; dater et versionner ces documents.
- **Méthode de vérification** : Relecture des documents corrigés ; comparaison avec le code et avec `data/ai-act-calendar.json`.

### AIA-012 : Statut des établissements déployeurs et date de première mise sur le marché à établir (art. 111, par. 2 ; art. 27)
- **Système d'IA concerné** : SYS-02 (et SYS-01 pour l'art. 50, par. 2).
- **Nature du constat** : À vérifier juridiquement ou organisationnellement.
- **Gravité** : Moyenne.
- **Niveau de confiance** : Faible (référence `[AV]`, faits non disponibles).
- **Preuve observée** : *Fait observé* : le README vise des « collèges et lycées de l'Union » sans préciser leur statut, et ne date que la mise en service de la « version actuelle » (2026-10-15). *Analyse juridique* : le statut public des déployeurs conditionne l'échéance spécifique de l'art. 111, par. 2 (2030-08-02 selon la majorité des sources, 2028-01-28 selon une source) et l'analyse d'impact sur les droits fondamentaux (art. 27). La date de première mise sur le marché du type conditionne l'art. 111, par. 2 et le délai de l'art. 50, par. 2.
- **Fichier(s) et lignes** : `README.md:8-10`.
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs.
- **Classification du système** : Haut risque probable (SYS-02).
- **Référence juridique** : Art. 111, par. 2 modifié `[AV]` ; art. 27 `[TI]` ; art. 26, par. 8 `[TI]`.
- **Date d'application** : Conditionnel ; si destiné à des autorités publiques : au plus tard le 2030-08-02 sous réserve de confirmation sur le texte officiel (**échéance à confirmer**, CAL-013, confiance faible) ; art. 27 : avec le chapitre III (CAL-011, échéance à confirmer).
- **Conditions et exceptions** : Divergence des sources sur l'échéance des autorités publiques (`legal-sources.md`, section 5).
- **Explication** : Les dates exactes auxquelles les obligations du haut risque s'appliqueront à ce système dépendent de deux informations absentes du dépôt : depuis quand le système existe sur le marché, et si les établissements clients sont publics.
- **Recommandation** : À vérifier. Établir la date de première mise sur le marché de chaque version majeure et le statut des établissements clients ; faire confirmer sur le texte officiel l'échéance applicable ; préparer, avec les établissements publics, l'analyse d'impact (art. 27).
- **Méthode de vérification** : Registre des versions et des contrats clients ; note juridique.

### AIA-010 : Mesures de maîtrise de l'IA non observables dans le dépôt
- **Système d'IA concerné** : SYS-01 et SYS-02.
- **Nature du constat** : À vérifier juridiquement ou organisationnellement.
- **Gravité** : Faible.
- **Niveau de confiance** : Moyenne (référence `[O26]` pour la nouvelle rédaction).
- **Preuve observée** : *Fait observé* : aucun document de formation, guide d'usage ou avertissement destiné au personnel de QuizMentor, aux enseignants ou au conseil de classe. *Analyse juridique* : l'absence dans le dépôt n'est pas une preuve d'absence de mesures.
- **Fichier(s) et lignes** : non disponible (dépôt entier examiné).
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs.
- **Classification du système** : Tous.
- **Référence juridique** : Art. 4 `[TI]`, rédaction modifiée par le règlement 2026/1744 `[O26]` (à confirmer sur le JO).
- **Date d'application** : En vigueur depuis le 2025-02-02 (CAL-002) ; nouvelle rédaction au 2026-07-27, **échéance à confirmer** (CAL-003).
- **Conditions et exceptions** : Selon les sources, la nouvelle rédaction impose de prendre des mesures sans exiger un niveau déterminé.
- **Explication** : Les personnes qui conçoivent et utilisent ces systèmes, en particulier les membres du conseil de classe confrontés à un score d'IA, doivent être aidées à en comprendre les limites. Le dépôt ne permet pas de savoir si c'est le cas.
- **Recommandation** : Obligation (art. 4). Documenter les mesures (formation des équipes, guide pour les enseignants sur les limites du score et le biais d'automatisation) et en conserver la trace (bonne pratique).
- **Méthode de vérification** : Plan de formation, supports, registre de participation.

### AIA-011 : Obligations des fournisseurs de modèles GPAI non applicables à QuizMentor
- **Système d'IA concerné** : SYS-01 et SYS-02.
- **Nature du constat** : Non applicable.
- **Gravité** : Information.
- **Niveau de confiance** : Élevée (dépôt) / Moyenne (contrats non vus).
- **Preuve observée** : *Fait observé* : modèle consommé via l'API de Mistral (`mistralai`, `mistral-large-latest`) ; aucun script d'entraînement ou d'affinage, aucun jeu de données, aucune publication de poids ; `README.md:11` : « Aucun entraînement de modèle ».
- **Fichier(s) et lignes** : `requirements.txt:2` ; `app/assistant.py:5-8` ; `README.md:11`.
- **Rôle réglementaire concerné** : Fournisseur de système d'IA (fournisseur en aval, art. 3, point 68) ; le fournisseur du modèle GPAI est Mistral.
- **Classification du système** : Sans objet.
- **Référence juridique** : Art. 3, points 63 et 68 ; art. 53 `[TI]`.
- **Date d'application** : 2025-08-02 (CAL-005), sans objet pour QuizMentor.
- **Conditions et exceptions** : Conclusion à revoir si QuizMentor affinait ou publiait un modèle.
- **Explication** : Les obligations propres aux modèles d'IA à usage général pèsent sur le fournisseur du modèle, pas sur l'entreprise qui l'intègre par API. QuizMentor reste en revanche responsable de ses propres systèmes.
- **Recommandation** : Bonne pratique : obtenir et conserver la documentation du fournisseur du modèle destinée aux fournisseurs en aval (annexe XII), vérifier ses conditions d'utilisation pour un usage auprès de mineurs et d'évaluation, et vérifier s'il applique un marquage en amont.
- **Méthode de vérification** : Contrat et documentation du fournisseur archivés.

---

## 10. Matrice des preuves

Commit : non versionné (toutes les preuves). Date de collecte : 2026-10-27. Méthode de reproduction
exprimée depuis la racine du projet (`demo-adversarial/`).

| PRV | Contrôle | Constat(s) | Fichier | Lignes | Commit | Date | Nature | Méthode de reproduction | État |
|---|---|---|---|---|---|---|---|---|---|
| PRV-001 | A1, A3 | AIA-001 | `app/assistant.py` | 10 | non versionné | 2026-10-27 | Statique | `sed -n '10p' app/assistant.py` | Non démontré |
| PRV-002 | A2 | AIA-001 | `app/assistant.py` | 13-14 | non versionné | 2026-10-27 | Statique | `sed -n '13,14p' app/assistant.py` (aucun prompt système ; comportement du modèle non testable statiquement) | Impossible à vérifier |
| PRV-003 | A4, A6 | AIA-003, AIA-002 | `app/assistant.py` | 18-19 | non versionné | 2026-10-27 | Statique | `sed -n '18,19p' app/assistant.py` | Démontré (mesure partielle) |
| PRV-004 | A5 | AIA-002 | `app/export.py` | 7-13 | non versionné | 2026-10-27 | Statique | `sed -n '7,13p' app/export.py` | Non démontré |
| PRV-005 | A5 | AIA-002 | `app/export.py` | 16-20 | non versionné | 2026-10-27 | Statique | `sed -n '16,20p' app/export.py` | Non démontré |
| PRV-006 | A6, A12 | AIA-003 | (dépôt entier) | n.a. | non versionné | 2026-10-27 | Statique | `grep -rniE "c2pa\|xmp\|iptc\|watermark\|filigrane\|detect\|metadata" .` → aucun résultat | Impossible à vérifier (outil éventuel hors dépôt) |
| PRV-007 | A7 | AIA-002 | `app/assistant.py` | 13-15 | non versionné | 2026-10-27 | Statique | `sed -n '13,15p' app/assistant.py` (génération de réponses libres) | Non applicable |
| PRV-008 | A11 | AIA-001 | (dépôt entier) | n.a. | non versionné | 2026-10-27 | Statique | `grep -rn "@app\|router\|FastAPI" .` → aucun résultat : interface absente | Impossible à vérifier |
| PRV-009 | F1 | AIA-006 | `app/assistant.py` | 22-26 | non versionné | 2026-10-27 | Statique | `sed -n '22,26p' app/assistant.py` (entrées textuelles uniquement) | Démontré (aucune entrée biométrique) |
| PRV-010 | F3, F4 | AIA-004 | `app/orientation.py` | 1-20 | non versionné | 2026-10-27 | Statique | `sed -n '1,20p' app/orientation.py` | Non démontré (qualification) |
| PRV-011 | F7, art. 5 c) | AIA-004, AIA-006 | `app/assistant.py` ; `app/orientation.py` | 16-17, 22-31 ; 8-11 | non versionné | 2026-10-27 | Statique | `sed -n '16,31p' app/assistant.py; sed -n '8,11p' app/orientation.py` | Démontré (profilage présent) |
| PRV-012 | B1, B3, B7 | AIA-005 | `app/orientation.py` | 17-19, 23-24 | non versionné | 2026-10-27 | Statique | `sed -n '17,24p' app/orientation.py` | Non démontré |
| PRV-013 | B2, B7 | AIA-005 | `app/orientation.py` | 11-16 | non versionné | 2026-10-27 | Statique | `sed -n '11,16p' app/orientation.py` (constantes 0.95 / 0.8 / 0.92) | Non démontré |
| PRV-014 | B1 | AIA-005, AIA-009 | `docs/human-oversight.md` | 3-4 | non versionné | 2026-10-27 | Statique | `sed -n '3,4p' docs/human-oversight.md` (comparer à PRV-012) | Non démontré (documentation contredite) |
| PRV-015 | E1, E2, E6 | AIA-008 | `app/config.py` ; `app/orientation.py` ; `app/assistant.py` | 2 ; 23-24 ; 29-31 | non versionné | 2026-10-27 | Statique | `grep -rn "LOG_RETENTION_DAYS" .` (une seule occurrence, jamais utilisée) ; `sed -n '23,24p' app/orientation.py` | Non démontré |
| PRV-016 | C4, E3 | AIA-007 | `app/assistant.py` | 8 | non versionné | 2026-10-27 | Statique | `sed -n '8p' app/assistant.py` | Non démontré |
| PRV-017 | D4 | AIA-007 | `app/assistant.py` ; `app/orientation.py` | 24-26, 30 ; 8 | non versionné | 2026-10-27 | Statique | `sed -n '24,30p' app/assistant.py; sed -n '8p' app/orientation.py` | Non démontré |
| PRV-018 | D8 | n.a. | `app/assistant.py` | 7 | non versionné | 2026-10-27 | Statique | `sed -n '7p' app/assistant.py` (clé lue dans l'environnement, aucune valeur en clair) | Démontré |
| PRV-019 | C11, C1-C10 | AIA-004, AIA-009 | `docs/compliance.md` ; `README.md` | 3-7 ; 6 | non versionné | 2026-10-27 | Statique | `cat docs/compliance.md; sed -n '6p' README.md` | Non démontré |
| PRV-020 | G1-G3 | AIA-010 | (dépôt entier) | n.a. | non versionné | 2026-10-27 | Statique | `find . -type f` (aucun support de formation) | Impossible à vérifier |
| PRV-021 | Inventaire | Tous | (dépôt entier) | n.a. | non versionné | 2026-10-27 | Statique | `python3 <skill>/scripts/scan_ai_signals.py <projet>` | Démontré (signaux) |
| PRV-022 | C3 | AIA-011 | `requirements.txt` | 1-3 | non versionné | 2026-10-27 | Statique | `cat requirements.txt` | Démontré |
| PRV-023 | F8 | AIA-006 | (dépôt entier) | n.a. | non versionné | 2026-10-27 | Statique | Absence d'interface (cf. PRV-008) | Impossible à vérifier |
| PRV-024 | F9, calendrier | AIA-004, AIA-012 | `README.md` ; calendrier du skill | 8-10 | non versionné | 2026-10-27 | Statique | `python3 <skill>/scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-10-15 --scope high-risk-annex-iii --public-authority` | Impossible à vérifier (statut des déployeurs) |
| PRV-025 | GPAI | AIA-011 | (dépôt entier) ; `README.md` | 11 | non versionné | 2026-10-27 | Statique | `grep -rniE "train\|fine_tune\|dataset\|upload" .` → aucun résultat | Non applicable |
| PRV-026 | Calendrier art. 50 | AIA-001 à AIA-003 | calendrier du skill | n.a. | non versionné | 2026-10-27 | Statique | `python3 <skill>/scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-10-15` puis `--placed-on-market 2026-03-01 --scope transparency` | Démontré (statuts calculés) |

**Preuves externes nécessaires** (non établissables par analyse statique) : interface et parcours
réels de l'élève ; configuration de production (modèle effectivement servi, journaux, rétention) ;
effet de `apply_decision` dans le système d'information scolaire ; contrats et statut des
établissements ; documentation et conditions d'utilisation de Mistral ; supports de formation ;
documentation technique, registre des risques et SGQ éventuels hors dépôt ; analyse juridique des
art. 5, par. 1, c) et f).

Rappel : « mesure observée » n'équivaut pas à « obligation satisfaite ».

---

## 11. Registre des éléments non vérifiables

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact sur la classification ou les obligations | Interlocuteur suggéré | Constat(s) liés |
|---|---|---|---|---|---|---|---|
| NV-01 | SYS-01, SYS-02 | Date de **première** mise sur le marché ou en service du type de système (versions antérieures à la « version actuelle » du 2026-10-15) | Information | Le README ne date que la version actuelle | CAL-010 (en vigueur ou 2026-12-02) ; CAL-013 (régime des systèmes antérieurs) | Direction produit QuizMentor | AIA-002, AIA-003, AIA-004, AIA-012 |
| NV-02 | SYS-01 | Interface réelle (web, mobile), textes affichés, comportement si l'élève demande s'il parle à un humain, accessibilité, copier-coller | Document / information | Aucune interface dans le dépôt | Art. 50, par. 1 et 5 | Équipe front-end | AIA-001 |
| NV-03 | SYS-02 | Statut des établissements clients (publics, privés sous contrat, autorités publiques) | Information / juridique | Art. 27, art. 26, par. 8, art. 111, par. 2 | Échéance 2030-08-02 ou régime conditionnel ; analyse d'impact | Direction commerciale, juriste | AIA-012 |
| NV-04 | SYS-02 | Effet réel de `apply_decision` (inscription dans le système d'information scolaire ?) et rôle effectif du conseil de classe | Information | Le dépôt se limite à un `print` | Gravité de l'automatisation ; art. 14 | Équipe technique, établissements | AIA-005 |
| NV-05 | SYS-02 | Autres usages du score d'engagement (« tableau de bord enseignant », `README.md:13`) | Information | Possible système d'évaluation distinct (annexe III, point 3, b)) | Classification d'un éventuel SYS-03 | Équipe produit | AIA-004, AIA-006 |
| NV-06 | SYS-02 | Information des élèves et familles sur la réutilisation des échanges et sur l'orientation assistée par IA | Document | Non observable | Art. 26, par. 11 (futur) ; appréciation de l'art. 5 | Établissements, QuizMentor | AIA-006 |
| NV-07 | SYS-01 | Modalités techniques de marquage des textes (lignes directrices art. 50 du 20.7.2026, code de bonnes pratiques du 10.6.2026) | Juridique | Format adapté au texte non établi `[AV]` | **Aucune exemption** : seulement le choix de la technique | Juriste, équipe technique | AIA-002, AIA-003 |
| NV-08 | SYS-01, SYS-02 | Documentation du fournisseur du modèle (annexe XII), conditions d'utilisation, marquage amont, version servie derrière l'alias | Document | Obligations de fournisseur en aval ; préservation du marquage | Art. 50, par. 2 ; art. 11 et 13 (futur) | Achats, Mistral | AIA-003, AIA-007, AIA-011 |
| NV-09 | Tous | Mesures de maîtrise de l'IA (formations, guides, registres) chez QuizMentor et chez les établissements | Document | Organisationnel | Art. 4 | RH, établissements | AIA-010 |
| NV-10 | Tous | Statut réel du projet : « fixture de test… Ne pas déployer » (`README.md:3-4`) ou produit commercialisé et mis en service (`README.md:8-10`) | Information | Art. 2, par. 8 (R&D avant mise sur le marché) | Champ d'application dans son ensemble | Direction | Tous |
| NV-11 | SYS-02 | Documentation technique, registre des risques, SGQ, tests d'évaluation du score (exactitude, biais par sous-groupes) hors dépôt | Document | Préparation du chapitre III | Art. 9, 10, 11, 15, 17 (futur) | Qualité, équipe données | AIA-004, AIA-007 |
| NV-12 | Tous | Confirmation sur le JO des dates issues du règlement 2026/1744 (CAL-003, CAL-010 délai, CAL-011, CAL-013) | Juridique | Sources secondaires uniquement | Statuts temporels « échéance à confirmer » | Juriste | AIA-002 à AIA-005, AIA-007, AIA-008, AIA-010, AIA-012 |
| NV-13 | SYS-02 | Qualification au titre de l'art. 5, par. 1, c) (notation sociale) et f) (inférence de motivation et de persévérance à partir de texte : hors art. 3, point 39 ?) | Juridique | Conditions cumulatives non établies | Pratique interdite (en vigueur) ou non | Juriste | AIA-006 |
| NV-14 | Tous | Statut PME de QuizMentor SAS | Information | Allègements (forme simplifiée de la documentation, plafonds de sanctions) | Effort de remédiation | Direction financière | AIA-004 |
| NV-15 | SYS-02 | Origine et qualité des notes (`grades`) et traitement des élèves sans échange avec l'assistant | Information | Gouvernance des données ; robustesse | Art. 10, 15 (futur) | Équipe technique | AIA-007 |

---

## 12. Plan de remédiation synthétique

Priorisation selon `findings-methodology.md`, section 6, ajustée au contexte lorsque c'est indiqué.

| Priorité | Constat(s) | Action | Base | Échéance réglementaire | Effort | Responsable suggéré | Preuve de clôture attendue |
|---|---|---|---|---|---|---|---|
| P1 | AIA-001 | Mention « assistant d'IA » à la première interaction, sur tous les canaux ; prompt système d'honnêteté | Obligation, art. 50, par. 1 et 5 | En vigueur (2026-08-02, CAL-009) | S | Produit / front-end | Capture, test automatisé |
| P1 | AIA-002 | Marquage de provenance dans les exports PDF (métadonnées, mention) et CSV (colonne ou fichier de provenance) ; tests de bout en bout | Obligation, art. 50, par. 2 | En vigueur (CAL-010) ; au plus tard 2026-12-02 (échéance à confirmer) | M | Back-end | Tests, fichiers d'exemple vérifiés |
| P1 (ajustée) | AIA-005 | Supprimer l'application automatique ; validation humaine obligatoire avec possibilité de modifier ou rejeter ; supprimer la « confiance » factice | Obligation future (art. 14, CAL-011) ; réduction d'un risque actuel pour des mineurs | 2027-12-02 (échéance à confirmer) ; risque actuel | S | Back-end, produit | Revue de code, test « aucune décision sans validation » |
| P1 (ajustée) | AIA-006 | Analyse juridique de la réutilisation des échanges (art. 5, par. 1, c) et f)) ; suspension de précaution du score d'engagement dans l'orientation | Obligation à vérifier (art. 5, en vigueur) | En vigueur (CAL-002) | S | Juriste, direction | Note juridique ; code sans flux engagement → orientation |
| P2 | AIA-003 | Format de provenance documenté, vérifiable et résistant à l'altération (code de bonnes pratiques) | Obligation, art. 50, par. 2 (technique : bonne pratique) | Idem AIA-002 | M | Back-end | Documentation, outil de vérification |
| P2 | AIA-009 | Retirer « conforme et certifié » ; corriger `docs/compliance.md` et `docs/human-oversight.md` | Bonne pratique (préparatoire art. 13, 47) | n.a. | S | Conformité | Documents corrigés et datés |
| P2 | AIA-007 | Épingler et journaliser la version du modèle ; protéger le prompt d'évaluation contre l'injection ; valider et borner la sortie ; assainir `student_id` | Obligation future (art. 15, annexe IV) ; bonne pratique immédiate | 2027-12-02 (échéance à confirmer) | S-M | Back-end | Tests unitaires et adverses |
| P2 | AIA-012 | Établir la date de première mise sur le marché et le statut des établissements ; faire confirmer l'échéance de l'art. 111, par. 2 | À vérifier | Conditionnel (CAL-013) | S | Juriste, commercial | Registre des versions ; note |
| P3 | AIA-004 | Décision d'architecture (retrait du score IA de l'orientation, ou feuille de route haut risque : art. 9 à 17, 43, 47 à 49) | Obligation future | 2027-12-02 (échéance à confirmer) ; CAL-013 | L | Direction, qualité | Fiche de classification ; plan ou preuve du retrait |
| P3 | AIA-008 | Journal d'audit des scores et des décisions ; rétention ≥ 6 mois appliquée | Obligation future (art. 12, 19, 26, par. 6) | 2027-12-02 (échéance à confirmer) | M | Back-end | Schéma et test de journalisation |
| P3 (ajustée) | AIA-010 | Documenter les mesures de maîtrise de l'IA (équipes, guide pour les conseils de classe) | Obligation, art. 4 | En vigueur (CAL-002 ; CAL-003 à confirmer) | S | RH, produit | Supports, registre |
| P4 | AIA-011 | Archiver la documentation et les conditions d'utilisation du fournisseur du modèle | Bonne pratique | n.a. | S | Achats | Documents archivés |

### Jalons

| Date | Évènement réglementaire | Actions à terminer avant |
|---|---|---|
| Immédiat (déjà en vigueur) | Art. 4, art. 5, art. 50, par. 1 et 5 ; art. 50, par. 2 (hypothèse d'une première mise sur le marché au 2026-10-15) | AIA-001, AIA-002, AIA-006 ; AIA-005 (risque actuel) |
| 2026-12-02 (échéance à confirmer) | Fin du délai de l'art. 50, par. 2 pour les systèmes antérieurs au 2026-08-02 (CAL-010) | AIA-002, AIA-003 au plus tard |
| 2027-12-02 (échéance à confirmer) | Exigences du haut risque, annexe III (CAL-011) | AIA-004, AIA-007, AIA-008 ; information des personnes (art. 26, par. 11) |
| 2030-08-02 (confiance faible) | Art. 111, par. 2 : systèmes antérieurs destinés à des autorités publiques (CAL-013) | Mise en conformité complète si SYS-02 est maintenu |

### Hypothèses
- Efforts estimés à partir du dépôt seul ; à recalibrer avec l'équipe.
- Les échéances issues du règlement 2026/1744 (confiance moyenne ou faible) sont à confirmer.
- Priorités AIA-005, AIA-006 et AIA-010 relevées par rapport au score indicatif : risque actuel pour
  des mineurs, obligation de l'art. 5 en vigueur, obligation de l'art. 4 en vigueur.

---

## 13. Limites de l'audit

- **Analyse statique** : le comportement réel, les données, les prompts dynamiques, la version de
  modèle servie et la configuration de production n'ont pas été observés. Le code n'a pas été exécuté.
- **Dépôt incomplet** : aucune interface, aucune route API, aucun appelant des fonctions principales.
  Les flux reposent en partie sur les docstrings, les commentaires et les chemins de fichiers partagés.
- **Contexte** : uniquement celui du projet, qui contient des affirmations contradictoires
  (« fixture de test » contre produit commercialisé) et une documentation volontairement erronée.
  Aucune personne n'a été interrogée.
- **Documents organisationnels** non disponibles : contrats, politiques, formations, registres,
  documentation technique, gestion des risques, notices.
- **Références juridiques** : textes officiels non relus en ligne lors de la dernière vérification
  (2026-10-27). Entrées à confirmer sur le Journal officiel : CAL-003, CAL-004, CAL-010 (délai
  transitoire), CAL-011, CAL-012, CAL-013, CAL-015, CAL-016.
- Lignes directrices (classification à haut risque : projet du 19.5.2026 ; art. 50 : 20.7.2026),
  normes harmonisées et actes d'exécution évolutifs.
- Les autres législations (protection des données, décisions automatisées, droit de l'éducation)
  sont signalées mais non analysées.
- Ce rapport est une aide à l'audit. Il ne remplace ni l'avis d'un juriste ni une évaluation de la
  conformité au sens de l'article 43, et n'affirme en aucun cas la conformité du projet.

---

## 14. Suivi (ré-audit)

Aucun audit précédent. Les identifiants AIA-001 à AIA-012 sont à conserver lors du prochain audit,
qui recalculera les statuts temporels à sa date (notamment après le 2026-12-02 pour CAL-010).

| Constat | Statut précédent | Statut actuel | Preuve |
|---|---|---|---|
| AIA-001 à AIA-012 | n.a. | Nouveau | Section 10 |
