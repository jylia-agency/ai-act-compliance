# Procédure de supervision humaine (SYS-02, fictif)

1. Le modèle produit une proposition de note, une justification et le détail par critère.
2. La proposition est affichée à l'enseignant avec un avertissement : « Proposition générée par IA,
   à vérifier. Ne pas valider sans lecture de la copie. »
3. L'enseignant peut approuver, modifier (motif obligatoire) ou rejeter la proposition.
4. Aucune note n'est publiée sans validation (`publish_grade` refuse toute publication sans
   `validated_by`).
5. Chaque décision est journalisée (identifiant de l'enseignant, décision, note finale, motif).
6. Une revue trimestrielle des écarts entre propositions et notes finales est organisée pour
   détecter un éventuel biais d'automatisation.

Formation : les enseignants suivent un module de 2 heures avant activation (voir ai-literacy-plan.md).
