#!/bin/bash

eval $(docker-machine env manager)

docker network create --driver=overlay --attachable mainnet

# docker stack deploy -c docker-swarm-large.yml finalT3 && \
#     docker run --rm --network=mainnet reco-storage-setup ./setup-storage_1.sh && \
#     docker run --rm --network=mainnet -it reco-storage-setup

docker stack deploy -c docker-swarm-large.yml finalT3 && \
    docker run --rm --network=mainnet -it reco-storage-setup