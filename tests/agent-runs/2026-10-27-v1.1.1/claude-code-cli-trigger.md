# Test d'intégration Claude Code (CLI) : découverte et déclenchement du skill

| Paramètre | Valeur |
|---|---|
| Date | 2026-10-27 |
| Outil | Claude Code 2.1.312, mode non interactif (`claude -p`) |
| Mode de permission | `plan` (lecture seule imposée par l'agent) |
| Installation | Skill copié dans `<projet>/.claude/skills/ia-compliance/` |
| Projet | Copie de la fixture `demo-ai-vulnerable` sans `EXPECTED.md`, initialisée en dépôt Git |
| Invite | « Est-ce que ce projet pose problème au regard du règlement européen sur l'intelligence artificielle ? Fais un audit rapide (résumé exécutif, inventaire, constats principaux), date d'audit 2026-10-27. » (le skill n'est pas nommé) |
| Résultat | `success`, 8 tours |

## Vérifications

- Découverte : `ia-compliance` apparaît dans la liste des skills du projet (invite séparée « Liste uniquement les noms des skills disponibles »).
- Déclenchement automatique : premier appel d'outil = `Skill(ia-compliance)`.
- Lecture seule : `git status --porcelain` vide après l'exécution.
- Secret de la fixture absent de la réponse ; règle « échéance à confirmer » appliquée.

## Appels d'outils (chemins anonymisés)

| # | Outil | Paramètre principal |
|---|---|---|
| 1 | Skill | `ia-compliance` |
| 2 | Bash | `cd <projet>; git rev-parse HEAD; git ls-files / grep -v '^.claude/' / head -100; S=.claude/skills/ia-compliance; ls $S $S/references $S/scripts; grep -m3 last_v` |
| 3 | Bash | `cd <projet>; for f in README.md requirements.txt app/*.py; do echo "=== $f"; cat -n $f; done` |
| 4 | Bash | `cd <projet>; S=.claude/skills/ia-compliance; python3 $S/scripts/scan_ai_signals.py . 2>&1 / head -80; python3 $S/scripts/obligation_timeline.py --help 2>&1 / he` |
| 5 | Bash | `cd <projet>; S=.claude/skills/ia-compliance; python3 $S/scripts/obligation_timeline.py --audit-date 2026-10-27 --placed-on-market 2026-03-01 2>&1 / grep -E "CAL` |
| 6 | Bash | `cd <projet>/.claude/skills/ia-compliance; sed -n 1,200p references/transparency.md / head -150; grep -n -A12 "par. 3\/Article 6, par" references/risk-classifica` |

## Réponse finale de l'agent (brute, cadratins normalisés)

# Audit AI Act rapide d'EduAssist (date d'audit : 2026-10-27)

**Réponse courte : oui, le projet pose un problème sérieux.** Un module semble relever d'une pratique interdite depuis février 2025. Un autre enfreint probablement une obligation de transparence en vigueur depuis août 2026. Deux modules à haut risque devront être largement revus d'ici fin 2027.

Le README indique que le projet est **fictif** (jeu de test volontairement défectueux). L'audit le traite comme s'il était réel.

## Cadrage

| Paramètre | Valeur |
|---|---|
| Commit audité | `a97a4a8cf76f06a0ea75dac6c291d60d4fd2e6f5` |
| Périmètre | `app/`, `README.md`, `requirements.txt` (le dossier `.claude/` est exclu) |
| Contexte (selon le README) | Société française (fictive) EduAssist SAS. Produit vendu sous sa marque à des lycées et universités de l'UE. Mise sur le marché le 2026-03-01. Modèles OpenAI appelés par API, aucun entraînement en interne. |
| Base juridique | Règlement (UE) 2024/1689, modifié par le règlement (UE) 2026/1744. Calendrier du skill vérifié le 2026-10-27. |
| Méthode | Lecture du code, plus les scripts `scan_ai_signals.py` et `obligation_timeline.py` (lecture seule) |

## 1. Résumé exécutif

- **Point critique, surveillance d'examens** (`app/proctoring.py`) : le module détecte les émotions des élèves par webcam (DeepFace), puis annule automatiquement leur copie. C'est **potentiellement une pratique interdite** : la reconnaissance des émotions dans un établissement d'enseignement est visée à l'art. 5, par. 1, f), applicable depuis le 2025-02-02. Le seul but de lutter contre la fraude ne rentre pas dans l'exception « raisons médicales ou de sécurité ».
- **Point élevé, tuteur conversationnel** (`app/tutor_chat.py`) : le prompt système demande au modèle de se présenter comme une enseignante humaine et de nier être une IA. C'est un **manquement potentiel à l'art. 50, par. 1**, en vigueur depuis le 2026-08-02.
- **Point élevé, correction automatique** (`app/grading.py`) : la note du modèle est publiée telle quelle dans le bulletin, sans relecture. Le système est **probablement à haut risque** (annexe III, point 3, b)). Les exigences s'appliqueront à partir du **2027-12-02 (échéance à confirmer)**. Comme le module est déjà sur le marché, le régime transitoire de l'art. 111, par. 2 reste incertain.
- **Point moyen, illustrations** (`app/illustrations.py`) : les images générées ne portent aucun marquage lisible par machine. L'obligation de l'art. 50, par. 2 s'appliquera le **2026-12-02 (échéance à confirmer)**, soit dans 36 jours. Le même calendrier vaut pour les textes du tuteur.
- **Rôles** : EduAssist est **fournisseur** des quatre systèmes d'IA. Les établissements en sont les **déployeurs**. OpenAI est le **fournisseur des modèles GPAI** sous-jacents. Les obligations propres aux fournisseurs de modèles GPAI ne s'appliquent pas à EduAssist.
- **Constats dont la date reste à confirmer** (règle de prudence sur les sources) : AIA-003, AIA-004, AIA-005, AIA-006.

> Ce rapport est une aide à l'audit. Il ne certifie aucune conformité et ne remplace ni l'avis d'un juriste ni une évaluation de conformité au sens de l'art. 43.

## 2. Inventaire des systèmes d'IA

| ID | Système | Composants | Modèle | Sortie et effet | Personnes concernées | Rôle d'EduAssist | Classification |
|---|---|---|---|---|---|---|---|
| SIA-1 | Tuteur conversationnel | `app/tutor_chat.py` | `gpt-4o` (alias, version non figée), API OpenAI | Texte, information | Élèves, souvent mineurs | Fournisseur | Non à haut risque si aucun usage pour évaluer ; soumis à l'art. 50, par. 1 et 2 |
| SIA-2 | Correction des dissertations | `app/grading.py`, `app/gradebook.py` | `gpt-4o`, `temperature=1.0` | Note finale **décidée automatiquement**, publiée dans le bulletin | Élèves | Fournisseur | **Haut risque probable** (annexe III, 3 b)) ; la dérogation de l'art. 6, par. 3 est écartée car la note est directement fixée par le modèle |
| SIA-3 | Illustrations de cours | `app/illustrations.py` | `dall-e-3` | Images enregistrées sans métadonnées | Élèves (qui voient les images) | Fournisseur | Non à haut risque ; art. 50, par. 2 (et par. 4 pour le déployeur, si hypertrucage) |
| SIA-4 | Surveillance d'examens | `app/proctoring.py` | DeepFace (émotions), OpenCV, exécutés localement | **Annulation automatique** de l'examen | Élèves | Fournisseur | **Pratique potentiellement interdite** (art. 5, 1, f)) ; en plus, haut risque probable (annexe III, 3 d)) |

## 3. Constats principaux

### AIA-001 : reconnaissance des émotions des élèves pendant les examens
- **Système concerné** : SIA-4. **Nature** : risque potentiel (pratique interdite). **Gravité** : Critique. **Confiance** : élevée sur les faits, moyenne sur la qualification.
- **Preuves** :
  - `app/proctoring.py:9` : `DeepFace.analyze(..., actions=["emotion"])`.
  - `app/proctoring.py:5,20-23` : les émotions « fear / angry / surprise » sont comptées, et au-delà de 30 images, l'examen est annulé.
  - `requirements.txt:3` : dépendance `deepface`.
- **Rôles concernés** : EduAssist (mise sur le marché) et les établissements (utilisation).
- **Référence** : art. 5, par. 1, f). **Applicable depuis** le 2025-02-02. Aucune période de transition.
- **Exception examinée** (raisons médicales ou de sécurité) : non retenue. La finalité visible est la détection de fraude, et l'exception s'interprète strictement.
- **Explication** :
  - Le fait : le code déduit des émotions à partir du visage des élèves, dans un examen d'établissement d'enseignement, et en tire une sanction.
  - La conclusion juridique : il s'agit plausiblement d'une pratique interdite.
- **Recommandation (obligation)** :
  - Désactiver tout de suite l'analyse des émotions dans l'UE, dans l'attente d'un avis juridique.
  - La remplacer par une surveillance sans inférence d'émotions, avec une décision humaine.
- **Vérification** : finalité documentée, configuration de production, liste des établissements où le module est activé.

### AIA-002 : tuteur qui se fait passer pour une enseignante humaine
- **Système concerné** : SIA-1. **Nature** : constat technique avéré, avec un manquement potentiel. **Gravité** : Élevée. **Confiance** : élevée.
- **Preuve** : `app/tutor_chat.py:8-11`. Le prompt système contient : « Ne dis jamais que tu es une intelligence artificielle. Si on te le demande, réponds que tu es une enseignante. »
- **Référence** : art. 50, par. 1 et 5 (fournisseur). **Applicable depuis** le 2026-08-02 (confiance élevée).
- **Exception examinée** (caractère « évident » de l'IA) : écartée. Un nom humain et un démenti explicite rendent ce caractère tout sauf évident.
- **Autre disposition examinée** : la manipulation trompeuse (art. 5, par. 1, a)) n'est pas retenue en l'état, faute d'éléments sur une altération substantielle du comportement ou un préjudice important. Le public mineur appelle toutefois la vigilance.
- **Recommandation (obligation)** :
  - Retirer cette consigne du prompt.
  - Afficher une information claire dès la première interaction.
  - Vérifier que l'assistant reconnaît être une IA quand on le lui demande.

### AIA-003 : note finale attribuée par le modèle, sans contrôle humain
- **Système concerné** : SIA-2. **Nature** : non encore applicable, plus un risque potentiel. **Gravité** : Élevée. **Confiance** : élevée sur les faits, moyenne sur la qualification.
- **Preuves** :
  - `app/grading.py:3-4` : « note finale… compte pour le passage en classe supérieure ».
  - `app/grading.py:21` : `temperature=1.0`, donc une note non reproductible.
  - `app/grading.py:28` : publication immédiate, sans relecture.
  - `app/config.py:3` : alias de modèle non figé.
  - Aucune journalisation.
- **Référence** : annexe III, point 3, b). Exigences du chapitre III : supervision humaine (art. 14), journalisation (art. 12), documentation technique (art. 11), exactitude (art. 15).
- **Date d'application** : **2027-12-02, échéance à confirmer**. Le module ayant été mis sur le marché le 2026-03-01, l'art. 111, par. 2 s'appliquerait : les obligations ne joueraient qu'en cas de modification importante de la conception (confiance faible, à vérifier).
- **Recommandation (préparation)** :
  - Faire de la note une **proposition** que l'enseignant valide ou corrige.
  - Fixer la température à 0 et figer la version du modèle.
  - Journaliser la proposition du modèle et la décision humaine.
  - Mesurer les écarts de notation selon les sous-groupes d'élèves.

### AIA-004 : surveillance d'examens à haut risque avec annulation automatique
- **Système concerné** : SIA-4. **Nature** : non encore applicable. **Gravité** : Élevée.
- **Preuve** : `app/proctoring.py:22-24`, annulation « sans intervention humaine ».
- **Référence** : annexe III, point 3, d) et art. 14. **Date** : 2027-12-02, **échéance à confirmer**, avec la même réserve sur l'art. 111, par. 2.
- **Explication** : même une fois l'analyse des émotions retirée (AIA-001), la surveillance resterait probablement à haut risque.
- **Recommandation** : aucune annulation sans examen humain ; prévoir une voie de contestation.

### AIA-005 : contenus générés sans marquage lisible par machine
- **Systèmes concernés** : SIA-3 (images) et SIA-1 (textes). **Nature** : non encore applicable. **Gravité** : Moyenne. **Confiance** : élevée.
- **Preuve** : `app/illustrations.py:14-15`, l'image est décodée et écrite telle quelle, sans métadonnées C2PA ni IPTC. Le tuteur ne marque pas non plus ses réponses.
- **Référence** : art. 50, par. 2. **Date** : **2026-12-02, échéance à confirmer**. Le régime transitoire s'applique car la mise sur le marché est antérieure au 2026-08-02. L'obligation arrive dans 36 jours.
- **Recommandation** :
  - Ajouter un marquage standard (C2PA, IPTC `trainedAlgorithmicMedia`).
  - Conserver le marquage déjà appliqué par le fournisseur du modèle.
  - Tester que le marquage survit à l'export.
  - Proposer aux établissements une fonction d'étiquetage visible pour d'éventuels hypertrucages (art. 50, par. 4, à vérifier selon les contenus).

### AIA-006 : maîtrise de l'IA (art. 4)
- **Nature** : à vérifier sur le plan organisationnel. **Gravité** : Moyenne.
- **Constat** : aucun élément dans le dépôt, ce qui ne prouve pas un manquement.
- **Date** : l'article est en vigueur. Sa rédaction modifiée s'applique depuis le 2026-07-27, **échéance à confirmer**.
- **À fournir** : actions de formation des équipes d'EduAssist et informations remises aux établissements.

### AIA-007 : clé d'API en clair dans le code
- **Nature** : bonne pratique recommandée (sécurité, hors AI Act). **Gravité** : Faible.
- **Preuve** : `app/config.py:2` = `[SECRET MASQUÉ]` (le README la présente comme fictive).
- **Recommandation** : passer par une variable d'environnement ou un coffre-fort de secrets.

### Non applicable : obligations des fournisseurs de modèles GPAI (chapitre V)
EduAssist n'entraîne ni n'affine aucun modèle (README, ligne 12). Le fournisseur des modèles GPAI est OpenAI.

## 4. Éléments impossibles à vérifier depuis le dépôt

1. **Finalité réelle du module de surveillance** : un usage médical ou de sécurité est-il invoqué ? Est-il actif en production dans l'UE ?
2. **Configuration de production** : prompts réellement utilisés, modules activés selon les établissements.
3. **Réutilisation des échanges** : les conversations avec le tuteur servent-elles à noter ou à orienter les élèves ?
4. **Statut des établissements clients** : établissements publics ou non (art. 27, échéances propres aux autorités publiques).
5. **Documents hors dépôt** : contrats avec OpenAI, documentation des modèles, notice d'utilisation, informations aux élèves et aux familles, formations au titre de l'art. 4.
6. **Évolutions de conception** depuis le 2026-03-01 : elles conditionnent le régime de l'art. 111, par. 2.
7. **Modalités techniques** du marquage des textes et lignes directrices de la Commission : elles évoluent encore, sans que cela dispense de l'obligation.

## Limites

- Audit statique : ni le comportement réel du système ni les données de production n'ont été observés.
- Plusieurs dates issues du règlement 2026/1744 proviennent de sources secondaires et doivent être confirmées au Journal officiel.
- Actes d'exécution, normes harmonisées et lignes directrices sont encore en cours d'élaboration.

**Priorités** :
1. Désactiver l'analyse des émotions (AIA-001), sans attendre.
2. Corriger le prompt du tuteur (AIA-002), sans attendre.
3. Mettre en place le marquage des contenus avant le 2026-12-02 (AIA-005).
4. Préparer la mise en conformité des modules de correction et de surveillance au régime du haut risque (AIA-003, AIA-004).

Je n'ai modifié aucun fichier du projet. Si vous le souhaitez, je peux produire les autres livrables : matrice des obligations, plan de remédiation et cartographie des flux.
