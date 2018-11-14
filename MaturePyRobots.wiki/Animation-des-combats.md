## Technologie utilisée 
L’animation est faite dans un canvas en javascript. 

### Le canvas 
Le canvas est une des nombreuses nouvelles possibilités offertes par HTML5. 

Il offre la possibilité de dessiner (carrés, rectangles, droites, textes, ronds, images ...) via du code JavaScript.

Pour nos utilisateurs sur internet explorer qui ne connaissent pas le canvas nous utilisons une librairie “excanvas.js” disponible à l’adresse suivante:
https://github.com/arv/explorercanvasa

## Arboressence 

* js
* js/classes
* maps
* sprites
* tilesets

### JS
Dans le dossier js/classes se trouve les codes javascript qui représentent des éléments du jeu, comme les joueurs, la carte ou les décors. 

Ces codes définissent comment les éléments du jeu doivent êtres chargés et dessinés.

Dans le dossier js se trouve le code mainAnimation.js qui permet de coordonner ce que doivent faire tous éléments et où ils se placent. 


### Tileset 
Le dossier tileset contient toutes nos images tileset. Un tileset est une sorte de collage d’images de taille 32/32 pixels la taille est définie dans le fichier Map.js situé dans /js/classes. 


### Maps 

-Dans le dossier maps se trouve les différentes map au format Json. 
-Chaque fichier map doit avoir 2 champs: “"tileset":” et ”"ground":” 
-Le champ tileset sert à définir le nom du fichier à utiliser pour la carte. Ce fichier doit être situé dans tileset  
-Le champ ground est une matrice qui sert à définir plusieurs éléments. Premièrement la taille de la carte en largeur et hauteur, pour définir la largeur de la carte nous prenons la taille du premier tableau situé dans la première case et pour définir la hauteur de la carte nous prenons la taille du tableau ground. Dans un second temps il définit aussi quelle partie du tileset est utilisé, il s’agit du dessin de la carte. 


### Sprites
Les sprites correspondent aux images qui sont utilisées par nos éléments du jeu.

Nos animations pour s'exécuter utilisent 8 images par mouvements. 

Par défaut nous avons mis en premier l’animation pour monter, l’animation pour aller à droite en deuxième, l’animation pour aller en bas en troisième, puis en dernier l’animation pour aller à gauche.

Nous avons défini ses différents états dans le fichier js/classe/Players.js avec la variable STATE .
 

## MainAnimation.js

Le fichier MainAnimation.js est le plus important des fichiers il se charge de recevoir l’animation générée par le serveur qui est une chaîne de caractères au format suivant:

[[QuelJoueur ,QuelAnimation ,QuelCaseEnX ,QuelCaseEnY],[QuelJoueur ,QuelAnimation ,QuelCaseEnX ,QuelCaseEnY]....]
 
QuelJoueur est un entier qui vaut soit 0 soit 1 et qui représente le joueur qui effectue l’action. 


QuelAnimation est une string qui peut valoir:
moveDown
     Si le joueur doit descendre d’une case 
moveUp
    Si le joueur doit monter d’une case 
moveLeft
    Si le joueur doit se déplacer sur la gauche d’une case 
moveRight
    Si le joueur doit se déplacer sur la droite d’une case 
Shoot
     Si le joueur tire sur une case  
endTurn
   Si un des joueurs à terminer son tour
dead
  Si le joueur est mort 


QuelCaseEnX ,QuelCaseEnY sont des entiers qui servent à définir quel case est la cible des actions utilisé notamment dans shoot. 


Ce fichier calcul aussi la taille que doivent prendre la carte et les éléments en fonction de la taille de la fenêtre de l’utilisateur pour cela il définit une réduction à appliquer à tous les éléments. Cette réduction est calculée dans la variable contrainte. 

Ce fichier défini aussi en combien de temps notre carte est rechargée et tout les combien nous avançons dans l'animation de nos joueur. Par défaut notre carte se recharge toute les 60 microsecondes et l’animation avance toute les 400 microsecondes. 


## Différentes classes déjà crée

### Players.js
Ce fichier représente un tank 
Il définit les méthodes move shoot, dead et draw 

-Draw sera appelé dans le fichier map et définit comment notre personnage doit se dessiner selon son état actuel. 

-Dead sert à faire passer notre personnage en état de mort 

-Shoot sert à faire passer notre personnage en état de tir 

-Move sert à faire passer notre personnage en état de mouvement


### Map.js
Ce fichier représente la map 

Il possède plusieurs tableaux d’éléments à afficher, ici nous avons les joueurs, les balles s’il y a un tir et les oiseaux. Si nous voulons voir un élément sur notre carte nous devons l’ajouter dans le tableau correspondant. 

Pour cela il existe 3 méthodes addPlayer, addBird, addBullet

Une fois qu'un joueur, une balle ou un oiseau a fini son animation il doit disparaître. Sa méthode draw doit ainsi renvoyer false et notre map l’enlèvera de son tableau d’élément à afficher. 

### Bullet.js
Ce fichier représente une balle tirée par un char

Il gère aussi l’animation du tank qu’il touche. 


### Bird.js
Ce fichier représente un oiseau. 

L’oiseau a seulement un but décoratif et ne fait que passer sur la carte puis disparais.






 
 


 
 










