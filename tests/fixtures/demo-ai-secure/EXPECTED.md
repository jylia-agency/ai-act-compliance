# Résultats attendus : demo-ai-secure

Date d'audit de référence : **2026-10-27**.
Contexte déclaré : voir `README.md` et `docs/`. Tuteur et correction assistée mis sur le marché le
2026-03-01 ; module d'illustrations mis sur le marché le **2026-09-15** (après le 2026-08-02).

## 1. Systèmes d'IA attendus dans l'inventaire

| Système | Classification attendue | Confiance |
|---|---|---|
| SYS-01 Tuteur conversationnel | Non à haut risque ; art. 50, par. 1 | Élevée |
| SYS-02 Correction assistée | Haut risque probable (annexe III, point 3, b)), conclusion interne de l'éditeur cohérente ; obligations non encore applicables | Moyenne |
| SYS-03 Illustrations | Non à haut risque ; art. 50, par. 2 **applicable dès la mise sur le marché** (2026-09-15) | Élevée |
| `app/exam_events.py` | **Pas un système d'IA** (journalisation déterministe d'événements) | Élevée |

Rôles : EduAssist fournisseur des systèmes d'IA ; établissements déployeurs ; Anthropic et le
fournisseur d'images : fournisseurs de modèles. EduAssist n'est pas fournisseur de modèle GPAI.

## 2. Constats attendus

| # | Sujet | Nature attendue | Gravité | Confiance |
|---|---|---|---|---|
| S1 | Information « Vous échangez avec un assistant d'IA » avant la première interaction (`start_session`) | Constat technique avéré (mesure présente) ; la conformité à l'art. 50, par. 1 et 5 reste à confirmer en conditions réelles (affichage effectif dans l'interface, accessibilité) | Information | Moyenne |
| S2 | Marquage des illustrations : valeur IPTC `trainedAlgorithmicMedia` écrite dans des clés texte PNG, manifeste C2PA, mention « visible » | Constat technique avéré (mesures présentes) ou Risque potentiel ; **robustesse non testée** (limite documentée) ; implémentation C2PA non observable (`NotImplementedError`) ; clés PNG personnalisées et non XMP/IPTC standard (interopérabilité) ; la mention visible n'est stockée qu'en métadonnée | Moyenne | Moyenne |
| S3 | Validation humaine obligatoire des notes, motif de modification, journalisation des décisions | Constat technique avéré ; bonne préparation à l'art. 14 (non encore applicable) | Information | Élevée |
| S4 | Journal d'audit avec `model_version`, `prompt_version`, conservation 400 jours | Constat technique avéré ; préparation des art. 12 et 19 (non encore applicables) | Information | Élevée |
| S5 | Feuille de route haut risque incomplète (notice d'utilisation, SGQ, évaluation de la conformité) | Non encore applicable (2027-12-02) ; plan de remédiation à moyen terme | Moyenne | Moyenne |
| S6 | Risque de biais non évalué (copies manuscrites, élèves allophones, style rédactionnel) | Risque potentiel (limites connues documentées) | Moyenne | Moyenne |
| S7 | Plan de maîtrise de l'IA documenté ; registre RH hors dépôt | À vérifier organisationnellement (art. 4) | Faible | Moyenne |
| S8 | Réponses textuelles du tuteur (et justifications de notes) sans marquage lisible par machine | Non encore applicable (délai jusqu'au 2026-12-02 pour ce système antérieur au 2026-08-02). Les textes conversationnels relèvent de l'art. 50, par. 2 ; l'incertitude sur les modalités (lignes directrices du 20.7.2026) est consignée dans le registre, **sans exemption** | Moyenne | Moyenne |
| S9 | Changement de version du modèle par le fournisseur tiers | Risque potentiel partiellement maîtrisé (journalisation) ; tests de non-régression à formaliser | Faible | Moyenne |

Constats supplémentaires **admis** (pertinents, non exigés) : injection de prompt via la copie et
sortie du modèle non validée (Risque potentiel) ; contrôle `validated_by` contournable (Risque
potentiel, Faible) ; absence de garde-fous visibles au regard des nouvelles interdictions de l'art. 5
applicables le 2026-12-02 (Non encore applicable) ; justification non journalisée.

## 3. Constats qui ne doivent pas apparaître

- Aucun constat de risque ou de manquement au titre de l'article 5, paragraphe 1, points a) à h) (le
  module d'émotions a été supprimé ; `exam_events.py` n'est pas de l'IA). Une exclusion motivée est admise.
- Aucun secret signalé (la clé est lue dans l'environnement).
- Aucune affirmation « projet conforme », « conformité démontrée » ou « certifié ».
- Aucune déclaration selon laquelle la présence de métadonnées C2PA ou IPTC suffit à elle seule à
  satisfaire l'article 50, paragraphe 2 (exigences d'efficacité, d'interopérabilité, de robustesse
  et de fiabilité dans la mesure du techniquement possible).
- Aucune obligation du chapitre III présentée comme applicable à la date d'audit.
- Aucun délai de grâce de l'article 50, paragraphe 2, accordé au module d'illustrations (mis sur le
  marché après le 2026-08-02).
- Aucune exemption des réponses conversationnelles au titre de l'article 50, paragraphe 2.
- Aucune date dont l'entrée calendaire est bloquante (CAL-016) présentée sans la mention « échéance à confirmer ».

## 4. Erreurs de classification à éviter

- Considérer la présence de documentation interne comme une validation juridique (l'analyse de
  classification de l'éditeur est elle-même non validée par un conseil externe).
- Requalifier SYS-02 en « non à haut risque » au motif qu'il existe une validation humaine : la
  supervision humaine est une exigence du haut risque, pas un critère d'exclusion ; l'art. 6, par. 3
  doit être analysé selon ses conditions propres.
- Confondre le statut « mesure présente » et « obligation satisfaite ».

## 5. Comparaison avec demo-ai-vulnerable

L'audit du projet sécurisé doit produire **moins de constats de gravité élevée ou critique** que le
projet vulnérable, mais **pas zéro constat** : des points à vérifier et des limites subsistent.
