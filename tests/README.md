# Procédure de test

## 1. Tests automatiques

```bash
python3 tests/run_tests.py
```

Bibliothèque standard uniquement, sans réseau. Couverture :

| Groupe | Ce qui est vérifié |
|---|---|
| `StructureTests` | Fichiers requis, frontmatter de `SKILL.md` (nom, longueur de la description), chemins cités, dates de vérification, citation d'une source officielle, absence d'affirmation de conformité |
| `CalendarDataTests` | Complétude et sourçage du calendrier JSON, confiance non « élevée » pour 2026/1744, synchronisation JSON / Markdown |
| `TimelineScenarioTests` | 18 scénarios de calendrier : chatbot, délai de l'art. 50, par. 2 selon la date de mise sur le marché, report du haut risque, art. 111, par. 2, autorités publiques, modèles GPAI antérieurs, nouvelles interdictions, date inconnue |
| `ScannerFixtureTests` | Détection attendue sur chaque fixture, absence de faux positifs sur `demo-no-ai`, masquage du secret, absence de modification des fichiers |
| `ExampleReportTests` | Champs obligatoires et natures des constats de l'exemple et du modèle |
| `ExpectedFilesTests` | Sections obligatoires des `EXPECTED.md` |

Ces tests ne mesurent pas la qualité du raisonnement juridique d'un agent.

## 2. Évaluation par agent (à l'aveugle)

Objectif : vérifier qu'un agent qui suit le skill produit les qualifications attendues, sans
faux positifs, faux négatifs ni erreurs de calendrier.

1. Copier chaque fixture **sans son `EXPECTED.md`** dans un répertoire temporaire.
2. Copier le skill (`SKILL.md`, `references/`, `templates/`, `scripts/`, `data/`) **sans** `examples/`
   (pour ne pas fournir la réponse du cas vulnérable).
3. Demander à l'agent, en mode lecture seule : « Applique le skill ia-compliance au projet X, date
   d'audit 2026-10-27, contexte limité au contenu du projet ; écris le rapport dans Y. »
4. Comparer le rapport à l'`EXPECTED.md` :
   - constats attendus présents, avec nature, gravité et confiance compatibles ;
   - constats interdits absents ;
   - statuts temporels exacts à la date d'audit ;
   - erreurs de classification listées non commises ;
   - secret non reproduit.
5. Consigner le résultat (modèle, date, écarts) dans `RESULTS.md`.

Les résultats d'agent ne sont pas déterministes : une évaluation ponctuelle n'est pas une validation
statistique.

## 3. Scénarios couverts par les fixtures

| Scénario demandé | Fixture |
|---|---|
| Chatbot classique non automatiquement à haut risque | `demo-ai-vulnerable` (SYS-01), `demo-ai-secure` (SYS-01) |
| Notation ou évaluation d'étudiants | `demo-ai-vulnerable` (SYS-02), `demo-ai-secure` (SYS-02) |
| Application utilisant l'API d'un fournisseur tiers | `demo-ai-vulnerable` (OpenAI), `demo-ai-secure` (Anthropic) |
| Générateur de contenus synthétiques | `demo-ai-vulnerable` (SYS-03), `demo-ai-secure` (SYS-03) |
| Projet sans fonctionnalité d'IA | `demo-no-ai` |
| Date de mise sur le marché influençant les obligations | SYS-03 : 2026-03-01 (délai jusqu'au 2026-12-02) contre 2026-09-15 (aucun délai) ; SYS-02 et art. 111, par. 2 |
| Informations insuffisantes pour classifier | `demo-insufficient-info` |
| Pratique potentiellement interdite | `demo-ai-vulnerable` (SYS-04, reconnaissance des émotions) |
