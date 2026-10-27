# IA et éducation

> Base : art. 5, par. 1, f) ; art. 6 ; annexe III, point 3 ; art. 26 ; art. 50 du règlement (UE)
> 2024/1689 `[TI]`, dates modifiées par le règlement (UE) 2026/1744 `[O26]`.
> Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, annexe III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3).

## 1. Principe

Tous les outils pédagogiques utilisant l'IA ne sont **pas** à haut risque. Seules les finalités de
l'annexe III, point 3, le sont (sous réserve de l'art. 6, par. 3), et la reconnaissance des
émotions dans les établissements d'enseignement est **interdite** (art. 5, par. 1, f)).

Pour l'échelle des scénarios (entraînement, notation indicative, classement, décision assistée,
décision automatisée), les questions obligatoires et l'effectivité du contrôle humain, appliquer
également `person-decisions.md`.

## 2. Grille d'analyse par fonctionnalité

| Fonctionnalité | Qualification à examiner en priorité | Qualification par défaut si les faits sont confirmés | Points de vigilance |
|---|---|---|---|
| Inférence d'émotions, de stress, d'ennui ou d'attention émotionnelle des élèves (webcam, voix) | Art. 5, par. 1, f) | Pratique potentiellement interdite, applicable depuis le 2025-02-02 | Exception médicale ou de sécurité d'interprétation stricte ; la lutte contre la fraude n'en relève pas |
| Notation de copies, évaluation des acquis, contrôle continu | Annexe III, point 3, b) | Haut risque probable si la sortie détermine ou influence substantiellement la note | Art. 6, par. 3 : une aide préparatoire (par exemple surlignage d'erreurs orthographiques soumis à l'enseignant) peut relever du point d) ; motiver |
| Orientation du parcours d'apprentissage selon l'évaluation | Annexe III, point 3, b) (« y compris pour orienter le processus d'apprentissage ») | Haut risque possible | Distinguer recommandation d'exercices et décision d'orientation |
| Admission, sélection, affectation | Annexe III, point 3, a) | Haut risque probable | Profilage : exclut la dérogation |
| Évaluation du niveau d'enseignement approprié | Annexe III, point 3, c) | Haut risque probable | Tests de positionnement à effet décisionnel |
| Surveillance d'examens (détection de comportements interdits) | Annexe III, point 3, d) ; art. 5 si émotions ; annexe III, point 1 si biométrie | Haut risque probable | Identification biométrique, décisions automatiques d'annulation |
| Évaluation des compétences (certification) | Annexe III, point 3, b) ou c) | Selon l'effet sur l'accès à une certification | Analyser la conséquence pour la personne |
| Aide à la décision pédagogique (conseil de classe, signalement de décrochage) | Annexe III, point 3, b) ou c) ; art. 6, par. 3, c) ou d) | Indéterminée sans contexte | Profilage d'élèves fréquent : exclut la dérogation |
| Tuteur conversationnel, aide aux devoirs, explication de cours | Art. 50, par. 1 (et par. 2 pour les contenus) | Non à haut risque si aucun usage évaluatif | Vérifier que les échanges ne sont pas réutilisés pour noter ou orienter |
| Génération de supports pédagogiques (textes, images) | Art. 50, par. 2 (fournisseur) et par. 4 (déployeur) | Non à haut risque | Hypertrucages de personnages historiques ou de personnes réelles |
| Détection de plagiat ou de texte généré par IA | Annexe III, point 3, b) ou d) selon l'usage | Indéterminée | Les faux positifs peuvent entraîner des sanctions ; supervision humaine |

## 3. Rôles typiques

- **Éditeur EdTech** qui commercialise la solution sous sa marque : fournisseur du système d'IA.
- **Établissement** (lycée, université, organisme de formation) qui l'utilise : déployeur.
  Les établissements **publics** peuvent être des autorités publiques au sens de l'article 111,
  paragraphe 2 (échéance spécifique, `[AV]`) et de l'article 27 (analyse d'impact sur les droits
  fondamentaux pour les organismes de droit public).
- **Enseignant** : personne chargée de la supervision humaine (art. 26, par. 2), pas un opérateur
  distinct.

## 4. Calendrier spécifique (à la date d'audit)

- Art. 5, par. 1, f) : applicable depuis le 2025-02-02.
- Art. 50 : par. 1, 3, 4, 5 depuis le 2026-08-02 ; par. 2 avec délai au 2026-12-02 pour les systèmes
  antérieurs au 2026-08-02 `[O26]`.
- Exigences du haut risque (annexe III, point 3) : **2027-12-02** `[O26]` ; systèmes antérieurs :
  art. 111, par. 2 `[AV]`.
- Art. 4 : applicable (rédaction modifiée `[O26]`).

## 5. Contrôles spécifiques

- La note produite par l'IA est-elle une **proposition** ou la **décision** ? Peut-on la publier sans
  validation ? (`human-oversight.md`)
- L'enseignant voit-il la justification et les critères ? Peut-il modifier ou rejeter sans friction ?
- Les élèves et familles sont-ils informés de l'utilisation d'un système d'IA dans l'évaluation
  (art. 26, par. 11 pour le haut risque, futur) ?
- Les performances sont-elles mesurées par sous-groupes (allophones, handicap, copies manuscrites) ?
- Le paramétrage est-il reproductible (température, version de modèle épinglée, version de grille) ?
- Les décisions et corrections humaines sont-elles journalisées ?
