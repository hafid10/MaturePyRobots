# Site Web
### L'index
Arrivé sur la page d'index, l'utilisateur peut, soit se connecter, soit s'inscrire.
Pour pouvoir s'inscrire, il doit se munir d'un pseudo, d'un émail ainsi que de son mot de passe.
Le mot de passe doit convenir à la norme fixée par Django.
Après l'inscription, il est automatiquement connecté, et il peut se connecter avec son pseudo et son mot de passe pour les prochaines connexions..

### L'accueil
Arrivé sur sa page [d'accueil](https://github.com/Petrole/MaturePyRobots/wiki/Quelques-images), l'utilisateur a accès à un résumé de ses informations.

Un navigateur en haut qui permet d'avoir accès à plusieurs fonctionnalités. 
Le montant d'argent que l'utilisateur possède, Le pseudo de l'utilisateur, et deux boutons.
Le premier sert à modifier ses informations personnelles, et le second permet de se déconnecter.
En cliquant sur le logo en haut a droite, une redirection nous permet de rejoindre cette page, la page d'accueil.

Dans le corps de la page on peut changer son mode d'agression, à savoir si l'utilisateur autorise les autres joueurs à l'attaquer.
Le bouton 'battle' permet évidement d'attaquer un autre joueur. Chaque combat fait gagner 100$ aux deux combattants.
Nous avons aussi un résumé des équipements de notre tank ainsi que ces statistiques.

La barre de navigation sur la droite sert à naviguer entre les pages:
* d'accueil
* la boutique
* l'éditeur
* l'inventaire
* l'historique de combat
* le.s tutoriel.s
* la FAQ
* la documentation

### La boutique
La [boutique](https://github.com/Xawirses/WebPyRobot/wiki/Quelques-images#boutique) permet à l'utilisateur d'acheter des équipements pour pouvoir améliorer son tank.
#### Les Canons
Le canon permet de faire plus de dégâts au tank adverse.
Certains canons ont besoin de plus de points d'action pour s’exécuter.
#### Le Blindage
Le blindage permet de réduire les dégâts subis par le tank adverse.
#### Les Chenilles
Les chenilles permettent au tank d'avoir plus de points de mouvement.
#### Le Système de Navigation
Le système permet d'effectuer des actions plus compliquées, ou simples plusieurs fois.

### L'éditeur
La page éditeur permet évidement de modifier son IA et de la tester.
Une IA de base est donnée par défaut à la création d'un utilisateur.
Pour exécuter une fonction de notre API, il faut ajouter le mot clé `self` devant les fonctions. 
```python
# Default ia
# Get the enemy position in the game
enemy = self.getEnemyTankId()
enemypos = self.getPosition(enemy)
# Move foward to the enemy
self.moveTank(enemypos)
# Shoot the enemy Gracefuly
self.shoot()
```
Cette IA basique permet de récupérer l'identifiant de l’ennemie, puis sa position, puis de se déplacer vers lui et de finir par tirer.

### L'inventaire
La page inventaire permet de s'équiper des différentes pièces de son tank.

### L'historique de combat
La page d'historique de combat permet de retrouver les noms des joueurs affrontés ainsi que le résultat de la partie (victoire/défaite).

### La documentation
Cette page permet de consulter rapidement les fonctions disponibles pour contrôler son robot.

### Tutoriels
Cette page permet de consulter des tutoriels quant à l'utilisation du site.

### FAQ
Une petite foire aux questions pour les interrogations qui ne trouvent pas de réponses ailleurs dans le site.

## Le CSS

#### Materialize
Tout le site a été crée avec le framework [Materialize](http://materializecss.com/).
De plus le site est responsive Mobile et Tablette.