# ai-act-compliance : skill `ia-compliance`

Skill open source au format **Agent Skills** pour auditer un projet logiciel intégrant de
l'intelligence artificielle au regard du **règlement européen sur l'IA (AI Act)**, règlement
(UE) 2024/1689, **tel que modifié par le règlement (UE) 2026/1744** (« Digital Omnibus on AI »).

Il s'adresse aux agents de développement (Claude Code, OpenAI Codex et autres agents compatibles) et
produit des livrables d'audit en français, exploitables dans des projets professionnels.

> **Ce skill n'est pas un outil de certification.** Il évalue des éléments observables dans un dépôt
> et des obligations **potentiellement** applicables. Il ne remplace ni un juriste, ni une évaluation
> de la conformité au sens de l'article 43 du règlement. Le calendrier juridique a été **relu sur le
> texte officiel le 2026-10-27** (15 entrées sur 16 ; une date d'enregistrement reste à interpréter) :
> voir [Sources juridiques](#sources-juridiques) et [Limites](#limites).

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Installation pour Claude Code](#installation-pour-claude-code)
- [Installation pour Codex](#installation-pour-codex)
- [Lecture seule garantie par l'agent](#lecture-seule-garantie-par-lagent)
- [Exemples d'utilisation](#exemples-dutilisation)
- [Structure du dépôt](#structure-du-dépôt)
- [Sources juridiques](#sources-juridiques)
- [Limites](#limites)
- [Procédure de test](#procédure-de-test)
- [Maintenance](#maintenance)
- [Contribution](#contribution)
- [Licence](#licence)

## Fonctionnalités

- **Méthodologie d'audit reproductible** en 12 phases (`SKILL.md`) : cadrage, exploration, détection
  des systèmes d'IA, fournisseurs de modèles, rôles, exclusions, classification, obligations et
  calendrier, vérifications techniques et documentaires, constats, livrables, ré-audit.
- **Détection des intégrations d'IA** : API de modèles (Anthropic, OpenAI, Google, Mistral...),
  modèles locaux et open source, RAG et bases vectorielles, agents, génération de médias,
  apprentissage automatique classique, biométrie, avec pièges de faux positifs et de faux négatifs.
- **Rôles réglementaires** : fournisseur du système, déployeur, fournisseur de modèle GPAI,
  importateur, distributeur, mandataire, requalification de l'article 25 ; distinction systématique
  entre fournisseur du système et fournisseur du modèle.
- **Classification conditionnelle et motivée** : article 5, article 6 et annexes I et III (dont
  dérogation de l'article 6, paragraphe 3 et profilage), article 50, modèles GPAI, article 4.
- **Calendrier juridique daté et exécutable** : date d'audit configurable, régimes transitoires
  (articles 111 et 113, délai de l'article 50, paragraphe 2), statuts « en vigueur », « non encore
  applicable », « conditionnel », « à vérifier ».
- **Checklists conditionnelles** : transparence, supervision humaine, documentation technique,
  gestion des risques, traçabilité, éducation, maîtrise de l'IA.
- **Constats normalisés** `AIA-NNN` en six natures (constat technique avéré, risque potentiel, à
  vérifier, bonne pratique, non applicable, non encore applicable), avec gravité, confiance, preuve,
  référence juridique et méthode de vérification.
- **Livrables** : rapport d'audit, inventaire des systèmes, analyse de classification, matrice des
  obligations, plan de remédiation, registre des éléments non vérifiables.
- **Règle bloquante des sources** : toute échéance dont la base juridique n'a pas été relue sur le
  texte officiel (sources secondaires ou incertaines) est restituée « échéance à confirmer » et ne
  fonde qu'une conclusion temporelle conditionnelle. Chaque entrée du calendrier porte sa base
  juridique complète (disposition, acte modificatif, date d'effet, conditions transitoires, URL
  officielle, statut de vérification).
- **Module article 50, paragraphe 2** : inventaire obligatoire des chemins de sortie (interface, API,
  copier-coller, PDF, tableur, texte, courriel, HTML, SVG, médias) et contrôle du marquage à chaque
  étape ; textes conversationnels analysés comme tout autre contenu.
- **Cartographie des flux** Utilisateur → Application → Modèle → Post-traitement → Stockage → Export,
  avec matrice fonctionnalités / modèles / versions.
- **Audit renforcé des décisions concernant des personnes** : échelle de scénarios, effectivité du
  contrôle humain, systèmes hybrides.
- **Matrice de preuves** : quatre états (démontré, non démontré, non applicable, impossible à vérifier)
  et preuves `PRV-NNN` rejouables (fichier, lignes, commit, méthode de reproduction).
- **Audit différentiel** des pull requests, avec exemple d'intégration continue.
- **Scripts d'aide sans dépendance** (Python 3.9+, bibliothèque standard, sans réseau, lecture seule) :
  - `scripts/scan_ai_signals.py` : inventaire des signaux d'IA et des chemins de sortie, secrets masqués ;
  - `scripts/obligation_timeline.py` : statut temporel des obligations à une date donnée ;
  - `scripts/diff_ai_signals.py` : comparaison de deux états Git (via `git show`, sans checkout).
- **Maintenance juridique outillée** : `scripts/verify_official_extracts.py` (rejoue la relecture du
  calendrier sur le texte officiel) et `scripts/check_legal_updates.py` avec le workflow
  `.github/workflows/legal-watch.yml` (veille mensuelle des actes liés à l'AI Act, issues de revue
  humaine, aucune règle modifiée automatiquement).

## Installation pour Claude Code

Le skill est autonome : il ne dépend d'aucun service, compte ou outil propriétaire et s'utilise sur
n'importe quel projet. Remplacez `<URL_DU_DEPOT>` par l'adresse du dépôt (ou de votre fork), ou copiez
simplement le dossier. Le dossier du skill doit s'appeler comme son `name` (`ia-compliance`).

Installation personnelle (tous vos projets) :

```bash
git clone <URL_DU_DEPOT> ~/.claude/skills/ia-compliance
```

Installation au niveau d'un projet (partagée avec l'équipe via Git) :

```bash
git clone <URL_DU_DEPOT> .claude/skills/ia-compliance
```

Claude Code découvre automatiquement le skill et le charge lorsque la demande correspond à sa
description (« audite ce projet au regard de l'AI Act »...). Vous pouvez aussi l'invoquer
explicitement avec `/ia-compliance`.

## Installation pour Codex

Codex (CLI et extension) prend en charge le format Agent Skills. L'emplacement des skills a évolué
selon les versions : consultez la documentation officielle <https://developers.openai.com/codex/skills>.
Emplacements couramment documentés :

```bash
# Skill personnel
git clone <URL_DU_DEPOT> ~/.agents/skills/ia-compliance
# ou, pour les versions antérieures
git clone <URL_DU_DEPOT> ~/.codex/skills/ia-compliance

# Skill de dépôt
git clone <URL_DU_DEPOT> .agents/skills/ia-compliance
```

Codex sélectionne le skill d'après sa description ; vous pouvez aussi le mentionner explicitement
(`$ia-compliance` ou « utilise le skill ia-compliance »).

Pour un agent sans prise en charge native des skills : demandez-lui de lire `SKILL.md` puis de suivre
la méthodologie ; les références sont des fichiers Markdown autonomes.

## Lecture seule garantie par l'agent

Le skill impose une conduite en lecture seule (section 2 de `SKILL.md`), mais **des instructions ne
constituent pas une garantie technique**. Le champ `allowed-tools: Read Grep Glob` **pré-approuve**
des outils de lecture ; il n'interdit pas les autres outils. Pour une garantie, configurez l'agent.

**Claude Code** : lancez l'audit en mode plan (`claude --permission-mode plan`, ou `Shift+Tab`), ou
ajoutez des règles de refus dans `.claude/settings.json` du projet audité :

```json
{
  "permissions": {
    "deny": ["Edit", "Write", "NotebookEdit", "WebFetch", "WebSearch"],
    "ask": ["Bash"]
  }
}
```

**Codex** : utilisez le bac à sable en lecture seule, par exemple
`codex --sandbox read-only --ask-for-approval on-request` (ou `codex exec --sandbox read-only "..."`).
Vérifiez les options exactes avec `codex --help` pour votre version.

Dans tous les cas : n'exposez pas de secrets de production à l'environnement d'audit et n'auditez pas
un dépôt connecté à des bases de production.

## Exemples d'utilisation

```text
Audite ce dépôt au regard de l'AI Act, date d'audit 2026-10-27. Nous sommes l'éditeur de
la solution, commercialisée sous notre marque auprès d'universités depuis mars 2026.
```

```text
Notre module de correction automatique est-il un système à haut risque ? Produis l'analyse
de classification et le registre des éléments non vérifiables.
```

```text
Refais l'audit après nos corrections (rapport précédent : docs/audit-2026-10.md), avec la
date d'audit du 2026-12-15.
```

Utilisation directe des scripts :

```bash
python3 scripts/scan_ai_signals.py /chemin/du/projet            # Markdown
python3 scripts/scan_ai_signals.py /chemin/du/projet --json     # JSON
python3 scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-03-01 --scope transparency
python3 scripts/diff_ai_signals.py /chemin/du/projet --base origin/main --head HEAD
```

Intégration continue : `examples/ci/ai-act-diff.yml` (GitHub Actions, permissions en lecture seule,
aucun envoi de données à un service externe).

Un rapport complet d'exemple figure dans [`examples/example-audit.md`](examples/example-audit.md).

## Structure du dépôt

```
ai-act-compliance/
├── SKILL.md                     # Point d'entrée du skill (frontmatter + méthodologie)
├── README.md, CHANGELOG.md, CONTRIBUTING.md, LICENSE, .gitignore
├── data/
│   └── ai-act-calendar.json     # Calendrier juridique machine (source des scripts)
├── references/                  # Références chargées à la demande par l'agent
│   ├── ai-act-overview.md       # Architecture, définitions, sanctions, apports de 2026/1744
│   ├── legal-sources.md         # Sources, versions, statut de vérification, divergences
│   ├── applicability-calendar.md
│   ├── roles-and-value-chain.md
│   ├── ai-detection-signals.md
│   ├── prohibited-practices.md
│   ├── risk-classification.md
│   ├── provider-obligations.md
│   ├── deployer-obligations.md
│   ├── gpai-obligations.md
│   ├── transparency.md
│   ├── human-oversight.md
│   ├── technical-documentation.md
│   ├── education-ai.md
│   ├── person-decisions.md
│   ├── audit-checklist.md
│   ├── findings-methodology.md
│   └── maintenance.md
├── templates/                   # Modèles de livrables
│   ├── audit-report.md, ai-system-inventory.md, risk-classification.md
│   ├── compliance-matrix.md, remediation-plan.md, unverifiable-register.md
│   └── data-flow-map.md
├── scripts/
│   ├── scan_ai_signals.py
│   ├── obligation_timeline.py
│   └── diff_ai_signals.py
├── examples/
│   ├── example-audit.md
│   └── ci/ai-act-diff.yml       # Exemple de workflow d'audit différentiel
└── tests/
    ├── README.md                # Procédure de test (automatique et par agent)
    ├── RESULTS.md               # Résultats réellement obtenus
    ├── run_tests.py
    ├── agent-runs/2026-10-27/   # Rapports bruts des audits par agent à l'aveugle
    └── fixtures/
        ├── demo-ai-vulnerable/  # EduAssist avec défauts volontaires + EXPECTED.md
        ├── demo-ai-secure/      # EduAssist corrigé + docs + EXPECTED.md
        ├── demo-no-ai/          # Projet sans IA (faux positifs) + EXPECTED.md
        ├── demo-insufficient-info/  # Contexte insuffisant + EXPECTED.md
        └── demo-adversarial/    # Documentation trompeuse, système hybride, marquage falsifiable
```

## Sources juridiques

Sources officielles (prévalent toujours) :

- Règlement (UE) 2024/1689 : <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Règlement (UE) 2026/1744 : <https://eur-lex.europa.eu/eli/reg/2026/1744/oj>
- AI Act Explorer de la Commission européenne : <https://ai-act-service-desk.ec.europa.eu/fr/ai-act-explorer>

Source complémentaire non officielle : <https://artificialintelligenceact.eu/fr/ai-act-explorer/>

Le détail des versions, des niveaux de confiance (`[TI]` texte initial, `[O26]` modifié par
2026/1744, `[AV]` à vérifier) et des divergences connues figure dans
[`references/legal-sources.md`](references/legal-sources.md).

**Vérification du 2026-10-27** : le règlement (UE) 2026/1744 (JO du 24.7.2026) et la version
consolidée 02024R1689-20260727 ont été **relus** à partir de Cellar (Office des publications).
Chaque entrée du calendrier cite l'extrait exact relu ; les empreintes des documents figurent dans
`data/official-sources.json`, et `python3 scripts/verify_official_extracts.py` rejoue la vérification
(22 extraits, 0 introuvable). Seule l'entrée CAL-016 (date effective de l'enregistrement de
l'art. 49, par. 2) reste « échéance à confirmer », pour une question d'interprétation.

## Limites

- **Audit statique** : comportement réel, données, prompts dynamiques, configuration de production
  et interfaces non observés ; aucun code n'est exécuté.
- **Pas de certification** : un contrôle « mesure présente » ne vaut pas « obligation satisfaite ».
- **Informations organisationnelles** (contrats, formation, finalités, dates de mise sur le marché)
  généralement hors dépôt : elles sont consignées comme éléments à vérifier.
- **Références datées** : le droit, les lignes directrices, les codes de bonnes pratiques et les
  normes harmonisées évoluent. Le calendrier a été relu sur le texte officiel le 2026-10-27 ; des
  points d'interprétation subsistent (`references/legal-sources.md`, section 5), et la version
  consolidée n'a pas de valeur juridique propre (seul le JO fait foi).
- **Périmètre** : AI Act uniquement. Les renvois à d'autres législations sont signalés sans être analysés.
- **Résultats d'agent non déterministes** : la qualité de l'audit dépend du modèle et du contexte
  fourni ; relire chaque rapport.
- Les instructions de lecture seule ne sont pas une garantie technique (voir ci-dessus).

## Procédure de test

```bash
python3 tests/run_tests.py
```

Les tests automatiques (bibliothèque standard et Git uniquement) vérifient la structure du skill,
le frontmatter, la complétude des bases juridiques et la règle bloquante, des scénarios calendaires,
le scanner sur les cinq fixtures (faux positifs, faux négatifs, chemins de sortie, masquage des
secrets, lecture seule), l'audit différentiel et le format des constats. **La réussite de ces tests
ne valide pas le contenu juridique** : elle ne lève jamais la mention « échéance à confirmer ». L'évaluation du raisonnement par un agent, à l'aveugle sur les fixtures, est décrite dans
[`tests/README.md`](tests/README.md) ; les résultats réellement obtenus sont consignés dans
[`tests/RESULTS.md`](tests/RESULTS.md).

## Maintenance

La veille juridique (trimestrielle et à chaque publication au JO) suit
[`references/maintenance.md`](references/maintenance.md) : vérification des actes modificatifs, des
versions consolidées, des lignes directrices et des actes délégués, mise à jour de
`data/ai-act-calendar.json` puis des références, exécution des tests et entrée au `CHANGELOG.md`.

## Contribution

Voir [`CONTRIBUTING.md`](CONTRIBUTING.md). Toute contribution juridique doit citer une référence
officielle vérifiable (ELI ou CELEX) ; aucune proposition non adoptée n'est intégrée comme droit positif.

## Licence

[MIT](LICENSE). Les extraits et résumés de textes de l'Union européenne restent soumis à la politique
de réutilisation des contenus de l'UE.
