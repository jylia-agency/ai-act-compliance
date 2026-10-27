# Résultats attendus : demo-ai-vulnerable

Date d'audit de référence : **2026-10-27**. Variante calendaire : **2026-12-15**.
Contexte déclaré : voir `README.md` (éditeur fictif EduAssist SAS, mise sur le marché le 2026-03-01,
commercialisation sous sa propre marque, modèles via l'API d'un fournisseur tiers).

Les identifiants `AIA-NNN` sont attribués par l'agent ; seuls le contenu et la qualification sont évalués.

## 1. Systèmes d'IA attendus dans l'inventaire

| Système | Fichiers | Classification attendue | Confiance |
|---|---|---|---|
| Tuteur conversationnel | `app/tutor_chat.py` | Non à haut risque ; soumis à l'article 50, par. 1 (et par. 2 pour les textes, à analyser) | Élevée |
| Correction automatique | `app/grading.py`, `app/gradebook.py` | Haut risque **probable** au titre de l'annexe III, point 3, b) ; dérogation de l'art. 6, par. 3 non applicable a priori (la note est la décision) | Moyenne |
| Illustrations | `app/illustrations.py` | Non à haut risque ; article 50, par. 2 (fournisseur) ; par. 4 à vérifier selon les contenus | Élevée |
| Surveillance d'examens | `app/proctoring.py` | **Pratique potentiellement interdite** : reconnaissance des émotions dans un établissement d'enseignement (art. 5, par. 1, f)) ; à défaut, annexe III, point 3, d) | Élevée sur les faits, moyenne à élevée sur la qualification |

Rôles attendus : EduAssist **fournisseur des systèmes d'IA** (art. 3, point 3 : développement et mise
sur le marché sous son nom) ; établissements clients **déployeurs** (art. 3, point 4) ; le fournisseur
de l'API est **fournisseur des modèles GPAI**. EduAssist **n'est pas** fournisseur de modèle GPAI.

## 2. Constats attendus (à la date du 2026-10-27)

| # | Sujet | Nature attendue | Gravité | Confiance | Référence | Statut temporel |
|---|---|---|---|---|---|---|
| E1 | Inférence d'émotions à partir de la webcam pendant les examens, avec annulation automatique | Risque potentiel (pratique interdite à confirmer juridiquement) ; fait technique avéré cité en preuve | Critique | Élevée | Art. 5, par. 1, f) ; art. 3, point 39 ; exception médicale ou de sécurité examinée et écartée | Applicable depuis le 2025-02-02 |
| E2 | Le tuteur ne signale pas qu'il est une IA et l'invite système lui demande de le nier | Constat technique avéré (absence d'information) ; manquement potentiel à l'art. 50, par. 1 | Élevée | Élevée | Art. 50, par. 1 et 5 | Applicable depuis le 2026-08-02 (aucun délai de grâce) |
| E3 | Images générées enregistrées sans marquage lisible par machine | Non encore applicable (délai jusqu'au 2026-12-02 pour un système mis sur le marché avant le 2026-08-02) ; recommandation de préparation | Moyenne | Moyenne (date issue du règlement 2026/1744) | Art. 50, par. 2 ; règlement 2026/1744 | Applicable le 2026-12-02 |
| E4 | Note finale publiée sans validation humaine | Risque potentiel ; obligations du chapitre III **non encore applicables** | Élevée | Moyenne | Art. 6, par. 2 ; annexe III, point 3, b) ; art. 14 ; art. 113 modifié | Non encore applicable (2027-12-02) ; régime de l'art. 111, par. 2 à vérifier |
| E5 | Aucune journalisation des notes, des versions de modèle ni des invites | Constat technique avéré + Bonne pratique recommandée dès maintenant ; art. 12 non encore applicable | Moyenne | Élevée | Art. 12, art. 19, art. 26, par. 6 (futurs) | Non encore applicable |
| E6 | Clé d'API codée en dur dans `app/config.py` (valeur masquée dans le rapport) | Constat technique avéré ; bonne pratique de sécurité (pas une obligation AI Act autonome à ce stade) | Élevée | Élevée | Hors AI Act, sauf art. 15 si haut risque (futur) | n.a. |
| E7 | Paramètre `temperature=1.0` pour la notation : résultats non reproductibles | Risque potentiel ; Bonne pratique recommandée | Moyenne | Élevée | Art. 15 (futur, si haut risque) | Non encore applicable |
| E8 | Absence de documentation technique, d'analyse de classification et de mesures de maîtrise de l'IA | À vérifier juridiquement ou organisationnellement (absence dans le dépôt ≠ absence dans l'organisation) | Moyenne | Faible | Art. 4 ; art. 6, par. 4 ; art. 11 (futur) | Art. 4 applicable ; art. 11 non encore applicable |
| E9 | Établissements publics clients : échéance spécifique de l'art. 111, par. 2 | À vérifier juridiquement | Information | Faible | Art. 111, par. 2 (texte relu : autorités publiques au 2.8.2030) | Conditionnel |
| E10 | Réponses textuelles du tuteur sans marquage lisible par machine | Non encore applicable (délai jusqu'au 2026-12-02, système antérieur au 2026-08-02) ; l'incertitude sur les modalités de marquage d'un texte est consignée à part, sans exemption | Moyenne | Moyenne | Art. 50, par. 2 | Applicable le 2026-12-02 |

**Règle bloquante** : depuis la relecture du texte officiel (version 1.2.0), seule CAL-016 est
bloquante ; aucun constat attendu ici ne doit porter la mention « échéance à confirmer », sauf un
éventuel constat sur l'enregistrement de l'art. 49, par. 2.

## 3. Variante calendaire (date d'audit 2026-12-15)

- E3 devient **applicable** (échéance du 2026-12-02 dépassée) : nature « Constat technique avéré » sur
  l'absence de marquage et manquement potentiel à l'article 50, paragraphe 2.
- Les nouvelles interdictions de l'article 5 (contenus intimes non consentis, CSAM) deviennent
  applicables le 2026-12-02 : l'agent doit vérifier si le générateur d'images dispose de garde-fous ;
  absence de preuve = « À vérifier », pas un manquement établi.
- E4, E5, E7 restent « Non encore applicable ».

## 4. Constats qui ne doivent pas apparaître

- « EduAssist est fournisseur de modèle GPAI » ou application des articles 53 et 55 à EduAssist.
- « La plateforme entière est à haut risque » (classification globale non motivée système par système).
- Le tuteur classé à haut risque au seul motif qu'il est utilisé dans l'éducation.
- Les obligations du chapitre III (art. 9 à 15, 16, 17, 26, 43, 49) présentées comme **déjà applicables**.
- L'article 50, paragraphe 2, présenté comme applicable au 2026-10-27 pour les illustrations.
- Le déni de nature IA du tuteur qualifié de pratique interdite de l'article 5, paragraphe 1, a)
  **sans** analyse du critère de préjudice important (il peut être mentionné comme point examiné).
- La valeur de la clé d'API reproduite en clair.
- Une exemption des réponses conversationnelles au titre de l'article 50, paragraphe 2.
- Une date dont l'entrée calendaire est bloquante (CAL-016) présentée sans la mention « échéance à confirmer ».
- Toute mention « conforme à l'AI Act » ou « certifié ».

## 5. Erreurs de classification à éviter

- Classer la surveillance d'examens seulement en haut risque (annexe III, point 3, d)) sans examiner
  d'abord l'article 5, paragraphe 1, f).
- Retenir l'exception « raisons médicales ou de sécurité » pour la détection de fraude.
- Appliquer la dérogation de l'article 6, paragraphe 3, à la correction automatique alors que la
  note produite est la décision finale.
- Oublier la règle transitoire de l'article 111, paragraphe 2, pour un système mis sur le marché
  avant la date d'application du chapitre III.
