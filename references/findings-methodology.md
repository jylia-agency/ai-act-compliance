# Méthodologie de rédaction des constats

> Dernière mise à jour : **2026-10-27**.

## 1. Natures (une seule par constat)

| Nature | Quand l'utiliser | Exemple |
|---|---|---|
| Constat technique avéré | Fait démontré par le code, la configuration ou un document disponible, avec fichier et lignes | « Le prompt système de `tutor_chat.py:9` demande de ne jamais révéler la nature d'IA. » |
| Risque potentiel | Problème plausible, qualification juridique ou effet réel à confirmer | « L'inférence d'émotions pendant les examens est susceptible de relever de l'art. 5, par. 1, f). » |
| À vérifier juridiquement ou organisationnellement | Impossible à confirmer par le dépôt seul (contrats, formation, finalité, date de mise sur le marché) | « Mesures de maîtrise de l'IA non observables dans le dépôt. » |
| Bonne pratique recommandée | Amélioration utile sans obligation identifiée à la date d'audit | « Épingler la version du modèle. » |
| Non applicable | Obligation exclue après analyse motivée | « Art. 53 : l'organisation n'est pas fournisseur de modèle GPAI. » |
| Non encore applicable | Obligation identifiée dont la date d'application n'est pas atteinte | « Art. 14 : applicable au 2027-12-02 pour l'annexe III. » |

Règle : lorsque le fait est avéré mais la qualification incertaine, la nature est « Risque
potentiel » et le fait est cité dans « Preuve observée ». Le texte distingue explicitement
« Fait observé » et « Analyse juridique ».

## 2. Gravité

| Niveau | Critères indicatifs |
|---|---|
| Critique | Pratique potentiellement interdite ; atteinte grave et plausible aux droits des personnes ; obligation applicable manifestement non respectée sur un système à fort impact |
| Élevée | Obligation applicable probablement non respectée (par exemple art. 50, par. 1) ; décision automatisée affectant des personnes sans contrôle ; secret exposé |
| Moyenne | Obligation future importante non préparée ; mesure présente mais efficacité non démontrée ; défaut de traçabilité |
| Faible | Écart documentaire ou organisationnel limité |
| Information | Point de contexte, mesure positive constatée, question ouverte |

La gravité d'un constat « Non encore applicable » reflète l'enjeu et l'effort de préparation, pas un
manquement actuel.

## 3. Niveau de confiance

| Niveau | Critères |
|---|---|
| Élevée | Preuve directe, interprétation non ambiguë, référence `[TI]` |
| Moyenne | Preuve indirecte ou partielle, ou référence `[O26]` |
| Faible | Hypothèse fondée sur un contexte incomplet, ou référence `[AV]` |

Si la confiance diffère entre faits et qualification, l'indiquer : « Élevée (faits) / Moyenne (qualification) ».

## 4. Champs obligatoires

| Champ | Contenu attendu |
|---|---|
| Identifiant | `AIA-NNN`, séquentiel, stable entre audits |
| Titre | Court, factuel, sans conclusion juridique excessive |
| Système d'IA concerné | Identifiant de l'inventaire (par exemple `SYS-02`) |
| Nature du constat | Une des six natures |
| Gravité | Échelle ci-dessus |
| Niveau de confiance | Échelle ci-dessus |
| Preuve observée | Description factuelle, extrait court (secrets masqués) |
| Fichier(s) et lignes | `chemin:ligne` ou « non disponible » |
| Rôle réglementaire concerné | Fournisseur, déployeur, fournisseur GPAI, importateur, distributeur, mandataire, ou « à déterminer » |
| Classification du système | Valeur de `risk-classification.md`, section 1 |
| Référence juridique | Article, paragraphe, point, annexe ; marqueur `[TI]`, `[O26]` ou `[AV]` ; lien officiel ; « Aucune (bonne pratique) » le cas échéant |
| Date d'application | Date et statut à la date d'audit (identifiant `CAL-NNN`) |
| Conditions et exceptions | Conditions examinées, exceptions retenues ou écartées et pourquoi |
| Explication | Pour un lecteur non juriste, 2 à 5 phrases |
| Recommandation | Action concrète, proportionnée ; préciser obligation ou bonne pratique |
| Méthode de vérification | Comment prouver la correction (test, fichier, document, capture) |

## 5. Formulations

À utiliser : « susceptible de », « au vu des éléments observés », « manquement potentiel »,
« à confirmer », « mesure présente, efficacité non démontrée ».

À proscrire : « conforme », « certifié », « en règle », « non conforme » (sans qualification),
« illégal », « l'entreprise encourt une amende de ... ».

## 6. Priorisation pour le plan de remédiation

Score indicatif : priorité **P1** si (Critique ou Élevée) et obligation en vigueur ; **P2** si Élevée
ou Moyenne et échéance dans moins de 6 mois, ou risque potentiel significatif ; **P3** si obligation
future à plus de 6 mois ou bonne pratique à fort bénéfice ; **P4** sinon. Effort estimé : S (moins
d'une semaine), M (1 à 4 semaines), L (plus d'un mois). Ajuster au contexte et le dire.

## 7. Matrice de preuves

Objectif : permettre à un auditeur externe de retrouver et de rejouer exactement la justification
de chaque constat.

### 7.1 États d'un contrôle

| État | Définition | Ne pas confondre avec |
|---|---|---|
| **Démontré** | Une preuve positive observée établit la présence de la mesure contrôlée | Une obligation satisfaite (la mesure peut être insuffisante) |
| **Non démontré** | Le dépôt contient l'emplacement où la mesure devrait figurer et elle n'y figure pas, ou une preuve établit son absence (par exemple publication directe sans validation) | Une absence de document organisationnel (voir « Impossible à vérifier ») |
| **Non applicable** | Le contrôle est sans objet, avec motif (classification, rôle, date) | Un contrôle non effectué |
| **Impossible à vérifier** | La preuve relève de l'organisation, de contrats, de tests réels, de la documentation des fournisseurs de modèles ou de la configuration de production | Un manquement |

Le statut temporel (en vigueur, non encore applicable, conditionnel, à vérifier, échéance à
confirmer) est **indépendant** de l'état du contrôle et figure dans une colonne distincte.

### 7.2 Enregistrement de preuve `PRV-NNN`

| Champ | Contenu |
|---|---|
| Identifiant | `PRV-NNN` |
| Contrôle | Identifiant de la checklist (par exemple `A4`) |
| Constat(s) | `AIA-NNN` liés |
| Fichier | Chemin relatif à la racine du dépôt |
| Lignes | Plage `début-fin` |
| Commit | Empreinte complète du commit audité (`git rev-parse HEAD`) ; « non versionné » sinon |
| Date | Date de collecte |
| Nature | Statique (code, configuration, document du dépôt) ou externe (fournie par l'organisation) |
| Méthode de reproduction | Commande ou démarche exacte, par exemple `git show <commit>:app/grading.py \| sed -n '19,29p'` ou `python3 scripts/scan_ai_signals.py . --json` |
| État établi | Démontré / Non démontré / Non applicable / Impossible à vérifier |

Les preuves externes (contrats, politiques, résultats de tests réels, attestations des fournisseurs)
sont listées séparément : elles ne peuvent pas être établies par analyse statique et sont
identifiées comme telles dans le rapport.
