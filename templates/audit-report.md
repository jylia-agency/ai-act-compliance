# Rapport d'audit AI Act : {{NOM_DU_PROJET}}

> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43
> du règlement (UE) 2024/1689.

| Paramètre | Valeur |
|---|---|
| Date d'audit | {{AAAA-MM-JJ}} |
| Périmètre | {{dépôt, branche, dossiers exclus}} |
| Commit audité | {{empreinte complète, `git rev-parse HEAD`, ou « non versionné »}} |
| Mode | {{complet / différentiel depuis <réf. de base>}} |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | {{meta.last_verified}} (voir `references/legal-sources.md`) |
| Contexte fourni par le demandeur | {{finalités, utilisateurs, dates de mise sur le marché, statut de l'organisation, ou « aucun »}} |
| Méthode | Skill `ia-compliance` v{{version}}, lecture seule, sans exécution du code |
| Audit précédent | {{référence ou « aucun »}} |

## 1. Résumé exécutif

- **Systèmes d'IA identifiés** : {{n}} ({{liste courte}}).
- **Points les plus sensibles** : {{2 à 4 puces, avec identifiants AIA-NNN}}.
- **Obligations en vigueur concernées** : {{art. 4, 5, 50...}}.
- **Échéances à venir** : {{dates et articles}}.
- **Principales incertitudes** : {{informations manquantes, références à confirmer}}.
- **Constats dont l'échéance est à confirmer** (base juridique non relue sur le texte officiel) : {{AIA-NNN et CAL-NNN}}.
- **Synthèse des constats** :

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | | | | | |
| Risque potentiel | | | | | |
| À vérifier juridiquement ou organisationnellement | | | | | |
| Bonne pratique recommandée | | | | | |
| Non encore applicable | | | | | |
| Non applicable | | | | | |

## 2. Périmètre et méthode

{{Arborescence analysée, fichiers clés, outils utilisés (scan_ai_signals, obligation_timeline), éléments non analysés.}}

## 3. Systèmes d'IA identifiés

Voir l'inventaire détaillé (`ai-system-inventory.md`). Synthèse :

| ID | Système | Finalité | Rôle(s) de l'organisation | Modèle(s) et fournisseur(s) | Classification | Confiance |
|---|---|---|---|---|---|---|

Éléments examinés et écartés (pas un système d'IA, hors champ) : {{liste motivée}}.

## 4. Rôles réglementaires

{{Par système : rôle retenu, fondement (art. 3), distinction fournisseur du système / fournisseur du modèle GPAI, hypothèses.}}

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|

## 6. Classification

Pour chaque système : critères examinés (art. 5, art. 6 et annexes I et III, art. 6, par. 3, art. 50,
GPAI), exceptions envisagées, conclusion, incertitudes. Détail : `risk-classification.md`.

## 7. Obligations et calendrier

Matrice détaillée : `compliance-matrix.md`. Statuts calculés à la date d'audit :

| Obligation | Système | Rôle | Statut temporel | Date | Réf. calendrier | Confiance |
|---|---|---|---|---|---|---|

## 8. Constats

<!-- Un bloc par constat, ordonnés par gravité puis par identifiant. -->

### AIA-001 : {{titre}}
- **Système d'IA concerné** :
- **Nature du constat** :
- **Gravité** :
- **Niveau de confiance** :
- **Preuve observée** :
- **Fichier(s) et lignes** :
- **Rôle réglementaire concerné** :
- **Classification du système** :
- **Référence juridique** :
- **Date d'application** :
- **Conditions et exceptions** :
- **Explication** :
- **Recommandation** :
- **Méthode de vérification** :

## 9. Éléments non vérifiables

Voir `unverifiable-register.md`. Synthèse des informations nécessaires pour compléter l'évaluation.

## 10. Recommandations et plan de remédiation

Voir `remediation-plan.md`. Synthèse des actions P1 et P2.

## 11. Limites de l'audit

- Analyse statique : comportement réel, données, prompts dynamiques et configuration de production non observés.
- Documents organisationnels non disponibles dans le dépôt : {{liste}}.
- Références juridiques : entrées de confiance moyenne ou faible à confirmer sur le Journal officiel : {{CAL-NNN}}.
- Lignes directrices, normes harmonisées et actes d'exécution évolutifs.
- {{Autres limites spécifiques}}.

## 12. Matrice des preuves

Voir `compliance-matrix.md`, section « Matrice des preuves ». Les preuves externes (contrats,
politiques, tests réels, documentation des fournisseurs, configuration de production) sont listées à part.

## 13. Suivi (ré-audit)

| Constat | Statut précédent | Statut actuel | Preuve |
|---|---|---|---|
