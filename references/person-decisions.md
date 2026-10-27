# Audit renforcé des systèmes produisant des effets sur des personnes

> Base : art. 5, art. 6, par. 2 et 3, art. 14, art. 26, art. 86 et annexe III, points 3 et 4, du
> règlement (UE) 2024/1689 `[TI]` ; dates du haut risque modifiées par le règlement (UE) 2026/1744 `[O26]`.
> Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6).

À appliquer dès qu'un système évalue, note, classe, sélectionne, oriente ou décide à propos de
personnes physiques (élèves, étudiants, candidats, salariés, usagers, clients). Complète
`education-ai.md`, `risk-classification.md` et `human-oversight.md`.

## 1. Deux conclusions simplistes à proscrire

1. « Toute IA d'évaluation est à haut risque » : faux. Seules les destinations de l'annexe III le
   sont, sous réserve de la dérogation de l'art. 6, par. 3, et la qualification dépend de l'effet
   réel de la sortie.
2. « La présence d'un humain exclut le haut risque » : faux. Le contrôle humain est une **exigence**
   du haut risque (art. 14), pas un critère d'exclusion. La dérogation de l'art. 6, par. 3 repose
   sur des conditions propres (tâche procédurale étroite, amélioration d'une activité humaine déjà
   réalisée, détection d'écarts sans remplacer l'évaluation humaine, tâche préparatoire) et sur
   l'absence de risque important ; elle est exclue en cas de profilage.

## 2. Échelle des scénarios

Situer chaque fonctionnalité sur l'échelle ; en cas de doute entre deux niveaux, retenir le plus
élevé à titre d'hypothèse et le signaler.

| Niveau | Scénario | Exemple (éducation / emploi) | Qualification de départ | Points décisifs |
|---|---|---|---|---|
| 0 | Entraînement ou aide sans effet sur la situation de la personne | Exercices d'entraînement auto-corrigés sans trace dans le dossier ; aide à la rédaction d'un CV par le candidat lui-même | Non à haut risque (motivé) ; art. 50 selon le cas | Vérifier que les résultats ne sont **jamais** réutilisés pour évaluer ou sélectionner |
| 1 | Évaluation indicative, préparatoire | Suggestion de note soumise à l'enseignant ; synthèse d'un dossier pour un recruteur | Haut risque possible ; examiner art. 6, par. 3, d) (tâche préparatoire) | La suggestion influence-t-elle substantiellement la décision ? Profilage ? |
| 2 | Classement ou tri de personnes | Classement de copies, de candidatures ; présélection | Haut risque probable (annexe III, point 3 ou 4) | Le classement détermine l'ordre ou la sélection des dossiers examinés |
| 3 | Décision assistée | Note ou admission proposée, validée par un humain | Haut risque probable | Effectivité du contrôle humain (section 4) |
| 4 | Décision entièrement automatisée | Note publiée, candidature rejetée, examen annulé sans intervention humaine | Haut risque probable ; vérifier l'art. 5 | Risque actuel pour les personnes même avant l'application du chapitre III |

## 3. Questions obligatoires

Pour chaque fonctionnalité, consigner la réponse et sa preuve (ou « impossible à vérifier ») :

1. Quelle est la **sortie exacte** (score, rang, note, catégorie, texte) et où va-t-elle (fichier:ligne) ?
2. La sortie **influence-t-elle réellement une décision** concernant la personne ? Laquelle, prise par qui ?
3. Existe-t-il un **contrôle humain** avant tout effet ? À quel moment ?
4. Ce contrôle peut-il **modifier, ignorer ou annuler** le résultat (art. 14, par. 4, d)) ? Le code le permet-il ?
5. Le contrôleur dispose-t-il des **éléments pour juger** (justification, données d'entrée, limites) ?
6. Le contrôle est-il **effectif** ou de pure forme (section 4) ?
7. Le système effectue-t-il un **profilage** (évaluation d'aspects personnels : performances,
   comportement, fiabilité, préférences) ? Si oui et si l'annexe III s'applique : pas de dérogation.
8. Quelles **données personnelles caractéristiques** sont utilisées (âge, origine, handicap,
   localisation) et pourraient produire des effets discriminatoires (gouvernance des données, art. 10, futur) ?
9. La personne est-elle **informée** de l'usage du système (art. 26, par. 11, futur) et peut-elle
   obtenir une **explication** (art. 86) ?
10. Une **réutilisation** des sorties pour une autre finalité (orientation, sanction) est-elle possible ?

## 4. Effectivité du contrôle humain

Indices d'un contrôle de pure forme (biais d'automatisation, art. 14, par. 4, b)) :

- validation en masse ou par défaut (« tout approuver ») ;
- délai de validation incompatible avec un examen réel ;
- absence d'affichage de la justification ou des données d'entrée ;
- modification de la sortie techniquement impossible ou dissuasive (motif long, workflow bloquant) ;
- champ `validated_by` rempli automatiquement ou non authentifié ;
- taux de modification humaine nul ou non mesuré ;
- contrôle confié à une personne sans compétence ni autorité (art. 26, par. 2).

Chaque indice observé donne un constat « Risque potentiel » (ou « Non encore applicable » si
l'obligation de l'art. 14 n'est pas en vigueur), avec la preuve correspondante.

## 5. Systèmes hybrides

Un même composant (par exemple un assistant conversationnel) peut servir à la fois une finalité non
évaluative et une finalité évaluative (synthèse des échanges transmise à l'enseignant, score
d'engagement). Dans ce cas :

- découper en **systèmes distincts** selon les finalités et classer chacun ;
- rechercher les **flux de réutilisation** (exports, tableaux de bord, appels croisés entre modules) ;
- ne pas laisser la qualification la plus favorable masquer la plus exigeante.
