# Résultats attendus : demo-no-ai

Date d'audit de référence : 2026-10-27.

## Constats attendus

- Conclusion : **aucun système d'IA identifié** dans le périmètre analysé, avec niveau de confiance
  élevé pour le code présent.
- Le rapport précise les limites : services tiers, outils internes ou usages d'IA par le personnel
  non observables dans le dépôt.
- Au plus un constat « À vérifier juridiquement ou organisationnellement » invitant à confirmer
  l'absence d'autres usages d'IA dans l'organisation (gravité Information).

## Constats qui ne doivent pas apparaître

- Aucun constat de risque, de manquement ou d'obligation applicable sur l'article 50, l'article 5, les
  exigences du chapitre III ou les obligations GPAI. Des exclusions motivées sont admises dans la
  section des exclusions ; une série de constats « Non applicable » article par article est un écart
  mineur (bruit), pas une erreur de qualification.
- Aucune qualification de `predict_due_date`, `loyalty_score` ou de la classe `Book` comme système d'IA.
- Aucune affirmation selon laquelle le projet est « conforme à l'AI Act » ou « hors champ de manière
  certaine » pour l'organisation dans son ensemble.

## Erreurs de classification à éviter

- Faux positif lexical : « model » (ORM), « predict » (arithmétique), « score » (règle fixe),
  « intelligence économique » (veille manuelle).
- `loyalty_score` est une règle déterministe définie par l'humain ; elle ne répond pas à la définition
  de l'article 3, point 1 (absence d'inférence), ce qui doit être motivé brièvement.

## Niveaux de confiance attendus

- Absence de système d'IA dans le code : élevé.
- Absence d'usage d'IA dans l'organisation : non évaluable (hors dépôt).
