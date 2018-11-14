# Que ce passe t'il lorsque l'on clique sur Battle ?
Deux emplacements: _/WebPyRobot/backend/views.py_ et _/WebPyRobot/backend/game/*_

## La Vue
Dans le fichier _views.py_ de l'application _backend_ se trouve la fonction `fight`. C'est ici que tout commence.

Pour commencer cette fonction commence par trouver un adversaire de manière aléatoire grâce à `random`.
(Donc avant de tester les combats assurez-vous d'avoir au minimum deux joueurs.)
Une fois les deux utilisateurs sélectionnés, on récupère leurs informations (ia et tank). On crée l'objet `Game` qui va effectué le vrai travail. On augmente les finances des deux joueurs peu importe l'issue du combat car on est gentils.

## Le Calcul
Le cœur du calcul: `Game`.

`Game` représente un module Python à part entière. On pourrait tout fait sortir le module du contexte et l'exécuter individuellement. Un module Python est représenté par la présence du fichier vide nommé \_\_init\_\_.py .  
Nous avons choisi de représenter le jeu en deux classes: `Game` et `Robot`. 

### La classe Robot
Cette classe possède les méthodes simples d’accès et d’écriture sur les divers attributs d'un tank (vie, mouvement, portée, etc.). Ces méthodes sont destinées à être utilisables seulement par le calculateur.

### La classe Game
La classe Game représente l'état du jeu (positions, tours, ...) et fournit les méthodes à l'utilisateur.

Ici reposent les différentes méthodes que peut utiliser le joueur dans son programme de jeux. On retrouve notamment les opérations de récupération des positions du joueur et de l'ennemie, ainsi que les données relatives au tank. Mais surtout deux méthodes essentielles `moveTank` qui permet de déplacer son tank et `shoot` qui permet de tirer sur l'ennemie. Ces deux méthodes répertorient les actions des joueurs dans le tableau `result`, ce qui permet de pouvoir générer un affichage graphique du combat.

La méthode `run` fait office de lancement principal. Elle va faire tourner séquentiellement les intelligences artificielles des joueurs 100 fois avant de retourner l'issue du combat sous forme d'un tableau d'actions individuelles. Le tableau est de forme suivante: `[[\<IDJoueur\>, \<Action\>, X, Y], ...]  
On retrouve plusieurs \<Action\> : moveLeft, moveRight, moveUp, moveDown, shoot, dead, endTurn
### Notification & Historique de combat 
Les joueurs sont prévenus de leur entrée et sortie en combat. Gérés dans update_battles.py et consumers.py & alertify, ce système utilise le module channels pour gérer les notifications en temps réel et sauvegarder le résultat du combat dans la base de données.

### Interprétation du python utilisateur
Tout le principe d'interprétation d'un code Joueur est basé sur le principe: **Qui mieux que Python pour exécuter du Python ?**  
Cependant cela implique de contrôler le script afin que le combat se déroule correctement.
Pour ce faire l'on fait appel à la fonction `exec` de python qui permet d'interpréter du code à la volée.

## Pour aller plus loin
On ne peut pas tout gérer avec des regex ! Notamment contrer des boucles infinies qui ne tournent pas sur le thread principal.
Un angle d'amélioration pour les prochaines version est de créer un mini interpréteur qui prend en charge une version simplifiée de python (mais qui garde la même syntaxe et sémantique de base comme les structures de contrôles et opérateurs de basiques).

