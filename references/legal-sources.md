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
| Règlement (UE) 2024/1689 | Texte publié au JO le 12.7.2024 ; rectificatifs 32024R1689R(01) à R(04) recensés | Base. |
| Règlement (UE) 2026/1744 | Adopté le 8.7.2026, publié au JO L du 24.7.2026, en vigueur le 27.7.2026 (art. 4) | **Texte officiel relu le 2026-10-27** (version française). |
| Version consolidée au 27.7.2026 | CELEX 02024R1689-20260727 ([FR](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:02024R1689-20260727)) | **Relue le 2026-10-27**. Outil de documentation sans effet juridique : en cas de doute, seul le JO fait foi. |
| Actes d'exécution | Règlement d'exécution (UE) 2025/454 (groupe scientifique) ; règlement d'exécution (UE) 2026/1755 (procédures de la Commission) | Recensés par la veille ; sans obligation nouvelle pour les systèmes audités. |
| Propositions | COM(2025) 836 (adoptée sous la forme de 2026/1744) ; COM(2025) 1023 (dispositifs médicaux, vise aussi l'AI Act) | Exclues : jamais intégrées comme droit applicable. COM(2025) 1023 à surveiller (annexe I). |

## 3. Conditions de vérification du 2026-10-27 (transparence)

- Le texte officiel a été **relu** à partir de Cellar, le référentiel de l'Office des publications
  de l'Union européenne (`https://publications.europa.eu/resource/celex/<CELEX>`, négociation de
  contenu en français). EUR-Lex servait une vérification anti-robot (HTTP 202 sans contenu).
- Documents relus, avec leur empreinte SHA-256 : `data/official-sources.json`.
- Chaque entrée du calendrier cite l'extrait exact relu (`official_extracts`). Le script
  `scripts/verify_official_extracts.py` retélécharge les documents et vérifie que chaque extrait y
  figure mot pour mot : **22 extraits vérifiés, 0 introuvable** le 2026-10-27.
- Une revue externe (assistant ChatGPT, transmise par l'utilisateur) avait indiqué les échéances du
  2.12.2026, 2.12.2027 et 2.8.2028 : confirmées par la relecture.
- Les sources secondaires (White & Case, Freshfields, Cooley, Gibson Dunn, Cuatrecasas, FPF, Lewis
  Silkin, Cloud Security Alliance, artificialintelligenceact.eu) n'ont servi qu'au repérage. Une
  date qu'elles rapportaient (28 janvier 2028 pour les autorités publiques) est **infirmée** par le
  texte officiel (2 août 2030).

## 4. Marqueurs utilisés dans les références

| Marqueur | Signification | Usage dans un constat |
|---|---|---|
| `[TI]` | Texte initial 2024/1689, non modifié par 2026/1744 (relu le 2026-10-27). | Citer directement. |
| `[O26]` | Introduit ou modifié par 2026/1744 (relu le 2026-10-27). | Citer avec la référence calendaire. |
| `[AV]` | Point d'**interprétation** non tranché par le texte, ou orientation non contraignante non relue. | Ne fonder qu'un constat « À vérifier juridiquement ». |

## 4 bis. Statut de vérification et règle bloquante

Chaque entrée de `data/ai-act-calendar.json` porte un objet `legal_basis` : disposition exacte,
acte modificatif, date d'effet, conditions transitoires, URL officielle, `verification_status`,
`official_text_checked_on` et `official_extracts`.

| `verification_status` | Signification | Effet dans un audit |
|---|---|---|
| `officielle_relue` | Relue sur le texte officiel à la date `official_text_checked_on`, extrait cité | Conclusion temporelle sans réserve |
| `officielle_extraits` | Confirmée par un extrait officiel sans relecture de l'acte | Conclusion admise, extrait cité |
| `texte_initial_non_relu` | Texte initial stable, non relu | Conclusion admise, source citée |
| `sources_secondaires` | Sans extrait officiel | **Bloquante** : « échéance à confirmer » |
| `incertaine` | Disposition non localisée ou date relevant d'une interprétation | **Bloquante** : idem |

État au 2026-10-27 : **15 entrées sur 16 `officielle_relue`**. Seule **CAL-016** reste `incertaine`
(bloquante) : l'art. 49, par. 2 (non modifié) et l'annexe VIII, section B (points 7 et 9 supprimés)
ont été relus, mais la date effective de l'obligation d'enregistrement n'est pas fixée par le texte
(art. 49 à la date générale, qualification de l'art. 6, par. 3 et 4 à partir du 2.12.2027).

## 5. Points d'interprétation restants (2026-10-27)

| Sujet | État | Traitement |
|---|---|---|
| Date effective de l'enregistrement de l'art. 49, par. 2 | Texte relu ; date non explicite | `[AV]`, bloquant (CAL-016) |
| Art. 49, 72, 73 et 86 pour les systèmes à haut risque | Hors chapitre III : date générale ; ne visent que des systèmes classés à haut risque, classification applicable au 2.12.2027 ou au 2.8.2028 | `[AV]` : apprécier au cas par cas |
| Notion d'« importantes modifications de leurs conceptions » (art. 111, par. 2) | Texte relu ; notion non définie | `[AV]` : analyser chaque changement (modèle, finalité, logique de décision) |
| Garde-fous « raisonnables et adéquats » (art. 5, par. 1 bis, a), ii)) | Texte relu ; appréciation au cas par cas | `[AV]` |
| Art. 50, par. 2 et textes conversationnels | Texte relu : les textes sont visés (art. 50, par. 2 et art. 111, par. 4) | Pas d'exemption ; seules les modalités techniques relèvent des lignes directrices et du code de bonnes pratiques |
| Rectificatifs 32024R1689R(01) à R(04) | Recensés, contenu par langue non examiné | À examiner lors de la prochaine revue |

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
