#!/bin/bash
CWD="$(dirname $0)"
DOCKER_COMPOSE_FILE="${CWD}/docker-compose.yml"

docker-compose -f ${DOCKER_COMPOSE_FILE} build --pull || exit 1
docker-compose -f ${DOCKER_COMPOSE_FILE} up --exit-code-from tox

docker-compose -f ${DOCKER_COMPOSE_FILE} rm -sf
