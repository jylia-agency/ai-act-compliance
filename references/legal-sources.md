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
| Règlement (UE) 2026/1744 | Adopté le 8.7.2026, publié au JO L du 24.7.2026, en vigueur le 27.7.2026 (art. 4 : entrée en vigueur le troisième jour suivant la publication ; extrait officiel) | Intégré. Dates principales confirmées par extraits officiels (voir section 4 bis). |
| Version consolidée du règlement 2024/1689 au 27.7.2026 | CELEX 02024R1689-20260727 ([FR](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:02024R1689-20260727), [EN](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727)) | Publiée sur EUR-Lex ; consultée par extraits le 2026-10-27. Les versions consolidées n'ont pas de valeur juridique propre : seul le JO fait foi. |
| Proposition COM(2025) 836 | Proposition de la Commission du 19.11.2025 | Exclue : plusieurs dates diffèrent du texte adopté (par exemple délai de l'art. 50, par. 2 proposé au 2 février 2027, retenu au 2 décembre 2026). |

## 3. Conditions de vérification du 2026-10-27 (transparence)

- L'accès **direct** à EUR-Lex, à l'AI Act Explorer et à artificialintelligenceact.eu était refusé
  par la politique réseau de l'environnement de rédaction.
- Le texte officiel a été consulté **par extraits** : recherche restreinte au domaine
  `eur-lex.europa.eu`, qui a restitué des passages du règlement 2026/1744 (JO, versions FR et EN) et
  de la version consolidée 02024R1689-20260727. Chaque extrait utilisé est recopié dans
  `data/ai-act-calendar.json` (`official_extracts`) avec son URL. Il ne s'agit pas d'une relecture
  intégrale de l'acte.
- Une **revue externe** (assistant ChatGPT, transmise par l'utilisateur le 2026-10-27) indique avoir
  consulté le règlement 2026/1744 sur EUR-Lex et y avoir trouvé les échéances du 2 décembre 2026
  (art. 50, par. 2), du 2 décembre 2027 (annexe III) et du 2 août 2028 (annexe I). Elle est
  consignée comme confirmation concordante (`external_confirmations`), pas comme preuve autonome.
- Les dispositions du **texte initial** reposent sur la connaissance du texte publié au JO,
  recoupée par recherche web.
- Sources secondaires consultées pour le repérage : White & Case, Freshfields, Cooley, Gibson Dunn,
  Cuatrecasas, Future of Privacy Forum, Lewis Silkin, Cloud Security Alliance,
  artificialintelligenceact.eu (page « Digital Omnibus »), service desk de la Commission, Conseil.

## 4. Marqueurs utilisés dans les références

| Marqueur | Signification | Usage dans un constat |
|---|---|---|
| `[TI]` | Texte initial 2024/1689, non modifié à notre connaissance. | Citer directement. |
| `[O26]` | Introduit ou modifié par 2026/1744. Le statut de vérification de chaque date est celui de son entrée `CAL-NNN`. | Citer avec la référence calendaire ; ajouter « échéance à confirmer » si l'entrée est bloquante. |
| `[AV]` | Sources divergentes, localisation incertaine ou point non vérifié. | Ne fonder qu'un constat « À vérifier juridiquement ». |

## 4 bis. Statut de vérification et règle bloquante

Chaque entrée de `data/ai-act-calendar.json` porte un objet `legal_basis` : disposition exacte,
acte modificatif, date d'effet, conditions transitoires, URL officielle, `verification_status`,
`official_text_checked_on` et, le cas échéant, `official_extracts` et `external_confirmations`.

| `verification_status` | Signification | Effet dans un audit |
|---|---|---|
| `officielle_relue` | Relue intégralement sur EUR-Lex ou le JO à la date `official_text_checked_on` | Conclusion temporelle sans réserve |
| `officielle_extraits` | Confirmée par un extrait textuel officiel cité (`official_extracts`), sans relecture intégrale | Conclusion admise, extrait et source cités |
| `texte_initial_non_relu` | Texte initial stable, non relu en ligne lors de la dernière vérification | Conclusion admise, source citée |
| `sources_secondaires` | Issue de 2026/1744 sans extrait officiel textuel | **Bloquante** : « échéance à confirmer », conclusion temporelle conditionnelle |
| `incertaine` | Sources divergentes ou disposition non localisée | **Bloquante** : idem |

État au 2026-10-27 :

| Entrée | Statut | Fondement |
|---|---|---|
| CAL-003 (art. 4, nouvelle rédaction) | `officielle_extraits` | Extrait FR et EN du règlement 2026/1744 |
| CAL-004 (nouvelles interdictions, 2.12.2026) | `officielle_extraits` | Extrait EN de l'art. 113, troisième alinéa, point a), modifié |
| CAL-010 (délai de l'art. 50, par. 2 au 2.12.2026) | `officielle_extraits` | Extrait FR de la version consolidée ; revue externe concordante |
| CAL-011 (annexe III, 2.12.2027) et CAL-012 (annexe I, 2.8.2028) | `officielle_extraits` (confiance moyenne) | Extrait FR d'un considérant ; disposition opérationnelle (art. 113 modifié) non citée textuellement ; revue externe concordante |
| CAL-015 (entrée en vigueur, 27.7.2026) | `officielle_extraits` | Extrait FR de l'art. 4 du règlement 2026/1744 |
| CAL-013 (art. 111, par. 2) | `sources_secondaires`, **bloquante** | Condition de modification importante confirmée par extrait ; échéance du 2.8.2030 pour les autorités publiques sans extrait textuel |
| CAL-016 (art. 49, par. 2) | `incertaine`, **bloquante** | Aucun extrait officiel |

Aucune entrée n'a encore le statut `officielle_relue`. Les tests refusent une entrée
`officielle_relue` sans date de relecture, une entrée `officielle_extraits` sans extrait cité, et
toute entrée issue de 2026/1744 qui échapperait à la règle bloquante sans l'un de ces deux statuts.

## 5. Points de divergence ou d'incertitude connus (2026-10-27)

| Sujet | État | Traitement |
|---|---|---|
| Art. 111, par. 2 : échéance pour les systèmes destinés aux autorités publiques | 2 août 2030 rapporté par une recherche sur EUR-Lex et par plusieurs sources, sans extrait textuel ; la date du 28 janvier 2028 citée par une source n'a pas été retrouvée | `[AV]`, bloquant |
| Art. 111, par. 2 : date de référence pour les systèmes antérieurs | Condition « importantes modifications de leurs conceptions » confirmée par extrait ; rattachement à la date d'application du chapitre III rapporté | `[AV]` sur la date de référence |
| Nouvelles interdictions de l'art. 5 | Points (ba) et (bb) et par. 1 bis et 1 ter confirmés par extrait (art. 113 modifié) ; conditions côté fournisseur et côté déployeur rapportées par la version consolidée | Libellé exact des par. 1 bis et 1 ter à relire |
| Art. 49, par. 2 : enregistrement des systèmes annexe III jugés non à haut risque | Maintenu avec contenu réduit selon des sources secondaires ; aucun extrait officiel | `[AV]`, bloquant |
| Art. 50, par. 2 appliqué aux textes conversationnels | Le paragraphe vise les textes ; seules les modalités dépendent des lignes directrices du 20.7.2026 | Pas d'exemption ; modalités `[AV]` |
| Annexe I : déplacement des machines de la section A vers la section B | Rapporté par une source | `[AV]` |

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
