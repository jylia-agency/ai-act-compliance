# Procédure de maintenance juridique

> Dernière exécution complète : **2026-10-27** (partielle : textes officiels inaccessibles depuis
> l'environnement de rédaction, voir `legal-sources.md`, section 3).

## 1. Fréquence

- **Trimestrielle** : revue de veille (section 3).
- **Immédiate** : à la publication au JO d'un acte modifiant le règlement, d'un acte délégué
  (notamment modification de l'annexe III, art. 7), d'un acte d'exécution, de lignes directrices ou
  d'un code de bonnes pratiques.
- **Avant chaque version majeure** du skill : revue complète (section 4).

## 1 bis. Veille automatisée (complément, jamais substitut)

`.github/workflows/legal-watch.yml` exécute chaque mois `scripts/check_legal_updates.py`, qui
interroge le point SPARQL public de l'Office des publications pour lister les actes liés au
règlement (modificatifs, rectificatifs, consolidations, actes fondés sur lui) et les compare à
`data/legal-watch.json`. Tout acte inconnu, ou un échec de la requête, ouvre une issue de **revue
humaine**. Une issue de rappel est aussi ouverte chaque trimestre. Le script ne modifie aucune règle ;
après revue, un humain met à jour `known_celex` et, si nécessaire, le calendrier (section 4) en
suivant `official-verification-worksheet.md`.

Limite : la requête SPARQL n'a pas pu être testée contre le service réel depuis l'environnement de
rédaction (accès réseau refusé) ; seule l'analyse d'une réponse fictive est testée. Le premier
passage du workflow doit être surveillé : un échec ouvre une issue dédiée.

## 2. Sources à surveiller

| Source | Objet |
|---|---|
| EUR-Lex, page du règlement 2024/1689 (onglet « Informations sur le document », liens modificatifs) | Actes modificatifs, rectificatifs, versions consolidées |
| EUR-Lex, règlement 2026/1744 | Texte définitif des modifications |
| AI Act Explorer et service desk de la Commission | Texte navigable, FAQ |
| Pages de la Commission sur l'AI Act (AI Office) | Lignes directrices, codes de bonnes pratiques, modèles |
| JO, série L | Actes délégués et d'exécution |
| Normes harmonisées (CEN-CENELEC JTC 21) | Présomption de conformité |
| artificialintelligenceact.eu (non officiel) | Repérage, jamais fondement |

## 3. Revue de veille (checklist)

- [ ] Rechercher tout nouvel acte modifiant le règlement 2024/1689 depuis la dernière vérification.
- [ ] Vérifier l'existence d'une version consolidée intégrant 2026/1744.
- [ ] Relire sur le texte officiel chaque entrée de confiance `moyenne` ou `faible` de
      `data/ai-act-calendar.json` ; relever la confiance si confirmée.
- [ ] Résoudre les divergences listées dans `legal-sources.md`, section 5.
- [ ] Vérifier les lignes directrices publiées (classification à haut risque définitive, art. 50,
      pratiques interdites mises à jour).
- [ ] Vérifier les modifications éventuelles de l'annexe III par acte délégué.
- [ ] Vérifier qu'aucune **proposition** non adoptée n'a été intégrée comme droit positif.

## 4. Mise à jour du dépôt

1. Modifier `data/ai-act-calendar.json` (source machine) : date, articles, `source_url`,
   `confidence`, `verified_on`, `notes` et l'objet `legal_basis`. Après relecture effective sur
   EUR-Lex : `verification_status` = `officielle_relue`, `official_text_checked_on` = date de
   relecture, disposition exacte de l'acte modificatif dans `amending_act`, confiance relevée.
2. Répercuter dans `references/applicability-calendar.md` (même identifiant `CAL-NNN`).
3. Mettre à jour les références concernées, leur en-tête « Dernière vérification » et les marqueurs
   `[TI]`, `[O26]`, `[AV]`.
4. Mettre à jour `metadata.legal-references-last-verified` dans `SKILL.md` et `meta.last_verified`
   dans le JSON.
5. Mettre à jour les fixtures `EXPECTED.md` si un résultat attendu change (par exemple une date).
6. Exécuter `python3 tests/run_tests.py`.
7. Documenter dans `CHANGELOG.md` : textes consultés (référence, version, date de consultation),
   changements, impacts sur les audits antérieurs.

## 5. Règles

- Une modification juridique n'est intégrée qu'avec une référence officielle vérifiable (ELI ou
  CELEX) ; à défaut, marqueur `[AV]` et confiance `faible`.
- Ne jamais supprimer l'historique d'une date modifiée : conserver `previous_date` dans le JSON.
- Les audits produits avant une mise à jour restent datés : en cas de changement significatif,
  recommander un ré-audit.
