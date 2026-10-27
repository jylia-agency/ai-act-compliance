# Obligations des fournisseurs de systèmes d'IA

> Base : art. 4, 5, 6, 8 à 22, 43, 47 à 49, 50, 72, 73 du règlement (UE) 2024/1689 `[TI]` ; dates
> modifiées par le règlement (UE) 2026/1744 `[O26]`. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 16](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-16).
> Les obligations des fournisseurs de **modèles GPAI** sont traitées dans `gpai-obligations.md`.

## 1. Obligations quelle que soit la classification

| Obligation | Article | Applicable depuis | Démontrable par le code ? |
|---|---|---|---|
| Ne pas mettre sur le marché ou en service une pratique interdite | Art. 5 | 2025-02-02 (nouveaux points : 2026-12-02 `[O26]`) | Partiellement (fonctionnalités) |
| Mesures de maîtrise de l'IA du personnel et des personnes agissant pour son compte | Art. 4 (rédaction `[O26]`) | 2025-02-02 ; nouvelle rédaction 2026-07-27 `[O26]` | Non (organisationnel) ; indices possibles (docs de formation) |
| Transparence : interaction directe, marquage des contenus synthétiques | Art. 50, par. 1, 2, 5 | 2026-08-02 ; par. 2 : 2026-12-02 pour les systèmes antérieurs `[O26]` | Oui, en grande partie |

## 2. Obligations du fournisseur d'un système à haut risque

**Non encore applicables** à la date du 2026-10-27 : annexe III à partir du **2027-12-02**, annexe I
à partir du **2028-08-02** `[O26]` ; systèmes antérieurs : art. 111, par. 2 `[AV]`. À traiter comme
feuille de route, sauf si la date d'audit est postérieure.

### 2.1 Exigences applicables au système (chapitre III, section 2)

| Article | Exigence | Preuves observables dans un dépôt |
|---|---|---|
| 9 | Système de gestion des risques, processus itératif sur tout le cycle de vie : identification et analyse des risques connus et raisonnablement prévisibles pour la santé, la sécurité et les droits fondamentaux, estimation, mesures de gestion, essais | Registre des risques, rapports de tests, critères d'acceptation |
| 10 | Données et gouvernance des données (entraînement, validation, test) : pratiques de gestion, pertinence, représentativité, examen des biais possibles ; par. 5 : traitement exceptionnel de données sensibles pour la détection et la correction des biais, sous stricte nécessité `[AV]` | Fiches de jeux de données, scripts de préparation, analyses de biais |
| 11 | Documentation technique établie avant la mise sur le marché, tenue à jour, contenu de l'annexe IV (forme simplifiée possible pour les PME) | Voir `technical-documentation.md` |
| 12 | Enregistrement automatique des événements (journaux) tout au long de la durée de vie, assurant la traçabilité appropriée à la destination | Code de journalisation, schéma des journaux |
| 13 | Transparence et fourniture d'informations aux déployeurs : notice d'utilisation (identité du fournisseur, caractéristiques, capacités et limites, niveau d'exactitude, risques, mesures de supervision humaine, ressources nécessaires, journaux) | Notice, guide utilisateur |
| 14 | Contrôle humain : conception permettant une supervision effective | Voir `human-oversight.md` |
| 15 | Exactitude, robustesse et cybersécurité, y compris contre l'empoisonnement de données ou de modèles, les exemples contradictoires, les attaques de confidentialité | Tests d'évaluation, tests adverses, durcissement, gestion des secrets |

### 2.2 Obligations de l'opérateur fournisseur (chapitre III, section 3)

| Article | Obligation |
|---|---|
| 16, a) | Veiller au respect des exigences de la section 2 |
| 16, b) | Indiquer nom, raison sociale ou marque et adresse de contact |
| 16, c) et 17 | Système de gestion de la qualité (politiques, procédures, documentation) |
| 16, d) et 18 | Conserver la documentation pendant **10 ans** après la mise sur le marché ou en service |
| 16, e) et 19 | Conserver les journaux générés automatiquement sous son contrôle pendant une durée adaptée d'au moins **six mois**, sauf disposition contraire |
| 16, f) et 43 | Procédure d'évaluation de la conformité avant mise sur le marché ou en service (contrôle interne de l'annexe VI pour la plupart des systèmes de l'annexe III, points 2 à 8) |
| 16, g) et 47 | Déclaration UE de conformité |
| 16, h) et 48 | Marquage CE |
| 16, i) et 49, par. 1 | Enregistrement dans la base de données de l'UE (systèmes de l'annexe III, sauf point 2) |
| 16, j) et 20 | Mesures correctives et devoir d'information en cas de non-conformité |
| 16, k) et 21 | Démontrer la conformité sur demande motivée d'une autorité ; coopération |
| 16, l) | Exigences d'accessibilité (directives (UE) 2016/2102 et (UE) 2019/882) |
| 22 | Mandataire si le fournisseur est établi hors de l'Union |
| 72 | Système de surveillance après commercialisation et plan associé |
| 73 | Signalement des incidents graves aux autorités de surveillance du marché : au plus tard 15 jours après la connaissance ; 2 jours en cas d'infraction de grande ampleur ou d'incident affectant une infrastructure critique ; 10 jours en cas de décès |

Dates des art. 49, 72 et 73 au regard du report : `[AV]` (voir `applicability-calendar.md`, section 3).

## 3. Fournisseur invoquant la dérogation de l'article 6, paragraphe 3

- Documenter l'évaluation avant la mise sur le marché ou la mise en service (art. 6, par. 4).
- Fournir cette documentation aux autorités sur demande.
- Enregistrement (art. 49, par. 2) maintenu avec contenu réduit selon les sources `[AV]`.

## 4. Points d'attention pour l'audit

- Un fournisseur qui intègre un modèle GPAI tiers reste responsable des obligations liées à **son**
  système ; il peut s'appuyer sur les informations que le fournisseur du modèle doit lui transmettre
  (art. 53, par. 1, b), annexe XII).
- Les obligations futures sont présentées comme « Non encore applicable » avec échéance, assorties
  d'une recommandation de préparation proportionnée à l'effort (la mise en place d'un SGQ ou d'une
  documentation de l'annexe IV demande plusieurs mois).
- Ne jamais déduire l'absence de SGQ, de documentation ou de procédure de leur absence du dépôt.
