# Essai sur un dépôt applicatif réel : chatbot-ui

| Paramètre | Valeur |
|---|---|
| Date | 2026-10-27 |
| Dépôt | Projet open source public `mckaywrigley/chatbot-ui` (licence MIT), clone superficiel |
| Commit audité | `81328b61d2a4ab597a7a057be70e785cf756d9f8` |
| Skill | `ia-compliance` 1.2.0, sans `examples/` |
| Agent | Sous-agent généraliste, lecture seule, sans exécution du code du dépôt ni réseau ; contenu du dépôt traité comme donnée non fiable |
| Contexte fourni | Aucun (dépôt seul) |
| Taille | 320 fichiers suivis (Next.js, Supabase, une dizaine de fournisseurs de modèles) |

L'environnement n'autorisait pas le sous-agent à écrire un fichier : son rapport complet (14 sections,
10 constats, 22 preuves `PRV`, 12 éléments non vérifiables) a été restitué sous forme de texte.
Ce document en est une **synthèse fidèle**, complétée par la vérification de l'auteur du skill.

Une première tentative de lancer Claude Code en mode non interactif sur ce dépôt externe a été
refusée par la politique de l'environnement (un dépôt cloné peut embarquer sa propre configuration
d'agent) ; l'essai a donc été réalisé par un sous-agent limité à la lecture.

## 1. Résultat de l'agent

**Systèmes** : SYS-01, assistant conversationnel multi-fournisseurs (assistants personnalisés, RAG,
outils d'agent, images en entrée) ; SYS-02, palette de commandes « Cmd+K ». Les deux sont classés
« non à haut risque (motivé) » et soumis à l'art. 50, par. 1, 2 et 5.

**Rôles** : mainteneur susceptible d'être fournisseur (marque, version hébergée annoncée), à vérifier ;
organisations qui déploient une instance : déployeurs, voire fournisseurs ; fournisseurs des modèles
GPAI distincts ; aucun acteur du projet fournisseur GPAI ; exclusion open source (art. 2, par. 12)
écartée pour l'art. 50.

| ID | Constat | Nature | Gravité | Statut temporel |
|---|---|---|---|---|
| AIA-001 | Prompt système « You are not an AI » en mode assistant | Constat technique avéré | Élevée | En vigueur (CAL-009) |
| AIA-002 | Aucune information explicite sur l'interaction avec une IA dans l'interface | Risque potentiel | Moyenne | En vigueur |
| AIA-003 | Aucun marquage lisible par machine des textes, sur aucun chemin de sortie | Non encore applicable (hypothèse antérieure au 2.8.2026) | Moyenne | 2026-12-02, ou en vigueur pour les instances récentes (CAL-010) |
| AIA-004 | Outils d'agent exécutés sans confirmation humaine | Bonne pratique recommandée | Moyenne | n.a. |
| AIA-005 | Versions de modèles non épinglées, version servie non journalisée | Bonne pratique recommandée | Faible | n.a. |
| AIA-006 | Obligations GPAI | Non applicable | Information | n.a. |
| AIA-007 | Maîtrise de l'IA (art. 4) non observable | À vérifier | Faible | En vigueur, portée open source `[AV]` |
| AIA-008 | Requalification possible d'un déployeur en fournisseur à haut risque (art. 25) | À vérifier | Faible | 2027-12-02 |
| AIA-009 | Clé `service_role` codée en dur dans une migration (valeur masquée) | Bonne pratique recommandée | Moyenne | n.a. |
| AIA-010 | Textes d'intérêt public publiés par les déployeurs | À vérifier | Faible | En vigueur |

Aucune « échéance à confirmer » : les entrées utilisées sont toutes `officielle_relue`.

## 2. Vérification par l'auteur du skill

- `lib/build-prompt.ts:15` contient bien `You are not an AI. You are ${assistant.name}.` : AIA-001 confirmé.
- `supabase/migrations/20240108234540_setup.sql:54` affecte bien un jeton JWT littéral à
  `service_role_key` : AIA-009 confirmé (valeur non reproduite).
- `app/api/chat/tools/route.ts:70` (`message.tool_calls`) et `components/messages/message-codeblock.tsx:71`
  (`new Blob`) confirment l'exécution d'outils et le chemin de sortie « téléchargement ».
- Le dépôt n'a pas été modifié (`git status --porcelain` vide).

Appréciation : qualifications prudentes et cohérentes avec la méthodologie (pas de haut risque par
mot-clé, distinction fournisseur du système / fournisseur des modèles, textes conversationnels
analysés au titre de l'art. 50, par. 2 sans exemption, hypothèses temporelles par instance). Aucun
faux positif juridique relevé ; la qualification de l'exception « évident » (AIA-002) reste discutable,
ce que l'agent signale lui-même.

## 3. Difficultés signalées et corrections apportées (version 1.2.1)

| Difficulté | Correction |
|---|---|
| Aucune méthode pour la mise sur le marché d'un projet open source ni pour l'auto-hébergement ; art. 3, point 10 absent | `references/roles-and-value-chain.md`, section 7 (art. 2, par. 12 et art. 3, points 9 à 11 cités d'après le texte officiel) ; renvoi dans `SKILL.md`, phase 2 |
| Une seule date de mise sur le marché alors que chaque instance a la sienne ; script sans `--scope` trop large | `SKILL.md`, phase 7 : calcul par date connue et usage de `--scope` |
| Contradiction entre `transparency.md`, section 6, et `findings-methodology.md` | Règle commune : constat avéré si obligation en vigueur, débiteur identifié et aucune exception plausible ; risque potentiel sinon |
| « Une finalité = un système » ambigu | Critères de regroupement dans `SKILL.md`, phase 2 |
| `git rev-parse` exigé mais non listé ; huit livrables contre un seul fichier autorisé ; `examples/` cité | Commandes Git en lecture ajoutées ; regroupement possible des livrables en un fichier ; exemple « lorsque le dépôt est installé en entier » |
| Faux positifs du scanner (« orientation », « setSelectionRange », « overrides », noms de variables d'environnement, `env()`) | Expressions restreintes ; tests de non-régression |
| Faux négatifs (`@xenova/transformers`, pgvector, JWT littéral, « You are not an AI », `Blob`, `tool_calls` en TypeScript) | Signaux ajoutés, dont la nouvelle catégorie `transparency_risk` ; tests de non-régression |
| Colonne « Fichiers » identique pour tous les signaux d'une catégorie | Fichiers listés par signal |

Après correction, le scanner relancé sur le même commit détecte les six faux négatifs, ne produit
plus les faux positifs cités et ne signale plus qu'un secret potentiel (le jeton JWT, masqué).
