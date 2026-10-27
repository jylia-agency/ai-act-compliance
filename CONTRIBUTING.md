# Contribuer à ai-act-compliance

Merci de votre intérêt. Ce dépôt contient un skill d'aide à l'audit juridique : la rigueur des sources
prime sur l'exhaustivité.

## Règles de fond

1. **Aucune obligation inventée.** Toute règle ajoutée cite l'article, le paragraphe, le point et,
   le cas échéant, l'annexe, avec un lien officiel (EUR-Lex, ELI ou AI Act Explorer de la Commission).
2. **Sources officielles d'abord.** Les commentaires et sites non officiels servent uniquement à repérer
   une évolution ; ils ne fondent jamais une règle.
3. **Pas de proposition comme droit positif.** Une proposition de la Commission ou un accord politique
   n'est intégré qu'après publication au JO, avec sa date d'application.
4. **Dates traçables.** Toute date juridique est ajoutée d'abord dans `data/ai-act-calendar.json`
   (source, version, `verified_on`, `confidence`), puis dans `references/applicability-calendar.md`.
5. **Marqueurs de confiance.** Utiliser `[TI]`, `[O26]`, `[AV]` (voir `references/legal-sources.md`)
   et documenter toute divergence de sources.
6. **Obligation ou bonne pratique.** Ne jamais rédiger une bonne pratique comme une obligation.
7. **Pas de promesse de conformité.** Aucune formulation du type « conforme », « certifié ».
8. **Périmètre.** AI Act uniquement ; les autres législations sont signalées comme hors périmètre.

## Règles de forme

- Français professionnel, accessible à un non-juriste.
- En-tête daté (« Dernière vérification : AAAA-MM-JJ ») en tête de chaque référence.
- `SKILL.md` reste sous 500 lignes ; le détail va dans `references/`.
- Scripts : Python 3.9+, bibliothèque standard, aucun accès réseau, aucune écriture hors sortie standard.

## Processus

1. Ouvrir une issue décrivant la modification et sa source officielle.
2. Créer une branche, modifier, mettre à jour les fixtures `EXPECTED.md` si un résultat attendu change.
3. Exécuter `python3 tests/run_tests.py` (tous les tests doivent passer).
4. Pour une modification de la méthodologie : réaliser au moins une évaluation par agent à l'aveugle
   (`tests/README.md`) et consigner le résultat dans `tests/RESULTS.md`.
5. Ajouter une entrée au `CHANGELOG.md` (textes consultés, date de consultation, impact).
6. Ouvrir une pull request ; une relecture par une personne compétente en droit du numérique est
   souhaitée pour toute modification juridique.

## Signaler une erreur juridique

Ouvrir une issue avec : fichier et ligne, texte actuel, correction proposée, référence officielle
(lien EUR-Lex), date de consultation.
