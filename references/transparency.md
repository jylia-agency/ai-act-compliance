# Obligations de transparence (article 50)

> Base : art. 50 du règlement (UE) 2024/1689 `[TI]` ; délai pour le par. 2 introduit par le règlement
> (UE) 2026/1744 `[O26]`. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50),
> lignes directrices de la Commission sur l'article 50 (20.7.2026, selon les sources),
> code de bonnes pratiques sur le marquage et l'étiquetage des contenus générés par IA (10.6.2026, volontaire).

## 1. Vue d'ensemble

| Par. | Débiteur | Situation | Obligation | Exceptions principales | Date |
|---|---|---|---|---|---|
| 1 | **Fournisseur** | Système destiné à **interagir directement** avec des personnes physiques | Concevoir et développer le système de sorte que les personnes soient **informées** qu'elles interagissent avec un système d'IA | Évident pour une personne raisonnablement informée, attentive et avisée, compte tenu des circonstances et du contexte ; systèmes autorisés par la loi à des fins répressives (sauf mise à disposition du public pour signaler une infraction) | 2026-08-02 |
| 2 | **Fournisseur** (y compris de systèmes d'IA à usage général) | Système **générant** des contenus synthétiques audio, image, vidéo ou **texte** | Sorties **marquées dans un format lisible par machine** et **détectables** comme générées ou manipulées artificiellement ; solutions techniques efficaces, interopérables, robustes et fiables dans la mesure du techniquement possible, compte tenu des types de contenus, des coûts et de l'état de l'art | Fonction d'assistance à la mise en forme standard ; absence de modification substantielle des données d'entrée ou de leur sémantique ; usages répressifs autorisés | 2026-08-02 ; **2026-12-02** pour les systèmes mis sur le marché avant le 2026-08-02 `[O26]` |
| 3 | **Déployeur** | Système de **reconnaissance des émotions** ou de **catégorisation biométrique** | **Informer** les personnes exposées du fonctionnement du système | Usages répressifs autorisés ; le traitement de données sous-jacent relève d'autres textes (hors périmètre) | 2026-08-02 |
| 4, al. 1 | **Déployeur** | Système générant ou manipulant des **hypertrucages** (image, audio, vidéo) | **Déclarer** que le contenu a été généré ou manipulé artificiellement | Usages répressifs autorisés ; œuvre manifestement **artistique, créative, satirique, fictionnelle** ou analogue : obligation limitée à la divulgation de l'existence du contenu, de manière appropriée qui n'entrave pas l'affichage ou la jouissance de l'œuvre | 2026-08-02 |
| 4, al. 2 | **Déployeur** | **Texte** généré ou manipulé **publié dans le but d'informer le public sur des questions d'intérêt public** | Déclarer que le texte a été généré ou manipulé artificiellement | Usages répressifs autorisés ; contenu ayant fait l'objet d'un **examen humain ou d'un contrôle éditorial** et dont une personne assume la **responsabilité éditoriale** | 2026-08-02 |
| 5 | Fournisseur et déployeur | Toutes les informations des par. 1 à 4 | Fournies de manière **claire et reconnaissable**, **au plus tard lors de la première interaction ou exposition**, conformément aux exigences d'**accessibilité** applicables | n.a. | 2026-08-02 |

Paragraphe 6 : l'article 50 est sans préjudice du chapitre III et des autres obligations de
transparence du droit de l'Union ou national. Paragraphe 7 : codes de bonnes pratiques ; la
Commission a jugé, selon les sources, que le code du 10.6.2026 couvre adéquatement les par. 2, 4 et 5.

## 2. Ce qu'une simple mention « généré par IA » ne couvre pas

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

## 3. Checklist (conditionnelle)

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
- [ ] Textes conversationnels : position documentée au regard des lignes directrices de la Commission `[AV]`.
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

## 4. Qualification des constats

- Absence d'information pour un chatbot mis à disposition : fait « Constat technique avéré » +
  « manquement potentiel à l'art. 50, par. 1 », gravité **Élevée**, à la date d'audit postérieure au 2026-08-02.
- Absence de marquage pour un générateur antérieur au 2026-08-02, audité avant le 2026-12-02 :
  nature « **Non encore applicable** », gravité Moyenne, recommandation de préparation.
- Présence de métadonnées sans test de robustesse : « Constat technique avéré » (mesure présente)
  + « Risque potentiel » (efficacité non démontrée).
