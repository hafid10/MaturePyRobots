## URL
http://maturepyrobot.com/

## Contact
contactmaturepyrobot@gmail.com

## Server
- Google Cloud Compute Engine n1-standard-1 (RAM: 3.75GB, Hdd: 10GB, 1 CPU)
- Debian 9 (stretch)

## Requirements
- Python3.6.2 (/usr/local/bin/python3.6 - /usr/local/lib/python3.6 - build from source)
- pip3 (/usr/local/lib/python3.6/bin/pip - $ python3.6 get_pip.py)
- PostgreSQL (docker, postgres, version 9.6.5)
- Nginx (1.10.3 - $ sudo apt-get install nginx-full)
- uWsgi (2.0.15 - /usr/local/lib/python3.6/bin/uwsgi - sudo pip36 install uwsgi )
- supervisord (/etc/supervisor - $ sudo apt-get install supervisor)
- Django (1.11.5 - $ pip36 install Django)
- Django Channels
- Redis

## Working
- Django Channels provides an ASGI server (daphne) and a worker for handling websocket requests. You can start as many workers as you want. Daphne and Channels workers are managed by Supervisord. Config file: `conf/webpyrobot_channels_supervisord.conf`
- Nginx works as a reverse proxy between Daphne and the world. It communicates with Daphne via socket
- All static files (js, css, image) and media files (uploaded file) are served directly via Nginx




