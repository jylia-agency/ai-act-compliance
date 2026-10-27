# Journal des modifications

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) ; versions selon
[SemVer](https://semver.org/lang/fr/). Chaque version indique la base juridique et la date de
vérification des références.

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
- Évaluation par agent à l'aveugle documentée dans `tests/RESULTS.md`.

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
