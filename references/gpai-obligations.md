# Modèles d'IA à usage général (GPAI)

> Base : art. 3, points 63 à 66 ; art. 51 à 56 ; art. 101 ; art. 111, par. 3 ; annexes XI à XIII du
> règlement (UE) 2024/1689 `[TI]`. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 53](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53),
> lignes directrices de la Commission sur les obligations des fournisseurs de modèles GPAI (juillet 2025),
> code de bonnes pratiques GPAI (juillet 2025).

## 1. Condition préalable : être fournisseur du modèle

Ces obligations ne s'appliquent **qu'au fournisseur du modèle GPAI** : l'entité qui développe le
modèle (ou le fait développer) et le **met sur le marché** (API, publication des poids, intégration
dans ses propres produits mis sur le marché). Elles ne s'appliquent **pas** à l'entreprise qui se
contente d'appeler l'API d'un tiers ou d'intégrer un modèle tiers dans son système.

Questions d'audit :
1. L'organisation entraîne-t-elle un modèle présentant une généralité significative (art. 3, point 63) ?
   Indicateur des lignes directrices de la Commission, selon les sources : calcul d'entraînement
   supérieur à 10^23 FLOP et capacité à générer du langage, du texte vers image ou du texte vers
   vidéo `[AV]`.
2. Le met-elle sur le marché ?
3. Modifie-t-elle un modèle tiers (affinage) de manière significative ? (voir `roles-and-value-chain.md`, section 4) `[AV]`

Si la réponse à 1 et 2 est non : constat « Non applicable » motivé, confiance selon les preuves.

## 2. Obligations de tous les fournisseurs de modèles GPAI (art. 53) `[TI]`

| Par. | Obligation |
|---|---|
| 1, a) | Documentation technique du modèle (entraînement, essais, résultats d'évaluation), contenu minimal de l'annexe XI, à fournir sur demande à l'AI Office et aux autorités nationales |
| 1, b) | Informations et documentation à l'intention des fournisseurs en aval qui intègrent le modèle, contenu minimal de l'annexe XII |
| 1, c) | Politique visant à respecter le droit de l'Union en matière de droit d'auteur et droits voisins, notamment l'identification et le respect des réservations de droits (art. 4, par. 3, de la directive (UE) 2019/790) |
| 1, d) | Résumé suffisamment détaillé du contenu utilisé pour l'entraînement, rendu public selon le modèle de l'AI Office |
| 2 | Exception pour les modèles publiés sous licence libre et ouverte (poids, architecture, informations d'utilisation publics) : dispense des points a) et b), **sauf** modèles présentant un risque systémique |
| 3 | Coopération avec la Commission et les autorités |
| 4 | Présomption de conformité possible par l'adhésion à un code de bonnes pratiques (art. 56) ou à des normes harmonisées |

Art. 54 : les fournisseurs établis dans un pays tiers désignent un **mandataire** dans l'Union
(sauf exception pour certains modèles open source sans risque systémique).

## 3. Modèles présentant un risque systémique (art. 51, 52, 55) `[TI]`

- Classification : capacités à fort impact, **présumées** lorsque le calcul cumulé d'entraînement
  dépasse **10^25 FLOP** (art. 51, par. 2), ou décision de la Commission (critères de l'annexe XIII).
- Notification à la Commission dans les deux semaines suivant le franchissement du seuil ou la
  connaissance de celui-ci (art. 52, par. 1).
- Obligations supplémentaires (art. 55) : évaluation des modèles selon l'état de l'art, y compris
  essais adverses ; évaluation et atténuation des risques systémiques ; suivi, documentation et
  signalement des incidents graves ; niveau adéquat de cybersécurité du modèle et de son infrastructure.

## 4. Calendrier

| Situation | Date | Référence |
|---|---|---|
| Modèle mis sur le marché à partir du 2025-08-02 | Obligations applicables dès la mise sur le marché | CAL-005 |
| Modèle mis sur le marché avant le 2025-08-02 | Conformité au plus tard le **2027-08-02** | CAL-006, art. 111, par. 3 |
| Amendes (art. 101) et pouvoirs d'exécution correspondants de la Commission | 2026-08-02 | CAL-007 |

## 5. Ce que l'intégrateur d'un modèle GPAI tiers doit vérifier (bonnes pratiques et obligations propres)

- Obtenir et conserver la documentation de l'annexe XII fournie par le fournisseur du modèle (utile
  à ses propres obligations de fournisseur de système, notamment art. 11 et 13 en cas de haut risque).
- Épingler les versions de modèles et journaliser la version effectivement servie.
- Vérifier les conditions d'utilisation du fournisseur du modèle (usages interdits).
- Ces points ne font pas de lui un fournisseur de modèle GPAI.
