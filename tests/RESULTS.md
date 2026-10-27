# Résultats des tests

Ce document présente d'abord l'état de la **version courante**, puis l'historique. Les nombres
indiqués ici sont vérifiés par `tests/run_tests.py` (`ConsistencyTests`).

## Version 1.2.1 : état actuel (2026-10-27)

### Synthèse

| Contrôle | Résultat | Détail |
|---|---|---|
| Tests automatiques | **61 tests, 61 réussis** | `python3 tests/run_tests.py`, Python 3.13, Git, Linux, 2026-10-27 |
| Relecture du texte officiel | **15 entrées sur 16 relues** | `python3 scripts/verify_official_extracts.py` : 22 extraits vérifiés, 0 introuvable ; CAL-016 bloquante (interprétation) |
| Rectificatifs | **Examinés** | R(01) seul en français (coquille de l'art. 10, par. 2) ; R(02) à R(04) : autres langues ; sans effet |
| Veille automatisée (service réel) | **Réussie** | Aucun acte nouveau depuis la revue des 27 actes remontés |
| Essai sur un dépôt applicatif réel | **Réalisé** | chatbot-ui (commit `81328b6`), 2 systèmes, 10 constats, constats principaux vérifiés dans le code : `tests/agent-runs/2026-10-27-v1.2.0/real-repo-chatbot-ui.md` |
| Scanner après correction (même dépôt) | **6 faux négatifs corrigés, faux positifs supprimés** | Persona « not an AI », transformers.js, pgvector, JWT, `Blob`, `tool_calls` détectés ; un seul secret signalé (masqué) |
| Intégration Claude Code (CLI 2.1.312) | **Réussi** | `tests/agent-runs/2026-10-27-v1.1.1/claude-code-cli-trigger.md` |
| Intégration OpenAI Codex | **Non testé** | Codex non installé, aucun identifiant OpenAI disponible |
| Validateur `skills-ref validate` | **Non exécuté** | Installation refusée par la politique de l'environnement |
| Évaluation par agent à l'aveugle (fixtures) | **Conforme** | Série 1.2.1 : `demo-ai-vulnerable` (modèle par défaut) et `demo-insufficient-info` (Sonnet), 0 faux négatif, 0 faux positif, 0 erreur de calendrier ; série 1.1.0 pour les trois autres fixtures |

### Enseignements de l'essai réel

- Le skill produit des qualifications prudentes sur un dépôt inconnu (pas de haut risque par
  mot-clé, rôles distingués, hypothèses temporelles par instance, aucune « échéance à confirmer »
  injustifiée).
- Les lacunes portaient sur les projets open source (désormais couverts), quelques ambiguïtés de
  méthode (corrigées) et la précision du scanner (corrigée, tests de non-régression).

### Évaluation à l'aveugle de la version 1.2.1

| Fixture | Modèle | Attendus couverts | Constats interdits | Calendrier | Rapport |
|---|---|---|---|---|---|
| demo-ai-vulnerable | Modèle par défaut de la session | E1 à E10 | Aucun (EduAssist non fournisseur GPAI, tuteur non à haut risque, chapitre III et art. 50, par. 2 non présentés comme applicables, secret masqué) | Exact ; aucune « échéance à confirmer » injustifiée | `tests/agent-runs/2026-10-27-v1.2.1/demo-ai-vulnerable.md` (brut) |
| demo-insufficient-info | Sonnet | 1 à 6 | Aucun | Exact (trois hypothèses de mise en service) | `tests/agent-runs/2026-10-27-v1.2.1/demo-insufficient-info-summary.md` (synthèse) |

Constat supplémentaire pertinent sur demo-ai-vulnerable : absence de garde-fous du générateur d'images
au regard des nouvelles interdictions de l'art. 5 (AIA-005, Non encore applicable, 2026-12-02).

### Ce qui reste non vérifié

- CAL-016 : date effective de l'obligation d'enregistrement de l'art. 49, par. 2 (interprétation).
- Intégration Codex et validateur officiel `skills-ref`.
- Variance entre exécutions (une exécution par couple fixture et modèle).

## Historique

### Version 1.2.0 (2026-10-27)

#### Synthèse

| Contrôle | Résultat | Détail |
|---|---|---|
| Tests automatiques | **58 tests, 58 réussis** | `python3 tests/run_tests.py`, Python 3.13, Git, Linux, 2026-10-27 |
| Relecture du texte officiel | **15 entrées sur 16 relues** | `python3 scripts/verify_official_extracts.py` : 2 documents officiels, empreintes identiques, **22 extraits vérifiés, 0 introuvable** ; CAL-016 reste bloquante (interprétation) |
| Veille automatisée (service réel) | **Réussie** | `python3 scripts/check_legal_updates.py` : requête SPARQL exécutée, 27 actes remontés et revus ; second passage : aucun acte nouveau ; rectificatifs R(01) à R(04) examinés, sans effet sur le texte français |
| Intégration Claude Code (CLI 2.1.312) | **Réussi** | `tests/agent-runs/2026-10-27-v1.1.1/claude-code-cli-trigger.md` |
| Intégration OpenAI Codex | **Non testé** | Codex non installé, aucun identifiant OpenAI disponible |
| Validateur `skills-ref validate` | **Non exécuté** | Installation refusée par la politique de l'environnement ; frontmatter validé par PyYAML et par les tests |
| Évaluation par agent à l'aveugle | **Conforme** (dernière série en version 1.1.0, quatre exécutions, trois modèles) | La version 1.2.0 ne modifie pas la méthodologie ; elle lève des réserves calendaires et précise des règles (art. 5, art. 6, art. 111) |
| Essai sur un dépôt applicatif réel | Réalisé (voir version 1.2.1) | |

#### Ce que la relecture officielle a changé

| Point | Avant (sources secondaires) | Texte officiel |
|---|---|---|
| Autorités publiques (art. 111, par. 2) | 2 août 2030 ou 28 janvier 2028 | **2 août 2030** |
| Délai art. 50, par. 2 | 2 décembre 2026, localisation inconnue | 2 décembre 2026, **art. 111, par. 4**, contenus « audio, image, vidéo ou texte » |
| Nouvelles interdictions (art. 5) | Contenu rapporté | Points b bis) et b ter), par. 1 bis (garde-fous raisonnables et adéquats) et 1 ter |
| Composant de sécurité | « Définition modifiée » | Art. 3, point 14 remplacé ; art. 6, par. 1 bis à 1 quater ajoutés |
| Art. 10, par. 5 | « Critère maintenu » | Supprimé, remplacé par l'art. 4 bis |
| Machines | « Déplacées selon une source » | Annexe I, section A point 1 supprimé, section B point 21 ajouté |

#### Ce qui reste non vérifié

- CAL-016 : date effective de l'obligation d'enregistrement de l'art. 49, par. 2 (interprétation).
- Intégration Codex et validateur officiel `skills-ref`.
- Variance des évaluations par agent.

### Version 1.1.1 (2026-10-27)

#### Synthèse

| Contrôle | Résultat | Détail |
|---|---|---|
| Tests automatiques | **58 tests, 58 réussis** | `python3 tests/run_tests.py`, Python 3.13, Git, Linux, 2026-10-27 |
| Intégration Claude Code (CLI 2.1.312) | **Réussi** | Skill découvert, déclenché sans être nommé, lecture seule respectée : `tests/agent-runs/2026-10-27-v1.1.1/claude-code-cli-trigger.md` |
| Intégration OpenAI Codex | **Non testé** | Codex n'est pas installé dans l'environnement et aucun identifiant OpenAI n'est disponible |
| Validateur `skills-ref validate` | **Non exécuté** | Installation refusée par la politique de l'environnement ; frontmatter validé par PyYAML et par les tests |
| Évaluation par agent à l'aveugle | **Conforme** (dernière série en version 1.1.0, quatre exécutions, trois modèles) | Voir l'historique 1.1.0 ; la version 1.1.1 ne modifie pas la méthodologie d'audit, seulement le statut de vérification du calendrier |
| Essai sur un dépôt applicatif réel | **En cours** | Résultats ajoutés à la fin de l'exécution |
| Vérification juridique officielle | **Partielle** | 6 entrées confirmées par extraits officiels EUR-Lex ; 2 entrées bloquantes (CAL-013, CAL-016) ; aucune relecture intégrale |

#### Tests automatiques ajoutés depuis la version 1.1.0

| Groupe | Contrôles ajoutés |
|---|---|
| `ConsistencyTests` | Version de `SKILL.md` = première entrée du CHANGELOG ; première section de ce fichier = version et nombre de tests courants |
| `CalendarDataTests` | Extraits officiels cités et sourcés pour tout statut `officielle_extraits` ; règle bloquante limitée aux entrées non confirmées |
| `TimelineScenarioTests` | Échéances confirmées par extrait non bloquantes ; CAL-013 et CAL-016 bloquantes |
| `LegalWatchTests` | Veille automatisée : détection des seuls actes inconnus (réponse SPARQL fictive), codes de sortie, absence d'écriture dans `data/`, fiche de vérification couvrant toutes les entrées bloquantes |

#### Vérification juridique

| Entrée | Statut | Preuve |
|---|---|---|
| CAL-003, CAL-004, CAL-010, CAL-015 | `officielle_extraits` (confiance élevée) | Extrait textuel du JO ou de la version consolidée, cité dans `data/ai-act-calendar.json` |
| CAL-011, CAL-012 | `officielle_extraits` (confiance moyenne) | Extrait d'un considérant ; revue externe concordante ; disposition opérationnelle à relire |
| CAL-013, CAL-016 | **Bloquantes** | Pas d'extrait officiel textuel pour l'échéance des autorités publiques ni pour l'art. 49, par. 2 |
| Autres entrées | `texte_initial_non_relu` | Texte initial de 2024 |

Ces résultats ne valident pas le contenu juridique du skill : ils attestent la cohérence interne et
la traçabilité des sources. Procédure de levée des réserves : `references/official-verification-worksheet.md`.

#### Ce qui reste non vérifié

- Relecture intégrale du règlement 2026/1744 et de la version consolidée (accès direct refusé).
- Intégration Codex et validateur officiel `skills-ref`.
- Requête de veille SPARQL contre le service réel (seule l'analyse d'une réponse fictive est testée).
- Variance des évaluations par agent (une exécution par couple fixture et modèle).

### Version 1.1.0 (2026-10-27) : revue externe et évaluation de contrôle

#### Tests automatiques

| Date | Commande | Environnement | Résultat |
|---|---|---|---|
| 2026-10-27 | `python3 tests/run_tests.py` | Python 3.13, Git, Linux | **50 tests, 50 réussis** |

Nouveaux contrôles : base juridique complète par entrée, règle bloquante des échéances non relues,
mention « échéance à confirmer », chemins de sortie, fixture adversariale, audit différentiel
(dépôt Git temporaire, lecture seule vérifiée). Rappel : ces tests ne valident pas le contenu juridique.

#### Évaluation par agent à l'aveugle, plusieurs modèles

Même protocole (fixtures sans `EXPECTED.md`, skill sans `examples/`). Rapports bruts dans
`tests/agent-runs/2026-10-27-v1.1/` ; seule normalisation appliquée : remplacement des tirets
cadratins de cellules vides par « n.a. » dans un rapport.

| Fixture | Modèle | Faux négatifs | Faux positifs | Erreurs de calendrier | Écarts de qualification | Verdict |
|---|---|---|---|---|---|---|
| demo-adversarial | Modèle par défaut de la session | 0 | 0 | 0 | Annexe III, point 3, a) retenu (oracle : b) ou c)) : lecture admise | Conforme |
| demo-adversarial | Sonnet | 0 | 0 | 0 | Art. 5, par. 1, c) en Risque potentiel Critique : hypothèse non prévue, défendable, admise dans l'oracle tant qu'elle reste au stade du risque | Conforme, gravité élevée |
| demo-ai-secure | Sonnet | 0 | 0 | 0 | Aucun ; textes du tuteur : Non encore applicable, échéance à confirmer (correction 1.1.0 vérifiée) | Conforme |
| demo-no-ai | Haiku | 0 | 0 | 0 | Aucun ; plus de série de constats « Non applicable » (correction 1.0.x vérifiée) | Conforme |

Points vérifiés sur la fixture adversariale (deux modèles) : dates erronées de la documentation non
reprises ; aucune exemption des textes conversationnels ; argument « un humain décide » rejeté ;
contradiction entre la procédure documentée et l'application automatique détectée ; champ
`ai_generated` jugé insuffisant et falsifiable ; perte du marquage dans les exports PDF et CSV ;
aucun délai transitoire pour une mise en service au 2026-10-15 ; « certifié » non repris ; système
hybride et profilage identifiés ; mention « échéance à confirmer » appliquée aux dates issues de 2026/1744.

Constats supplémentaires pertinents relevés par les agents : note `None` publiable et image sauvegardée
avant la signature C2PA (demo-ai-secure) ; injection de prompt via les messages dans le calcul du
score d'engagement (demo-adversarial).

#### Ce qui reste non vérifié

- **Contenu juridique** : aucune disposition relue sur EUR-Lex ou l'AI Act Explorer (accès refusé par
  la politique réseau de l'environnement). Les entrées issues de 2026/1744 restent bloquantes.
- Une exécution par couple (fixture, modèle) : pas de mesure de variance.
- demo-ai-vulnerable et demo-insufficient-info n'ont pas été réévalués avec la version 1.1.0.
- `skills-ref validate` et installation réelle dans Claude Code et Codex : non exécutés.

### Version 1.0.0 (2026-10-27)

#### 1. Tests automatiques

| Date | Commande | Environnement | Résultat |
|---|---|---|---|
| 2026-10-27 | `python3 tests/run_tests.py` | Python 3.13, Linux | **38 tests, 38 réussis** |

Vérifications complémentaires exécutées le 2026-10-27 :

- Frontmatter de `SKILL.md` analysé avec PyYAML (`yaml.safe_load`) : valide ; description de 976 caractères (limite 1024).
- Exécution manuelle des deux scripts sur les quatre fixtures : sorties conformes aux attentes, valeur de la fausse clé absente de la sortie.

Non exécuté :

- Validateur officiel `skills-ref validate` : son installation (`pip install skills-ref`) a été refusée par la politique de l'environnement de rédaction. Il reste à lancer.
- Installation et déclenchement effectifs dans Claude Code et dans Codex (CLI) : non testés dans cet environnement. La compatibilité repose sur le respect du format Agent Skills.

#### 2. Évaluation par agent à l'aveugle (2026-10-27)

Protocole : `tests/README.md`, section 2. Les fixtures ont été copiées **sans** `EXPECTED.md`, et le skill **sans** `examples/`. Un agent généraliste (même famille de modèle que l'auteur du skill) a suivi `SKILL.md`, avec pour date d'audit le 2026-10-27, en lecture seule et sans réseau. Les rapports bruts sont dans `tests/agent-runs/2026-10-27/`.

Il s'agit d'une seule exécution par fixture, ce qui n'est pas une validation statistique. Le biais lié au fait que l'auteur et l'évaluateur appartiennent à la même famille de modèle n'est pas neutralisé.

##### demo-ai-vulnerable : conforme aux attentes

| Attendu (EXPECTED.md) | Obtenu | Verdict |
|---|---|---|
| E1 émotions en examen : Risque potentiel, Critique, art. 5, par. 1, f), en vigueur | AIA-001 : Risque potentiel, Critique, en vigueur depuis le 2025-02-02 | OK |
| E2 tuteur sans information : Constat avéré, Élevée, art. 50, par. 1, en vigueur | AIA-003 : identique | OK |
| E3 images sans marquage : Non encore applicable au 2026-12-02 | AIA-007 : identique | OK (calendrier exact) |
| E4 note publiée sans relecture : Risque potentiel, Élevée, haut risque non encore applicable | AIA-004 : identique, régime transitoire conditionnel | OK |
| E5 absence de journalisation | AIA-009 : Non encore applicable, Moyenne | OK (nature acceptable) |
| E6 clé d'API en clair, valeur masquée | AIA-005 ; valeur absente du rapport | OK |
| E7 notation non reproductible | AIA-006 | OK |
| E8 documentation et art. 4 non observables | AIA-012, AIA-008 | OK |
| E9 établissements publics, art. 111, par. 2 | AIA-016 | OK |
| Interdits : EduAssist fournisseur GPAI, plateforme entière à haut risque, tuteur à haut risque, chapitre III applicable, art. 50, par. 2 applicable, art. 5, par. 1, a) retenu sans analyse, secret en clair, « conforme » | Aucun | OK |

Constats supplémentaires pertinents : annulation automatique d'examen (AIA-002), hypertrucages possibles (AIA-010), garde-fous face aux nouvelles interdictions de l'article 5 (AIA-011, Non encore applicable), marquage des textes du tuteur (AIA-013).

##### demo-ai-secure : conforme aux attentes, un écart léger

| Attendu | Obtenu | Verdict |
|---|---|---|
| SYS-03 sans délai de grâce (mise sur le marché le 2026-09-15) | Art. 50, par. 2 en vigueur (CAL-010) | OK (calendrier exact) |
| `exam_events.py` n'est pas un système d'IA | Écarté avec motif | OK |
| S1, S3, S5, S6, S7, S9 | AIA-013, AIA-014, AIA-006, AIA-003, AIA-012, AIA-010 | OK |
| S2 marquage : mesure présente, robustesse non démontrée | AIA-001 : Risque potentiel ; l'agent relève en plus que les métadonnées sont des clés PNG non standard | OK, et meilleur que l'oracle |
| S8 textes : À vérifier, Faible | AIA-002 : Non encore applicable, Moyenne | **Écart léger** |
| Aucun Critique ni Élevé, mais pas zéro constat | 0 Critique, 0 Élevé, 16 constats | OK |
| Interdits : secret, « conforme », chapitre III applicable, métadonnées jugées suffisantes | Aucun | OK |

##### demo-insufficient-info : conforme aux attentes

Système d'IA identifié avec une confiance élevée. Classification « indéterminée » avec une confiance faible, hypothèses annexe III, point 4, a) et point 3, a) posées sans conclusion ferme, profilage relevé. Variable `age` signalée en risque potentiel. Date de mise en service inconnue, donc statut conditionnel. Registre de 12 questions. Aucune obligation du haut risque présentée comme applicable, aucun constat art. 50 ni GPAI au-delà d'exclusions motivées.

##### demo-no-ai : conforme sur le fond, un écart mineur

Aucun système d'IA identifié. Les faux positifs `model`, `predict`, `score`, « intelligence » et « prêt » sont correctement écartés. Un constat « À vérifier » porte sur les composants hors dépôt.

**Écart mineur** : plusieurs constats « Non applicable » portent sur les articles 4, 5, 50 et GPAI, alors que l'oracle demandait l'absence de constats sur ces articles. Il n'y a pas d'erreur de qualification, seulement du bruit.

#### 3. Corrections apportées après l'évaluation

| Écart | Correction | Re-vérifié par agent ? |
|---|---|---|
| Multiplication des constats « Non applicable » (demo-no-ai) | `SKILL.md`, phase 2 et section 5 : projet sans IA traité par un rapport court, exclusions regroupées, usage restreint de la nature « Non applicable ». Oracle précisé (bruit toléré, erreur de qualification interdite). | Non |
| Marquage des textes conversationnels qualifié avec trop d'assurance (demo-ai-secure, S8) | `SKILL.md`, section 5 : une portée incertaine (`[AV]`) donne la nature « À vérifier ». `references/transparency.md`, section 4 : règle explicite. Oracle : tolérance documentée. | Non |
| Métadonnées PNG non standard non anticipées par l'oracle | `references/transparency.md`, section 4 : qualification des métadonnées « maison ». Oracle S2 enrichi, constats supplémentaires admis listés. | Non |

Mise à jour : les deux premières corrections ont été revérifiées par agent en version 1.1.0 (section 4.2 : demo-no-ai avec Haiku, demo-ai-secure avec Sonnet). La règle sur les textes conversationnels a entre-temps été remplacée (section 4).
