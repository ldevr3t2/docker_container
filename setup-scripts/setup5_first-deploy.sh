#!/bin/bash

eval $(docker-machine env manager)

docker network create --driver=overlay --attachable mainnet

docker stack deploy -c final-swarm.yml finalT3 && \
    docker run --rm --network=mainnet -it musica-storage-setup