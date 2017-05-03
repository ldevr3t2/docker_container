#!/bin/bash

eval $(docker-machine env manager)

docker build -t reco-storage-mongodb ./docker/reco-storage-mongodb

docker build -t reco-storage-setup ./docker/reco-storage-setup

docker build -t reco-storage-webserver .



eval $(docker-machine env worker1)

docker build -t reco-storage-mongodb ./docker/reco-storage-mongodb

docker build -t reco-storage-setup ./docker/reco-storage-setup

docker build -t reco-storage-webserver .



eval $(docker-machine env worker2)
docker build -t reco-storage-mongodb ./docker/reco-storage-mongodb

docker build -t reco-storage-setup ./docker/reco-storage-setup

docker build -t reco-storage-webserver .



eval $(docker-machine env worker3)
docker build -t reco-storage-mongodb ./docker/reco-storage-mongodb

docker build -t reco-storage-setup ./docker/reco-storage-setup

docker build -t reco-storage-webserver .
