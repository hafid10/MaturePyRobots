# Development Diary [TER]
When we make changes in our project and push them to github then others pull those changes, it sometimes requires more additional steps to apply those changes (migrate, install requirements ...). So the committers, please note your summary of changes and how to apply these changes here.

### May 18, 2018 - Alex & Ayoub

* To apply all changes:
~~~~~
$ rm db.sqlite3
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py loaddata backend/fixtures/database.json
~~~~~

* Alex
  * PA & PM transition to PA
  * Users special [almost done]
  * Disabling some content

* Ayoub
  * Set Up urls tests

### May 13, 2018 - Ayoub

* Merge [Failure]

### May 12, 2018 - Alex

* Users special for tests (not stable)

### May 9 to 11, 2018 - Alex

* Set up users special

* Set up Championship mode: Private/Public

* New registration form

### May 7 & 8, 2018 - Alex

* Health bar in battle view

* New deign (pictures, icons, navbar style)

* Set up CronJob

### May 1 to 3, 2018 - Alex
* To apply all changes:
~~~~~
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py loaddata backend/fixtures/database.json
~~~~~

* Material Icons support for FAQ

* [In battle] Pop-Up system for more interactive animation

* Handling the defense for a better game experience

* Improve game mechanics for better animation

* Change password [UPDATE]

* Bugs fixed

### Apr 29 & 30, 2018 - Alex
* Contextual autocomplete (editor update)

* Change time zone - Update timestamp view for BH

* Some pictures of the development

### Apr 28, 2018 - Alex

* To apply all changes:
~~~~~
$ rm db.sqlite3
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py loaddata backend/fixtures/database.json
~~~~~

* Championship development completed

### Apr 27, 2018 - Alex
* Disable point gain in versus mode

* Enable add code via a file from player's computer

### Apr 20 to 26, 2018 - Alex
* Standard tank for all players

* Ranking display

* Choose a player to challenge him

* Choose a player to train

* Bug fix

### Apr 19, 2018 - Alex
* Update of the graphic charter (2)

* Bug fix

### Apr 16 to 17, 2018 - Alex
* Update of the graphic charter (1)

* Update of the framework version