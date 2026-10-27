# Supervision humaine

> Base : art. 14 (fournisseurs) et art. 26, par. 2 et 5 (déployeurs) du règlement (UE) 2024/1689 `[TI]` ;
> applicables aux systèmes à haut risque à partir du **2027-12-02** (annexe III) ou du **2028-08-02**
> (annexe I) `[O26]`. Dernière vérification : **2026-10-27**.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [AI Act Explorer, art. 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14).

## 1. Champ

Le contrôle humain de l'article 14 est une **exigence des systèmes à haut risque**. Pour les autres
systèmes, la supervision humaine est une **bonne pratique** (à présenter comme telle), sauf lorsque
d'autres dispositions l'imposent (hors périmètre).

## 2. Contenu de l'article 14 `[TI]`

- Par. 1 : conception et développement permettant un contrôle effectif par des personnes physiques
  pendant la période d'utilisation, y compris par des outils d'interface homme-machine appropriés.
- Par. 2 : objectif de prévenir ou réduire les risques pour la santé, la sécurité ou les droits
  fondamentaux, y compris en cas de mauvaise utilisation raisonnablement prévisible.
- Par. 3 : mesures proportionnées aux risques, au niveau d'autonomie et au contexte, intégrées par le
  fournisseur et/ou identifiées par lui pour mise en œuvre par le déployeur.
- Par. 4 : le système est fourni de manière à permettre aux personnes chargées du contrôle, selon le cas :
  - a) de comprendre correctement les capacités et limites du système et de surveiller son
    fonctionnement, y compris pour détecter anomalies, dysfonctionnements et performances inattendues ;
  - b) d'avoir conscience d'une possible tendance à se fier automatiquement ou excessivement aux
    sorties (**biais d'automatisation**), en particulier pour les systèmes fournissant des
    informations ou recommandations pour des décisions ;
  - c) d'**interpréter correctement** les sorties, compte tenu des outils et méthodes disponibles ;
  - d) de décider de **ne pas utiliser** le système ou d'**ignorer, remplacer ou inverser** sa sortie ;
  - e) d'**intervenir** ou d'**interrompre** le système par un bouton d'arrêt ou une procédure similaire
    permettant un arrêt en toute sécurité.
- Par. 5 : identification biométrique à distance de l'annexe III, point 1, a) : vérification et
  confirmation séparées par au moins deux personnes physiques compétentes (sauf exceptions).

## 3. Checklist technique (conditionnelle : système à haut risque probable ou bonne pratique)

| Contrôle | Preuve attendue | Référence |
|---|---|---|
| La sortie est une **proposition** et non une décision exécutée automatiquement | Statut `pending_review`, absence d'appel direct à une action irréversible | Art. 14, par. 4, d) |
| L'humain peut **refuser, modifier, annuler** | Fonctions `override`, `reject`, motif saisi | Art. 14, par. 4, d) |
| L'humain peut **interrompre** le système | Drapeau de désactivation, procédure d'arrêt | Art. 14, par. 4, e) |
| Les sorties sont **interprétables** | Justification, facteurs, score de confiance, critères | Art. 14, par. 4, c) ; art. 13 |
| Les limites sont **affichées** | Avertissements contextuels, documentation | Art. 14, par. 4, a) |
| Le **biais d'automatisation** est traité | Formation, revue des écarts, absence de validation en masse par défaut | Art. 14, par. 4, b) |
| Les **erreurs et anomalies** déclenchent des alertes | Seuils, supervision, journal d'erreurs | Art. 14, par. 4, a) |
| Les **interventions** sont tracées | Journal : qui, quand, décision, motif | Art. 12 ; art. 26, par. 6 |
| Les superviseurs ont **compétence et autorité** | Rôles applicatifs, procédure (organisationnel) | Art. 26, par. 2 |

## 4. Signaux de risque d'automatisation excessive

- Publication, envoi ou exécution directe de la sortie (note publiée, candidature rejetée, compte bloqué).
- Validation « en un clic » de lots entiers sans affichage du détail.
- Absence de justification affichée à l'humain.
- Agent autonome disposant d'outils à effets irréversibles (paiement, suppression, envoi) sans
  confirmation humaine.
- Taux de modification humaine nul ou non mesuré.

## 5. Qualification

- Système à haut risque probable, date d'audit antérieure à la date d'application : constat
  « Non encore applicable » ou « Risque potentiel » (si le risque pour les personnes existe déjà),
  avec recommandation, sans affirmer un manquement à l'article 14.
- Système non à haut risque : « Bonne pratique recommandée ».
