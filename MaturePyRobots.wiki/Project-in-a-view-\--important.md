# MaturePyRobots

For people who want to continue this project ...

## Description
This project provides a simple coding game for Pythonisti. Well, you create an account then you have a tank with some basic equipments and an AI which helps you control your tank in a battle. You can edit this AI with some pre-defined functions from the system. So this is not really a coding game, it's kind of customizing game or puzzle game. You have functions (move, shoot ...) like puzzles and your job is to try your best to sort them out. When you start a battle, the system will randomly choose a player as your opponent. You will get experience and money after the battle, and yes winner always takes more than loser. Your level will up once you get enough experience. When your level ups, your tank hp value will increase too. You can buy new equipments in Shop to make your tank stronger. Note that weapon needs a number of PA (point d'action) points to be able to shoot. This PA points of your tank comes from Processeur. 

## Techniques
This project has been built using Python3, Django, Django Channels (for realtime notifications), Materialize + Jquery + WebSocket + html5 for frontend, PostgreSQL and has been deployed using Nginx, Redis (for Channels layer), Supervisord (managing processes) on a Debian server.

## Architecture
Well, this project is really ... awesome. Just kidding, believe me, if I have enough time I would rather build it from scratch than to continue this project. The team who started this project, I guess they didn't even read any tutorial of Django. So if you wanna continue this project and you don't know anything about Django I suggest that you should pass through the getting started tutorial on https://www.djangoproject.com/ . It costs you few days to read, however it will save you weeks of coding. Don't just try to make it work, let try to make it work perfectly!

So what do we have here? A Django project named WebPyRobot. We (my team) changed the repo name to MaturePyRobots as the teachers want. However the project name is still WebPyRobot. There is only one app named "backend" (hmm, it's not a good name - Django doesn't like it). Here is the architecture in files:

-- WebPyRobot/ : Root dir

---- backend/ : app dir. backend/frontend code are here

---- conf/ : this dir contains all configuration files to deploy the project to production

---- WebPyRobot/ : Django settings dir of the project

-------- development.py: for local development only

-------- production.py: for production

-------- settings.py: base settings of the project

---- manage.py : django command file for depvelopment

---- prod_manage.py : django command file for deployment

---- requirements.txt : python dependencies of the projects

----  init.sh : for lazy users who want to install the project on their machine. 

---- run.sh : run the project for lazy users. After running this file, go to localhost:8000 and enjoy!

Let's talk deeply into the core of the project. In backend/models.py, there are definitions of all models: UserProfile (profile of user ...), Tank, Weapon, BattleHistory (hold battle info), AI ... I guess I don't need to tell you what is model in Django. There is a module in backend/Game named Game.py. It contains all logic code of how to process a battle between two players. In this module, there are two class: Robot and Game. The Robot class represents a tank with AI. The Game class handle battle between two users. So how does a battle occur? You will find in backend/views.py a method/function named fight(request), it's a Django view method. In this method you will see, the system get a list of players which have level in the range of [current player's level -5, current player's level + 5], then it randomly selects a player in this list as the opponent for the current player in the battle. When two users are available, the system get their tanks and AI scripts then the Game class will be called and take these info to initiate a battle. The battle will be calculated very quickly by the Game class. When you see the battle starts on your browser, actually its result is ready in the system. All you see in the browser is just a replay ^^ However don't worry, end users have no way to know this result. You can stop your battle in the middle and resume it. It will start from where it left. You can also finish the running battle to start new one. Note that if you have a running battle, you can't start other battle. We setup Django Channels to handle realtime notifications (opponent will get a realtime notification if he is online and you start a battle against him) and other realtime data like battle info: we send players's position info from the frontend to the backend to save in a BattleHistory object in order to be able to resume this battle if it stops in the middle. About AI system, you have maximum 5 AI script. There is only one active script at a time and it will be selected for the battle. Dont try to use "import" or "exec" here. It's illegal! Hmm, the code of the equipment system is really mess. Unfortunately we don't have enough time to clean it. 

## What we have done
- Changed the frontend design. It's more beautiful than before.
- Updated old templates to make them extend one base template. Before each template file has its own style
- Added battle history
- Added FAQ
- Added Tutorial
- Added constraint for equipping weapon
- Stop/Resume battle
- Finish battle immediately
- Added support for multiple AI scripts
- Added experience, level system, HP for tank
- Corrected bonus money for each battle
- Added validation for AI script 
- Battle replay
- Realtime notifications. This is quite important implement. You can base on it to create a realtime game, not a 'replay' game like it now.
- Clean up some code to make them DRY - we haven't finished it yet :((
- Deploy a production: http://maturepyrobot.com/. If this site died, that means my Google Compute Engine instance is running out of money :)

## Next targets
- If you have enough time, let build the project from scratch!
- Currently players can't select their opponent. I think the system should let players be able to select their opponents. Because players may want to compare their AI. One user should be able to accept or deny a challenge from other user. Sending/Accepting/Denying challenge could be done using Django Channels.
- Friend list. Players should have their friends list.
- Notification history like Facebook (already added model for this)
- Showing hp values during the battle
- Obstacles in map should work. Currently battle animation is build using html5. Maybe you should use other javascript framework for better animation display. 
- Clean up the code, break down the views.py file into small separated views (one view per file). Take a look in the code and you know why.
- Should change the app name 'backend' to something more Django friendly.
- Write unit tests

## Our advices 
- I repeat again: if you don't know anything about Django, please start by taking some tutorials about it before touching the code. The same for Python. Remember DRY (don't repeat yourself) principles of Python and Django. It's good to start by reading this book: https://www.twoscoopspress.com/products/two-scoops-of-django-1-11. If not, the getting started tutorial from djangoproject.com is good enough.
- Should have a production server. Development is just 80% of a web project, deployment holds the rest 20%. Deployment will let you know how your project run in real life.
- Add comments to your code, so the next team will handle the code easily. We didn't add so many comments to our code, but I think it's good enough for you to understand what we did. However we don't have enough time to add comments to other codes.
- If you love Python and Django, Django Channels is something you should study carefully. It's the future of Django!
- Feel free to ask us any smart question about the project. 