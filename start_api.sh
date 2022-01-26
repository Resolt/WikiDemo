#!/bin/sh

: ${HOST=0.0.0.0}
: ${PORT=80}
: ${THREADS=2}

gunicorn wiki_demo.wsgi -b $HOST:$PORT -w $THREADS