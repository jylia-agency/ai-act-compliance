# Calendrier d'application de l'AI Act

> Base : règlement (UE) 2024/1689 (art. 111 et 113), tel que modifié par le règlement (UE) 2026/1744.
> Dernière vérification : **2026-10-27**. Source machine : `data/ai-act-calendar.json` (faisant foi
> pour les scripts ; ce fichier doit rester synchronisé, ce que vérifie `tests/run_tests.py`).
> Marqueurs : `[TI]` texte initial, `[O26]` modifié par 2026/1744 (sources secondaires), `[AV]` à vérifier.
> Sources : [EUR-Lex 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689),
> [EUR-Lex 2026/1744](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1744),
> [AI Act Explorer, art. 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113).
> Voir `legal-sources.md` pour les conditions de vérification.

## 1. Règles d'utilisation

1. Toujours raisonner à la **date d'audit** (paramètre explicite du rapport).
2. Une obligation est :
   - **en vigueur** si sa date d'application (éventuellement décalée par un régime transitoire) est
     antérieure ou égale à la date d'audit ;
   - **non encore applicable** si cette date est postérieure : le constat prend la nature
     « Non encore applicable » et indique l'échéance ;
   - **conditionnelle** si elle dépend d'un fait inconnu (date de mise sur le marché, nature
     publique du déployeur, modification importante) ;
   - **à vérifier** si la date n'est pas établie de manière fiable.
3. La date de **mise sur le marché** (art. 3, point 9) ou de **mise en service** (art. 3, point 11)
   s'apprécie système par système ; selon le considérant 39 du règlement 2026/1744 (rapporté par les
   sources), au niveau du type et du modèle pour l'article 111, paragraphe 2.
4. Ne jamais appliquer une proposition de modification non adoptée.
5. Le script `scripts/obligation_timeline.py` applique ces règles au fichier JSON.

## 2. Tableau de référence

| ID | Obligation ou évènement | Article(s) | Date | Régime transitoire | Confiance |
|---|---|---|---|---|---|
| CAL-001 | Entrée en vigueur de l'AI Act | Art. 113, al. 1 `[TI]` | 2024-08-01 | n.a. | Élevée |
| CAL-002 | Chapitres I et II : dispositions générales, **maîtrise de l'IA (art. 4)**, **pratiques interdites (art. 5, points a) à h))** | Art. 113, al. 3, a) `[TI]` | 2025-02-02 | Aucun : s'applique aussi aux systèmes déjà sur le marché | Élevée |
| CAL-003 | Nouvelle rédaction de l'art. 4 (mesures pour soutenir la maîtrise de l'IA) | Art. 4 modifié `[O26]` | 2026-07-27 (présumée) | n.a. | Moyenne |
| CAL-004 | **Nouvelles interdictions** : contenus intimes non consentis de personnes identifiables, matériel pédopornographique | Art. 5, par. 1, nouveaux points `[O26]` | 2026-12-02 | Aucun rapporté | Moyenne |
| CAL-005 | Chapitre V (**modèles GPAI**), chapitre VII (gouvernance), chapitre XII (sanctions, sauf art. 101), chapitre III section 4, art. 78 | Art. 113, al. 3, b) `[TI]` | 2025-08-02 | Voir CAL-006 | Élevée |
| CAL-006 | Modèles GPAI mis sur le marché **avant le 2025-08-02** | Art. 111, par. 3 `[TI]` | 2025-08-02 | Conformité au plus tard le **2027-08-02** | Élevée |
| CAL-007 | Amendes applicables aux fournisseurs de modèles GPAI | Art. 101 `[TI]` | 2026-08-02 | n.a. | Élevée |
| CAL-008 | Date générale d'application | Art. 113, al. 2 `[TI]` | 2026-08-02 | Haut risque reporté (CAL-011, CAL-012) | Élevée |
| CAL-009 | **Article 50, par. 1, 3, 4 et 5** (interaction avec une IA, émotions et catégorisation biométrique, hypertrucages, textes d'intérêt public, modalités) | Art. 50 `[TI]`, date non modifiée `[O26]` | 2026-08-02 | Aucun | Élevée |
| CAL-010 | **Article 50, par. 2** (marquage et détectabilité des contenus synthétiques, fournisseurs) | Art. 50, par. 2 `[TI]` + délai `[O26]` | 2026-08-02 | Systèmes mis sur le marché **avant le 2026-08-02** : jusqu'au **2026-12-02** | Moyenne |
| CAL-011 | **Haut risque annexe III** (art. 6, par. 2) : chapitre III, sections 1 à 3 (art. 8 à 27) | Art. 113 modifié `[O26]` | **2027-12-02** (initialement 2026-08-02) | Voir CAL-013 | Moyenne |
| CAL-012 | **Haut risque annexe I** (art. 6, par. 1) | Art. 113 modifié `[O26]` | **2028-08-02** (initialement 2027-08-02) | Voir CAL-013 | Moyenne |
| CAL-013 | Systèmes à haut risque mis sur le marché ou en service **avant** la date d'application du chapitre III | Art. 111, par. 2 modifié `[AV]` | Référence : 2027-12-02 (annexe III) ; 2028-08-02 (annexe I) | Soumis au règlement seulement en cas de **modification importante de la conception** après cette date ; systèmes destinés aux **autorités publiques** : au plus tard le **2030-08-02** (divergence : une source indique 2028-01-28) | Faible |
| CAL-014 | Composants des systèmes d'information à grande échelle (annexe X) mis sur le marché avant le 2027-08-02 | Art. 111, par. 1 `[TI]` | 2027-08-02 | Conformité au plus tard le 2030-12-31 | Élevée |
| CAL-015 | Entrée en vigueur du règlement 2026/1744 | `[O26]` | 2026-07-27 | n.a. | Moyenne |
| CAL-016 | Enregistrement (art. 49, par. 2) des systèmes de l'annexe III que le fournisseur estime non à haut risque | Art. 6, par. 4 ; art. 49, par. 2 `[AV]` | Non établie | n.a. | Faible |

## 3. Points d'attention

- **Le report du haut risque ne reporte ni l'article 5, ni l'article 50, ni l'article 4.** Un
  système d'IA qui n'est pas encore soumis aux exigences du haut risque reste soumis aux obligations
  déjà applicables.
- Les obligations liées au haut risque situées **hors du chapitre III** (art. 49 enregistrement,
  art. 72 surveillance après commercialisation, art. 73 incidents graves, art. 86 droit à
  l'explication) ne concernent que des systèmes à haut risque ; leur date effective, au regard du
  report, doit être confirmée sur le texte consolidé `[AV]`. Dans le doute, statut « conditionnel ».
- **Article 111, paragraphe 2** : un système mis sur le marché avant la date de référence peut ne
  jamais devenir soumis aux exigences du haut risque s'il n'est pas modifié de manière importante.
  Toute mise à jour majeure (changement de modèle sous-jacent, changement de finalité, refonte de la
  logique de décision) doit être analysée comme une possible modification importante `[AV]`.
- Un **changement de finalité** qui fait entrer un système dans l'annexe III crée en pratique un
  nouveau système et peut faire de l'opérateur un fournisseur (art. 25, par. 1, c)).

## 4. Scénarios de contrôle (repris par les tests)

| Scénario | Date d'audit | Mise sur le marché | Résultat attendu |
|---|---|---|---|
| Générateur d'images antérieur | 2026-10-27 | 2026-03-01 | CAL-010 non encore applicable (échéance 2026-12-02) |
| Générateur d'images antérieur | 2026-12-15 | 2026-03-01 | CAL-010 en vigueur |
| Générateur d'images récent | 2026-10-27 | 2026-09-15 | CAL-010 en vigueur (aucun délai) |
| Chatbot | 2026-10-27 | quelconque | CAL-009 en vigueur |
| Notation d'élèves (annexe III) | 2026-10-27 | 2026-03-01 | CAL-011 non encore applicable ; CAL-013 conditionnel |
| Modèle GPAI antérieur | 2026-10-27 | 2025-06-01 | CAL-006 non encore applicable (échéance 2027-08-02) |
| Reconnaissance des émotions en classe | 2026-10-27 | quelconque | CAL-002 en vigueur |
| Nouvelles interdictions art. 5 | 2026-10-27 | quelconque | CAL-004 non encore applicable (2026-12-02) |
