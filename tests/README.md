# Procédure de test

## 1. Tests automatiques

```bash
python3 tests/run_tests.py
```

Bibliothèque standard et Git uniquement, sans réseau. Couverture :

| Groupe | Ce qui est vérifié |
|---|---|
| `StructureTests` | Fichiers requis, frontmatter de `SKILL.md` (nom, longueur de la description), chemins cités, dates de vérification, citation d'une source officielle, absence d'affirmation de conformité |
| `CalendarDataTests` | Complétude et sourçage du calendrier JSON, base juridique complète par entrée, relecture officielle datée, **règle bloquante** pour toute échéance issue de 2026/1744 non relue, synchronisation JSON / Markdown |
| `TimelineScenarioTests` | Scénarios de calendrier : chatbot, délai de l'art. 50, par. 2 selon la date de mise sur le marché, report du haut risque, art. 111, par. 2, autorités publiques, modèles GPAI antérieurs, nouvelles interdictions, date inconnue, mention « échéance à confirmer » |
| `ScannerFixtureTests` | Détection attendue sur chaque fixture, chemins de sortie, absence de faux positifs sur `demo-no-ai`, masquage du secret, absence de modification des fichiers |
| `DiffAuditTests` | Audit différentiel dans un dépôt Git temporaire : nouvel usage biométrique, mesures supprimées, changement de modèle, secret, lecture seule, absence d'alerte entre états identiques |
| `ScannerRegressionTests` | Faux positifs et faux négatifs relevés sur un dépôt réel (persona « not an AI », transformers.js, pgvector, JWT, `Blob`, `tool_calls`, vocabulaire d'interface, références d'environnement) |
| `LegalWatchTests` | Veille automatisée sur une réponse SPARQL fictive : actes inconnus seuls, bruit écarté, codes de sortie, aucune écriture dans `data/`, fiche de vérification complète |
| `ConsistencyTests` | Version de `SKILL.md` = première entrée du CHANGELOG ; en-tête de `RESULTS.md` = version et nombre de tests courants |
| `ExampleReportTests` | Champs obligatoires et natures des constats de l'exemple et du modèle |
| `ExpectedFilesTests` | Sections obligatoires des `EXPECTED.md` |

Ces tests ne mesurent pas la qualité du raisonnement juridique d'un agent et **ne valident pas le
contenu juridique** : une échéance non relue sur le texte officiel reste « à confirmer » quel que
soit le résultat des tests.

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
| Documentation trompeuse (fausses dates, fausse exemption, « conforme ») | `demo-adversarial` |
| Système hybride (assistant dont un score est réutilisé pour l'orientation) | `demo-adversarial` |
| Marquage falsifiable et perdu à l'export | `demo-adversarial` |
| Contradiction entre procédure documentée et code | `demo-adversarial` |
| Absence de preuves organisationnelles | toutes les fixtures (registre des éléments non vérifiables) |

## 4. Mesurer les faux négatifs juridiques

Lors de la comparaison avec `EXPECTED.md`, compter séparément :

- **faux négatifs** : constat attendu absent ou obligation applicable non identifiée (le plus grave) ;
- **faux positifs** : constat interdit présent (obligation inventée, haut risque par mot-clé) ;
- **erreurs de calendrier** : statut temporel faux ou absence de la mention « échéance à confirmer » ;
- **écarts de qualification** : nature, gravité ou confiance incompatibles.

Répéter l'évaluation avec plusieurs modèles ; consigner chaque exécution dans `RESULTS.md`.
