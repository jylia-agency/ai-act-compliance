# Résultats des tests

## 1. Tests automatiques

| Date | Commande | Environnement | Résultat |
|---|---|---|---|
| 2026-10-27 | `python3 tests/run_tests.py` | Python 3.13, Linux | **38 tests, 38 réussis** |

Vérifications complémentaires exécutées le 2026-10-27 :

- Frontmatter de `SKILL.md` analysé avec PyYAML (`yaml.safe_load`) : valide ; description de 976 caractères (limite 1024).
- Exécution manuelle des deux scripts sur les quatre fixtures : sorties conformes aux attentes, valeur de la fausse clé absente de la sortie.

Non exécuté :

- Validateur officiel `skills-ref validate` : son installation (`pip install skills-ref`) a été refusée par la politique de l'environnement de rédaction. Il reste à lancer.
- Installation et déclenchement effectifs dans Claude Code et dans Codex (CLI) : non testés dans cet environnement. La compatibilité repose sur le respect du format Agent Skills.

## 2. Évaluation par agent à l'aveugle (2026-10-27)

Protocole : `tests/README.md`, section 2. Les fixtures ont été copiées **sans** `EXPECTED.md`, et le skill **sans** `examples/`. Un agent généraliste (même famille de modèle que l'auteur du skill) a suivi `SKILL.md`, avec pour date d'audit le 2026-10-27, en lecture seule et sans réseau. Les rapports bruts sont dans `tests/agent-runs/2026-10-27/`.

Il s'agit d'une seule exécution par fixture, ce qui n'est pas une validation statistique. Le biais lié au fait que l'auteur et l'évaluateur appartiennent à la même famille de modèle n'est pas neutralisé.

### demo-ai-vulnerable : conforme aux attentes

| Attendu (EXPECTED.md) | Obtenu | Verdict |
|---|---|---|
| E1 émotions en examen : Risque potentiel, Critique, art. 5, par. 1, f), en vigueur | AIA-001 : Risque potentiel, Critique, en vigueur depuis le 2025-02-02 | OK |
| E2 tuteur sans information : Constat avéré, Élevée, art. 50, par. 1, en vigueur | AIA-003 : identique | OK |
| E3 images sans marquage : Non encore applicable au 2026-12-02 | AIA-007 : identique | OK (calendrier exact) |
| E4 note publiée sans relecture : Risque potentiel, Élevée, haut risque non encore applicable | AIA-004 : identique, régime transitoire conditionnel | OK |
| E5 absence de journalisation | AIA-009 : Non encore applicable, Moyenne | OK (nature acceptable) |
| E6 clé d'API en clair, valeur masquée | AIA-005 ; valeur absente du rapport | OK |
| E7 notation non reproductible | AIA-006 | OK |
| E8 documentation et art. 4 non observables | AIA-012, AIA-008 | OK |
| E9 établissements publics, art. 111, par. 2 | AIA-016 | OK |
| Interdits : EduAssist fournisseur GPAI, plateforme entière à haut risque, tuteur à haut risque, chapitre III applicable, art. 50, par. 2 applicable, art. 5, par. 1, a) retenu sans analyse, secret en clair, « conforme » | Aucun | OK |

Constats supplémentaires pertinents : annulation automatique d'examen (AIA-002), hypertrucages possibles (AIA-010), garde-fous face aux nouvelles interdictions de l'article 5 (AIA-011, Non encore applicable), marquage des textes du tuteur (AIA-013).

### demo-ai-secure : conforme aux attentes, un écart léger

| Attendu | Obtenu | Verdict |
|---|---|---|
| SYS-03 sans délai de grâce (mise sur le marché le 2026-09-15) | Art. 50, par. 2 en vigueur (CAL-010) | OK (calendrier exact) |
| `exam_events.py` n'est pas un système d'IA | Écarté avec motif | OK |
| S1, S3, S5, S6, S7, S9 | AIA-013, AIA-014, AIA-006, AIA-003, AIA-012, AIA-010 | OK |
| S2 marquage : mesure présente, robustesse non démontrée | AIA-001 : Risque potentiel ; l'agent relève en plus que les métadonnées sont des clés PNG non standard | OK, et meilleur que l'oracle |
| S8 textes : À vérifier, Faible | AIA-002 : Non encore applicable, Moyenne | **Écart léger** |
| Aucun Critique ni Élevé, mais pas zéro constat | 0 Critique, 0 Élevé, 16 constats | OK |
| Interdits : secret, « conforme », chapitre III applicable, métadonnées jugées suffisantes | Aucun | OK |

### demo-insufficient-info : conforme aux attentes

Système d'IA identifié avec une confiance élevée. Classification « indéterminée » avec une confiance faible, hypothèses annexe III, point 4, a) et point 3, a) posées sans conclusion ferme, profilage relevé. Variable `age` signalée en risque potentiel. Date de mise en service inconnue, donc statut conditionnel. Registre de 12 questions. Aucune obligation du haut risque présentée comme applicable, aucun constat art. 50 ni GPAI au-delà d'exclusions motivées.

### demo-no-ai : conforme sur le fond, un écart mineur

Aucun système d'IA identifié. Les faux positifs `model`, `predict`, `score`, « intelligence » et « prêt » sont correctement écartés. Un constat « À vérifier » porte sur les composants hors dépôt.

**Écart mineur** : plusieurs constats « Non applicable » portent sur les articles 4, 5, 50 et GPAI, alors que l'oracle demandait l'absence de constats sur ces articles. Il n'y a pas d'erreur de qualification, seulement du bruit.

## 3. Corrections apportées après l'évaluation

| Écart | Correction | Re-vérifié par agent ? |
|---|---|---|
| Multiplication des constats « Non applicable » (demo-no-ai) | `SKILL.md`, phase 2 et section 5 : projet sans IA traité par un rapport court, exclusions regroupées, usage restreint de la nature « Non applicable ». Oracle précisé (bruit toléré, erreur de qualification interdite). | Non |
| Marquage des textes conversationnels qualifié avec trop d'assurance (demo-ai-secure, S8) | `SKILL.md`, section 5 : une portée incertaine (`[AV]`) donne la nature « À vérifier ». `references/transparency.md`, section 4 : règle explicite. Oracle : tolérance documentée. | Non |
| Métadonnées PNG non standard non anticipées par l'oracle | `references/transparency.md`, section 4 : qualification des métadonnées « maison ». Oracle S2 enrichi, constats supplémentaires admis listés. | Non |

Ces corrections n'ont pas fait l'objet d'une nouvelle exécution par agent : une évaluation de contrôle est recommandée.
