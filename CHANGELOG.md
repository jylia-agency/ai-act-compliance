# Journal des modifications

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) ; versions selon
[SemVer](https://semver.org/lang/fr/). Chaque version indique la base juridique et la date de
vérification des références.

## [1.2.0] - 2026-10-27

Première version dont le calendrier juridique est **relu sur le texte officiel**.

### Textes et sources consultés (2026-10-27)
- Règlement (UE) 2026/1744 du 8.7.2026, JO L du 24.7.2026, version française (CELEX 32026R1744).
- Version consolidée du règlement (UE) 2024/1689 au 27.7.2026 (CELEX 02024R1689-20260727).
- Récupération depuis Cellar (Office des publications) ; empreintes SHA-256 dans
  `data/official-sources.json` ; EUR-Lex servait une vérification anti-robot.
- Point SPARQL public de l'Office des publications (veille) : premier passage réel.

### Modifié
- Calendrier : 15 entrées sur 16 au statut `officielle_relue`, avec l'extrait exact et la disposition
  modificative (art. 1, points 5, 7, 39, 40, 41 et 42, et art. 4 du règlement 2026/1744).
- CAL-013 levée : art. 111, par. 2 confirmé (importantes modifications de la conception ; autorités
  publiques au **2 août 2030**) ; la date du 28 janvier 2028 rapportée par une source secondaire est infirmée.
- CAL-010 : délai inscrit à l'**art. 111, par. 4**, qui vise expressément les contenus « audio,
  image, vidéo ou texte », y compris pour les systèmes d'IA à usage général.
- CAL-016 reste bloquante : art. 49, par. 2 non modifié, annexe VIII, section B allégée (points 7 et
  9 supprimés), date effective non fixée par le texte.
- Art. 5 : texte officiel des points b bis) et b ter) et des par. 1 bis et 1 ter (côté fournisseur,
  interdiction liée à la destination ou à un résultat raisonnablement prévisible et reproductible
  **en l'absence de garde-fous raisonnables et adéquats**).
- Classification : définition remplacée du composant de sécurité (art. 3, point 14), nouveaux
  par. 1 bis à 1 quater de l'art. 6, machines déplacées en annexe I, section B.
- Art. 10, par. 5 supprimé et remplacé par l'art. 4 bis (mention, analyse hors périmètre) ;
  documentation simplifiée étendue aux petites entreprises à moyenne capitalisation (art. 11).
- Fixtures `EXPECTED.md` et exemple de rapport alignés (plus de réserve sur CAL-013).

### Ajouté
- `scripts/verify_official_extracts.py` : relecture reproductible (22 extraits vérifiés, 0 introuvable).
- `data/official-sources.json` : documents officiels relus et empreintes.
- Veille : filtre du bruit (consolidations d'autres actes) et référentiel revu des 27 actes remontés
  (rectificatifs, actes d'exécution 2025/454 et 2026/1755, propositions exclues).

## [1.1.1] - 2026-10-27

Version de fiabilisation, sans nouvelle fonctionnalité d'audit. Base juridique inchangée ; statut
de vérification des sources renforcé.

### Ajouté
- Statut de vérification `officielle_extraits` : extrait textuel du texte officiel (JO du 24.7.2026
  ou version consolidée 02024R1689-20260727 sur EUR-Lex) recopié avec son URL dans
  `data/ai-act-calendar.json` (`official_extracts`), et confirmations externes consignées à part
  (`external_confirmations`).
- `references/official-verification-worksheet.md` : fiche de levée des réserves, entrée par entrée.
- Veille automatisée des sources : `scripts/check_legal_updates.py`, `data/legal-watch.json` et
  `.github/workflows/legal-watch.yml` (détection mensuelle des actes liés au règlement et rappel
  trimestriel ; ouverture d'issues de revue humaine, aucune règle modifiée automatiquement).
- Test d'intégration Claude Code (CLI) : découverte, déclenchement automatique, lecture seule
  (`tests/agent-runs/2026-10-27-v1.1.1/`).
- `ConsistencyTests` : version de `SKILL.md` alignée sur le CHANGELOG, en-tête de `tests/RESULTS.md`
  aligné sur la version et le nombre de tests. 58 tests automatiques.

### Modifié
- Calendrier : CAL-003, CAL-004, CAL-010, CAL-011, CAL-012 et CAL-015 confirmées par extraits
  officiels (plus de mention « échéance à confirmer ») ; CAL-013 (art. 111, par. 2, autorités
  publiques) et CAL-016 (art. 49, par. 2) restent bloquantes.
- Art. 5 : numérotation des nouvelles interdictions confirmée (points (ba) et (bb), par. 1 bis et
  1 ter) et conditions côté fournisseur et côté déployeur ajoutées.
- Art. 4 : libellé officiel (« prennent des mesures pour favoriser le développement de la maîtrise
  de l'IA »).
- `references/legal-sources.md` : existence de la version consolidée du 27.7.2026, conditions de
  vérification, état par entrée.
- `tests/RESULTS.md` réorganisé : état de la version courante en tête, historique ensuite.
- Fixtures `EXPECTED.md` et exemple de rapport alignés sur le nouveau statut des échéances.

### Textes et sources consultés (2026-10-27)
- Règlement (UE) 2026/1744 (JO L du 24.7.2026) et version consolidée 02024R1689-20260727 : extraits
  obtenus par recherche restreinte au domaine eur-lex.europa.eu (accès direct refusé).
- Revue externe transmise par l'utilisateur, indiquant avoir lu sur EUR-Lex les échéances du
  2.12.2026, 2.12.2027 et 2.8.2028.

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
