#!/bin/bash

# Possible fix for using Compose file version 3.2 for network.attached property

# docker-machine create --virtualbox-boot2docker-url \
#     https://github.com/boot2docker/boot2docker/releases/download/v17.05.0-ce-rc3/boot2docker.iso \
#     manager

# docker-machine create --virtualbox-boot2docker-url \
#     https://github.com/boot2docker/boot2docker/releases/download/v17.05.0-ce-rc3/boot2docker.iso \
#     worker1

# docker-machine create --virtualbox-boot2docker-url \
#     https://github.com/boot2docker/boot2docker/releases/download/v17.05.0-ce-rc3/boot2docker.iso \
#     worker2

# docker-machine create --virtualbox-boot2docker-url \
#     https://github.com/boot2docker/boot2docker/releases/download/v17.05.0-ce-rc3/boot2docker.iso \
#     worker3

docker-machine create manager

docker-machine create worker1

docker-machine create worker2

docker-machine create worker3