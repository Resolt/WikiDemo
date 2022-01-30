#!/bin/sh

docker-compose -f docker-compose.prod.yml --env-file ./docker-compose.env down --remove-orphans
source ./docker-compose.env
docker rmi $IMAGE_TAG