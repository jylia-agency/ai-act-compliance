# Obligations des déployeurs

> Base : art. 4, 5, 26, 27, 50, 86 du règlement (UE) 2024/1689 `[TI]` ; dates modifiées par le
> règlement (UE) 2026/1744 `[O26]`. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26).

## 1. Obligations quelle que soit la classification

| Obligation | Article | Applicable depuis |
|---|---|---|
| Ne pas utiliser une pratique interdite | Art. 5 | 2025-02-02 (nouveaux points : 2026-12-02 `[O26]`) |
| Mesures de maîtrise de l'IA | Art. 4 (rédaction `[O26]`) | 2025-02-02 |
| Informer les personnes exposées à un système de reconnaissance des émotions ou de catégorisation biométrique | Art. 50, par. 3 | 2026-08-02 |
| Déclarer les hypertrucages | Art. 50, par. 4, al. 1 | 2026-08-02 |
| Déclarer les textes générés publiés pour informer le public sur des questions d'intérêt public (sauf contrôle éditorial) | Art. 50, par. 4, al. 2 | 2026-08-02 |

## 2. Déployeurs de systèmes à haut risque (art. 26) `[TI]`

**Non encore applicables** au 2026-10-27 (annexe III : 2027-12-02 ; annexe I : 2028-08-02 `[O26]`).

| Par. | Obligation | Observable dans un dépôt ? |
|---|---|---|
| 1 | Mesures techniques et organisationnelles pour utiliser le système conformément à la notice | Partiellement (configuration) |
| 2 | Confier le contrôle humain à des personnes disposant des compétences, de la formation et de l'autorité nécessaires, et du soutien requis | Non (organisation) ; indices : rôles applicatifs |
| 4 | Dans la mesure où il exerce un contrôle sur les données d'entrée, veiller à leur pertinence et à leur représentativité suffisante | Partiellement |
| 5 | Surveiller le fonctionnement, informer le fournisseur, suspendre l'utilisation en cas de risque, signaler les incidents graves | Partiellement (procédures, alertes) |
| 6 | Conserver les journaux générés automatiquement sous son contrôle pendant une durée adaptée d'au moins **six mois** | Oui (configuration de rétention) |
| 7 | Employeurs : informer les représentants des travailleurs et les travailleurs concernés avant la mise en service ou l'utilisation sur le lieu de travail | Non |
| 8 | Autorités publiques : enregistrement de l'utilisation ; ne pas utiliser un système non enregistré | Non |
| 9 | Utiliser les informations de l'art. 13 pour les analyses d'impact exigées par d'autres textes (hors périmètre de ce skill) | Non |
| 11 | Informer les personnes physiques qu'elles sont soumises à l'utilisation d'un système de l'annexe III prenant ou aidant à prendre des décisions les concernant | Oui (textes d'interface, notifications) |
| 12 | Coopérer avec les autorités | Non |

## 3. Analyse d'impact sur les droits fondamentaux (art. 27) `[TI]`

Avant la première utilisation d'un système de l'annexe III (sauf point 2), pour :
- les déployeurs qui sont des **organismes de droit public** ou des **entités privées fournissant des
  services publics** ;
- les déployeurs de systèmes de l'annexe III, point 5, b) (solvabilité) et c) (assurance vie et maladie).

Contenu : processus, durée et fréquence d'utilisation, catégories de personnes concernées, risques
spécifiques de préjudice, mesures de contrôle humain, mesures en cas de matérialisation des risques.
Notification des résultats à l'autorité de surveillance du marché. Date : avec le chapitre III `[O26]`.

## 4. Droit à l'explication (art. 86) `[TI]`

Toute personne faisant l'objet d'une décision prise par un déployeur sur la base des sorties d'un
système de l'annexe III (sauf point 2), produisant des effets juridiques ou l'affectant de manière
significative, a le droit d'obtenir des explications claires et pertinentes sur le rôle du système
dans la procédure décisionnelle. Date effective au regard du report : `[AV]`.
Contrôle technique : le système conserve-t-il les éléments permettant d'expliquer une décision
(sorties, facteurs, version du modèle, décision humaine) ?

## 5. Déployeur requalifié en fournisseur

Voir `roles-and-value-chain.md`, section 3 (art. 25) : nom ou marque apposé, modification
substantielle, modification de la destination.

## 6. Points d'attention pour l'audit

- Le dépôt audité est souvent celui du **fournisseur** : les obligations du déployeur relèvent alors
  du « À vérifier organisationnellement » auprès des clients, et le fournisseur peut les **outiller**
  (fonction d'étiquetage, rétention configurable, écrans d'information).
- Lorsque l'organisation est à la fois fournisseur et déployeur (outil interne), cumuler les deux listes.
