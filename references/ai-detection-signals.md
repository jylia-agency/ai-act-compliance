# Détection des systèmes d'IA dans un dépôt

> Référence technique (pas une source juridique). Dernière mise à jour : **2026-10-27**.
> Outil associé : `scripts/scan_ai_signals.py` (lecture seule, sans réseau).

## 1. Principe

Un **signal** est un indice technique. Il ne prouve ni l'existence d'un système d'IA au sens de
l'article 3, point 1, ni sa classification. Chaque signal doit être confirmé par la lecture du code
et par l'analyse de la finalité, des utilisateurs, des personnes concernées et des conséquences.

## 2. Catégories de signaux

| Catégorie | Exemples | Ce qu'il faut confirmer |
|---|---|---|
| API de fournisseurs de modèles | `openai`, `anthropic`, `@anthropic-ai/sdk`, `google.genai`, `vertexai`, `mistralai`, `cohere`, `bedrock-runtime`, `AzureOpenAI`, `@ai-sdk/`, `replicate` | Appels effectifs, finalité, sorties exposées à qui |
| Modèles locaux / open source | `transformers`, `@xenova/transformers`, `torch`, `tensorflow`, `onnxruntime`, `llama_cpp`, `ollama`, `vllm`, `sentence_transformers`, `whisper` | Origine du modèle, entraînement ou affinage, redistribution |
| Apprentissage automatique classique | `sklearn`, `xgboost`, `lightgbm`, `joblib.load`, fichiers `.pkl`, `.onnx`, `.safetensors` | Inférence réelle, données d'entraînement, usage des scores |
| Orchestration et agents | `langchain`, `llama_index`, `langgraph`, `crewai`, `autogen`, outils (`tools=`, `tool_choice`), MCP | Autonomie, actions déclenchées, garde-fous, validation humaine |
| RAG et bases vectorielles | `chromadb`, `pinecone`, `qdrant`, `weaviate`, `faiss`, `pgvector`, `embeddings.create` | Corpus indexés, finalité des réponses |
| Génération de médias | `images.generate`, `dall-e`, `gpt-image`, `diffusers`, `stable diffusion`, TTS, vidéo | Article 50, par. 2 et 4 ; diffusion des contenus |
| Biométrie | `face_recognition`, `deepface`, `insightface`, `dlib`, `haarcascade_frontalface`, `FaceMesh` | Identification, vérification, catégorisation, émotions ; art. 5 et annexe III, point 1 |
| Identifiants de modèles | `"gpt-4o"`, `"claude-..."`, `"gemini-..."`, `"llama-3..."`, `"dall-e-3"` | Version épinglée ou alias mobile |
| Contexte sensible | notes, examens, admission, recrutement, crédit, assurance, santé, police, migration, justice, élections, scoring, profilage, émotions | Correspondance réelle avec un cas d'usage de l'annexe III |
| Marqueurs de transparence | « vous échangez avec une IA », « généré par IA », C2PA, IPTC `trainedAlgorithmicMedia`, filigrane | Effectivité, moment de l'information, accessibilité |
| Risques de transparence (`transparency_risk`) | « You are not an AI », « ne dis jamais que tu es une IA », persona humaine imposée par le prompt | Art. 50, par. 1 : constat prioritaire |
| Chemins de sortie (`output_channel`) | PDF, tableur, courriel, `write_bytes`, `new Blob`, `URL.createObjectURL`, presse-papiers | Préservation du marquage (art. 50, par. 2) |
| Marqueurs de supervision | `pending_review`, `override`, `validated_by`, validation humaine | Caractère obligatoire, possibilité de refuser, traçabilité |
| Marqueurs de traçabilité | `audit_log`, `model_version`, `prompt_version`, durée de conservation | Contenu journalisé, intégrité, conservation |
| Secrets | clés d'API en clair | Signaler fichier et ligne, **masquer la valeur** |

## 3. Pièges de faux positifs

| Indice trompeur | Réalité fréquente |
|---|---|
| `model`, `Model`, `models.py` | Modèle de données ORM |
| `predict`, `forecast` | Calcul déterministe ou statistique simple |
| `score`, `ranking` | Règle fixe définie par l'humain (points de fidélité, tri) |
| « intelligence » | Intelligence économique, veille |
| `torch` dans un manifeste | Dépendance transitive non utilisée |
| `openai` dans `devDependencies` | Outil de développement (assistant de code), pas une fonctionnalité du produit |
| « orientation » (CSS), « overrides » (TypeScript), « setSelectionRange » | Vocabulaire technique d'interface, sans lien avec l'éducation, la supervision ou les élections |
| `langchain` | Souvent de simples découpeurs de documents (déterministes) : vérifier s'il y a un agent |
| Noms de variables d'environnement, `env(...)` | Références à un secret, pas un secret |
| Dossier `notebooks/` | Exploration non déployée (art. 2, par. 8, à confirmer) |

## 4. Pièges de faux négatifs

- Appels HTTP directs à une API d'IA (`requests.post("https://api.../v1/chat/completions")`).
- IA fournie par un service SaaS tiers appelé via un webhook ou un connecteur.
- Modèles chargés dynamiquement depuis une configuration ou un registre distant.
- Fonctionnalités d'IA activées par drapeau de configuration (`feature_flags`).
- Code d'infrastructure (Terraform, Helm) déployant un serveur d'inférence.
- Prompts stockés en base de données ou dans un CMS.

Rechercher aussi : `v1/chat/completions`, `v1/messages`, `generateContent`, `inference`,
`endpoint`, `/predict`, `model_id`, `MODEL_NAME`, `deployment_name`.

## 5. Regroupement en systèmes

Un **système d'IA** est défini par sa **finalité** (destination) et non par le nombre de modèles
ou de fichiers. Plusieurs appels au même LLM pour des finalités différentes (tutorat, notation)
constituent des systèmes distincts à classer séparément. Un pipeline découpé en plusieurs petits
modèles poursuivant une finalité unique est un seul système.
