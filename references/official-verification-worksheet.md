# Fiche de vérification officielle des échéances

> Objet : permettre à une personne disposant d'un accès à EUR-Lex de lever, entrée par entrée, la
> mention « échéance à confirmer ». Dernière vérification : **2026-10-27** (texte officiel relu à cette
> date : 15 entrées levées, CAL-016 reste bloquante pour une question d'interprétation).
> Sources à consulter : [règlement (UE) 2026/1744](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1744),
> [règlement (UE) 2024/1689 et ses versions consolidées](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer](https://ai-act-service-desk.ec.europa.eu/fr/ai-act-explorer).

## 0. Résultat de la relecture du 2026-10-27

Textes relus : règlement (UE) 2026/1744 (JO L du 24.7.2026, FR) et version consolidée
02024R1689-20260727, récupérés depuis Cellar (empreintes : `data/official-sources.json`).
Reproduction : `python3 scripts/verify_official_extracts.py` (22 extraits vérifiés, 0 introuvable).

| ID | Résultat | Disposition exacte |
|---|---|---|
| CAL-003 | Confirmé | Art. 4 remplacé par le règlement 2026/1744, art. 1, point 5 |
| CAL-004 | Confirmé (points b bis et b ter, par. 1 bis et 1 ter) | Art. 1, points 7 et 40 |
| CAL-010 | Confirmé ; délai inscrit à l'art. 111, par. 4 (textes inclus) | Art. 1, point 39 |
| CAL-011 | Confirmé : 2.12.2027 | Art. 113, al. 3, c) i), modifié par l'art. 1, point 40 |
| CAL-012 | Confirmé : 2.8.2028 ; machines déplacées en annexe I, section B | Art. 113, al. 3, c) ii) ; art. 1, point 41 |
| CAL-013 | Confirmé : importantes modifications de la conception ; autorités publiques au 2.8.2030 (la date du 28.1.2028 est infirmée) | Art. 111, par. 2, remplacé par l'art. 1, point 39, a) |
| CAL-015 | Confirmé : entrée en vigueur au 27.7.2026 | Règlement 2026/1744, art. 4 |
| CAL-016 | Textes relus, date effective non fixée par le texte : **reste bloquante** | Art. 49, par. 2 (non modifié) ; annexe VIII, section B (art. 1, point 42) |

Rectificatifs examinés le 2026-10-27 : seul 32024R1689R(01) existe en français (coquille de
l'art. 10, par. 2) ; R(02) à R(04) ne visent que d'autres langues. Sans effet.

Reste à faire : trancher l'interprétation de CAL-016 (avis juridique) ; relire les lignes
directrices de la Commission.

## 1. Mode opératoire

1. Ouvrir le texte du règlement 2026/1744 au JO (version française) et, si elle existe, la version
   consolidée du règlement 2024/1689 intégrant cette modification.
2. Pour chaque ligne du tableau, lire la disposition indiquée et remplir les trois dernières
   colonnes : disposition exacte de l'acte modificatif, date confirmée ou corrigée, nom et date du
   relecteur.
3. Reporter le résultat dans `data/ai-act-calendar.json` :
   - date confirmée : `legal_basis.verification_status` = `officielle_relue`,
     `legal_basis.official_text_checked_on` = date de relecture, `legal_basis.amending_act` =
     disposition exacte, `confidence` = `elevee` ;
   - date différente : corriger `date` et `legal_basis.effective_date`, puis appliquer la même mise à jour ;
   - disposition introuvable : laisser `incertaine` et décrire le problème dans `notes`.
4. Répercuter dans `references/applicability-calendar.md`, les références concernées, les fixtures
   `EXPECTED.md` si un résultat attendu change, puis exécuter `python3 tests/run_tests.py`.
5. Consigner la relecture dans `CHANGELOG.md` (textes consultés, version, date).

Les tests refusent une entrée `officielle_relue` sans date de relecture : la levée de la réserve
est donc toujours datée et traçable.

## 2. Entrées à vérifier

| ID | Statut au 2026-10-27 | Obligation | Disposition visée | Date actuellement retenue | Point précis à confirmer | Disposition exacte (à remplir) | Date confirmée (à remplir) | Relecteur et date (à remplir) |
|---|---|---|---|---|---|---|---|---|
| CAL-003 | `officielle_extraits` | Article 4 (maîtrise de l'IA) dans sa rédaction issue du règlement (UE) 2026/1744 | Art. 4 (nouvelle rédaction) | 2026-07-27 | Localiser la disposition de 2026/1744 qui remplace l'art. 4 ; recopier la nouvelle rédaction ; vérifier sa date d'application propre (entrée en vigueur ou date différée). | | | |
| CAL-004 | `officielle_extraits` | Nouvelles pratiques interdites insérées à l'article 5, paragraphe 1 (contenus intimes non consentis, matériel d'abus sexuel sur enfants) | Art. 5, par. 1, nouveaux points (ba) et (bb) (numérotation à confirmer) | 2026-12-02 | Localiser l'insertion des nouvelles interdictions à l'art. 5, par. 1 ; confirmer la numérotation ((ba), (bb) ?), le libellé exact, les conditions (consentement, caractère réaliste, personnes identifiables) et la date d'application (2026-12-02 ?). | | | |
| CAL-010 | `officielle_extraits` | Article 50, paragraphe 2 : marquage lisible par machine et détectabilité des contenus synthétiques (fournisseurs) | Art. 50, par. 2 ; disposition transitoire insérée par 2026/1744 | 2026-08-02 | Localiser la disposition transitoire relative à l'art. 50, par. 2 ; confirmer la date limite (2026-12-02 ?), le critère (mise sur le marché avant le 2026-08-02 ?) et son champ (tous contenus, y compris textes ?). | | | |
| CAL-011 | `officielle_extraits` | Systèmes d'IA à haut risque relevant de l'annexe III (art. 6, par. 2) : exigences et obligations du chapitre III, sections 1 à 3 | Art. 113 modifié ; art. 6, par. 2 ; chapitre III, sections 1 à 3 | 2027-12-02 | Lire l'art. 113 consolidé : confirmer la date d'application des exigences du chapitre III, sections 1 à 3, pour l'annexe III (2027-12-02 ?) et le sort de l'art. 6, par. 5. | | | |
| CAL-012 | `officielle_extraits` | Systèmes d'IA à haut risque relevant de l'annexe I (art. 6, par. 1) et obligations correspondantes | Art. 113 modifié ; art. 6, par. 1 ; annexe I | 2028-08-02 | Lire l'art. 113 consolidé : confirmer la date pour l'art. 6, par. 1 et l'annexe I (2028-08-02 ?) ; vérifier le déplacement éventuel des machines en section B de l'annexe I. | | | |
| CAL-013 | `sources_secondaires` (bloquante) | Systèmes à haut risque déjà mis sur le marché ou mis en service avant la date d'application du chapitre III | Art. 111, par. 2 (rédaction modifiée) | 2027-12-02 | Lire l'art. 111, par. 2 consolidé : date de référence (date d'application du chapitre III ?), notion de modification importante, échéance pour les autorités publiques (2030-08-02 ou 2028-01-28 ?) ; lire le considérant 39 (type et modèle). | | | |
| CAL-015 | `officielle_extraits` | Entrée en vigueur du règlement (UE) 2026/1744 (Digital Omnibus on AI) | Règlement (UE) 2026/1744, disposition finale (entrée en vigueur) | 2026-07-27 | Confirmer la date d'adoption, la référence de publication au JO et la date d'entrée en vigueur du règlement 2026/1744. | | | |
| CAL-016 | `incertaine` (bloquante) | Enregistrement dans la base de données de l'UE des systèmes de l'annexe III que le fournisseur estime non à haut risque (art. 6, par. 3 et 4) | Art. 6, par. 4 ; art. 49, par. 2 ; annexe VIII, section B | non établie | Lire l'art. 49, par. 2 et l'annexe VIII, section B consolidés : maintien de l'enregistrement, contenu réduit, date d'application effective. | | | |

## 3. Entrées du texte initial (non bloquantes)

Les entrées de statut `texte_initial_non_relu` (CAL-001, CAL-002, CAL-005 à CAL-009, CAL-014)
reposent sur des dispositions stables du texte de 2024. Leur relecture est recommandée lors de la
même session (art. 111 et 113, art. 50), en vérifiant aussi qu'aucune n'a été modifiée par le
règlement 2026/1744.
