# Cartographie des flux et des modèles : {{NOM_DU_PROJET}}

Date d'audit : {{AAAA-MM-JJ}} | Commit audité : {{hash}}. Méthode : `SKILL.md`, phase 3 ;
`references/transparency.md`, section 5.

## 1. Chaînes de traitement (une par fonctionnalité)

Représenter chaque chaîne complète : Utilisateur → Application → Modèle → Post-traitement → Stockage → Export.

```
FCT-01 {{fonctionnalité}}
  Utilisateur : {{qui, quelle entrée}}            [fichier:ligne]
  Application : {{route, service, prompt système}} [fichier:ligne]
  Modèle      : {{fournisseur / modèle / version}} [fichier:ligne]
  Post-trait. : {{parsing, filtrage, redimensionnement, marquage}} [fichier:ligne]
  Stockage    : {{base, fichier, journal}}         [fichier:ligne]
  Export      : {{UI, API, PDF, CSV, courriel...}}  [fichier:ligne]
```

## 2. Matrice fonctionnalités / modèles

Un même modèle peut servir plusieurs systèmes ; un même système peut enchaîner plusieurs modèles.

| Fonctionnalité | Système (SYS) | Fournisseur | Modèle | Version épinglée ? | Version journalisée ? | Entrées | Sorties | Traitements intermédiaires | Personnes concernées |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | | | | Oui / Non (alias) | Oui / Non | | | | |

## 3. Chemins de sortie et marquage (art. 50, par. 2)

| Fonctionnalité | Chemin de sortie | Marquage à la génération | Marquage après transformation | Mécanisme (standard ou propriétaire) | Détectable par un tiers ? | Outil de vérification | Falsifiable ? | État du contrôle | Preuve (PRV) |
|---|---|---|---|---|---|---|---|---|---|
| FCT-01 | Interface | | | | | | | Démontré / Non démontré / Non applicable / Impossible à vérifier | |
| FCT-01 | Export PDF | | | | | | | | |

## 4. Ruptures de chaîne identifiées

| Fonctionnalité | Étape | Rupture (perte de marquage, perte de version, absence de journal) | Constat(s) |
|---|---|---|---|
