#!/bin/bash

eval $(docker-machine env manager)

docker swarm init --advertise-addr 192.168.99.100 > swarm-init.out

echo 'Copy and paste the command from ./swarm-init.out into the command line below:'

read docker_join_cmd

rm ./swarm-init.out

eval $(docker-machine env worker1)
eval ${docker_join_cmd}

eval $(docker-machine env worker2)
eval ${docker_join_cmd}

eval $(docker-machine env worker3)
eval ${docker_join_cmd}
