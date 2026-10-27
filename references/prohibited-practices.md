# Pratiques d'IA interdites (article 5)

> Base : art. 5 du règlement (UE) 2024/1689 `[TI]`, complété par le règlement (UE) 2026/1744 `[O26]`.
> Applicable depuis le **2025-02-02** (art. 113, al. 3, a)) ; nouvelles interdictions le **2026-12-02** `[O26]`.
> Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5),
> lignes directrices de la Commission sur les pratiques interdites (février 2025).

## 1. Règles d'analyse

- L'article 5 vise la **mise sur le marché**, la **mise en service** et l'**utilisation** : il
  concerne donc fournisseurs **et** déployeurs.
- Aucune règle transitoire : un système mis sur le marché avant le 2025-02-02 est concerné.
- Chaque point comporte des **conditions cumulatives** et parfois des **exceptions** : les examiner
  toutes. Un constat sur l'article 5 est presque toujours de nature « Risque potentiel » ou
  « À vérifier juridiquement » ; le fait technique qui le fonde est cité comme preuve.
- Gravité par défaut d'un risque plausible : **Critique**.

## 2. Liste des pratiques `[TI]`

| Point | Pratique | Conditions et exceptions à examiner | Indices techniques |
|---|---|---|---|
| a) | Techniques subliminales, délibérément manipulatrices ou trompeuses | Objet ou effet d'altérer substantiellement le comportement en portant atteinte à la capacité de décision éclairée, entraînant une décision qui n'aurait pas été prise autrement, **et** causant ou susceptible de causer un **préjudice important** | Prompts demandant de tromper, dark patterns pilotés par IA |
| b) | Exploitation des vulnérabilités dues à l'âge, au handicap ou à une situation sociale ou économique spécifique | Altération substantielle du comportement et préjudice important | Ciblage de mineurs, de personnes vulnérables |
| c) | Notation sociale | Évaluation ou classification de personnes sur la base de leur comportement social ou de caractéristiques personnelles, menant à un traitement préjudiciable dans des contextes sans lien, ou injustifié ou disproportionné | Scores de « confiance » ou de « fiabilité » de personnes réutilisés hors contexte |
| d) | Évaluation du risque d'infraction pénale fondée **uniquement** sur le profilage ou des traits de personnalité | Exception : appui à une évaluation humaine fondée sur des faits objectifs et vérifiables directement liés à une activité criminelle | Prédiction de récidive |
| e) | Constitution ou développement de bases de reconnaissance faciale par moissonnage **non ciblé** d'images faciales (internet, vidéosurveillance) | Caractère non ciblé | Scrapers d'images de visages, constitution d'index faciaux |
| f) | **Reconnaissance des émotions sur le lieu de travail et dans les établissements d'enseignement** | Exception : système destiné à être mis en place ou sur le marché pour des **raisons médicales ou de sécurité** | `deepface` avec `actions=["emotion"]`, scores de stress, d'attention émotionnelle, analyse vocale des émotions |
| g) | Catégorisation biométrique déduisant race, opinions politiques, appartenance syndicale, convictions religieuses ou philosophiques, vie sexuelle ou orientation sexuelle | Exceptions : étiquetage ou filtrage de jeux de données biométriques acquis légalement ; domaine répressif | Classifieurs d'attributs sensibles sur visages ou voix |
| h) | Identification biométrique à distance **en temps réel** dans des espaces accessibles au public **à des fins répressives** | Exceptions strictement encadrées (par. 1, h), i) à iii) et par. 2 à 7) : recherche ciblée de victimes, prévention d'une menace, localisation de suspects de certaines infractions, avec autorisation préalable | Rarement pertinent hors autorités répressives |

## 3. Nouvelles interdictions introduites par le règlement 2026/1744 `[O26]`

Applicables le **2026-12-02** : art. 113, troisième alinéa, point a), tel que modifié (extrait
officiel : « with the exception of Article 5(1), first subparagraph, points (ba) and (bb), and
Article 5(1a) and (1b) which shall apply from 2 December 2026 » ; voir CAL-004).

- **Point (ba)** : mise sur le marché, mise en service ou utilisation d'un système d'IA qui génère ou
  manipule des images, vidéos, sons ou contenus similaires **réalistes** représentant les parties
  intimes d'une **personne physique identifiable** ou sa participation à des activités sexuellement
  explicites, **sans son consentement** (extrait officiel du point (ba), version anglaise) ;
- **Point (bb)** : systèmes d'IA générant ou manipulant du **matériel pédopornographique** ; selon
  les considérants, un moyen de défense « sans droit » prévu par le droit national (art. 5,
  par. 1, de la directive 2011/93/UE) n'est pas affecté.
- **Paragraphes 1 bis et 1 ter** (selon la version consolidée, libellé exact à relire `[AV]`) :
  côté **fournisseur**, l'interdiction ne joue que si la génération de tels contenus est la
  destination du système ou un **résultat raisonnablement prévisible et reproductible** ; côté
  **déployeur**, que s'il utilise le système pour générer ou manipuler de tels contenus.

Un système génératif généraliste peut donc être concerné si un tel résultat est raisonnablement
prévisible et reproductible, notamment en l'absence de garde-fous. Contrôles d'audit : filtres de
prompts et de sorties, politique d'usage, détection de personnes réelles, signalement. Avant le
2026-12-02, un défaut de garde-fou est « Non encore applicable » au titre de l'article 5 (il peut
relever d'autres législations, hors périmètre).

## 4. Points de vigilance par domaine

- **Éducation** : l'analyse émotionnelle des élèves (attention, stress, ennui) en classe ou en
  examen relève a priori du point f). La détection de fraude n'est pas une « raison de sécurité » au
  sens de l'exception, qui doit être interprétée strictement `[TI]`. Voir `education-ai.md`.
- **Emploi** : analyse émotionnelle des entretiens vidéo ou des appels de salariés : point f).
- **Chatbots** : un assistant qui nie être une IA soulève d'abord l'article 50, paragraphe 1. Le
  point a) n'est retenu que si les conditions d'altération substantielle et de préjudice important
  sont plausibles ; sinon, le mentionner comme « examiné et non retenu ».
- **Distinction** : la reconnaissance des émotions **hors** travail et enseignement n'est pas
  interdite mais relève de l'annexe III, point 1, c) (haut risque) et de l'article 50, paragraphe 3.

## 5. Recommandations types

- Désactiver la fonctionnalité concernée dans l'Union dans l'attente d'une analyse juridique.
- Documenter la finalité réelle et l'éventuelle exception invoquée.
- Remplacer par une solution sans inférence d'émotions (par exemple, surveillance humaine,
  événements techniques non biométriques).
