#!/bin/bash

eval $(docker-machine env manager)
docker stack rm finalT3
docker volumes purge


eval $(docker-machine env worker1)
docker volumes purge

eval $(docker-machine env worker2)
docker volumes purge

eval $(docker-machine env worker3)
docker volumes purge

