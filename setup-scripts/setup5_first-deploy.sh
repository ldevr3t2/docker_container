#!/bin/bash

eval $(docker-machine env manager)

docker network create --driver=overlay --attachable mainnet

docker stack deploy -c final-swarm.yml finalT3 && \
    docker service update finalT3_reco-storage-router --replicas 0 && \
    docker run --rm --network=mainnet -it musica-storage-setup ./setup-storage_1.sh && \
    docker service update finalT3_reco-storage-router --replicas 0 && \
    sleep 5 && \
    docker run --rm --network=mainnet -it musica-storage-setup ./setup-storage_2.sh