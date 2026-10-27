# Rapport d'audit AI Act : EduAssist (fixture `demo-ai-vulnerable`)

> **Exemple de livrable** produit selon la méthodologie du skill `ia-compliance` sur le projet fictif
> `tests/fixtures/demo-ai-vulnerable`. Il illustre le format attendu et sert de référence : il a été
> rédigé manuellement et n'est pas une sortie brute d'agent (voir `tests/RESULTS.md` pour les essais réels).
>
> **Avertissement.** Ce rapport est une aide à l'audit fondée sur l'analyse statique d'un dépôt et
> sur des références juridiques datées. Il **ne constitue ni une certification, ni une attestation
> de conformité**, ni un avis juridique, ni une évaluation de la conformité au sens de l'article 43.

| Paramètre | Valeur |
|---|---|
| Date d'audit | 2026-10-27 |
| Périmètre | `tests/fixtures/demo-ai-vulnerable/` (intégralité) |
| Commit audité | Fixture du dépôt du skill, version 1.1.0 (dans un audit réel : empreinte complète `git rev-parse HEAD`) |
| Mode | Complet |
| Base juridique | Règlement (UE) 2024/1689 tel que modifié par le règlement (UE) 2026/1744 |
| Références vérifiées le | 2026-10-27 (texte officiel relu ; voir `references/legal-sources.md`) |
| Contexte fourni | `README.md` : éditeur EduAssist SAS (France), commercialisation sous sa marque auprès de lycées et universités de l'Union, mise sur le marché de tous les modules le 2026-03-01, modèles via l'API d'OpenAI |
| Méthode | Lecture du code, `scripts/scan_ai_signals.py`, `scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-03-01` ; aucune exécution du code audité |
| Audit précédent | Aucun |

## 1. Résumé exécutif

- **Quatre systèmes d'IA** identifiés : tuteur conversationnel (SYS-01), correction automatique
  (SYS-02), génération d'illustrations (SYS-03), surveillance d'examens (SYS-04).
- **Point le plus sensible** : SYS-04 infère les émotions des élèves à partir de la webcam pendant
  les examens et annule automatiquement des copies. Cette fonctionnalité est susceptible de relever
  de la **pratique interdite** de l'article 5, paragraphe 1, f), applicable depuis le 2025-02-02
  (AIA-001).
- **Obligation en vigueur probablement non respectée** : le tuteur ne s'identifie pas comme une IA
  et son prompt système lui impose de le nier (art. 50, par. 1, en vigueur depuis le 2026-08-02, AIA-002).
- **Échéance proche** : marquage des images générées (art. 50, par. 2) exigible le **2026-12-02**
  pour ce système antérieur au 2026-08-02 (AIA-003 ; art. 111, par. 4).
- **Haut risque à préparer** : la correction automatique est un système à haut risque probable
  (annexe III, point 3, b)) ; exigences non encore applicables (2027-12-02), régime transitoire de
  l'article 111, paragraphe 2 à analyser (AIA-004, AIA-009).
- **Incertitudes principales** : documents organisationnels absents du dépôt, statut public de
  certains établissements clients, échéance de l'art. 111, par. 2 pour les autorités publiques à confirmer sur le JO.
- **Constats dont l'échéance est à confirmer** (entrée calendaire bloquante) : aucun (seule CAL-016 est bloquante et n'est pas mobilisée ici).

| Nature | Critique | Élevée | Moyenne | Faible | Information |
|---|---|---|---|---|---|
| Constat technique avéré | | 2 | 1 | | |
| Risque potentiel | 1 | 1 | 1 | | |
| À vérifier juridiquement ou organisationnellement | | | 1 | | 1 |
| Bonne pratique recommandée | | | | | |
| Non encore applicable | | | 2 | | |
| Non applicable | | | | | 1 |

## 2. Périmètre et méthode

Fichiers analysés : `README.md`, `requirements.txt`, `app/config.py`, `app/tutor_chat.py`,
`app/grading.py`, `app/gradebook.py`, `app/illustrations.py`, `app/proctoring.py`. Le scanner a
relevé des signaux `provider_api` (openai), `media_generation` (images.generate, dall-e),
`biometric` (deepface), `model_identifier` (`gpt-4o`, `dall-e-3`), un secret potentiel (masqué) et
des signaux de contexte « éducation » et « émotions ». Aucun signal de transparence, de supervision
ou de journalisation.

## 3. Systèmes d'IA identifiés

| ID | Système | Finalité | Rôle(s) d'EduAssist | Modèle(s) et fournisseur | Classification | Confiance |
|---|---|---|---|---|---|---|
| SYS-01 | Tuteur conversationnel | Répondre aux questions des élèves sur les cours | Fournisseur du système | `gpt-4o`, OpenAI (API) | Non à haut risque ; art. 50, par. 1 (et par. 2 pour les textes, à analyser) | Élevée |
| SYS-02 | Correction automatique | Attribuer la note finale des dissertations | Fournisseur du système | `gpt-4o`, OpenAI (API) | Haut risque probable (annexe III, point 3, b)) | Moyenne |
| SYS-03 | Illustrations de cours | Générer des images pour les supports publiés | Fournisseur du système | `dall-e-3`, OpenAI (API) | Non à haut risque ; art. 50, par. 2 | Élevée |
| SYS-04 | Surveillance d'examens | Détecter des comportements suspects et annuler des copies | Fournisseur du système | DeepFace (bibliothèque open source, modèle d'émotions local) | Pratique potentiellement interdite (art. 5, par. 1, f)) ; à défaut, annexe III, point 3, d) | Élevée (faits) / Moyenne à élevée (qualification) |

Écartés : `app/gradebook.py` (stockage, pas d'inférence), `app/config.py` (configuration).

## 4. Rôles réglementaires

EduAssist développe les quatre systèmes et les met sur le marché sous sa marque : elle est
**susceptible d'être fournisseur** de chacun (art. 3, point 3). Les établissements clients sont
**déployeurs** (art. 3, point 4). OpenAI est **fournisseur des modèles GPAI** sous-jacents ; EduAssist
n'entraîne, n'affine ni ne publie de modèle et **n'est pas fournisseur de modèle GPAI** au vu du dépôt.
Pour SYS-04, le modèle d'émotions provient d'une bibliothèque open source ; l'exclusion de l'art. 2,
par. 12 ne bénéficie pas à un système relevant de l'article 5.

## 5. Exclusions et exceptions examinées

| Disposition | Système | Retenue / écartée | Motif |
|---|---|---|---|
| Art. 2, par. 8 (R&D avant mise sur le marché) | Tous | Écartée | Systèmes mis sur le marché le 2026-03-01 |
| Art. 2, par. 12 (open source) | SYS-04 | Écartée | Ne s'applique pas aux systèmes relevant de l'art. 5 ou de l'art. 50 ni au haut risque |
| Art. 5, par. 1, f), exception médicale ou de sécurité | SYS-04 | Écartée | Finalité déclarée : détection de fraude |
| Art. 6, par. 3 (dérogation) | SYS-02 | Écartée a priori | La sortie est la note finale publiée : influence déterminante sur la décision |
| Art. 50, par. 1, exception « évident » | SYS-01 | Écartée | Persona humaine (« Claire, professeure ») et déni explicite |
| Art. 111, par. 2 (systèmes antérieurs) | SYS-02 | À vérifier | Voir AIA-009 |

## 6. Classification

- **SYS-01** : aucun cas d'usage de l'annexe III (pas d'évaluation des acquis : les échanges ne sont
  pas utilisés pour noter). Art. 5, par. 1, a) examiné : la persona trompeuse ne suffit pas, sans
  élément sur une altération substantielle du comportement causant un préjudice important ; non
  retenu, traité au titre de l'art. 50. Conclusion : non à haut risque, soumis à l'art. 50.
- **SYS-02** : annexe III, point 3, b) (évaluation des acquis d'apprentissage) ; pas de dérogation.
  Conclusion : haut risque probable ; exigences applicables le 2027-12-02 (CAL-011) sous réserve de
  l'art. 111, par. 2 (CAL-013).
- **SYS-03** : non à haut risque ; art. 50, par. 2 (fournisseur) ; art. 50, par. 4 pour les
  déployeurs si des images ressemblent à des personnes ou événements réels.
- **SYS-04** : art. 5, par. 1, f) examiné en premier ; à défaut d'interdiction, annexe III, point 3,
  d) et point 1, c).

## 7. Obligations et calendrier

| Obligation | Système | Rôle | Statut temporel | Date | Réf. | Confiance |
|---|---|---|---|---|---|---|
| Interdiction de la reconnaissance des émotions dans l'enseignement | SYS-04 | Fournisseur | En vigueur | 2025-02-02 | CAL-002 | Élevée |
| Maîtrise de l'IA | Tous | Fournisseur | En vigueur | 2025-02-02 / 2026-07-27 | CAL-002, CAL-003 | Élevée / Moyenne |
| Information sur l'interaction avec une IA | SYS-01 | Fournisseur | En vigueur | 2026-08-02 | CAL-009 | Élevée |
| Marquage des contenus synthétiques (images et textes) | SYS-03, SYS-01 | Fournisseur | Non encore applicable | 2026-12-02 | CAL-010 | Élevée |
| Exigences du haut risque (art. 9 à 15, 16, 17, 43, 47 à 49) | SYS-02 | Fournisseur | Non encore applicable / conditionnel (CAL-013) | 2027-12-02 | CAL-011, CAL-013 | Élevée |
| Obligations des déployeurs à haut risque (art. 26, 27) | SYS-02 | Établissements | Non encore applicable | 2027-12-02 | CAL-011 | Moyenne |
| Obligations des fournisseurs de modèles GPAI | n.a. | n.a. | Non applicable | n.a. | CAL-005 | Élevée |

## 8. Constats

### AIA-001 : Inférence des émotions des élèves pendant les examens avec annulation automatique
- **Système d'IA concerné** : SYS-04 Surveillance d'examens
- **Nature du constat** : Risque potentiel (qualification de pratique interdite à confirmer juridiquement)
- **Gravité** : Critique
- **Niveau de confiance** : Élevée (faits) / Moyenne à élevée (qualification)
- **Preuve observée** : Fait observé : `DeepFace.analyze(frame, actions=["emotion"])` est appliqué aux images de la webcam ; les émotions `fear`, `angry`, `surprise` sont comptées comme suspectes ; au-delà de 30 images, l'examen est annulé sans intervention humaine.
- **Fichier(s) et lignes** : `app/proctoring.py:5`, `app/proctoring.py:9-10`, `app/proctoring.py:20-24`
- **Rôle réglementaire concerné** : Fournisseur (EduAssist) ; déployeurs (établissements) au titre de l'utilisation
- **Classification du système** : Pratique potentiellement interdite
- **Référence juridique** : Art. 5, par. 1, f) `[TI]` ; art. 3, point 39 `[TI]` ; [AI Act Explorer, art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)
- **Date d'application** : 2025-02-02 (CAL-002), en vigueur ; aucune règle transitoire
- **Conditions et exceptions** : Système de reconnaissance des émotions (déduction d'émotions à partir de données biométriques faciales) utilisé dans un établissement d'enseignement. Exception « raisons médicales ou de sécurité » examinée et écartée (finalité : détection de fraude).
- **Explication** : Le règlement interdit les systèmes d'IA qui déduisent les émotions des personnes dans les établissements d'enseignement, sauf raisons médicales ou de sécurité. Le module analyse les expressions faciales des élèves pour décider d'annuler un examen. Il s'agit de la catégorie de risque la plus élevée du règlement.
- **Recommandation** : Désactiver immédiatement le module dans l'Union ; solliciter une analyse juridique ; remplacer par une surveillance humaine ou par des événements techniques non biométriques soumis à un surveillant (voir la version corrigée `demo-ai-secure/app/exam_events.py`).
- **Méthode de vérification** : Absence de tout appel à `DeepFace.analyze` ou à une inférence d'émotions dans le code déployé ; preuve de désactivation en production ; avis juridique écrit.

### AIA-002 : Le tuteur conversationnel ne s'identifie pas comme une IA et doit le nier
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel
- **Nature du constat** : Constat technique avéré
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : le prompt système impose une persona humaine (« Tu es Claire, professeure ») et interdit de révéler la nature d'IA ; aucun message d'information n'est affiché avant ou pendant l'échange. Analyse juridique : manquement potentiel à l'art. 50, par. 1.
- **Fichier(s) et lignes** : `app/tutor_chat.py:8-11`, `app/tutor_chat.py:14-18`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non à haut risque ; soumis à l'art. 50
- **Référence juridique** : Art. 50, par. 1 et 5 `[TI]` ; [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)
- **Date d'application** : 2026-08-02 (CAL-009), en vigueur ; aucun délai de grâce
- **Conditions et exceptions** : Exception « évident pour une personne raisonnablement informée » écartée (persona humaine, public de mineurs) ; exception répressive sans objet. Art. 5, par. 1, a) examiné et non retenu faute d'éléments sur un préjudice important.
- **Explication** : Lorsqu'un système d'IA dialogue directement avec des personnes, son fournisseur doit faire en sorte qu'elles sachent qu'elles parlent à une IA, au plus tard au début de l'échange. Ici, le système est configuré pour se faire passer pour une enseignante.
- **Recommandation** : Supprimer la persona humaine et la consigne de déni ; afficher un message clair avant la première interaction ; faire répondre le système qu'il est une IA si on le lui demande ; vérifier l'accessibilité du message.
- **Méthode de vérification** : Revue du prompt système ; test d'interface (capture du message initial) ; test conversationnel « Es-tu humain ? ».

### AIA-003 : Images générées enregistrées sans marquage lisible par machine
- **Système d'IA concerné** : SYS-03 Illustrations de cours
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : l'image renvoyée par l'API est décodée et écrite telle quelle, sans ajout de métadonnées de provenance ni de mention ; la préservation d'un éventuel marquage appliqué par le fournisseur du modèle n'est pas vérifiée.
- **Fichier(s) et lignes** : `app/illustrations.py:12-15`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non à haut risque ; soumis à l'art. 50, par. 2
- **Référence juridique** : Art. 50, par. 2 `[TI]` ; délai : art. 111, par. 4, ajouté par le règlement (UE) 2026/1744 `[O26]` (CAL-010)
- **Date d'application** : 2026-12-02 pour ce système mis sur le marché le 2026-03-01 (CAL-010, art. 111, par. 4) ; non encore applicable au 2026-10-27 (dans 36 jours)
- **Conditions et exceptions** : Exceptions « assistance à la mise en forme standard » et « absence de modification substantielle » sans objet (génération à partir d'un texte). Art. 50, par. 4 (hypertrucages, déployeurs) à vérifier selon les contenus générés.
- **Explication** : Les fournisseurs de systèmes générant des images doivent faire en sorte que ces images soient marquées dans un format lisible par machine et détectables comme artificielles. Pour ce module, l'obligation devient exigible le 2 décembre 2026. Une simple mention visible ne suffirait pas.
- **Recommandation** : Avant le 2026-12-02 : ajouter des métadonnées de provenance (C2PA, IPTC `trainedAlgorithmicMedia`), préserver le marquage amont, tester la robustesse au ré-encodage, documenter la méthode de détection ; s'appuyer sur le code de bonnes pratiques du 10.6.2026.
- **Méthode de vérification** : Lecture des métadonnées d'une image produite ; test de ré-encodage ; documentation de la méthode de détection.

### AIA-004 : Note finale publiée sans validation humaine
- **Système d'IA concerné** : SYS-02 Correction automatique
- **Nature du constat** : Risque potentiel
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée (faits) / Moyenne (qualification)
- **Preuve observée** : Fait observé : la note extraite de la réponse du modèle est publiée immédiatement dans le bulletin (`publish_grade`), sans étape de relecture ni possibilité d'annulation ; le docstring indique qu'elle compte pour le passage en classe supérieure.
- **Fichier(s) et lignes** : `app/grading.py:1-5`, `app/grading.py:27-28`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs (art. 26, par. 2, futur)
- **Classification du système** : Haut risque probable (annexe III, point 3, b))
- **Référence juridique** : Art. 6, par. 2 et annexe III, point 3, b) `[TI]` ; art. 14, par. 4, d) `[TI]` ; art. 113 modifié `[O26]`
- **Date d'application** : Exigences du haut risque au 2027-12-02 (CAL-011), non encore applicables ; régime transitoire conditionnel (CAL-013)
- **Conditions et exceptions** : Dérogation de l'art. 6, par. 3 écartée (la sortie constitue la décision). La supervision humaine n'est pas un critère d'exclusion du haut risque.
- **Explication** : L'évaluation des acquis des élèves par une IA est un usage à haut risque. Les exigences correspondantes, dont la possibilité pour un humain d'ignorer ou de corriger le résultat, ne s'appliquent qu'à partir de décembre 2027 ; mais le risque d'erreur affectant des élèves existe dès aujourd'hui.
- **Recommandation** : Transformer la note en proposition soumise à l'enseignant (approuver, modifier avec motif, rejeter) ; bloquer la publication sans validation ; afficher la justification et les critères.
- **Méthode de vérification** : Test : aucune note publiée sans `validated_by` ; revue de l'interface enseignant ; journal des décisions.

### AIA-005 : Clé d'API codée en dur dans le dépôt
- **Système d'IA concerné** : SYS-01, SYS-02, SYS-03
- **Nature du constat** : Constat technique avéré
- **Gravité** : Élevée
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : une valeur de type clé d'API est affectée en clair à `OPENAI_API_KEY` (valeur : `[SECRET MASQUÉ]`).
- **Fichier(s) et lignes** : `app/config.py:2`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Selon le système (voir inventaire)
- **Référence juridique** : Aucune obligation autonome de l'AI Act à la date d'audit (bonne pratique de sécurité) ; pertinent pour l'art. 15 (cybersécurité) lorsque les exigences du haut risque s'appliqueront à SYS-02 `[TI]`
- **Date d'application** : n.a. (art. 15 : 2027-12-02, CAL-011)
- **Conditions et exceptions** : Valeur fictive dans cette fixture ; dans un projet réel, considérer la clé comme compromise.
- **Explication** : Une clé d'API stockée dans le code peut être exposée à toute personne ayant accès au dépôt et permettre un usage frauduleux du service.
- **Recommandation** : Révoquer la clé, la stocker dans un gestionnaire de secrets ou une variable d'environnement, purger l'historique Git si nécessaire, ajouter un contrôle de secrets en intégration continue.
- **Méthode de vérification** : Recherche de secrets sur le dépôt et son historique ; vérification de la révocation.

### AIA-006 : Absence de journalisation des notes, versions de modèle et invites
- **Système d'IA concerné** : SYS-02 (et SYS-01, SYS-03)
- **Nature du constat** : Constat technique avéré
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : aucune instruction de journalisation ; la version du modèle servie (`response.model`), le prompt et la note ne sont pas enregistrés ; l'alias `gpt-4o` n'est pas épinglé.
- **Fichier(s) et lignes** : `app/grading.py:19-29`, `app/config.py:3`
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs (art. 26, par. 6, futur)
- **Classification du système** : Haut risque probable (SYS-02)
- **Référence juridique** : Art. 12, art. 19 et art. 26, par. 6 `[TI]`, applicables avec le chapitre III ; bonne pratique immédiate
- **Date d'application** : 2027-12-02 (CAL-011), non encore applicable ; conditionnel (CAL-013)
- **Conditions et exceptions** : Obligation future ; la recommandation immédiate relève de la bonne pratique.
- **Explication** : Sans journal, il est impossible d'expliquer ou de contester une note, de détecter une dérive après un changement de modèle ou de répondre à une demande d'autorité.
- **Recommandation** : Journal d'audit append-only : identifiant, horodatage, version du modèle servie, version du prompt et de la grille, paramètres, note proposée, décision humaine ; durée de conservation définie (au moins six mois pour les journaux au titre des obligations futures).
- **Méthode de vérification** : Revue du code de journalisation ; échantillon de journaux ; configuration de rétention.

### AIA-007 : Paramétrage non reproductible de la notation
- **Système d'IA concerné** : SYS-02 Correction automatique
- **Nature du constat** : Risque potentiel
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : `temperature=1.0`, sortie JSON non validée, absence d'évaluation des performances dans le dépôt.
- **Fichier(s) et lignes** : `app/grading.py:21`, `app/grading.py:27`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 15 (exactitude, robustesse) et art. 9 (essais) `[TI]`, applicables avec le chapitre III ; bonne pratique immédiate
- **Date d'application** : 2027-12-02 (CAL-011), non encore applicable
- **Conditions et exceptions** : n.a.
- **Explication** : Une même copie peut recevoir des notes différentes à chaque correction, et une réponse mal formée peut provoquer une erreur ou une note aberrante.
- **Recommandation** : Température basse, validation stricte de la sortie, campagne d'évaluation sur un jeu de copies notées par des enseignants, mesure par sous-groupes.
- **Méthode de vérification** : Rapport d'évaluation ; tests de reproductibilité ; tests de validation de schéma.

### AIA-008 : Documentation, analyse de classification et maîtrise de l'IA non observables
- **Système d'IA concerné** : Tous
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Moyenne
- **Niveau de confiance** : Faible
- **Preuve observée** : Fait observé : aucun document de classification, de documentation technique, de gestion des risques ou de formation dans le dépôt. Ce constat ne prouve pas leur absence dans l'organisation.
- **Fichier(s) et lignes** : non disponible
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Selon le système
- **Référence juridique** : Art. 4 `[TI]`, rédaction `[O26]` ; art. 11 et annexe IV `[TI]` (futur pour SYS-02)
- **Date d'application** : Art. 4 en vigueur (CAL-002) ; nouvelle rédaction en vigueur depuis le 2026-07-27 (CAL-003) ; art. 11 au 2027-12-02 (CAL-011)
- **Conditions et exceptions** : Art. 4 : obligation de prendre des mesures, sans niveau déterminé selon la nouvelle rédaction `[O26]`.
- **Explication** : Le règlement demande aux fournisseurs de prendre des mesures pour développer la maîtrise de l'IA de leur personnel ; ces mesures sont organisationnelles et ne se voient pas dans le code.
- **Recommandation** : Fournir le plan de formation et le registre associé ; préparer l'analyse de classification écrite de chaque système et la documentation technique de SYS-02.
- **Méthode de vérification** : Revue documentaire avec l'équipe ; entretien.

### AIA-009 : Effet de l'article 111, paragraphe 2, et établissements publics clients
- **Système d'IA concerné** : SYS-02 Correction automatique
- **Nature du constat** : À vérifier juridiquement ou organisationnellement
- **Gravité** : Information
- **Niveau de confiance** : Faible
- **Preuve observée** : Contexte déclaré : mise sur le marché le 2026-03-01, clients incluant des lycées (potentiellement publics).
- **Fichier(s) et lignes** : `README.md` (contexte)
- **Rôle réglementaire concerné** : Fournisseur ; déployeurs publics
- **Classification du système** : Haut risque probable
- **Référence juridique** : Art. 111, par. 2, tel que modifié par le règlement (UE) 2026/1744 `[O26]` (texte officiel relu)
- **Date d'application** : Conditionnel (CAL-013) : système mis sur le marché avant le 2027-12-02, donc soumis seulement en cas d'importantes modifications de sa conception à compter de cette date ; systèmes destinés aux autorités publiques : au plus tard le 2030-08-02
- **Conditions et exceptions** : Appréciation au niveau du type et du modèle (considérant 39 du règlement 2026/1744) ; la notion d'« importantes modifications » n'est pas définie : un changement de modèle sous-jacent pourrait en constituer une `[AV]`.
- **Explication** : Selon la date de mise sur le marché et la nature des clients, les exigences du haut risque peuvent s'appliquer plus tard, ou seulement après une évolution importante du système. Ce point dépend de faits non disponibles dans le dépôt (statut public des clients, historique des versions).
- **Recommandation** : Établir le statut public ou privé de chaque établissement client ; faire valider par un juriste la notion d'importantes modifications ; documenter la date de mise sur le marché par version ; définir une politique de gestion des modifications importantes.
- **Méthode de vérification** : Avis juridique ; registre des versions.

### AIA-010 : Obligations des fournisseurs de modèles GPAI
- **Système d'IA concerné** : Tous
- **Nature du constat** : Non applicable
- **Gravité** : Information
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : aucun script d'entraînement, d'affinage ou de publication de modèle ; modèles consommés via l'API d'OpenAI et une bibliothèque tierce.
- **Fichier(s) et lignes** : `requirements.txt:2-3`, `app/config.py:3-4`
- **Rôle réglementaire concerné** : Fournisseur du système (et non du modèle)
- **Classification du système** : n.a.
- **Référence juridique** : Art. 3, point 63 ; art. 53 et 55 `[TI]`
- **Date d'application** : 2025-08-02 (CAL-005), sans objet pour EduAssist
- **Conditions et exceptions** : Serait à réexaminer en cas d'entraînement ou d'affinage significatif de modèles.
- **Explication** : Les obligations relatives aux modèles d'IA à usage général pèsent sur le fournisseur du modèle (ici OpenAI), pas sur l'entreprise qui l'utilise via une API.
- **Recommandation** : Conserver la documentation transmise par le fournisseur du modèle (annexe XII) pour les besoins de la documentation de SYS-02.
- **Méthode de vérification** : Revue des scripts et pipelines à chaque audit.

### AIA-011 : Réponses textuelles du tuteur sans marquage lisible par machine
- **Système d'IA concerné** : SYS-01 Tuteur conversationnel
- **Nature du constat** : Non encore applicable
- **Gravité** : Moyenne
- **Niveau de confiance** : Élevée
- **Preuve observée** : Fait observé : le texte renvoyé par le modèle est transmis tel quel, sans métadonnée ni marquage de provenance, quel que soit le chemin de sortie (seul chemin observé : retour de fonction vers l'interface, non incluse dans la fixture).
- **Fichier(s) et lignes** : `app/tutor_chat.py:17-18`
- **Rôle réglementaire concerné** : Fournisseur
- **Classification du système** : Non à haut risque ; soumis à l'art. 50
- **Référence juridique** : Art. 50, par. 2 `[TI]` (contenus synthétiques textuels expressément visés) ; délai transitoire `[O26]`
- **Date d'application** : 2026-12-02 pour ce système mis sur le marché le 2026-03-01 (CAL-010)
- **Conditions et exceptions** : Exceptions examinées et écartées : le tuteur ne se limite pas à une assistance à la mise en forme standard et génère un contenu nouveau. L'incertitude sur les modalités de marquage d'un texte (lignes directrices du 20.7.2026) n'est pas une exemption : elle est consignée en NV-05.
- **Explication** : Les réponses rédigées par l'IA sont des contenus synthétiques textuels. Leur fournisseur doit prévoir un marquage lisible par machine permettant de les détecter, y compris dans une conversation. Pour ce système antérieur au 2 août 2026, l'obligation devient exigible le 2 décembre 2026.
- **Recommandation** : Définir le mécanisme de marquage des réponses pour chaque chemin de sortie (métadonnées de réponse d'API, attributs dans l'interface, gestion du copier-coller, exports) en s'appuyant sur le code de bonnes pratiques et les lignes directrices ; documenter les limites.
- **Méthode de vérification** : Inventaire des chemins de sortie (`templates/data-flow-map.md`) ; contrôle du marquage sur chaque chemin.

## 9. Éléments non vérifiables

| ID | Système | Élément manquant | Impact |
|---|---|---|---|
| NV-01 | Tous | Plan et registre de formation (art. 4) | AIA-008 |
| NV-02 | SYS-02 | Liste des établissements clients et statut public ou privé | AIA-009 |
| NV-03 | SYS-02 | Historique des versions et dates de mise sur le marché par version | AIA-009 |
| NV-04 | SYS-03 | Nature des images générées (personnes ou événements réels ?) | Art. 50, par. 4 |
| NV-05 | SYS-01 | Modalités techniques de marquage des textes conversationnels selon les lignes directrices du 20.7.2026 (l'obligation elle-même n'est pas en cause) | AIA-011 |
| NV-06 | SYS-04 | Statut de déploiement réel du module et pays concernés | AIA-001 |

## 10. Plan de remédiation (synthèse)

| Priorité | Constat(s) | Action | Base | Échéance | Effort |
|---|---|---|---|---|---|
| P1 | AIA-001 | Désactiver l'inférence d'émotions ; analyse juridique | Art. 5, par. 1, f) | Immédiate | S |
| P1 | AIA-002 | Information IA dans le tuteur, suppression de la persona | Art. 50, par. 1 | Immédiate | S |
| P1 | AIA-005 | Révocation et externalisation de la clé | Bonne pratique de sécurité | Immédiate | S |
| P2 | AIA-003, AIA-011 | Marquage des images et des textes, tests de robustesse par chemin de sortie | Art. 50, par. 2 | 2026-12-02 | M |
| P2 | AIA-004 | Validation humaine obligatoire des notes | Art. 14 (futur) ; risque actuel | 2027-12-02 | M |
| P3 | AIA-006, AIA-007 | Journal d'audit, épinglage, évaluation | Art. 9, 12, 15 (futurs) | 2027-12-02 | M |
| P3 | AIA-008, AIA-009 | Documentation, avis juridique sur l'art. 111 | Art. 4, 11 | Selon avis | L |

## 11. Matrice des preuves (extrait)

| PRV | Contrôle | Constat(s) | Fichier | Lignes | Commit | Date | Nature | Méthode de reproduction | État |
|---|---|---|---|---|---|---|---|---|---|
| PRV-001 | F1 | AIA-001 | `app/proctoring.py` | 9-10, 20-24 | fixture v1.1.0 | 2026-10-27 | Statique | `sed -n '1,30p' app/proctoring.py` | Non démontré (absence d'inférence d'émotions) |
| PRV-002 | A1, A2 | AIA-002 | `app/tutor_chat.py` | 8-18 | fixture v1.1.0 | 2026-10-27 | Statique | `sed -n '8,18p' app/tutor_chat.py` | Non démontré |
| PRV-003 | A4, A5 | AIA-003 | `app/illustrations.py` | 12-15 | fixture v1.1.0 | 2026-10-27 | Statique | `python3 scripts/scan_ai_signals.py . --json` (catégories `media_generation`, `output_channel`) | Non démontré |
| PRV-004 | B1, B3 | AIA-004 | `app/grading.py` | 27-28 | fixture v1.1.0 | 2026-10-27 | Statique | `sed -n '19,29p' app/grading.py` | Non démontré |
| PRV-005 | D8 | AIA-005 | `app/config.py` | 2 | fixture v1.1.0 | 2026-10-27 | Statique | `python3 scripts/scan_ai_signals.py .` (section « Secrets potentiels ») | Non démontré (valeur masquée) |
| PRV-006 | G1 | AIA-008 | n.a. | n.a. | fixture v1.1.0 | 2026-10-27 | Externe | Demande du plan de formation | Impossible à vérifier |
| PRV-007 | A4 | AIA-011 | `app/tutor_chat.py` | 17-18 | fixture v1.1.0 | 2026-10-27 | Statique | `sed -n '14,18p' app/tutor_chat.py` | Non démontré |

## 12. Limites de l'audit

- Analyse statique d'une fixture fictive ; aucune interface utilisateur ni configuration de production observée.
- Texte officiel relu le 2026-10-27 ; seule CAL-016 (date effective de l'art. 49, par. 2) reste à confirmer.
- Lignes directrices de la Commission sur l'article 50 et code de bonnes pratiques non relus directement.
- Projet de lignes directrices sur la classification à haut risque non définitif.
