# docker_container
The docker swarm for the final.

- [What is this repository for?](#what-is-this-repository-for-)
- [Single Docker Container](#single-docker-container)
  * [Prerequisites to Run](#prerequisites-to-run)
  * [How to generate a single Docker container and run locally](#how-to-generate-a-single-docker-container-and-run-locally)
  * [How to Stop the Docker Container](#how-to-stop-the-docker-container)
  * [To configure host/ui address](#to-configure-host-ui-address)
  * [Changing the port number](#changing-the-port-number)
- [Local Docker Swarm](#local-docker-swarm)
  * [Prerequisites to Run](#prerequisites-to-run-1)
  * [Creating a Docker Swarm](#creating-a-docker-swarm)
    + [Creating the Docker Machines](#creating-the-docker-machines)
    + [Initializing the Swarm](#initializing-the-swarm)
    + [Building the container in the docker machines](#building-the-container-in-the-docker-machines)
    + [Deploying the service](#deploying-the-service)
    + [Testing the service](#testing-the-service)
    + [Stopping the Swarm](#stopping-the-swarm)
- [Online Docker Swarm](#online-docker-swarm)
  * [Prerequisites to Run](#prerequisites-to-run-2)
  * [Creating a Docker Swarm](#creating-a-docker-swarm-1)
  * [To configure host/ui address](#to-configure-host-ui-address-1)
  * [Changing the port number](#changing-the-port-number-1)

## What is this repository for? ##

* This project is to a music recognition and recommendation service, runnable as a docker container.
* Version 1.0

## How to generate a single Docker container and run locally ##
1. go ahead and gitclone this repo
`git clone https://github.com/ldevr2t1/docker_storage.git`
2. Run **git checkout local**
3. Navigate into the web directory (i.e. cd web)
4. run docker commands to get server running - may have to **sudo**
    * `docker-compose build`
    * `docker-compose run`
5. Access your machine-ip address (docker-machine ip) in your web browser
    * `The UI should be viewable at **192.168.99.100/v2/ui**`
6.  If you cannot access the UI then change the **'host'** address in the **swagger.yaml** file
    * **To get Machine ip address:** `Run docker-machine ip` 
    * **Update swagger.yaml:** `host: "<Machine Ip-Address>"`
    * Repeat steps 4 and 5

## How to Stop the Docker Container ##
Run the command `docker stop [id]`, where `[id]` is the generated id number of your container. If you do not know what your container id is, use the command `docker ps` to view all running containers.

## To configure host/ui address
1. To change the server's IP-address edit the **'host'** parameter in main.
    * `File: web/swagger_server/__main__.py`
        - `app.run(host='<your_address>', port=<port_number>)`
    
2. Change the host parameter in the **swagger.yaml** file for the UI to work
    * `web/swagger_server/server/swagger.yaml`
        - `host: "<your_address>:<port_number>"`

## Changing the port number
1. Change the *<port_number>* in the same files for configuring the host/ui address
2. Go into the base directory /docker_pathfind and edit the **docker-compose.yml**
    * `ports: ` 
        `- "<port_number>:<port_number>"`
3. Change the **Dockerfile** (i.e. change the EXPOSE #)
    * `#Expose port # for testing`
    -`    EXPOSE <port_number>`

# Local Docker Swarm #

## Prerequisites to Run ##
* Docker is installed
* VirtualBox is installed
* Your device is connected to the internet (to clone the repository and download required libraries)

## Creating a Docker Swarm ##

In order to build a Docker Swarm locally on your machine, follow the steps below:

### Creating the Docker Machines ###
1. Build the Manager with `docker-machine create <name_of_manager>`, where name_of_manager is the name of your machine
2. Build the Workers with `docker-machine create <name_of_worker>`, where name_of_worker is the name of your machine. You may repeat this as many times as you'd like, but **remember the machine names!**.

### Initializing the Swarm ###
Run these commands in the following order:
1. SSH into your manager directory with `docker-machine ssh <name_of_manager>`
2. Run `docker swarm init --advertise-addr <ip_of_manager>` to initialize the manager
3. Copy the returned command, and detach from the container with `^d`
4. Now, ssh into the other workers using the command in part 1, pasting in the command returned from part 3.

### Building the container in the docker machines ###
1. Run `docker-machine env <name_of_worker>` to get access to a command in the commments. This command allows you to reroute your container from your own files, and is different depending on the OS. Run that command now.
2. go ahead and gitclone this repo
`git clone https://github.com/ldevr2t1/docker_storage.git`
3. Navigate to the cloned directory
4. Run **git checkout local**
5. Run `docker-compose -f docker-compose-swarm.yml build`
6. Repeat step 1 and 5 with all workers.

### Deploying the service ### 
1. Run `docker-machine env <name_of_manager>` to get access to a command in the commments. This command allows you to reroute your container from your own files, and is different depending on the OS. Run that command now.
2. run `docker stack deploy -c docker-compose-swarm.yml <name_of_service`, where name_of_service is the name of your swarm.

### Testing the service ###
1. Type `docker-machine ls` to see the addresses hosting your machines
2. Go to a browser and type **<address>:8000/v3/ui/**, where address is the ip of one of the machines

### Stopping the Swarm ###
`docker-machine stop <name_of_machine>`

# Online Docker Swarm #

In order to build a Docker Swarm remotely, follow the steps below:

## Prerequisites to Run ##
* Docker is installed
* Your device is connected to the internet (to clone the repository and download required libraries)

## Creating a Docker Swarm ##
Follow the steps located in **Local Docker Swarm**, but use `docker-machine create driver amazonec2 --amazonec2-access-key <access_key> --amazonec2-secret-key <secret_key> <name_of_machine>` instead.


## To configure host/ui address ##
1. To change the server's IP-address edit the **'host'** parameter in main.
    * `File: web/swagger_server/__main__.py`
        - `app.run(host='<your_address>', port=<port_number>)`
    
2. Change the host parameter in the **swagger.yaml** file for the UI to work
    * `web/swagger_server/server/swagger.yaml`
        - `host: "<your_address>:<port_number>"`

## Changing the port number ##
1. Change the *<port_number>* in the same files for configuring the host/ui address
2. Go into the base directory /docker_pathfind and edit the **docker-compose.yml**
    * `ports: ` 
        `- "<port_number>:<port_number>"`
3. Change the **Dockerfile** (i.e. change the EXPOSE #)
    * `#Expose port # for testing`
    -`    EXPOSE <port_number>`

### Authors ###

* David Gwizdala

