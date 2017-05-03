#!/bin/bash

eval $(docker-machine env manager)

docker network create --driver=overlay --attachable mainnet

docker stack deploy -c docker-swarm-large.yml finalT3 && \
    docker run --rm reco-storage-setup ./setup-storage_1.sh && \
    docker run --rm -it reco-storage-setup
