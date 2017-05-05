# docker_container
The docker swarm for team 3's final project.


# What is this repository for? #

- This project is a music recognition and recommendation service, runnable as a docker swarm.
- Version 1.0


# Docker Swarm Setup #

The process to setup the docker swarm is tedious, so the folder `setup-scripts` contains helper scripts to automate sections of this setup. All setup scripts are intended to be run within the `docker_container` folder, e.g. `$ ./setup-scripts/build-images.sh`.


## Prerequisites ##
- OS: Ubuntu 16.04 LTS
- Docker is installed
- Strong network connection
- VirtualBox is installed


## Setup steps ##
### Step 1 - Create Virtual Machines ###

Run `$ ./setup-scripts/setup1_create-machines.sh`

- Sets up 4 VMs: `manager`, `worker1`, `worker2`, `worker3`
- Creates port forwarding rules to access web servers from localhost
  * Port `8080`: web app
  * Port `8081`: fingerprint service
  * Port `8082`: suggestion service
  * Port `8083`: storage service


### Step 2 - Create Swarm ###

Run `$ ./setup-scripts/setup2_create-swarm.sh`

When shown, copy the displayed command and paste it into the command prompt

- Initializes a swarm on the manager machine
- Commands worker machines to join the swarm as workers


### Step 3 - Label Machines ###

Run `$ ./setup-scripts/setup3_machine-labels.sh`

- Applies labels to the worker nodes for placement of database containers


### Step 4 - Build Images on VMs ###

Run `$ ./setup-scripts/setup4_machine-builds.sh`

- Builds docker container images on each VM


### Step 5 - Deploy Swarm for the First Time ###

Run `$ ./setup-scripts/setup5_first-deploy.sh`

- Creates the external network (allows external setup containers to be attached to the network and easily removed)
- Deploys swarm
- Runs setup container to create replica sets
- Starts up mongo shard router
- Configures sharded database on shard router


## Redeploy Swarm ##

If needed, run `$ ./setup-scripts/setup6_redeploy.sh` to redeploy the swarm.

This script performs the following actions:

- Remove the stack from the swarm
- Pull the git repo
- Re-build container images on VMs
- SRe-sart stack on swarm

**NOTE:** The shards, replica sets, and mongo shard router retain their configuration as long as the docker volumes are not removed in the redeploy process


## Shallow Clean Machines ##

To "shallow clean" the VMs (by removing unused container images), run `$ ./setup-script/shallow-clean-machines.sh`


## Deep Clean Machines ##

To "deep clean" the VMs (by removing all docker container images and removing all docker volumes) run `$ ./setup-script/setup8_deep-clean-machines.sh`


