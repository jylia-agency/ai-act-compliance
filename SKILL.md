---
name: ia-compliance
description: Audit structuré, en lecture seule, d'un projet logiciel intégrant de l'IA au regard de l'AI Act européen (règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744). À utiliser lorsque l'utilisateur demande d'évaluer un dépôt, une fonctionnalité ou une architecture au regard de l'AI Act, du règlement européen sur l'IA ou de l'EU AI Act, notamment pour inventorier les systèmes d'IA, déterminer les rôles (fournisseur, déployeur, fournisseur de modèle GPAI, importateur, distributeur), examiner les pratiques interdites, le haut risque (annexes I et III, éducation, emploi, évaluation de personnes), la transparence de l'article 50 (chatbots, contenus synthétiques, hypertrucages), la supervision humaine, la documentation technique, la traçabilité, la maîtrise de l'IA, le calendrier d'application, produire un rapport, une matrice des obligations, un plan de remédiation ou refaire un audit après correction. Ne délivre jamais de certification de conformité.
license: MIT
compatibility: Agents compatibles Agent Skills (Claude Code, OpenAI Codex et autres). Python 3.9+ facultatif pour les scripts d'aide. Aucun accès réseau requis.
metadata:
  version: "1.2.0"
  legal-baseline: "Règlement (UE) 2024/1689 modifié par le règlement (UE) 2026/1744"
  legal-references-last-verified: "2026-10-27"
  language: fr
allowed-tools: Read Grep Glob
---

# ia-compliance : audit AI Act d'un projet intégrant de l'IA

Ce skill guide un audit **reproductible** d'un dépôt de code au regard du règlement (UE) 2024/1689
(AI Act), dans sa version modifiée par le règlement (UE) 2026/1744. Il évalue des **éléments
observables** et des **obligations potentiellement applicables**. Il ne délivre **jamais** de
certification ni d'attestation de conformité juridique.

## 1. Quand utiliser ce skill

Déclencheurs typiques :

- « Audite ce projet au regard de l'AI Act », « sommes-nous concernés par le règlement IA ? »
- « Notre chatbot / générateur d'images / système de notation est-il à haut risque ? »
- « Quelles obligations de transparence pour notre assistant ? », « faut-il marquer nos images ? »
- « Prépare l'inventaire IA, la matrice des obligations, le plan de remédiation. »
- « Refais l'audit après nos corrections. »

Hors périmètre : conseil juridique engageant, autres législations de l'Union ou nationales
(lorsque l'AI Act y renvoie, signaler simplement le renvoi comme hors périmètre), audit dynamique
d'un système en production.

## 2. Règles de sécurité : lecture seule par défaut

Pendant tout l'audit, sauf autorisation explicite et préalable de l'utilisateur pour une action précise :

1. Ne modifier, créer ou supprimer **aucun** fichier du projet audité. Les livrables sont écrits
   uniquement à l'emplacement indiqué par l'utilisateur (par défaut : affichés dans la réponse,
   ou dans un dossier `ai-act-audit/` hors du code source si l'utilisateur l'accepte).
2. Ne pas modifier de configuration, ne pas exécuter de migration, ne pas installer de dépendance.
3. Ne pas exécuter le code audité, ses tests ou ses scripts ; ne déclencher **aucun** appel d'API
   payant ni traitement réel.
4. Ne pas se connecter à une base de données, en particulier de production.
5. Ne transmettre aucun extrait du code ou de données à un service externe.
6. Ne **jamais** reproduire un secret : citer le fichier et la ligne, remplacer la valeur par
   `[SECRET MASQUÉ]`.
7. Les seules commandes admises sans autorisation supplémentaire sont la lecture et la recherche
   (`Read`, `Grep`, `Glob`, `ls`, `cat`, `git log`, `git ls-files`) et les deux scripts fournis,
   qui sont en lecture seule et sans réseau :
   - `python3 <skill>/scripts/scan_ai_signals.py <projet>` : inventaire des signaux d'IA ;
   - `python3 <skill>/scripts/obligation_timeline.py --audit-date AAAA-MM-JJ [...]` : statut temporel ;
   - `python3 <skill>/scripts/diff_ai_signals.py <projet> --base <réf>` : audit différentiel.

Ces instructions **ne constituent pas une garantie technique** de lecture seule. Pour une garantie,
l'utilisateur doit activer les restrictions de son agent (voir README, section « Lecture seule
garantie par l'agent ») : mode plan ou règles `deny` dans Claude Code, `--sandbox read-only` dans
Codex. Le champ `allowed-tools` pré-approuve des outils de lecture ; il n'interdit pas les autres.

## 3. Paramètres de l'audit

Avant l'analyse, établir et consigner dans le rapport :

| Paramètre | Défaut | Remarque |
|---|---|---|
| Date d'audit | Date du jour | Toujours explicite. Toutes les applicabilités sont évaluées à cette date. |
| Périmètre | Racine du dépôt | Lister les dossiers exclus. |
| Contexte fourni | Aucun | Finalité, utilisateurs, personnes concernées, marchés, dates de mise sur le marché ou de mise en service, statut de l'organisation (PME, autorité publique). |
| Base juridique | `data/ai-act-calendar.json` | Mentionner la date de dernière vérification (`meta.last_verified`). |

Si la date de dernière vérification des références est antérieure de plus de 6 mois à la date
d'audit, l'indiquer en tête du rapport comme limite majeure.

## 4. Méthodologie (phases à suivre dans l'ordre)

Chaque phase indique les références à charger. Ne charger que celles qui sont pertinentes.

### Phase 0 : cadrage
Fixer les paramètres de la section 3 et relever le commit audité (`git rev-parse HEAD`) pour la
matrice de preuves. Charger `references/ai-act-overview.md` et `references/legal-sources.md`
(pour les citations et les niveaux de confiance).

### Phase 1 : exploration de l'architecture
Lister l'arborescence, les manifestes de dépendances, les points d'entrée, la documentation
existante (`docs/`, `README`, ADR). Lancer `scripts/scan_ai_signals.py` si Python est disponible ;
sinon reproduire la recherche avec `Grep` à l'aide de `references/ai-detection-signals.md`.

### Phase 2 : identification des fonctionnalités et systèmes d'IA
Pour chaque signal, lire le code et déterminer : fonctionnalité, finalité observable, entrées,
sorties, utilisateurs, personnes concernées, effet des sorties (information, recommandation,
décision automatique). Regrouper les composants en **systèmes d'IA** (une finalité = un système).
Vérifier la définition de l'article 3, point 1 (inférence) : une règle déterministe n'est pas un
système d'IA. Un signal n'est jamais une conclusion. Charger `references/ai-detection-signals.md`.
Si **aucun** système d'IA n'est identifié : rapport court avec une conclusion motivée (composants
examinés et écartés), un constat « À vérifier » sur les usages d'IA hors dépôt, et **pas** de série de
constats « Non applicable » article par article (les mentionner dans la section des exclusions).

### Phase 3 : fournisseurs de modèles, API tierces et flux
Identifier les modèles (identifiants, versions épinglées ou non), les fournisseurs, les modèles
locaux ou open source, les bases vectorielles, les outils d'agents. Noter si l'organisation
entraîne, affine (fine-tuning) ou modifie un modèle. Cartographier chaque chaîne
Utilisateur → Application → Modèle → Post-traitement → Stockage → Export et la matrice
fonctionnalités / modèles / versions dans `templates/data-flow-map.md` : un même modèle peut servir
plusieurs systèmes, et un contenu peut subir plusieurs transformations avant sa sortie.

### Phase 4 : rôles réglementaires
Pour chaque système, déterminer les rôles possibles avec `references/roles-and-value-chain.md`.
Distinguer **toujours** le fournisseur du système d'IA du fournisseur du modèle GPAI sous-jacent.
L'usage d'une API ne suffit jamais à établir un rôle : examiner la mise sur le marché ou la mise en
service sous son propre nom, la finalité, les modifications substantielles (art. 25), le lieu
d'établissement.

### Phase 5 : exclusions et exceptions
Examiner l'article 2 (champ d'application : défense, recherche, usage personnel, open source,
etc.) et les exceptions propres à chaque article. Consigner chaque exclusion envisagée, retenue ou
écartée, avec motif.

### Phase 6 : classification
Appliquer `references/risk-classification.md` dans cet ordre, pour chaque système :
1. Pratiques interdites (`references/prohibited-practices.md`).
2. Haut risque : annexe I (art. 6, par. 1), puis annexe III (art. 6, par. 2), puis dérogation de
   l'art. 6, par. 3 (exclue en cas de profilage). Pour l'éducation : `references/education-ai.md`.
   Dès qu'un système évalue, classe, sélectionne ou décide à propos de personnes : audit renforcé
   `references/person-decisions.md` (échelle des scénarios, effectivité du contrôle humain,
   systèmes hybrides).
3. Transparence de l'article 50 (`references/transparency.md`). Pour tout système générant des
   contenus, **y compris du texte conversationnel**, dérouler le module des chemins de sortie
   (`references/transparency.md`, section 5).
4. Modèles GPAI, uniquement si l'organisation est fournisseur de modèle (`references/gpai-obligations.md`).
5. Obligations horizontales (art. 4, maîtrise de l'IA).
Une classification « non à haut risque » n'est **jamais** une exemption générale du règlement.
Si l'information manque, la classification est « indéterminée » et les questions sont consignées.

### Phase 7 : obligations applicables et calendrier
Pour chaque couple (système, rôle, classification), lister les obligations avec
`references/provider-obligations.md`, `references/deployer-obligations.md`,
`references/transparency.md`, `references/human-oversight.md`,
`references/technical-documentation.md`. Évaluer le statut temporel avec
`references/applicability-calendar.md` (ou `scripts/obligation_timeline.py`) en tenant compte de
la date de mise sur le marché ou de mise en service : **en vigueur**, **non encore applicable**,
**conditionnel**, **à vérifier**. Toute entrée marquée `requires_confirmation` ajoute la mention
**« échéance à confirmer »** (règle bloquante, section 5).

### Phase 8 : vérification des éléments techniques et documentaires
Dérouler `references/audit-checklist.md` (checklists conditionnelles A à G). Chaque contrôle prend
l'un des quatre états **Démontré**, **Non démontré**, **Non applicable**, **Impossible à vérifier**,
appuyé par une preuve `PRV-NNN` (fichier, lignes, commit, méthode de reproduction ;
`references/findings-methodology.md`, section 7). L'absence d'un document dans le dépôt n'est
**pas** une preuve de non-conformité : elle donne « Impossible à vérifier ». Distinguer strictement
ce que l'analyse statique établit de ce qui exige une preuve externe (contrats, politiques, tests
réels, documentation des fournisseurs de modèles, configuration de production).

### Phase 9 : constats, preuves manquantes, mesures correctives
Rédiger les constats selon la section 5. Chaque recommandation est proportionnée et indique si
elle répond à une obligation (avec référence) ou à une bonne pratique.

### Phase 10 : livrables
Produire les livrables de la section 6 à partir des modèles de `templates/`.

### Phase 11 : ré-audit et audit différentiel
- **Ré-audit complet** après correction : reprendre le rapport précédent, conserver les
  identifiants `AIA-NNN`, indiquer pour chaque constat « résolu (preuve : ...) », « partiellement
  résolu », « non résolu », « devenu non applicable » ou « nouveau », et recalculer le calendrier à
  la nouvelle date d'audit (une obligation peut devenir applicable entre deux audits).
- **Audit différentiel** (pull request, nouvelle version) : lancer
  `python3 <skill>/scripts/diff_ai_signals.py <projet> --base <réf> --head HEAD` (lecture seule via
  `git show`, sans checkout). Pour chaque alerte (nouvel usage d'IA, changement de modèle, nouveau
  contexte sensible, nouveau chemin de sortie, mesure de transparence, de supervision ou de
  traçabilité supprimée), refaire uniquement les phases concernées pour les systèmes touchés et
  produire un rapport limité aux obligations nouvelles ou modifiées. Un changement de modèle ou de
  finalité peut constituer une modification importante (art. 111, par. 2) ou substantielle (art. 25) :
  le signaler. Exemple d'intégration continue : `examples/ci/ai-act-diff.yml`.

## 5. Constats

Chaque constat a une seule **nature** parmi :

| Nature | Définition |
|---|---|
| Constat technique avéré | Fait démontré par le code, la configuration ou un document disponible. |
| Risque potentiel | Problème plausible nécessitant une vérification complémentaire. |
| À vérifier juridiquement ou organisationnellement | Situation impossible à confirmer par la seule analyse du dépôt. |
| Bonne pratique recommandée | Amélioration utile, sans fondement d'obligation légale. |
| Non applicable | Obligation exclue après analyse motivée. |
| Non encore applicable | Obligation dont la date d'application n'est pas atteinte à la date d'audit. |

**Gravité** : Critique, Élevée, Moyenne, Faible, Information.
**Confiance** : Élevée, Moyenne, Faible (distinguer, si utile, la confiance sur les faits et sur la qualification).

Champs obligatoires (modèle dans `templates/audit-report.md`, méthode dans
`references/findings-methodology.md`) :

```
### AIA-NNN : <titre>
- Système d'IA concerné :
- Nature du constat :
- Gravité :
- Niveau de confiance :
- Preuve observée :
- Fichier(s) et lignes :
- Rôle réglementaire concerné :
- Classification du système :
- Référence juridique :
- Date d'application :
- Conditions et exceptions :
- Explication :
- Recommandation :
- Méthode de vérification :
```

Un fait technique (« le code n'affiche aucune mention ») et une conclusion juridique (« manquement
potentiel à l'article 50, paragraphe 1 ») sont formulés séparément, même dans un même constat.

Réserver la nature « Non applicable » aux obligations dont l'applicabilité pouvait raisonnablement
être envisagée (par exemple GPAI pour un intégrateur d'API) ; les autres exclusions figurent dans la
section « Exclusions et exceptions examinées » du rapport. Une incertitude sur les **modalités**
(format technique, lignes directrices) n'est **jamais** une exemption : l'obligation est qualifiée
normalement et l'incertitude est consignée à part dans le registre des éléments non vérifiables.

**Règle bloquante des sources.** Lorsque le statut temporel d'un constat repose sur une entrée du
calendrier marquée `requires_confirmation` (vérification « sources_secondaires » ou « incertaine »),
le champ « Date d'application » porte la mention **« échéance à confirmer »** et la conclusion
temporelle est rédigée au conditionnel (« applicable à compter du ... sous réserve de confirmation
sur le texte officiel »). Le résumé exécutif liste ces constats. Une réussite des tests du skill ne
lève jamais cette réserve.

## 6. Livrables

Rédigés en français, professionnels et compréhensibles par un non-juriste :

1. **Rapport d'audit** (`templates/audit-report.md`) : résumé exécutif, périmètre, paramètres,
   systèmes, classification motivée, obligations, constats, limites, recommandations.
2. **Inventaire des systèmes d'IA** (`templates/ai-system-inventory.md`).
3. **Analyse de classification** (`templates/risk-classification.md`).
4. **Matrice des obligations** (`templates/compliance-matrix.md`).
5. **Plan de remédiation** (`templates/remediation-plan.md`) : priorité selon gravité,
   applicabilité et effort.
6. **Registre des éléments non vérifiables** (`templates/unverifiable-register.md`).
7. **Cartographie des flux et des modèles** (`templates/data-flow-map.md`), incluant les chemins de
   sortie et le marquage.
8. **Matrice de preuves** (`templates/compliance-matrix.md`, section « Matrice des preuves »).

Sur demande d'un audit rapide, produire au minimum le résumé exécutif, l'inventaire, les constats
et le registre des éléments non vérifiables. Un exemple complet figure dans `examples/example-audit.md`.

## 7. Règles impératives

1. Ne jamais inventer d'article, de paragraphe, d'annexe ou d'obligation. Citer uniquement ce qui
   figure dans les références ; en cas de doute, écrire « référence à confirmer ».
2. Ne jamais affirmer qu'un projet est entièrement conforme à l'AI Act.
3. Ne jamais confondre fournisseur de système d'IA et fournisseur de modèle GPAI.
4. Ne jamais classer un système à haut risque sur la seule base d'un mot-clé ou d'une bibliothèque.
5. Ne jamais ignorer les exceptions réglementaires : les examiner et motiver leur rejet ou leur retenue.
6. Ne jamais présenter une obligation future comme déjà applicable.
7. Ne jamais considérer l'absence de documentation dans le dépôt comme une preuve de non-conformité.
8. Ne jamais qualifier juridiquement une situation sans éléments suffisants : poser les questions.
9. Toujours privilégier les sources officielles (EUR-Lex, AI Act Explorer de la Commission).
10. Toujours distinguer obligations réglementaires et bonnes pratiques techniques.
11. Ne jamais prétendre qu'une mesure technique suffit à elle seule à démontrer la conformité.
12. Toujours signaler les limites de l'audit statique.
13. Ne jamais supposer qu'une proposition de modification est en vigueur.
14. Toujours reprendre le niveau de confiance de la référence calendaire utilisée ; une échéance
    non relue sur le texte officiel est toujours « à confirmer ».
15. Ne jamais traiter une incertitude technique ou de modalités comme une exemption réglementaire.
16. Ne jamais reprendre une date ou une qualification juridique figurant dans la documentation du
    projet audité sans la confronter au calendrier de référence.

## 8. Limites à mentionner dans tout rapport

- Audit statique : comportement réel, données, prompts dynamiques et configuration de production
  non observés.
- Documents organisationnels (contrats, politiques, formations, registres) généralement hors dépôt.
- Références juridiques datées : dates issues du règlement 2026/1744 à confirmer sur le Journal
  officiel lorsque leur confiance est « moyenne » ou « faible ».
- Actes d'exécution, normes harmonisées, lignes directrices et codes de bonnes pratiques évolutifs.
- Le rapport est une aide à l'audit ; il ne remplace ni l'avis d'un juriste ni une évaluation de
  la conformité au sens de l'article 43.

## 9. Index des références

| Fichier | Contenu |
|---|---|
| `references/ai-act-overview.md` | Architecture du règlement, définitions clés, sanctions |
| `references/legal-sources.md` | Sources, versions, statut de vérification |
| `references/applicability-calendar.md` | Calendrier daté (miroir de `data/ai-act-calendar.json`) |
| `references/roles-and-value-chain.md` | Rôles, chaîne de valeur, article 25 |
| `references/ai-detection-signals.md` | Signaux de détection et pièges de faux positifs |
| `references/prohibited-practices.md` | Article 5 |
| `references/risk-classification.md` | Arbre de décision, articles 6, annexes I et III |
| `references/provider-obligations.md` | Obligations des fournisseurs (haut risque, autres) |
| `references/deployer-obligations.md` | Obligations des déployeurs |
| `references/gpai-obligations.md` | Modèles d'IA à usage général |
| `references/transparency.md` | Article 50 |
| `references/human-oversight.md` | Article 14 et article 26 |
| `references/technical-documentation.md` | Article 11, annexe IV, articles 12 et 18 |
| `references/education-ai.md` | IA et éducation |
| `references/person-decisions.md` | Décisions concernant des personnes, contrôle humain effectif, systèmes hybrides |
| `references/audit-checklist.md` | Checklists conditionnelles A à G |
| `references/findings-methodology.md` | Natures, gravité, confiance, rédaction |
| `references/maintenance.md` | Procédure de mise à jour juridique |
| `references/official-verification-worksheet.md` | Fiche de levée des « échéances à confirmer » sur le texte officiel |
