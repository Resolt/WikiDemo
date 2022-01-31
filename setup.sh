#!/bin/sh

source ./docker-compose.env
docker build . -t $IMAGE_TAG
docker-compose -f docker-compose.prod.yml --env-file ./docker-compose.env up -d