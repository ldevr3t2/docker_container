#!/bin/bash

eval $(docker-machine env manager)
docker stack rm finalT3
# docker volume prune

git pull

./setup-scripts/setup4_machine-builds.sh

# eval $(docker-machine env worker1)
# docker volume prune


# eval $(docker-machine env worker2)
# docker volume prune


# eval $(docker-machine env worker3)
# docker volume prune


eval $(docker-machine env manager)

docker stack deploy -c final-swarm.yml finalT3
