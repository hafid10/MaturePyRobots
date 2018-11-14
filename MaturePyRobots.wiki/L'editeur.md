# CodeMirror

Pour l'édition des codes utilisateur nous avons utilisé [CodeMirror](https://github.com/codemirror/CodeMirror)
, spécialisé dans l’édition de code il permet une intégration complète des fonctionnalités
de tout bon IDE: fermeture automatique des caractères de contrôles, indentation, documentation à la volée, etc...

## Fonctionnement

Les fichiers principaux de CodeMirror ce trouve dans _/WebPyRobot/backend/static/codemirror/*_.
Ce dossier contient les dépendances de l'éditeur ainsi que les points d'entrées (codemirror{.js,.css}).

## La Vue

Dans le fichier _view.py_ de l'application _backend_ ce trouve une méthode `editor`.
Cette fonction est très simple, elle sauvegarde l'Ia du joueur si la requête est 'POST'
ou envoie le code de l'utilisateur au template si la méthode est 'GET'.

## Le Template

La page _/WebPyRobot/backend/templates/backend/editeur.html_ contient un simple formulaire
qui va recueillir le programme de l'utilisateur. Le champs `textarea` va être recouvert par
CodeMirror. Pour son bon fonctionnement il faut inclure les fichiers _js_ et _css_ mais aussi
les composants de l'éditeur que l'on veut utiliser (matchBraket, python, etc.)


## Le script Js

Le petit script d'initialisation _/WebPyRobot/backend/static/js/editor.js_ sert à créer le
bloc CodeMirror qui va remplacer le `textarea` grâce à la méthode `fromTextArea` de CodeMirror
qui sert également de constructeur. On passe comme argument de ce constructeur les propriétés de
l'éditeur. La méthode `save()` de CodeMirror fait le transfert du texte de l'éditeur vers le `textarea`.


## Drag N Drop (glisser déposer)
Il est possible de glisser déposer un fichier directement dans l'éditeur cf backend/static/js/editor.js

## Sauvegardes de fichiers différents
L'utilisateur peut sauvegarder jusqu'à 5 scripts différents et choisir celui qui sera "activé" c'est à dire celui que le moteur de jeu considérera lors des combats.
