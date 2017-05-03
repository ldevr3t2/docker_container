#!/bin/bash

eval $(docker-machine env manager)

docker swarm init --advertise-addr 192.168.99.100

echo 'Copy and paste the command shown above into the command line below:'

read docker_join_cmd

eval $(docker-machine env worker1)
eval ${docker_join_cmd}

eval $(docker-machine env worker2)
eval ${docker_join_cmd}

eval $(docker-machine env worker3)
eval ${docker_join_cmd}
