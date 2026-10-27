# Audit à l'aveugle : demo-insufficient-info (skill 1.2.1, Sonnet, 2026-10-27)

Synthèse fidèle du rapport restitué sous forme de texte par l'agent (environnement sans droit
d'écriture pour le sous-agent). Le rapport complet comportait 15 sections, 7 constats, 8 preuves
`PRV` et 9 éléments non vérifiables.

| Élément | Résultat de l'agent | Attendu (`EXPECTED.md`) | Verdict |
|---|---|---|---|
| Système d'IA | SYS-01 TalentRank, GradientBoostingClassifier, système d'IA au sens de l'art. 3, point 1 (confiance moyenne à élevée) | Système d'IA probable, confiance élevée | OK |
| Classification | Indéterminée (confiance faible) ; hypothèses emploi (annexe III, point 4, a)), formation (point 3, a)), autre usage | Indéterminée, hypothèses sans conclusion ferme | OK |
| Profilage | Relevé : dérogation de l'art. 6, par. 3 probablement exclue | Hypothèse de profilage à examiner | OK |
| Rôle | Fournisseur et déployeur probables (mise en service pour usage propre), non établi | Rôle indéterminé | OK |
| Variable `age` | AIA-001 Risque potentiel, Élevée ; art. 10 futur si haut risque | Risque potentiel, Élevée ou Moyenne | OK |
| Date de mise en service | Inconnue ; calendrier calculé pour trois hypothèses ; CAL-013 conditionnel | Statut conditionnel | OK |
| Questions | Registre NV-01 à NV-09 | Questions sur finalité, utilisateurs, effets, date, commercialisation, profilage | OK |
| Constats interdits | Aucun haut risque ferme, aucun « non à haut risque », aucune obligation du chapitre III applicable, pas d'art. 50, pas de GPAI | Idem | OK |
| Constats supplémentaires | Classement tronqué au top 20 sans justification ni trace (AIA-004) ; import circulaire nuisant à la reproductibilité (AIA-005) ; `joblib.load` sans contrôle d'intégrité (AIA-007) | Non exigés | Pertinents |

Verdict : conforme, 0 faux négatif, 0 faux positif, 0 erreur de calendrier.
