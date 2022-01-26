#!/bin/sh

: ${HOST=0.0.0.0}
: ${PORT=8888}
: ${WORKERS=2}

python manage.py migrate
gunicorn wiki_demo.wsgi -b $HOST:$PORT -w $WORKERS