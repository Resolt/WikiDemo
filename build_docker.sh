#!/bin/sh

: ${TAG=wiki-demo}

poetry export --format requirements.txt --output requirements.txt
docker build . -t $TAG
rm requirements.txt