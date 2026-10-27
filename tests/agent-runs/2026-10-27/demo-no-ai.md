# Rapport d'audit AI Act : BiblioGest (demo-no-ai)

> **Avertissement.** Ce rapport est une aide à l'audit. Il repose sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689.

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | Dossier `demo-no-ai/` entier : `README.md`, `requirements.txt`, `app/__init__.py` (vide), `app/loans.py`, `app/models.py`, `app/watch.py`. Le dossier n'est pas un dépôt git : aucune branche ni aucun commit identifiable. Aucun dossier exclu. |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (`meta.last_verified` de `data/ai-act-calendar.json`). Écart avec la date d'audit inférieur à 6 mois : pas de limite majeure à ce titre. |
| Contexte fourni par le demandeur | **Aucun.** Le seul contexte est le dépôt. Le README présente une application de gestion de prêts de bibliothèque. |
| Méthode | Skill `ia-compliance` v1.0.0. Audit en lecture seule, sans exécuter le code audité. Outils : `scan_ai_signals.py` et `obligation_timeline.py --audit-date 2026-10-27`. |
| Audit précédent | Aucun |

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : **0**. Aucun composant du dépôt ne répond à la définition de système d'IA de l'art. 3, point 1.
  - Le calcul de la date de retour (« predict ») est une addition de jours.
  - Les points de fidélité (« score ») suivent une formule fixe définie par l'humain.
  - La veille « intelligence économique » est une liste de liens saisie à la main.
  - Les « models » sont des tables de base de données (ORM).
- **Classification** : « Pas un système d'IA (motivé) » pour chaque composant examiné (confiance élevée).
- **Points les plus sensibles** :
  - Le scanner a relevé un faux positif sur le contexte « services essentiels » : il s'agit de prêts de livres, pas de crédit (AIA-002).
  - Des composants hors dépôt n'ont pas pu être examinés : interface, services tiers, éventuels outils d'IA utilisés par le personnel (AIA-005).
- **Obligations en vigueur concernées** : aucune au titre de ce dépôt. Les art. 4, 5 et 50 et le chapitre V supposent un système ou un modèle d'IA (AIA-004).
- **Échéances à venir** : aucune pour ce dépôt. À réexaminer si une fonctionnalité d'IA est ajoutée (AIA-006).
- **Principales incertitudes** :
  - Existence de composants ou services d'IA hors dépôt.
  - Implémentation, non observée dans le code, du « classement des lecteurs les plus assidus » annoncé par le README.
- **Synthèse des constats** (6) :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | 0 | 0 | 0 | 0 | 0 |
| Risque potentiel | 0 | 0 | 0 | 0 | 0 |
| À vérifier juridiquement ou organisationnellement | 0 | 0 | 0 | 0 | 1 |
| Bonne pratique recommandée | 0 | 0 | 0 | 0 | 1 |
| Non encore applicable | 0 | 0 | 0 | 0 | 0 |
| Non applicable | 0 | 0 | 0 | 0 | 4 |

Ce constat d'absence d'IA vaut **pour le seul périmètre analysé**. Il ne constitue pas une attestation que l'organisation n'est soumise à aucune obligation de l'AI Act.

## 2. Périmètre et méthode

Arborescence analysée (6 fichiers) :

```
demo-no-ai/
├── README.md          présentation : catalogue, prêts, date de retour, fidélité, veille
├── requirements.txt   flask==3.0.3, sqlalchemy==2.0.35
└── app/
    ├── __init__.py    (vide)
    ├── loans.py       predict_due_date, loyalty_score
    ├── models.py      modèles ORM Book, Loan
    └── watch.py       liste de liens LINKS, add_link
```

Outils et vérifications :

- **`scan_ai_signals.py`** conclut : « Signaux d'IA détectés : non ». Il relève seulement 2 occurrences `sensitive_context` / `essential-services` (`app/loans.py:1`, `app/models.py:15`), dues au mot « prêt » / `Loan` (voir AIA-002).
- **Recherche manuelle complémentaire** (lecture intégrale des 6 fichiers) des pièges de faux positifs et de faux négatifs de `ai-detection-signals.md` :
  - aucun appel HTTP (`requests`, `httpx`, `v1/chat/completions`, `/predict`) ;
  - aucune bibliothèque d'IA ou d'apprentissage automatique ;
  - aucun fichier de modèle (`.pkl`, `.onnx`, `.joblib`) ;
  - aucun drapeau de fonctionnalité, aucune configuration et aucun code d'infrastructure.
- **Secrets** : aucun secret détecté.
- **`obligation_timeline.py --audit-date 2026-10-27`** a été exécuté pour référence. Les statuts temporels sont sans objet, faute de système d'IA.

Éléments non analysés :

- l'interface utilisateur (gabarits, front-end) et les routes Flask : aucune n'est présente bien que Flask soit déclaré ;
- la base de données et l'environnement de production ;
- les services tiers éventuellement connectés ;
- le code de tri des lecteurs (non présent).

## 3. Systèmes d'IA identifiés

| ID | Système | Finalité | Rôle(s) de l'organisation | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|
| Aucun | | | | | | |

**Composants examinés et écartés** :

| Composant | Fichier | Motif |
|---|---|---|
| `predict_due_date` | `app/loans.py:7-9` | Ce n'est **pas un système d'IA** : `start + timedelta(days=LOAN_DAYS * (1 + renewals))`, avec `LOAN_DAYS = 21` (`app/loans.py:4`). Calcul arithmétique déterministe sans inférence. « predict » est un piège lexical, et la docstring le dit elle-même : « « Prédit » la date de retour par simple addition de jours ». |
| `loyalty_score` | `app/loans.py:12-14` | Ce n'est **pas un système d'IA** : `max(0, loans_count * 10 - late_returns * 5)`. Règle fixe définie par l'humain (« règle fixe affichée aux lecteurs »), sans apprentissage ni inférence. |
| Classement des lecteurs les plus assidus | `README.md:7-8` (annoncé) | Aucun code de classement n'est présent. Au vu du dépôt, un simple tri sur `loyalty_score` est vraisemblable. À vérifier (NV-02). |
| Veille « intelligence économique » | `app/watch.py:1-6` | Ce n'est **pas un système d'IA** : liste `LINKS` alimentée par `add_link(url)`, avec des liens « saisis à la main par les bibliothécaires ». « Intelligence » désigne ici la veille. |
| `Book`, `Loan`, `model_number` | `app/models.py:1-19` | Ce n'est **pas un système d'IA** : modèles de données ORM SQLAlchemy (« « Model » désigne ici une table, pas un modèle d'IA »). `model_number` est une « référence d'édition ». |
| Dépendances `flask`, `sqlalchemy` | `requirements.txt:1-2` | Framework web et ORM, sans composant d'IA. |

## 4. Rôles réglementaires

Aucun système d'IA ni aucun modèle GPAI n'a été identifié. Au titre de ce dépôt, l'organisation n'est donc ni fournisseur, ni déployeur, ni importateur, ni distributeur d'un système d'IA (art. 3, points 3 à 7) `[TI]`, ni fournisseur de modèle GPAI. Elle pourrait néanmoins avoir de tels rôles pour d'autres outils hors périmètre (NV-01, NV-03).

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 3, point 1 (définition du système d'IA) | Tous les composants | **Retenue** : aucun système d'IA | Règles et calculs définis uniquement par des humains, sans inférence. Les lignes directrices de la Commission de février 2025 confirment que de tels traitements peuvent ne pas relever de la définition. |
| Art. 2 (exclusions du champ) | n.a. | Non examinée au fond | Sans objet en l'absence de système d'IA |
| Annexe III, point 5, b) (solvabilité, note de crédit) | `app/loans.py`, `app/models.py` | Écartée | Il s'agit de prêts de documents de bibliothèque et non de crédit (AIA-002) |

## 6. Classification

| Étape | Question | Réponse | Preuves | Référence |
|---|---|---|---|---|
| 0 | Système d'IA au sens de l'art. 3, point 1 ? | **Non**, pour chaque composant | Section 3 | Art. 3, point 1 `[TI]` |
| 1 à 8 | Art. 2, 5, 6, 50, GPAI, art. 4 | Sans objet (arrêt à l'étape 0) | Voir AIA-003 et AIA-004 pour les points examinés à titre de contrôle | `risk-classification.md`, section 2 |

**Conclusion** : « Pas un système d'IA (motivé) » pour l'ensemble des composants du dépôt. Confiance élevée sur les faits (code intégralement lu, 6 fichiers) et sur la qualification. Seuls les composants hors dépôt (NV-01) pourraient remettre ce résultat en cause.

## 7. Obligations et calendrier

Statuts calculés par `obligation_timeline.py --audit-date 2026-10-27`. Ils sont donnés pour mémoire et ne s'appliquent pas à ce dépôt.

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|
| Maîtrise de l'IA (art. 4) | Aucun | n.a. | En vigueur ; non applicable au titre du dépôt | 2025-02-02 / 2026-07-27 | CAL-002, CAL-003 | Élevée / Moyenne |
| Pratiques interdites (art. 5) | Aucun | n.a. | En vigueur ; non applicable (aucun système d'IA) | 2025-02-02 | CAL-002 | Élevée |
| Art. 50 | Aucun | n.a. | En vigueur ; non applicable | 2026-08-02 | CAL-009, CAL-010 | Élevée / Moyenne |
| Chapitre V (GPAI) | Aucun | n.a. | En vigueur ; non applicable | 2025-08-02 | CAL-005 | Élevée |
| Haut risque, annexe III et annexe I | Aucun | n.a. | Non encore applicable ; sans objet | 2027-12-02 / 2028-08-02 | CAL-011, CAL-012 | Moyenne |

## 8. Constats

Les constats sont ordonnés par gravité, puis par identifiant.

### AIA-001 : Aucun système d'IA identifié : les composants « predict », « score » et « model » sont des règles déterministes ou des tables ORM
- **Système d'IA concerné** : Aucun (composants `predict_due_date`, `loyalty_score`, `watch`, ORM)
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** :
  - Fait observé : la date de retour est calculée par `start + timedelta(days=LOAN_DAYS * (1 + renewals))`.
  - Les points de fidélité sont calculés par `max(0, loans_count * 10 - late_returns * 5)`.
  - La veille est une liste de liens ajoutés manuellement.
  - `Book` et `Loan` sont des tables SQLAlchemy.
  - Les dépendances se limitent à `flask` et `sqlalchemy`.
  - Le scanner ne détecte aucun signal d'IA.
- **Fichier(s) et lignes** : `app/loans.py:4-14`, `app/watch.py:1-6`, `app/models.py:1-19`, `requirements.txt:1-2`
- **Rôle réglementaire concerné** : Aucun au titre du dépôt
- **Classification du système** : Pas un système d'IA (motivé)
- **Référence juridique** :
  - Art. 3, point 1 `[TI]` ; lignes directrices de la Commission sur la définition de système d'IA (février 2025, non contraignantes).
  - Source : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689).
- **Date d'application** : Sans objet (CAL-001 : règlement en vigueur depuis le 2024-08-01).
- **Conditions et exceptions** :
  - La définition exige que le système **déduise**, à partir des entrées, la manière de générer des sorties.
  - Des règles définies uniquement par des humains n'en relèvent pas.
  - Aucune exception n'a eu à être invoquée.
- **Explication** :
  - Les mots « predict », « score », « model » et « intelligence » apparaissent dans le code, mais ils désignent des calculs simples, une table de base de données et une activité de veille.
  - Aucune partie du programme n'apprend à partir de données ni ne produit de prédiction par inférence.
  - Le règlement sur l'IA ne trouve donc pas à s'appliquer à ce code.
- **Recommandation** : Aucune action requise.
- **Méthode de vérification** : relecture des fichiers cités ; nouvelle exécution de `scan_ai_signals.py` lors de chaque audit.

### AIA-002 : Signal « services essentiels » (prêts) : faux positif, il s'agit de prêts de documents et non de crédit
- **Système d'IA concerné** : Aucun
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** : Le scanner signale `essential-services` sur « Règles de prêt » (`app/loans.py:1`) et sur `class Loan(Base)` (`app/models.py:15`). Le contexte (README, `Book`, `reader_id`, durée de prêt de 21 jours, renouvellements) établit qu'il s'agit de prêts de bibliothèque.
- **Fichier(s) et lignes** : `app/loans.py:1-9`, `app/models.py:8-19`, `README.md:3-9`
- **Rôle réglementaire concerné** : Aucun
- **Classification du système** : Pas un système d'IA (motivé)
- **Référence juridique** :
  - Annexe III, point 5, b) (évaluation de la solvabilité, note de crédit) `[TI]`, examinée et écartée.
  - Source : [AI Act Explorer, art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6).
- **Date d'application** : Sans objet (CAL-011 : 2027-12-02, non encore applicable, pour mémoire).
- **Conditions et exceptions** : Le point 5, b) vise l'évaluation de la solvabilité de personnes physiques par un système d'IA. Ces deux conditions font défaut : il n'y a ni crédit, ni système d'IA.
- **Explication** : Le mot « prêt » a déclenché un signal de contexte sensible, mais il s'agit d'emprunter des livres. Ce n'est pas un crédit financier.
- **Recommandation** : Aucune.
- **Méthode de vérification** : Sans objet.

### AIA-003 : Classement des lecteurs par points de fidélité : règle fixe, sans inférence ; notation sociale (art. 5) sans objet
- **Système d'IA concerné** : Aucun (composant `loyalty_score`)
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée (code observé) / Moyenne (classement annoncé par le README mais non observé)
- **Preuve observée** :
  - Fait observé : `loyalty_score` applique une formule fixe et publique (« règle fixe affichée aux lecteurs »). Elle tient compte du nombre de prêts et des retours en retard.
  - Le README annonce un « classement des lecteurs les plus assidus ». Aucun code de tri n'est présent.
- **Fichier(s) et lignes** : `app/loans.py:12-14`, `README.md:7-8`
- **Rôle réglementaire concerné** : Aucun
- **Classification du système** : Pas un système d'IA (motivé)
- **Référence juridique** :
  - Art. 5, par. 1, c) (notation sociale) `[TI]` ; art. 3, point 1 `[TI]`.
  - Source : [AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5).
- **Date d'application** : Art. 5 en vigueur depuis le 2025-02-02 (CAL-002), sans objet ici.
- **Conditions et exceptions** :
  - L'art. 5 vise des **systèmes d'IA**. Une règle de calcul définie par l'humain n'en est pas un.
  - De plus, aucun traitement préjudiciable dans un contexte sans lien n'est observé : les points restent internes à la bibliothèque.
- **Explication** : Le classement des lecteurs repose sur un barème simple, connu des lecteurs. Ce n'est pas une notation par IA, et l'interdiction de la notation sociale ne s'applique pas.
- **Recommandation** : Aucune action au titre de l'AI Act. Si le classement venait à être produit par un modèle appris, ou si les points servaient à restreindre l'accès au service, réexaminer l'art. 5, par. 1, c) et l'art. 3, point 1.
- **Méthode de vérification** : confirmation de l'implémentation du tri (NV-02).

### AIA-004 : Obligations des art. 4, 5 et 50 et du chapitre V (GPAI) non applicables au titre de ce dépôt
- **Système d'IA concerné** : Aucun
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée (au titre du dépôt) / Faible (au niveau de l'organisation)
- **Preuve observée** : Aucun système d'IA ni aucun modèle d'IA dans le dépôt (AIA-001). Aucune interaction conversationnelle, aucune génération de contenu, aucune biométrie, aucun entraînement de modèle.
- **Fichier(s) et lignes** : ensemble du dépôt
- **Rôle réglementaire concerné** : Aucun au titre du dépôt
- **Classification du système** : Pas un système d'IA (motivé)
- **Référence juridique** :
  - Art. 4 `[TI]` / `[O26]` ; art. 5 `[TI]` ; art. 50 `[TI]` ; art. 53 `[TI]`.
  - Source : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689).
- **Date d'application** : CAL-002, CAL-003, CAL-005 et CAL-009 en vigueur ; CAL-010 conditionnel ; tous sans objet pour ce dépôt.
- **Conditions et exceptions** :
  - Ces obligations visent les fournisseurs et déployeurs de systèmes d'IA ou les fournisseurs de modèles GPAI.
  - L'art. 4 pourrait néanmoins s'appliquer à l'organisation si elle déploie d'autres systèmes d'IA hors de ce dépôt (NV-03).
- **Explication** :
  - Sans IA dans l'application, ni la maîtrise de l'IA, ni les interdictions, ni les obligations de transparence ne s'appliquent à ce logiciel.
  - Cela ne dit rien des autres outils que la bibliothèque pourrait utiliser.
- **Recommandation** : Aucune au titre du dépôt.
- **Méthode de vérification** : Sans objet.

### AIA-005 : Composants hors dépôt et usages d'IA par l'organisation non observables
- **Système d'IA concerné** : Aucun identifié
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Information
- **Niveau de confiance** : Moyenne
- **Preuve observée** :
  - Flask est déclaré (`requirements.txt:1`) mais aucune route, aucun gabarit ni aucune interface n'est présent.
  - Le classement annoncé (`README.md:7-8`) n'est pas implémenté dans le dépôt.
  - Aucune configuration ni aucune infrastructure n'est fournie.
- **Fichier(s) et lignes** : `requirements.txt:1`, `README.md:7-9`
- **Rôle réglementaire concerné** : À déterminer (déployeur éventuel d'outils tiers)
- **Classification du système** : Pas un système d'IA (motivé), pour le périmètre analysé
- **Référence juridique** : Art. 3, point 1 et art. 4 `[TI]` / `[O26]`
- **Date d'application** : Art. 4 en vigueur (CAL-002, CAL-003) si un système d'IA est utilisé ailleurs ; conditionnel.
- **Conditions et exceptions** : Faux négatifs possibles selon `ai-detection-signals.md`, section 4 : IA fournie par un service SaaS, un widget ou un connecteur ; prompts stockés en base ; modules activés par configuration.
- **Explication** :
  - Le dépôt semble incomplet (pas d'interface).
  - Une fonctionnalité d'IA pourrait exister ailleurs : chatbot sur le site, recommandations de lecture d'un prestataire, résumé automatique de la veille. L'audit ne peut pas l'exclure.
- **Recommandation** : Confirmer l'absence d'IA dans les composants non fournis et dans les services tiers connectés. Recenser les outils d'IA éventuellement utilisés par le personnel. Vérification organisationnelle.
- **Méthode de vérification** : inventaire applicatif signé ; dépôt complet (interface, configuration) soumis à un nouvel audit.

### AIA-006 : Documenter la qualification « pas d'IA » et prévoir une réévaluation en cas d'évolution fonctionnelle
- **Système d'IA concerné** : Aucun
- **Nature du constat** : Bonne pratique recommandée
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** :
  - Les docstrings signalent déjà l'absence d'inférence (`app/loans.py:1`, `app/loans.py:8`, `app/models.py:1`). C'est une mesure positive.
  - Aucune procédure de réévaluation n'est observée.
- **Fichier(s) et lignes** : `app/loans.py:1`, `app/loans.py:8`, `app/models.py:1`
- **Rôle réglementaire concerné** : Aucun
- **Classification du système** : Pas un système d'IA (motivé)
- **Référence juridique** : Aucune (bonne pratique)
- **Date d'application** : n.a.
- **Conditions et exceptions** : Néant.
- **Explication** : L'ajout futur d'une fonctionnalité d'IA ferait entrer le logiciel dans le champ du règlement. Exemples : prédiction des retards par apprentissage, recommandations de lecture, synthèse automatique de la veille, assistant conversationnel. Les art. 4, 5 et 50 seraient alors immédiatement applicables.
- **Recommandation** :
  - Conserver une courte note de qualification (composants, motif « pas d'inférence »).
  - Prévoir un nouvel audit de type `ia-compliance` avant toute mise en service d'une fonctionnalité d'IA.
  - Bonne pratique.
- **Méthode de vérification** : note de qualification datée ; point de contrôle « IA » dans la procédure de revue des évolutions.

## 9. Éléments non vérifiables

**Registre des éléments non vérifiables** (date d'audit : 2026-10-27). Comme le demandeur n'a pas pu être interrogé, toutes les questions sont consignées ici.

| ID | Système | Élément manquant | Type | Pourquoi c'est nécessaire | Impact sur la classification ou les obligations | Interlocuteur suggéré | Constat(s) liés |
|---|---|---|---|---|---|---|---|
| NV-01 | n.a. | Composants non fournis : interface Flask, gabarits, configuration, services tiers ou SaaS connectés (catalogue, portail, chatbot) | Document / information | Écarter les faux négatifs | Pourrait révéler un système d'IA soumis aux art. 4, 5 et 50 | Direction technique | AIA-005 |
| NV-02 | n.a. | Implémentation du « classement des lecteurs les plus assidus » et usage des points de fidélité (restriction de service ?) | Information | Confirmer qu'il s'agit d'un tri déterministe sans effet préjudiciable | Art. 3, point 1 ; art. 5, par. 1, c) si un modèle était utilisé | Responsable produit | AIA-003 |
| NV-03 | n.a. | Outils d'IA utilisés par l'organisation hors de cette application (personnel des bibliothèques) | Information | Rôle éventuel de déployeur | Art. 4 au niveau de l'organisation | Direction / RH | AIA-004, AIA-005 |
| NV-04 | n.a. | Évolutions prévues (feuille de route) comportant de l'IA | Information | Anticiper un nouvel audit | Entrée dans le champ du règlement | Responsable produit | AIA-006 |

## 10. Recommandations et plan de remédiation

Aucune action P1 ni P2. Au titre de ce dépôt, aucune obligation de l'AI Act n'a été identifiée.

| Priorité | Constat(s) | Action | Base | Échéance | Effort | Preuve de clôture attendue |
|---|---|---|---|---|---|---|
| P4 | AIA-005 | Confirmer l'absence d'IA dans les composants et services hors dépôt | Vérification organisationnelle | n.a. | S | Inventaire applicatif signé |
| P4 | AIA-006 | Note de qualification et point de contrôle « IA » avant chaque évolution | Bonne pratique | n.a. | S | Note datée, procédure de revue |

## 11. Limites de l'audit

- **Analyse statique** : comportement réel, base de données et configuration de production non observés. Le dépôt ne contient ni interface ni routes.
- **Documents organisationnels non disponibles** : inventaire applicatif, contrats avec des prestataires, politique d'usage d'outils d'IA.
- **Références juridiques** : les entrées de confiance moyenne ou faible (CAL-003, CAL-010, CAL-011) sont à confirmer sur le Journal officiel. Elles sont sans incidence ici.
- **Textes évolutifs** : lignes directrices de la Commission (définition du système d'IA, février 2025) non contraignantes et susceptibles d'évoluer.
- **Portée de la conclusion** : elle vaut pour le seul code fourni à la date d'audit. Elle ne constitue ni une attestation de conformité ni une attestation d'absence d'obligations pour l'organisation.
- **Nature du rapport** : il ne remplace ni l'avis d'un juriste ni une évaluation de la conformité au sens de l'article 43.

## 12. Suivi (ré-audit)

Aucun audit précédent. Ce premier audit établit les identifiants AIA-001 à AIA-006, à conserver lors des audits ultérieurs.

| Constat | Statut précédent | Statut actuel | Preuve |
|---|---|---|---|
| AIA-001 à AIA-006 | n.a. | Nouveau | Présent rapport |
