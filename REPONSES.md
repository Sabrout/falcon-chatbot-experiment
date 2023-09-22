# Réponses aux questions suite à développement:

## Pourquoi avez-vous fait ces choix technologiques ?



## Comment valideriez-vous le bon fonctionnement de cette IA ?
L'évaluation des grands modèles de langage (LLM) peut être un processus complexe, et les critères d'évaluation spécifiques peuvent varier en fonction de la tâche et de l'application. Cependant, en réduisant le champ d'application à notre cas d'utilisation, voici quelques méthodes et considérations communes pour l'évaluation des modèles LLM :

### Perplexité:

La perplexité est une mesure couramment utilisée pour évaluer la capacité de modélisation linguistique des LLM. Elle mesure le degré de prédiction d'une séquence de mots par le modèle. Une perplexité plus faible indique une meilleure performance.

### Génération de texte: 

Pour les tâches de génération de texte, vous pouvez évaluer la qualité et la cohérence du texte généré. L'évaluation humaine ou des mesures automatisées telles que BLEU, ROUGE ou METEOR peuvent être utilisées pour comparer le texte généré avec le texte de référence.

### Réponse aux questions (QA): 

Pour les tâches d'assurance qualité, il s'agit d'évaluer dans quelle mesure le modèle répond aux questions. Utilisez des mesures telles que la précision, le score F1 ou la correspondance exacte pour comparer les réponses du modèle aux réponses fournies par l'homme.

### Classification de textes: 

Dans les tâches de classification de textes, utilisez l'exactitude, la précision, le rappel, le score F1 ou l'aire sous la courbe ROC (AUC-ROC) pour évaluer les performances du modèle.

### Efficacité des données: 

Évaluez les performances du modèle avec des données limitées. Vous pouvez utiliser des courbes d'apprentissage ou mesurer les performances sur de petits ensembles de données.

### Évaluation humaine: (Trés Important)

Effectuer des évaluations humaines afin d'évaluer la qualité des résultats du modèle. Des annotateurs humains notent le contenu généré par le modèle en fonction de sa pertinence, de sa cohérence et de sa fluidité.

### Comparaison avec les lignes de base: 

Comparez la performance du LLM aux modèles de base ou aux modèles de pointe précédents pour évaluer son avancement.

## Quels serait les principaux chantiers d'industrialisation à mener pour intégrer cet agent au produit Weloop (et l'exposer à nos utilisateurs) ?



## Votre implémentation a-t-elle des limites, si oui lesquelles ?



## Quelles seraient selon vous les axes d'améliorations principaux de votre agent conversationnel (hors industrialisation) ?"


