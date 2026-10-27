# Obligations de transparence (article 50)

> Base : art. 50 du règlement (UE) 2024/1689 `[TI]` ; délai pour le par. 2 introduit par le règlement
> (UE) 2026/1744 `[O26]` (art. 111, par. 4 ; art. 50, par. 7 remplacé). Texte officiel relu. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50),
> lignes directrices de la Commission sur l'article 50 (20.7.2026, selon les sources),
> code de bonnes pratiques sur le marquage et l'étiquetage des contenus générés par IA (10.6.2026, volontaire).

## 1. Vue d'ensemble

| Par. | Débiteur | Situation | Obligation | Exceptions principales | Date |
|---|---|---|---|---|---|
| 1 | **Fournisseur** | Système destiné à **interagir directement** avec des personnes physiques | Concevoir et développer le système de sorte que les personnes soient **informées** qu'elles interagissent avec un système d'IA | Évident pour une personne raisonnablement informée, attentive et avisée, compte tenu des circonstances et du contexte ; systèmes autorisés par la loi à des fins répressives (sauf mise à disposition du public pour signaler une infraction) | 2026-08-02 |
| 2 | **Fournisseur** (y compris de systèmes d'IA à usage général) | Système **générant** des contenus synthétiques audio, image, vidéo ou **texte** | Sorties **marquées dans un format lisible par machine** et **détectables** comme générées ou manipulées artificiellement ; solutions techniques efficaces, interopérables, robustes et fiables dans la mesure du techniquement possible, compte tenu des types de contenus, des coûts et de l'état de l'art | Fonction d'assistance à la mise en forme standard ; absence de modification substantielle des données d'entrée ou de leur sémantique ; usages répressifs autorisés | 2026-08-02 ; **2026-12-02** pour les systèmes mis sur le marché avant le 2026-08-02 (art. 111, par. 4, ajouté par 2026/1744 ; texte officiel relu) |
| 3 | **Déployeur** | Système de **reconnaissance des émotions** ou de **catégorisation biométrique** | **Informer** les personnes exposées du fonctionnement du système | Usages répressifs autorisés ; le traitement de données sous-jacent relève d'autres textes (hors périmètre) | 2026-08-02 |
| 4, al. 1 | **Déployeur** | Système générant ou manipulant des **hypertrucages** (image, audio, vidéo) | **Déclarer** que le contenu a été généré ou manipulé artificiellement | Usages répressifs autorisés ; œuvre manifestement **artistique, créative, satirique, fictionnelle** ou analogue : obligation limitée à la divulgation de l'existence du contenu, de manière appropriée qui n'entrave pas l'affichage ou la jouissance de l'œuvre | 2026-08-02 |
| 4, al. 2 | **Déployeur** | **Texte** généré ou manipulé **publié dans le but d'informer le public sur des questions d'intérêt public** | Déclarer que le texte a été généré ou manipulé artificiellement | Usages répressifs autorisés ; contenu ayant fait l'objet d'un **examen humain ou d'un contrôle éditorial** et dont une personne assume la **responsabilité éditoriale** | 2026-08-02 |
| 5 | Fournisseur et déployeur | Toutes les informations des par. 1 à 4 | Fournies de manière **claire et reconnaissable**, **au plus tard lors de la première interaction ou exposition**, conformément aux exigences d'**accessibilité** applicables | n.a. | 2026-08-02 |

Paragraphe 6 : l'article 50 est sans préjudice du chapitre III et des autres obligations de
transparence du droit de l'Union ou national. Paragraphe 7 : codes de bonnes pratiques ; la
Commission a jugé, selon les sources, que le code du 10.6.2026 couvre adéquatement les par. 2, 4 et 5.

## 2. Trois notions à ne pas confondre

| Notion | Disposition | Débiteur | Forme | Destinataire |
|---|---|---|---|---|
| Transparence de l'interaction | Art. 50, par. 1 | Fournisseur | Information de la personne qu'elle interagit avec une IA | La personne qui interagit |
| Marquage machine et détectabilité | Art. 50, par. 2 | Fournisseur | Marquage lisible par machine des sorties (métadonnées, filigrane, empreinte...) | Outils de détection, plateformes, tiers |
| Mention visible | Art. 50, par. 3 et 4 (déployeur) ; par. 5 (modalités) | Déployeur (le fournisseur peut l'outiller) | Déclaration perceptible par l'humain | Le public exposé au contenu |

Une mesure de l'une de ces catégories ne satisfait pas les deux autres : un bandeau « assistant IA »
(par. 1) ne marque pas les sorties (par. 2), et une métadonnée (par. 2) n'informe pas le public (par. 4).

## 3. Ce qu'une simple mention « généré par IA » ne couvre pas

- Le **par. 2** exige un **marquage lisible par machine** et une **détectabilité** : une mention
  visible seule ne suffit pas. Selon les sources, le code de bonnes pratiques prévoit plusieurs
  couches (métadonnées, filigrane, autres techniques) lorsque nécessaire, et la Commission considère
  qu'aucune technique unique ne satisfait à elle seule les exigences `[O26]`.
- Le **par. 1** exige une information **au plus tard à la première interaction** : une mention en
  bas de page des CGU n'est pas une information claire au moment de l'interaction.
- Le **par. 5** exige accessibilité et caractère reconnaissable (contraste, lecteurs d'écran, langue).
- Les **par. 3 et 4** pèsent sur le **déployeur** : le fournisseur peut l'outiller (fonction
  d'étiquetage) mais l'obligation reste celle du déployeur.
- Une mention ne peut pas être contredite par le comportement du système (un assistant qui nie être
  une IA lorsqu'on le lui demande).

## 4. Checklist (conditionnelle)

### Interaction directe (par. 1), si un chatbot, un assistant vocal ou un agent conversant existe
- [ ] Message d'information affiché ou prononcé avant ou au début de la première interaction (preuve : fichier, ligne, capture).
- [ ] Le prompt système n'impose pas de se présenter comme humain ; le système répond qu'il est une IA si on le lui demande.
- [ ] Information présente sur tous les canaux (web, mobile, téléphone, messagerie, API exposée à des tiers).
- [ ] Exception « évident » invoquée ? Motivation écrite et contexte (rarement admissible pour un assistant à nom humain).

### Contenus synthétiques (par. 2), si le système génère texte, image, audio ou vidéo
- [ ] Marquage lisible par machine (métadonnées C2PA, IPTC `DigitalSourceType` = `trainedAlgorithmicMedia`, XMP, filigrane invisible, empreinte) : preuve dans le code.
- [ ] Le marquage survit au pipeline interne (redimensionnement, compression, ré-encodage) : tests présents ?
- [ ] Les marquages appliqués par le fournisseur du modèle en amont sont **préservés** et non supprimés.
- [ ] Moyen de détection documenté (outil de vérification, API).
- [ ] Exception « assistance à la mise en forme standard » ou « absence de modification substantielle » : motivée ?
- [ ] Textes, y compris les réponses conversationnelles : analysés au titre du par. 2 comme tout autre contenu (voir section 6).
- [ ] Inventaire des chemins de sortie réalisé (section 5) et marquage contrôlé pour chacun.
- [ ] Date de mise sur le marché connue (délai au 2026-12-02 ou non).

### Émotions et catégorisation biométrique (par. 3)
- [ ] Vérifier d'abord l'art. 5, par. 1, f) et g) et l'annexe III, point 1.
- [ ] Information des personnes exposées (déployeur).

### Hypertrucages (par. 4, al. 1)
- [ ] Le système permet-il de générer des contenus ressemblant à des personnes, lieux ou événements réels ?
- [ ] Fonction d'étiquetage visible proposée au déployeur ; consigne d'usage.
- [ ] Régime allégé pour les œuvres artistiques ou satiriques documenté.

### Textes d'intérêt public (par. 4, al. 2)
- [ ] Publication automatique de textes générés (actualités, communiqués) ?
- [ ] Circuit de relecture humaine et responsabilité éditoriale identifiée, sinon mention.

## 5. Module d'audit de l'article 50, paragraphe 2 : chemins de sortie

À dérouler pour **chaque** système générant ou manipulant des contenus. Objectif : vérifier que le
marquage existe au point de génération **et** qu'il survit jusqu'à chaque point de sortie. Consigner
le résultat dans `templates/data-flow-map.md`.

### 5.1 Inventaire obligatoire des chemins de sortie

Rechercher dans le code tous les chemins par lesquels une sortie générée quitte le système
(`scripts/scan_ai_signals.py`, catégorie `output_channel`, puis lecture du code) :

| Chemin | Indices techniques | Point de vigilance pour le marquage |
|---|---|---|
| Interface web ou mobile | Rendu de template, composant de chat, `innerHTML` | Texte affiché : marquage machine possible (métadonnées de réponse, attributs, API de provenance) ; mention visible distincte |
| API exposée à des tiers | Routes REST/GraphQL, `JSONResponse`, webhooks | Champ ou en-tête de provenance documenté ; préservé par le client ? |
| Copier-coller | `navigator.clipboard`, bouton « copier » | Le marquage du texte copié est généralement perdu : documenter la solution ou la limite |
| PDF | `reportlab`, `weasyprint`, `fpdf`, `pdfkit` | Métadonnées XMP du document, manifeste C2PA, mention |
| Tableur (Excel, CSV) | `openpyxl`, `xlsxwriter`, `to_csv`, `csv.writer` | CSV sans métadonnées : colonne ou fichier de provenance ; propriétés du classeur |
| Texte brut (TXT, Markdown) | `write_text`, `open(..., "w")` | Aucun support natif : mécanisme alternatif documenté |
| Courriel | `smtplib`, `send_mail`, SDK d'envoi | En-têtes, pièces jointes marquées, mention |
| HTML | Génération de pages, gabarits exportés | Balises `meta`, attributs, manifeste |
| SVG | Génération ou conversion SVG | Métadonnées `<metadata>` ; perte lors de la rastérisation |
| Images, audio, vidéo | `PIL.Image.save`, `write_bytes`, encodeurs | Préservation des métadonnées amont (le ré-encodage les supprime souvent), filigrane |

### 5.2 Contrôles par chemin

| Contrôle | Question | Preuve attendue |
|---|---|---|
| Mécanisme de provenance | Quel marquage est appliqué (standard ou propriétaire) ? | Code, configuration ; norme utilisée (C2PA, IPTC/XMP, filigrane) |
| Détectabilité | Un tiers peut-il détecter le caractère artificiel avec un outil disponible ? | Outil ou API de vérification documenté |
| Conservation après transformation | Le marquage survit-il aux post-traitements (redimensionnement, compression, conversion, export) ? | Tests automatisés de bout en bout |
| Marquage amont | Le marquage du fournisseur du modèle est-il préservé ? | Absence de suppression des métadonnées, tests |
| Outil de vérification | Existe-t-il une procédure ou un outil pour vérifier une sortie donnée ? | Documentation, script |
| Falsifiabilité | Le marquage est-il trivialement retirable ou imitable (clé texte libre, champ JSON non signé) ? | Analyse ; signature du manifeste |

Une case « mesure présente » à la génération mais « perdue » à l'export donne un constat sur le
chemin concerné, pas une conclusion favorable sur le système.

## 6. Qualification des constats

- Absence d'information pour un chatbot mis à disposition (règle commune avec
  `findings-methodology.md`, section 1) :
  - « **Constat technique avéré** » lorsque l'obligation est en vigueur, que le débiteur est identifié
    et qu'aucune exception n'est plausible (par exemple un prompt qui ordonne de nier être une IA) ;
    l'analyse juridique « manquement potentiel à l'art. 50, par. 1 » est rédigée à part, gravité **Élevée** ;
  - « **Risque potentiel** » lorsqu'une exception est plausible (caractère évident) ou que le débiteur
    n'est pas établi, gravité Moyenne.
- Absence de marquage pour un générateur antérieur au 2026-08-02, audité avant le 2026-12-02 :
  nature « **Non encore applicable** », gravité Moyenne, recommandation de préparation.
- Présence de métadonnées sans test de robustesse : « Constat technique avéré » (mesure présente)
  + « Risque potentiel » (efficacité non démontrée).
- Métadonnées « maison » (clés texte PNG personnalisées, champs propriétaires) au lieu d'un format
  standard lu par les outils de détection (XMP/IPTC, manifeste C2PA) : « Risque potentiel » sur
  l'interopérabilité et la détectabilité.
- **Textes, y compris conversationnels** : tout système générant des contenus textuels fait l'objet
  d'une analyse de l'art. 50, par. 2, y compris lorsqu'il s'agit de réponses conversationnelles. Le
  paragraphe vise expressément les contenus synthétiques textuels, et l'art. 111, par. 4 (délai
  transitoire) vise lui aussi les contenus « audio, image, vidéo ou texte ». Toute exception (assistance à la
  mise en forme standard, absence de modification substantielle des données d'entrée ou de leur
  sémantique, usage répressif autorisé) doit être motivée. Une incertitude sur les modalités
  techniques (format de marquage d'un texte, lignes directrices) **n'équivaut pas à une exemption** :
  l'absence de marquage est qualifiée comme pour les autres contenus (manquement potentiel si
  l'obligation est en vigueur, « Non encore applicable » sinon), et seule l'incertitude sur les
  modalités est consignée, à part, dans le registre des éléments non vérifiables.
