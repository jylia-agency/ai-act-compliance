# Méthodologie de classification des systèmes d'IA

> Base : art. 5, 6, 50, 51, annexes I et III du règlement (UE) 2024/1689 `[TI]`, dates modifiées
> par le règlement (UE) 2026/1744 `[O26]`. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6),
> projet de lignes directrices de la Commission sur la classification à haut risque (mai 2026, non définitif).

## 1. Principes

1. Classer **chaque système** séparément, selon sa **destination** (art. 3, point 12) et son usage
   raisonnablement prévisible, jamais selon un mot-clé ou une bibliothèque.
2. Les qualifications ne sont pas exclusives : un système peut être à haut risque **et** soumis à
   l'article 50. Une pratique interdite prime sur toute autre qualification.
3. Chaque classification est **motivée** : critères examinés, exceptions envisagées, éléments
   manquants, niveau de confiance.
4. Valeurs possibles : « Pratique potentiellement interdite », « Haut risque probable »,
   « Haut risque possible (à confirmer) », « Non à haut risque (motivé) », « Indéterminée »
   (information insuffisante), « Hors champ (motivé) », « Pas un système d'IA (motivé) ».
5. « Non à haut risque » ne signifie jamais « non soumis au règlement » (art. 4, art. 5, art. 50).

## 2. Arbre de décision

```
Étape 0 : est-ce un système d'IA (art. 3, point 1) ?
          non -> « Pas un système d'IA » (motiver : absence d'inférence, règle déterministe)
Étape 1 : exclusion de l'art. 2 applicable (défense, recherche exclusive, usage personnel,
          open source hors haut risque / art. 5 / art. 50) ?
          oui -> « Hors champ » (motiver ; confiance selon les preuves)
Étape 2 : une pratique de l'art. 5 est-elle plausible ? (prohibited-practices.md)
          oui -> « Pratique potentiellement interdite » ; poursuivre l'analyse pour le reste
Étape 3 : annexe I (art. 6, par. 1) : le système est-il un produit, ou le composant de sécurité
          d'un produit, couvert par la législation d'harmonisation de l'annexe I ET soumis à une
          évaluation de la conformité par un tiers ?
          oui -> « Haut risque probable (annexe I) » ; date CAL-012
Étape 4 : annexe III (art. 6, par. 2) : la destination correspond-elle à un cas d'usage listé ?
          non -> étape 6
          oui -> étape 5
Étape 5 : dérogation de l'art. 6, par. 3 :
          - le système effectue-t-il un profilage de personnes physiques ? oui -> haut risque, pas de dérogation
          - sinon, une des conditions a) à d) est-elle remplie ET le système ne présente-t-il pas de
            risque important de préjudice, notamment en n'influençant pas substantiellement le
            résultat de la prise de décision ?
            oui -> « Non à haut risque (dérogation art. 6, par. 3) » + obligation de documenter
                   l'évaluation (art. 6, par. 4) et d'enregistrement (art. 49, par. 2, CAL-016 [AV])
            non -> « Haut risque probable (annexe III) » ; date CAL-011 ; vérifier CAL-013
Étape 6 : art. 50 : interaction directe, contenus synthétiques, émotions / catégorisation
          biométrique, hypertrucages, textes d'intérêt public ? (transparency.md)
Étape 7 : l'organisation est-elle fournisseur d'un modèle GPAI ? (gpai-obligations.md)
Étape 8 : obligations horizontales : art. 4 pour tout fournisseur ou déployeur
```

## 3. Annexe III : cas d'usage à haut risque `[TI]`

| Point | Domaine | Cas d'usage (résumé fidèle, relire le texte pour toute qualification) |
|---|---|---|
| 1 | Biométrie (dans la mesure où le droit l'autorise) | a) identification biométrique à distance (hors simple vérification d'identité) ; b) catégorisation biométrique selon des attributs sensibles ou protégés ; c) reconnaissance des émotions |
| 2 | Infrastructures critiques | Composants de sécurité de la gestion et de l'exploitation d'infrastructures numériques critiques, du trafic routier, de l'approvisionnement en eau, gaz, chauffage, électricité |
| 3 | Éducation et formation professionnelle | a) accès, admission ou affectation à des établissements ; b) **évaluation des acquis d'apprentissage**, y compris pour orienter le processus d'apprentissage ; c) évaluation du niveau d'enseignement approprié ; d) surveillance et détection de comportements interdits lors des examens |
| 4 | Emploi, gestion des travailleurs, accès à l'emploi indépendant | a) recrutement ou sélection (annonces ciblées, analyse et filtrage des candidatures, évaluation des candidats) ; b) décisions sur les conditions de travail, promotion, licenciement, attribution de tâches selon le comportement ou des traits personnels, suivi et évaluation des performances |
| 5 | Services privés et publics essentiels | a) éligibilité aux prestations et services d'assistance publique (y compris soins de santé) ; b) solvabilité et note de crédit (sauf détection de fraude financière) ; c) évaluation des risques et tarification en assurance vie et maladie ; d) évaluation et classement des appels d'urgence, triage des patients |
| 6 | Répression | Évaluations de risque de victimisation, polygraphes, fiabilité des preuves, risque d'infraction ou de récidive (hors profilage seul), profilage dans les enquêtes |
| 7 | Migration, asile, contrôle aux frontières | Polygraphes, évaluation des risques, examen des demandes, détection et identification de personnes |
| 8 | Administration de la justice et processus démocratiques | a) aide aux autorités judiciaires pour rechercher et interpréter les faits et le droit ; b) influence sur le résultat d'une élection ou d'un référendum ou sur le comportement électoral (hors outils d'organisation de campagne non exposés directement aux personnes) |

La Commission peut modifier l'annexe III par actes délégués (art. 7) : vérifier la version en vigueur
à la date d'audit.

## 4. Annexe I `[TI]`, modifiée `[O26]`

- Section A (nouveau cadre législatif) : notamment jouets, ascenseurs, équipements sous pression,
  équipements radio, équipements de protection individuelle, appareils à gaz, dispositifs médicaux,
  dispositifs médicaux de diagnostic in vitro, bateaux de plaisance, équipements ATEX, installations à
  câbles. Les **machines** (règlement (UE) 2023/1230) ont été retirées de la section A et ajoutées
  à la section B (point 21) par le règlement 2026/1744 (art. 1, point 41).
- Section B : aviation civile, véhicules à moteur et agricoles, équipements marins, systèmes
  ferroviaires, etc. Pour ces produits, seules certaines dispositions s'appliquent via la
  législation sectorielle (art. 2, par. 2).
- « Composant de sécurité » (art. 3, point 14, remplacé) : composant qui remplit une fonction de
  sécurité, ou dont la défaillance ou le dysfonctionnement met en danger la santé et la sécurité des
  personnes ou des biens. Art. 6, par. 1 bis à 1 quater (nouveaux) : les systèmes utilisés
  **uniquement** pour l'assistance aux utilisateurs, l'optimisation des performances, l'efficacité,
  l'automatisation, la commodité ou le contrôle de la qualité ne sont pas des composants de sécurité,
  sauf si leur défaillance met en danger la santé et la sécurité ; une évaluation par un tiers imposée
  uniquement pour d'autres risques (spectre radioélectrique, interférences) ne remplit pas la condition
  de l'art. 6, par. 1, b).

## 5. Dérogation de l'article 6, paragraphe 3 `[TI]`

Conditions alternatives (au moins une), en plus de l'absence de risque important :

- a) tâche procédurale étroite ;
- b) amélioration du résultat d'une activité humaine **préalablement réalisée** ;
- c) détection de schémas décisionnels ou d'écarts par rapport à des schémas antérieurs, sans
  remplacer ni influencer l'évaluation humaine réalisée sans examen humain approprié ;
- d) tâche **préparatoire** à une évaluation pertinente pour un cas d'usage de l'annexe III.

Exclusion : un système de l'annexe III qui effectue un **profilage** de personnes physiques est
toujours à haut risque (art. 6, par. 3, dernier alinéa).

Obligations associées : le fournisseur qui invoque la dérogation documente son évaluation **avant**
la mise sur le marché ou la mise en service (art. 6, par. 4) ; enregistrement (art. 49, par. 2,
non modifié ; annexe VIII, section B allégée) ; date effective : CAL-016.

Erreurs fréquentes :
- considérer qu'une validation humaine en aval suffit à appliquer la dérogation (la supervision
  humaine est une exigence du haut risque, pas un critère d'exclusion) ;
- découper artificiellement un système pour que chaque partie paraisse « procédurale ».

## 6. Information insuffisante

Si la destination, les utilisateurs, les personnes concernées ou les effets ne sont pas établis :

- classification « Indéterminée », confiance faible ;
- lister les **hypothèses** (par exemple : « si les candidats sont des candidats à un emploi :
  annexe III, point 4, a) ») avec leurs conséquences ;
- consigner les questions dans le registre des éléments non vérifiables ;
- ne présenter aucune obligation du haut risque comme applicable.
