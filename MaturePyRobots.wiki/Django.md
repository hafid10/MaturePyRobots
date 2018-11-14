**/!\ Cette documentation ne remplace en aucun cas celle de [Django](https://docs.djangoproject.com/en/1.10/) /!\**  
Elle en illustre seulement notre usage.
# Architecture

```
WebPyRobot
├── backend
│   ├── admin.py
│   ├── apps.py
│   ├── fixtures/
│   ├── forms.py
│   ├── api_views.py
│   ├── constants.py
│   ├── consumers.py
│   ├── funct/
│   ├── game/
│   ├── migrations/
│   ├── models.py
│   ├── static/
│   ├── templates/
│   ├── tests.py
│   ├── update_battles.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── db.sqlite3
└── WebPyRobot
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── asgi.py
    ├── production.py
    └── development.py
```

# L'arborescence du site

Le fichier _/WebPyRobot/backend/urls.py_ contient arborescence interne de notre
application sous forme d'expressions régulières. Ce fichier est ensuite inclut dans
le site grâce au fichier _/WebPyRobot/WebPyRobot/urls.py_ qui représente 
l'arborescence de tout le site. Cette hiérarchisation permet de déplacer toute
l'application sans modifier son comportement interne en cas de changement d'url.

Chaques expressions est rattachée à une action et à un nom. Les actions sont
représentées sous la forme de fonctions dans le contrôleur (voir chapitre suivant).
Les noms quant à eux servent à faire des résolutions dynamiques entre noms et 
adresses réelles.

Afin de séparer environnement de production et developpement, deux configurations
_/WebPyRobot/WebPyRobot/production.py et _/WebPyRobot/WebPyRobot/developpement.py
ont été crées.

# Les contrôleurs/vues
Remarque intéressante: dans Django, le contrôleur, comme sont nom l'indique,
s’appelle `view.py` car ils ne correspondent qu'a une seule entité.

Chaque vue est responsable de faire une des deux choses suivantes: retourner un
objet HttpResponse contenant le contenu de la page demandée, ou lever une 
exception, par exemple Http404.Nous avons utilisé le système de gabarits de 
Django pour séparer le style du code Python en créant des gabarits que les vues pourront utiliser.

Un répertoire nommé _/WebPyRobot/backend/templates_ ce trouve dans notre
application. C’est là que Django recherche les gabarits. Ce dossier contient donc
toute les "sources" que verra l'utilisateur (image, html, css, js, etc.).
Pour une représentation plus traditionnelle du MVC: _templates_ représente les vues
et _view.py_ représente les contrôleurs.

# Les modèles

Un modèle est la source d’information unique et définitive pour nos données. 
Il contient les champs essentiels et le comportement attendu des données que vous 
stockerez. Django respecte la philosophie DRY (Don’t Repeat Yourself).
Le but est de définir le modèle des données à un seul endroit, et 
ensuite de dériver automatiquement ce qui est nécessaire à partir de celui-ci.

Ceci inclut les migrations. Au contraire de Ruby On Rails, par exemple, les
migrations sont entièrement dérivées du fichier des modèles et ne sont 
fondamentalement qu’un historique que Django peut parcourir pour mettre à jour le 
schéma de la base de données pour qu’il corresponde aux modèles actuels.

Les modèles ce trouve dans le fichier _/WebPyRobot/backend/models.py_.
Le modèle `UserProfile` étant le modèle d'authentification de Django pour ajouter
des informations seulement nécessaire dans l'application.
