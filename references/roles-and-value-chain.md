# Rôles réglementaires et chaîne de valeur

> Base : art. 3, 22 à 25, 54 du règlement (UE) 2024/1689 `[TI]`. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 25](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-25).

## 1. Principe

Les obligations dépendent du **rôle** tenu à l'égard de **chaque** système ou modèle. Une même
organisation peut cumuler plusieurs rôles (fournisseur d'un système et déployeur d'un autre ;
fournisseur et déployeur du même système utilisé en interne). Le rôle ne se déduit **jamais** de la
seule utilisation d'une API ou d'une bibliothèque.

## 2. Arbre de détermination (par système)

1. **L'organisation développe-t-elle le système d'IA (ou le fait-elle développer) et le met-elle sur
   le marché ou en service sous son propre nom ou sa propre marque ?** (art. 3, point 3)
   - Oui : **fournisseur du système d'IA**, y compris si le système repose sur l'API d'un tiers
     et y compris pour un usage interne (mise en service pour usage propre, art. 3, point 11).
   - Non : passer à 2.
2. **L'organisation utilise-t-elle le système sous sa propre autorité, dans un cadre professionnel ?**
   (art. 3, point 4) : **déployeur**.
3. **L'organisation est-elle établie dans l'Union et met-elle sur le marché un système portant le
   nom ou la marque d'une personne établie hors de l'Union ?** (art. 3, point 6) : **importateur**.
4. **L'organisation met-elle le système à disposition sans être fournisseur ni importateur ?**
   (art. 3, point 7) : **distributeur**.
5. **L'organisation a-t-elle reçu un mandat écrit d'un fournisseur établi hors de l'Union ?**
   (art. 3, point 5 ; art. 22 pour le haut risque ; art. 54 pour les modèles GPAI) : **mandataire**.
6. **L'organisation développe-t-elle un modèle d'IA à usage général et le met-elle sur le marché**
   (publication des poids, API, intégration dans ses produits mis sur le marché) ? :
   **fournisseur de modèle GPAI** (art. 3, points 3 et 63). Voir `gpai-obligations.md`.
7. **Fabricant de produits** (art. 25, par. 3) : un fabricant d'un produit relevant de l'annexe I,
   section A, qui intègre un système d'IA à haut risque comme composant de sécurité sous son nom est
   considéré comme fournisseur.

## 3. Requalification en fournisseur (art. 25, par. 1) `[TI]`

Un distributeur, importateur, déployeur ou autre tiers est considéré comme **fournisseur d'un
système d'IA à haut risque** s'il :

- a) appose son nom ou sa marque sur un système à haut risque déjà mis sur le marché ou en service
  (sans préjudice d'arrangements contractuels) ;
- b) apporte une **modification substantielle** à un système à haut risque de sorte qu'il reste à
  haut risque ;
- c) **modifie la destination** d'un système d'IA, y compris d'un système d'IA à usage général, non
  classé à haut risque, de telle manière qu'il devient à haut risque.

Le fournisseur initial n'est alors plus considéré comme fournisseur de ce système spécifique, mais
doit coopérer (art. 25, par. 2), sauf s'il a clairement exclu la transformation en système à haut
risque.

Exemple d'audit : une application qui détourne un assistant généraliste (système d'IA à usage
général d'un tiers) pour trier des candidatures à un emploi modifie sa destination et peut devenir
fournisseur d'un système à haut risque de l'annexe III, point 4, a) `[TI]`.

## 4. Distinction impérative : système d'IA et modèle GPAI

| Situation | Fournisseur du système d'IA | Fournisseur du modèle GPAI |
|---|---|---|
| Une société intègre l'API d'un fournisseur de LLM dans son logiciel vendu sous sa marque | La société | Le fournisseur du LLM |
| Une société utilise en interne un chatbot acheté à un éditeur | L'éditeur (la société est déployeur) | Le fournisseur du modèle |
| Une société affine (fine-tuning) un modèle ouvert et publie le modèle obtenu | La société, pour ses systèmes | Possiblement la société pour le modèle modifié, selon l'ampleur de la modification `[AV]` |
| Une société utilise un modèle local open source sans le redistribuer, dans un produit vendu | La société | L'auteur du modèle ; la société n'est pas fournisseur de modèle GPAI du seul fait de l'intégration |

Les lignes directrices de la Commission de juillet 2025 sur les modèles GPAI retiennent, selon les
sources, qu'un opérateur qui modifie un modèle devient fournisseur du modèle modifié lorsque la
modification mobilise une part significative de la puissance de calcul d'entraînement initiale
(indicateur : plus d'un tiers) `[AV]`. Ne jamais l'affirmer sans avoir les informations de calcul.

## 5. Informations à rechercher dans le dépôt et à demander

| Information | Où la chercher | Si absente |
|---|---|---|
| Nom commercial, marque, éditeur | README, `package.json`, mentions légales, interface | À demander |
| Clients et utilisateurs (internes, B2B, grand public) | Documentation, CGU, configuration multi-locataires | À demander |
| Établissement de l'organisation et du fournisseur du modèle | Contrats (hors dépôt) | À demander |
| Entraînement ou affinage de modèles | Scripts `train`, `fine_tune`, jeux de données, poids | Constat technique |
| Publication de modèles ou de poids | Registres de modèles, `huggingface_hub.upload`, releases | Constat technique |
| Modification de la destination d'un système tiers | Prompts système, cas d'usage | Analyse |

## 6. Formulations à utiliser

- Correct : « Au vu des éléments observés (marque EduAssist, commercialisation auprès
  d'établissements), EduAssist est **susceptible d'être fournisseur** du système d'IA X (art. 3,
  point 3). Elle n'est pas, au vu du dépôt, fournisseur du modèle GPAI sous-jacent. »
- Incorrect : « EduAssist utilise GPT-4o, elle est donc fournisseur GPAI. »
- Incorrect : « EduAssist utilise une API, elle est donc simple déployeur. »
