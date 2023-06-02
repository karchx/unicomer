#!/bin/bash

dev="dev"
deploy="deploy"

if [[ $1 == $dev ]]; then
    docker-compose -f docker-compose.dev.yml up
else
    echo "env not config"
fi