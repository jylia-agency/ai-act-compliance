# Résultats attendus : demo-insufficient-info

Date d'audit de référence : 2026-10-27.

## Constats attendus

1. **Système d'IA probable** : modèle d'apprentissage automatique entraîné (GradientBoostingClassifier)
   qui infère une probabilité à partir de données d'entrée (`src/rank.py`, `src/train.py`).
   Nature : Constat technique avéré (sur l'existence du modèle). Confiance : élevée.
2. **Classification indéterminée** : le terme « candidats » peut désigner des candidats à un emploi
   (annexe III, point 4, a)), à une admission dans un établissement d'enseignement (annexe III,
   point 3, a)), ou tout autre chose (prospects commerciaux, candidatures à un concours non lié à
   l'emploi). Nature : À vérifier juridiquement ou organisationnellement. Confiance : faible.
3. **Rôle indéterminé** : outil « interne » : l'organisation pourrait être fournisseur (développement
   et mise en service pour usage propre, art. 3, points 3 et 11) et déployeur ; à confirmer.
4. **Variable `age` parmi les caractéristiques** : Risque potentiel (discrimination, qualité et
   gouvernance des données). Si le système est à haut risque, l'article 10 (gouvernance des données,
   examen des biais) deviendrait pertinent à compter de sa date d'application. Gravité : élevée
   si haut risque confirmé, sinon moyenne. Confiance : moyenne.
5. **Date de mise sur le marché ou de mise en service inconnue** : le calendrier (art. 113, art. 111,
   par. 2) ne peut pas être établi ; statut temporel « conditionnel ».
6. **Questions à poser** (registre des éléments non vérifiables) : finalité exacte, nature des
   « candidats », qui utilise le classement, conséquences pour les personnes classées, existence
   d'une décision humaine ultérieure, date de mise en service, commercialisation éventuelle,
   présence de profilage au sens de l'article 6, paragraphe 3, dernier alinéa.

## Constats qui ne doivent pas apparaître

- Aucune affirmation « système à haut risque » ferme sur la base du seul mot « candidats ».
- Aucune affirmation « système non à haut risque ».
- Aucune obligation du chapitre III présentée comme applicable à la date d'audit (report au
  2 décembre 2027 pour l'annexe III).
- Aucun constat article 50 (pas d'interaction directe ni de contenu synthétique observés).
- Aucune obligation GPAI.

## Erreurs de classification à éviter

- Classification par mot-clé (« candidats » donc emploi donc haut risque).
- Considérer l'absence de documentation comme une preuve de non-conformité.
- Ignorer l'hypothèse de profilage, qui exclurait la dérogation de l'article 6, paragraphe 3, si
  le système relève de l'annexe III.

## Niveaux de confiance attendus

- Existence d'un composant d'IA : élevé.
- Classification réglementaire : faible (insuffisance d'information explicitement signalée).
