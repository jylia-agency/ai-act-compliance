# Journal des modifications

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) ; versions selon
[SemVer](https://semver.org/lang/fr/). Chaque version indique la base juridique et la date de
vérification des références.

## [1.1.0] - 2026-10-27

Suite à une revue externe de la version 1.0.0. Base juridique inchangée ; textes officiels toujours
non relus (accès refusé), d'où le renforcement de la règle bloquante.

### Ajouté
- `legal_basis` pour chaque entrée du calendrier (disposition, acte modificatif, date d'effet,
  conditions transitoires, URL officielle, `verification_status`, `official_text_checked_on`).
- Règle bloquante : `requires_confirmation` et mention « échéance à confirmer » pour toute échéance
  issue de sources secondaires ou incertaines (script, `SKILL.md`, modèles, exemple).
- `references/transparency.md` : trois notions distinguées (interaction, marquage machine, mention
  visible) et module d'audit des chemins de sortie de l'art. 50, par. 2.
- `references/person-decisions.md` : échelle des scénarios, questions obligatoires, effectivité du
  contrôle humain, systèmes hybrides.
- `templates/data-flow-map.md` : chaînes de traitement, matrice fonctionnalités / modèles, marquage par chemin de sortie.
- Matrice de preuves à quatre états et preuves `PRV-NNN` rejouables.
- `scripts/diff_ai_signals.py` (audit différentiel en lecture seule) et `examples/ci/ai-act-diff.yml`.
- Scanner : catégorie `output_channel`, signaux d'orientation et de profilage.
- Fixture `demo-adversarial` ; 50 tests automatiques ; évaluation à l'aveugle multi-modèles.

### Modifié
- Textes conversationnels : analysés au titre de l'art. 50, par. 2 comme tout contenu ; une
  incertitude de modalités n'est jamais une exemption (correction d'une règle de la 1.0.0 qui
  pouvait produire des faux négatifs).
- Checklists : états Démontré / Non démontré / Non applicable / Impossible à vérifier.
- Oracles `EXPECTED.md` mis à jour en conséquence.

## [1.0.0] - 2026-10-27

Base juridique : règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744.
Références vérifiées le 2026-10-27 (texte officiel non relu en ligne : voir ci-dessous).

### Ajouté
- `SKILL.md` (`name: ia-compliance`) : méthodologie d'audit en 12 phases, règles de lecture seule,
  classification des constats, livrables, règles impératives, limites.
- 17 références datées dans `references/` (vue d'ensemble, sources, calendrier, rôles, détection,
  article 5, classification, fournisseurs, déployeurs, GPAI, article 50, supervision humaine,
  documentation technique, éducation, checklists A à G, méthodologie des constats, maintenance).
- Calendrier juridique machine `data/ai-act-calendar.json` (16 entrées sourcées, niveau de confiance
  par entrée).
- Scripts en lecture seule : `scan_ai_signals.py` (signaux d'IA, secrets masqués, exclusions) et
  `obligation_timeline.py` (statut temporel selon la date d'audit et la date de mise sur le marché).
- Six modèles de livrables dans `templates/` et un rapport d'exemple complet.
- Quatre fixtures de test avec `EXPECTED.md` et suite `tests/run_tests.py` (38 tests).
- Évaluation par agent à l'aveugle sur les quatre fixtures (rapports bruts dans
  `tests/agent-runs/2026-10-27/`, analyse dans `tests/RESULTS.md`).

### Modifié (après l'évaluation par agent)
- `SKILL.md` : traitement des projets sans IA, usage restreint de la nature « Non applicable »,
  qualification « À vérifier » pour les portées juridiques incertaines.
- `references/transparency.md` : métadonnées non standard et marquage des textes conversationnels.
- Oracles `EXPECTED.md` de `demo-no-ai` et `demo-ai-secure` précisés.

### Textes et sources consultés
- Règlement (UE) 2024/1689 (JO L, 2024/1689, 12.7.2024) : connaissance du texte publié, recoupée
  par recherche web le 2026-10-27.
- Règlement (UE) 2026/1744 du 8.7.2026 (publication au JO le 24.7.2026, entrée en vigueur le
  27.7.2026 selon les sources) : sources secondaires concordantes consultées le 2026-10-27.
- EUR-Lex, AI Act Explorer et artificialintelligenceact.eu : **inaccessibles** depuis
  l'environnement de rédaction le 2026-10-27 (politique réseau).

### Points à confirmer (voir `references/legal-sources.md`, section 5)
- Article 111, paragraphe 2, après 2026/1744 : date de référence et échéance pour les autorités publiques.
- Numérotation des nouvelles interdictions de l'article 5.
- Date effective de l'enregistrement de l'article 49, paragraphe 2.
- Portée de l'article 50, paragraphe 2, pour les textes conversationnels.
