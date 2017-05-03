#!/bin/bash

eval $(docker-machine env manager)

docker node update \
    --label-add config=false \
    --label-add shard0=false \
    --label-add shard1=false \
    --label-add shard2=false \
    --label-add replicanum=-1 \
    manager

docker node update \
    --label-add config=true \
    --label-add shard0=true \
    --label-add shard1=true \
    --label-add shard2=true \
    --label-add replicanum=0 \
    worker1

docker node update \
    --label-add config=true \
    --label-add shard0=true \
    --label-add shard1=true \
    --label-add shard2=true \
    --label-add replicanum=1 \
    worker2

docker node update \
    --label-add config=true \
    --label-add shard0=true \
    --label-add shard1=true \
    --label-add shard2=true \
    --label-add replicanum=2 \
    worker3

./build-images.sh


eval $(docker-machine env worker1)
./build-images.sh

eval $(docker-machine env worker2)
./build-images.sh

eval $(docker-machine env worker3)
./build-images.sh
