@echo off

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata backend/fixtures/database.json
python manage.py runserver

pause