# Vue d'ensemble de l'AI Act pour l'audit

> Base : règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744.
> Dernière vérification : **2026-10-27**. Marqueurs : voir `legal-sources.md`.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [EUR-Lex 2026/1744](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1744),
> [AI Act Explorer](https://ai-act-service-desk.ec.europa.eu/fr/ai-act-explorer).

## 1. Logique du règlement

Le règlement suit une approche fondée sur les risques et sur les **rôles** des opérateurs :

| Niveau | Dispositions principales | Qui est visé |
|---|---|---|
| Pratiques interdites | Art. 5 `[TI]`, complété `[O26]` | Tout opérateur (mise sur le marché, mise en service, utilisation) |
| Systèmes à haut risque | Art. 6 à 49, annexes I, III, IV `[TI]`, dates `[O26]` | Fournisseurs, déployeurs, importateurs, distributeurs, mandataires |
| Obligations de transparence | Art. 50 `[TI]` | Fournisseurs et déployeurs de certains systèmes |
| Modèles d'IA à usage général | Art. 51 à 56, annexes XI à XIII `[TI]` | Fournisseurs de modèles GPAI (et mandataires) |
| Obligation horizontale | Art. 4, maîtrise de l'IA `[TI]` modifié `[O26]` | Fournisseurs et déployeurs de tout système d'IA |

Un système peut cumuler plusieurs niveaux (par exemple un système à haut risque qui interagit avec
des personnes est aussi soumis à l'article 50). L'absence de classification à haut risque n'exempte
**pas** du reste du règlement.

## 2. Définitions clés (art. 3) `[TI]`

| Point | Terme | Éléments déterminants pour l'audit |
|---|---|---|
| 1 | Système d'IA | Système automatisé, conçu pour fonctionner à différents niveaux d'autonomie, pouvant faire preuve d'adaptabilité après déploiement, qui, pour des objectifs explicites ou implicites, **déduit** à partir des entrées reçues la manière de générer des sorties (prédictions, contenus, recommandations, décisions) pouvant influencer des environnements physiques ou virtuels. Les lignes directrices de la Commission (février 2025) précisent que certains systèmes simples (traitement de données basique, heuristiques classiques, règles définies uniquement par des humains) peuvent ne pas relever de la définition. |
| 3 | Fournisseur | Développe un système d'IA ou un modèle GPAI, ou le fait développer, et le **met sur le marché ou le met en service sous son propre nom ou sa propre marque**, à titre onéreux ou gratuit. |
| 4 | Déployeur | Utilise un système d'IA **sous sa propre autorité**, sauf usage personnel non professionnel. |
| 5 | Mandataire | Établi dans l'Union, mandaté par écrit par un fournisseur établi hors de l'Union. |
| 6 | Importateur | Établi dans l'Union, met sur le marché un système portant le nom d'une personne établie dans un pays tiers. |
| 7 | Distributeur | Met un système à disposition sur le marché, sans être fournisseur ni importateur. |
| 8 | Opérateur | Fournisseur, fabricant de produits, déployeur, mandataire, importateur ou distributeur. |
| 9 | Mise sur le marché | Première mise à disposition d'un système d'IA ou d'un modèle GPAI sur le marché de l'Union. |
| 11 | Mise en service | Fourniture d'un système en vue d'une première utilisation directement au déployeur ou pour usage propre dans l'Union, conformément à sa destination. |
| 12 | Destination | Utilisation prévue par le fournisseur (notice, publicité, documentation). |
| 14 | Composant de sécurité | Définition **modifiée** par le règlement 2026/1744 pour en réduire l'ambiguïté `[O26]` : relire le texte officiel avant toute qualification au titre de l'annexe I. |
| 23 | Modification substantielle | Modification non prévue par l'évaluation initiale de la conformité, affectant la conformité ou la destination. |
| 39 | Système de reconnaissance des émotions | Identifie ou déduit les émotions ou intentions de personnes physiques sur la base de leurs données biométriques. |
| 56 | Maîtrise de l'IA | Compétences, connaissances et compréhension permettant un déploiement éclairé et la prise de conscience des possibilités, risques et préjudices. |
| 60 | Hypertrucage (deep fake) | Contenu image, audio ou vidéo généré ou manipulé par l'IA, présentant une ressemblance avec des personnes, objets, lieux, entités ou événements existants et pouvant être perçu à tort comme authentique. |
| 63 | Modèle d'IA à usage général | Modèle présentant une généralité significative, capable d'exécuter de manière compétente un large éventail de tâches distinctes, intégrable dans divers systèmes. |
| 66 | Système d'IA à usage général | Système fondé sur un modèle GPAI, capable de servir diverses finalités. |
| 68 | Fournisseur en aval | Fournisseur d'un système d'IA intégrant un modèle d'IA, y compris d'un tiers. |

## 3. Champ d'application et exclusions (art. 2) `[TI]`

À examiner en phase 5 de l'audit :

- Application territoriale : fournisseurs mettant sur le marché ou en service dans l'Union, où
  qu'ils soient établis ; déployeurs établis ou situés dans l'Union ; fournisseurs et déployeurs de
  pays tiers lorsque les **sorties** sont utilisées dans l'Union (art. 2, par. 1).
- Exclusions : systèmes utilisés exclusivement à des fins militaires, de défense ou de sécurité
  nationale (par. 3) ; systèmes et modèles développés et mis en service **uniquement** à des fins de
  recherche et développement scientifiques (par. 6) ; activités de recherche, d'essai et de
  développement avant mise sur le marché, hors essais en conditions réelles (par. 8) ; usage par des
  personnes physiques dans un cadre **purement personnel et non professionnel** (par. 10).
- Logiciels libres et open source (par. 12) : exclus **sauf** s'ils sont mis sur le marché ou en
  service en tant que systèmes à haut risque, ou s'ils relèvent de l'article 5 ou de l'article 50.
- Renvois à d'autres législations (par. 7 et suivants) : hors périmètre de ce skill ; les signaler
  sans les analyser.

## 4. Sanctions (art. 99 et 101) `[TI]`

| Manquement | Plafond | Article |
|---|---|---|
| Pratiques interdites (art. 5) | 35 000 000 EUR ou 7 % du chiffre d'affaires annuel mondial, le montant le plus élevé | Art. 99, par. 3 |
| Autres obligations des opérateurs (dont art. 16, 22, 23, 24, 26, 31, 33, 34 et 50) | 15 000 000 EUR ou 3 % | Art. 99, par. 4 |
| Informations inexactes, incomplètes ou trompeuses fournies aux autorités | 7 500 000 EUR ou 1 % | Art. 99, par. 5 |
| PME et jeunes pousses | Le montant le moins élevé des deux | Art. 99, par. 6 |
| Fournisseurs de modèles GPAI | 15 000 000 EUR ou 3 % | Art. 101 (applicable depuis le 2026-08-02) |

L'article 4 ne figure pas dans la liste de l'article 99, paragraphe 4 ; le régime de sanction de
son éventuelle méconnaissance relève des règles nationales prises en application de l'article 99,
paragraphe 1 `[AV]`. Un rapport d'audit ne chiffre **jamais** une amende.

## 5. Ce que le règlement 2026/1744 a changé (synthèse) `[O26]`

Selon les sources consultées (voir `legal-sources.md`), sans relecture du texte officiel :

- Report des exigences du haut risque : annexe III au 2027-12-02, annexe I au 2028-08-02.
- Délai jusqu'au 2026-12-02 pour l'article 50, paragraphe 2, pour les systèmes mis sur le marché
  avant le 2026-08-02.
- Nouvelles interdictions à l'article 5 (contenus intimes non consentis, matériel pédopornographique),
  applicables le 2026-12-02.
- Article 4 réécrit : obligation de prendre des mesures pour soutenir la maîtrise de l'IA, sans
  exigence d'un niveau déterminé ; rôle d'appui de la Commission et des États membres.
- Article 111, paragraphe 2 : date de référence alignée sur l'application du chapitre III ;
  appréciation au niveau du type et du modèle.
- Enregistrement des systèmes de l'annexe III jugés non à haut risque maintenu avec contenu réduit.
- Définition du composant de sécurité (art. 3, point 14) modifiée ; machines déplacées vers
  l'annexe I, section B `[AV]`.
- Détection et correction des biais (art. 10, par. 5) : critère de stricte nécessité maintenu,
  garanties ajoutées `[AV]`.
- Mesures d'allègement pour les PME et les petites entreprises de taille intermédiaire `[AV]` :
  vérifier le texte avant de les invoquer.
