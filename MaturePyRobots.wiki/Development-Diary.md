# Development Diary
When we make changes in our project and push them to github then others pull those changes, it sometimes requires more additional steps to apply those changes (migrate, install requirements ...). So the committers, please note your summary of changes and how to apply these changes here.

### Nov 29 Son and Alex
Alex: Updated frontend

Son:  Added weapon PA constraint, make FAQ addable/editable via admin dashboard.

### Nov 29 Samy
Updated wiki.

### Nov 28 Son
Update Alex's exp calculator

Hide result from end-users in html soure

Only calculate exp/level when battle ends on the frontend side

Added Tank hp value

Apply: `python3 manage.py migrate`


### Nov 28 Alex
Enable Exp function relative to level - Tutorial - Update views

Apply:
`$ python3 ./manage.py migrate`

before
`$ python3 ./manage.py runserver`

### Nov 27 Samy
Enabled script testing via the "Tester" button in the editor view.

### Nov 26 Son
Added support for resuming battle (correct using of Skip button)

Apply:
` $ python3 manage.py migrate`

Added support for finishing a battle immediately (Finish Battle button)


### Nov 25 Alex
Passive Mode corrected

Default User lvl modified

New Design Items

Apply:

`$ python3 ./manage.py migrate`

`$ python3 ./manage.py loaddata backend/fixtures/database.json`

before 

`$ python3 ./manage.py runserver`

### Nov 24 Alex and Son
Validation for AI script content


### Nov 23 Alex and Son
Updated design

Added support multiple AI


### Nov 22 Alex and Son
Updated the templates (converted from old style to new)

Added some utility functions for Game class


### Nov 15, 2017 - Alex and Son
#### Alex
New template design

Exp and level support - ongoing
#### Son
Real time notification

Added pagination to history view

Apply:

`$ pip install -r requirements.txt`

`$ ./manage.py migrate`


### Nov 8, 2017 - Son
Reverted changes in development.py file. This file should not be committed because it contains our local settings only


### Nov 4, 2017 - Son
Added battle history view

Apply:

`$ ./manage.py migrate`



###  Nov 1, 2017 - Alex
Automatic login after signing up

Some small fixes about URLs


### Oct 27, 2017 - Alex
Drag and drop


### Oct 25, 2017 - Samy and Alex
#### Samy
Added Travis support

Updated README

#### Alex
Added autocomple to python editor

Updated some small changes on the main page


### Oct 18, 2017 - Son
Added install guide


### Oct 4, 2017 - Son
Deployed the code to the production server


### Oct 3, 2017 - Son
Added production settings


### Sep 28, 2017 - Son and Samy
Initiated the code 
