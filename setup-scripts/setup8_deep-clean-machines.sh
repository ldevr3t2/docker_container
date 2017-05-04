#!/bin/bash

eval $(docker-machine env worker1)
docker rmi -f $(docker images -q)
docker volume prune -f

eval $(docker-machine env worker2)
docker rmi -f $(docker images -q)
docker volume prune -f

eval $(docker-machine env worker3)
docker rmi -f $(docker images -q)
docker volume prune -f

eval $(docker-machine env manager)
docker rmi -f $(docker images -q)
docker volume prune -f
