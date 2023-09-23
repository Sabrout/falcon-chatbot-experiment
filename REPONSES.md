# Réponses aux questions suite à développement:

Dans ce dossier, je réponds à toutes les questions posées dans votre email et j'ajoute plus de détails au projet. Bien que je fournisse les réponses en français. C'est la seule partie écrite en français alors que le reste du projet est documenté et implémenté en anglais car je crois que c'est une meilleure pratique générale pour les améliorations futures et les collaborations avec d'autres développeurs.


## Pourquoi avez-vous fait ces choix technologiques ?

### Falcon-7B

En plus d'être le modèle sous licence open-source le plus populaire à l'heure actuelle, Falcon-7B est relativement performant sur les GPU grand public. Pour les besoins de ce projet, j'ai loué un serveur GPU sur [runpod.io](https://www.runpod.io/) avec les spécifications suivantes :

| Pod Specs     |
| ------------- |
| RTX A4500     |
| 12 CPUs       |
| 62 GB RAM     | 
| Pytorch 2.0.1 | 
| Cuda   11.8.0 | 
| Python   3.10 | 

Sans les limitations de mon matériel, j'aurais utilisé le Falcon-30B qui est un modèle beaucoup plus grand et plus complexe et qui permet plus de personnalisation à condition que nous ayons un plus grand ensemble de données de WeLoop.

### OpenAI

En ce qui concerne le GPT 3.5-turbo d'OpenAI, j'ai préféré l'utiliser pour tester ma mise en œuvre initiale de l'API et du notebook Jupyter parce qu'il a un temps de réponse beaucoup plus rapide puisqu'il n'est pas exécuté localement.

C'est aussi pour avoir un standard à comparer avec n'importe quel modèle LLM local comme référence.

### Bottle API

Il s'agit d'un framework minimaliste connu pour sa simplicité et son efficacité, ce qui le rend adapté aux projets de petite et moyenne taille pour lesquels un développement rapide et une empreinte minimale sont importants. Bottle est facile à apprendre et n'a pas beaucoup de dépendances, ce qui en fait un choix pratique pour créer des services web simples ou des prototypes avec un minimum de code de base.

Traduit avec www.DeepL.com/Translator (version gratuite)

### Docker

Docker est utilisé pour conteneuriser les projets Python à des fins de portabilité et de reproductibilité. Il encapsule le projet et ses dépendances dans un seul conteneur, garantissant ainsi la cohérence entre les différents environnements. Cela simplifie le déploiement, la scaling et la collaboration, car les développeurs peuvent partager des conteneurs en ayant l'assurance qu'ils fonctionneront partout de la même manière. Docker améliore également l'isolation, la sécurité et l'efficacité des ressources, ce qui en fait un choix idéal pour déployer des applications Python dans divers scénarios, du développement à la production.



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

Voici donc quelques projets clés pour industrialiser l'intégration d'un chatbot dans une plateforme utilisateur comme WeLoop:

### Projet de développement d'un chatbot :

Objectif : Développer et affiner le modèle de chatbot.

Activités : Développement du modèle NLP, conception du dialogue et formation.

### Projet d'intégration et de déploiement :

Objectif : Intégrer le chatbot dans la plateforme utilisateur.

Activités : Intégration de la plateforme, développement de l'API, conception de l'interface utilisateur.

### Projet de test et d'assurance qualité :

Objectif : Assurer la fonctionnalité et la performance du chatbot.

Activités : Tests fonctionnels, tests de régression, UAT.

### Projet de suivi et d'analyse :

Objectif : Mettre en place des outils de suivi et d'analyse.

Activités : Suivi des données, analyse du comportement des utilisateurs.

### Projet de gestion des coûts et d'analyse du retour sur investissement :

Objectif : Évaluer les coûts et le retour sur investissement du projet.

Activités : Analyse des coûts, mesure du retour sur investissement.


## Votre implémentation a-t-elle des limites, si oui lesquelles ?

Oui, bien sûr, ma mise en œuvre a des limites puisqu'il s'agit d'un travail de quelques heures seulement, mais ces limites peuvent être expliquées comme suit :

### 1. Sécurité :

Pour l'instant, il n'y a pas de méthode dans cette implémentation pour empêcher d'autres personnes d'interagir avec le modèle ou l'API. Ainsi, l'authentification des utilisateurs et le contrôle des performances de l'API doivent être mis en œuvre.

### 2. Optimisation et test du modèle :
Après avoir testé le modèle pendant quelques heures, le modèle fournit des réponses imprécises et parfois en anglais au lieu du français. Ce type de problème nécessite davantage de débogage et d'ajustements des paramètres. Pour l'instant, le modèle ne fonctionne que s'il n'est pas testé correctement.

### 3. Configuration d'Hardware :

Comme discuté précédemment, j'ai remplacé le modèle Falcon-7B par le modèle OpenAI pour un temps de réponse plus rapide car je n'ai pas de machine puissante. Cependant, le modèle Falcon-7B (ou tout autre modèle) doit être configuré en fonction des serveurs de déploiement




## Quelles seraient selon vous les axes d'améliorations principaux de votre agent conversationnel (hors industrialisation) ?


À côté de l'aspect technique MLOps de ce projet, voici les domaines dans lesquels des améliorations sont nécessaires pour tout modèle LLM que nous déploierions :

### Compréhension du contexte : 

Améliorer la capacité de l'agent à maintenir le contexte sur des conversations plus longues et à fournir des réponses plus cohérentes et tenant compte du contexte.

### Capacités multimodales : 

Intégration de la prise en charge des entrées multimodales, telles que le texte, les images et la voix, afin de permettre des interactions plus naturelles.

### Vérification des faits et exactitude : (_l'amélioration le plus important_) 

renforcement des capacités de vérification des faits de l'agent pour garantir que les informations fournies sont exactes et à jour.

### Personnalisation de l'utilisateur : 

Améliorer la personnalisation en comprenant les préférences de l'utilisateur et en adaptant les réponses en conséquence.

### Réduction des répétitions : 

Minimiser les réponses répétitives et fournir des informations concises et pertinentes.
