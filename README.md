# docker_container
The docker swarm for team 3's final project.


# What is this repository for? #

- This project is a music recognition and recommendation service, runnable as a docker swarm.
- Version 1.0

# Public Web Link #

A Docker swarm has been set up on Matt Nikkel's desktop, and the services should be available at a link given in the submission. If any issues arise, please send an email to `nikkelma@vt.edu`.


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
  * Port `8080`: web app (UI accessible at `http://localhost:8080`)
  * Port `8081`: fingerprint service (UI accessible at `http://localhost:8081/team2/ui`)
  * Port `8082`: suggestion service (UI accessible at `http://localhost:8082/v1/ui`)
  * Port `8083`: storage service (UI accessible at `http://localhost:8083/v1/ui`)


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


# Individual Portions #
## Web App ##

Build: `$ docker build -t musica-webapp ./webapp`

Run: `$ docker run -p "80:80" musica-webapp`

**WARNING:** This will ***NOT*** result in a usable website. The nginx server is configured to forward the following URIs:

- `/suggestion/artist={artist_name}` => `http://suggest-server:8080/v1/artist={artist_name}`
- `/fingerprint` => `http://fingerprint-server:8080/team2/fingerprint`

**If any of the desination hosts cannot be reached, the web server will exit. Therefore, a standalone container will start and quickly exit.**

### Testing ###

Build test container: `$ docker build -t selwd:v1 ./webapp_testing`

Run tests: `$ docker run --rm selwd:v1`


## Fingerprint Service ##

Build: `$ docker build -t musica-fingerprint ./fingerprint`

Run: `$ docker run -p "8080:8080" musica-fingerprint`

**NOTE:** Submitting a recorded audio file requires sending a Base-64 string of length over 100,000+ characters to the server; testing this independently of the web app is a pain, but still possible using the fingerprint testing repository code.

### Testing ###

Found at [https://github.com/ldevr3t2/fingerprint_testing](<https://github.com/ldevr3t2/fingerprint_testing>)

Due to the large strings used, tests are best implemented using python.


## Suggestion Service ##

Build: `$ docker build -t musica-suggest ./music_suggest`

Run: `$ docker run -p "8080:8080" musica-suggest`

**NOTE:** This suggestion service relies on the storage service for cached data, so running a standalone contianer will add a fixed delay (equal to the timeout delay used when attempting to contact the storage service) to all requests.

### Testing ###

Build test containers: `$ docker-compose -f ./music_suggest/docker-compose.yaml build`

Run tests: `$ docker-compose -f ./music_suggest/docker-compose.yaml up`


## Storage Service ##

Build:
`$ docker build -t musica-storage-mongodb ./reco_storage/docker/reco-storage-mongodb && 
docker build -t musica-storage-setup ./reco_storage/docker/reco-storage-setup && 
docker build -t musica-storage-webserver ./reco_storage`

Run:
`docker network create --attachable mainnet; 
docker-compose -f ./reco_storage/docker-swarm-large.yml up -d && 
sleep 15 && 
docker run --network=mainnet musica-storage-setup ./setup-storage_1.sh && 
docker restart recostorage_reco-storage-router_1 && 
sleep 30 && \
docker run --network=mainnet musica-storage-setup ./setup-storage_2.sh`

**NOTE:** Service will be accessible on port `8083`.

### Testing ###

Build test container: `$ docker build -t reco-storage-test ./reco_storage/docker/reco-storage-test`

Run tests: `$ docker-compose -f ./reco_storage/docker-testing.yml up`

