# Sources juridiques, versions et statut de vérification

> Dernière vérification : **2026-10-27**. Responsable : mainteneurs du dépôt (voir `maintenance.md`).

## 1. Hiérarchie des sources

1. **Sources officielles (prévalent toujours)**
   - Règlement (UE) 2024/1689 du Parlement européen et du Conseil du 13 juin 2024 établissant des
     règles harmonisées concernant l'intelligence artificielle (AI Act), JO L, 2024/1689, 12.7.2024.
     - ELI : <http://data.europa.eu/eli/reg/2024/1689/oj>
     - EUR-Lex (FR) : <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689>
     - Lien indiqué par la mission : <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
   - Règlement (UE) 2026/1744 du Parlement européen et du Conseil du 8 juillet 2026 modifiant les
     règlements (UE) 2024/1689, (UE) 2018/1139 et (UE) 2023/1230 en ce qui concerne la simplification
     de la mise en œuvre des règles harmonisées en matière d'intelligence artificielle
     (« Digital Omnibus on AI »).
     - ELI : <http://data.europa.eu/eli/reg/2026/1744/oj>
     - EUR-Lex (FR) : <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1744>
   - AI Act Explorer et service desk de la Commission européenne :
     <https://ai-act-service-desk.ec.europa.eu/fr/ai-act-explorer>
     (articles au format `https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5`).
   - Lignes directrices et actes de la Commission (non contraignants pour les lignes directrices),
     publiés sur le site de la Commission et au JO.
2. **Source documentaire complémentaire, non officielle** : <https://artificialintelligenceact.eu/fr/ai-act-explorer/>
   (Future of Life Institute). Utile pour la navigation ; ne jamais la citer comme fondement unique.
3. **Commentaires** (cabinets, associations, éditeurs) : uniquement pour repérer une évolution à
   vérifier, jamais comme fondement d'un constat.

## 2. Versions retenues

| Texte | Version | Statut dans ce dépôt |
|---|---|---|
| Règlement (UE) 2024/1689 | Texte publié au JO le 12.7.2024 | Base. Dispositions non modifiées : confiance élevée. |
| Règlement (UE) 2026/1744 | Adopté le 8.7.2026, publié au JO le 24.7.2026, en vigueur le 27.7.2026 (selon les sources consultées) | Intégré. Confiance moyenne tant que le texte officiel n'a pas été relu. |
| Version consolidée EUR-Lex intégrant 2026/1744 | Non consultée | À consulter dès que possible ; selon une source, aucune version consolidée n'était encore publiée. |
| Propositions non adoptées | Exclues | Ne jamais intégrer une proposition comme droit applicable. |

## 3. Conditions de vérification du 2026-10-27 (transparence)

- EUR-Lex, l'AI Act Explorer de la Commission et artificialintelligenceact.eu étaient
  **inaccessibles depuis l'environnement de rédaction** (refus de la politique réseau). Aucun
  texte officiel n'a pu être relu en ligne ce jour-là.
- Les dispositions du **texte initial** reposent sur la connaissance du texte publié au JO,
  recoupée par recherche web.
- Les modifications du **règlement 2026/1744** reposent sur des **sources secondaires
  concordantes** obtenues par recherche web, notamment : White & Case, Freshfields, Cooley,
  Gibson Dunn, Cuatrecasas, Future of Privacy Forum, Lewis Silkin, Cloud Security Alliance,
  artificialintelligenceact.eu (page « Digital Omnibus »), ainsi que l'extrait du service desk de
  la Commission sur l'article 5 et le communiqué du Conseil du 29 juin 2026.
- Conséquence : toute disposition marquée `[O26]` ou `[AV]` doit être confirmée sur le JO avant
  un usage engageant. Ce point figure dans les limites de chaque rapport.

## 4. Marqueurs de confiance utilisés dans les références

| Marqueur | Signification | Usage dans un constat |
|---|---|---|
| `[TI]` | Texte initial 2024/1689, non modifié à notre connaissance. Confiance élevée. | Citer directement. |
| `[O26]` | Modifié ou introduit par 2026/1744, rapporté de manière concordante. Confiance moyenne. | Citer en précisant « selon le règlement 2026/1744, à confirmer sur le JO ». |
| `[AV]` | Sources divergentes, localisation incertaine ou point non vérifié. Confiance faible. | Ne fonder qu'un constat « À vérifier juridiquement ». |

## 4 bis. Statut de vérification et règle bloquante

Chaque entrée de `data/ai-act-calendar.json` porte un objet `legal_basis` : disposition exacte,
acte modificatif, date d'effet, conditions transitoires, URL officielle, `verification_status` et
`official_text_checked_on`.

| `verification_status` | Signification | Effet dans un audit |
|---|---|---|
| `officielle_relue` | Relue sur EUR-Lex ou le JO à la date `official_text_checked_on` | Conclusion temporelle sans réserve |
| `texte_initial_non_relu` | Texte initial stable, non relu en ligne lors de la dernière vérification | Conclusion admise, source citée |
| `sources_secondaires` | Issue de 2026/1744 via des commentaires concordants | **Bloquante** : « échéance à confirmer », conclusion temporelle conditionnelle |
| `incertaine` | Sources divergentes ou disposition non localisée | **Bloquante** : idem |

Au 2026-10-27, **aucune** entrée n'a le statut `officielle_relue` (textes officiels inaccessibles).
Les tests (`tests/run_tests.py`) refusent qu'une entrée soit marquée `officielle_relue` sans date de
relecture, ou qu'une entrée issue de 2026/1744 échappe à la règle bloquante sans relecture officielle.

## 5. Points de divergence ou d'incertitude connus (2026-10-27)

| Sujet | Divergence | Traitement |
|---|---|---|
| Art. 111, par. 2 : échéance pour les systèmes destinés aux autorités publiques | 2 août 2030 (plusieurs sources) contre 28 janvier 2028 (une source) | `[AV]` ; retenir 2030 avec confiance faible et signaler. |
| Art. 111, par. 2 : date de référence pour les systèmes antérieurs | Devient la date d'application du chapitre III (2.12.2027 annexe III, 2.8.2028 annexe I) selon une source | `[AV]`. |
| Numérotation des nouvelles interdictions de l'art. 5 | Points (ba) et (bb) selon une source | `[O26]` pour le contenu, `[AV]` pour la numérotation. |
| Art. 49, par. 2 : enregistrement des systèmes annexe III jugés non à haut risque | Maintenu avec procédure simplifiée selon les sources ; date effective non établie | `[AV]`. |
| Art. 50, par. 2 appliqué aux textes conversationnels | Dépend des lignes directrices de la Commission du 20.7.2026 (C(2026) 5054 selon les sources) | `[AV]` sur les modalités. |
| Annexe I : déplacement des machines de la section A vers la section B | Rapporté par une source | `[AV]`. |
| Art. 4 : date d'application de la nouvelle rédaction | Entrée en vigueur du règlement 2026/1744 présumée | `[O26]`. |

## 6. Documents d'orientation de la Commission à connaître (non contraignants)

| Document | Date (selon sources) | Statut |
|---|---|---|
| Lignes directrices sur la définition de système d'IA (art. 3, point 1) | Février 2025 | Publiées |
| Lignes directrices sur les pratiques interdites (art. 5) | Février 2025 | Publiées ; mise à jour éventuelle après 2026/1744 à vérifier |
| Lignes directrices sur le champ des obligations des fournisseurs de modèles GPAI | Juillet 2025 | Publiées |
| Code de bonnes pratiques GPAI | Juillet 2025 | Publié |
| Code de bonnes pratiques sur le marquage et l'étiquetage des contenus générés par IA | 10.6.2026 | Publié (volontaire) |
| Lignes directrices sur l'article 50 | 20.7.2026 | Publiées selon les sources |
| Lignes directrices sur la classification à haut risque (art. 6, par. 5) | Projet du 19.5.2026 | Projet ; version finale attendue fin 2026 |

Ces dates proviennent de recherches web du 2026-10-27 et doivent être confirmées sur le site de la
Commission avant d'être citées dans un rapport.
