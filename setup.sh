#!/bin/sh

: ${TAG=wiki-demo}
docker build . --file Dockerfile --tag $TAG
docker-compose -f docker-compose.prod.yml --env-file ./docker-compose.env up -d