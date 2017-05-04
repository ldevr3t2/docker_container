#!/bin/bash

eval $(docker-machine env manager)

docker build -t musica-webapp ./webapp

docker build -t musica-fingerprint ./fingerprint

docker build -t musica-suggest ./music_suggest

docker build -t musica-storage-mongodb ./reco_storage/docker/reco-storage-mongodb

docker build -t musica-storage-setup ./reco_storage/docker/reco-storage-setup

docker build -t musica-storage-webserver ./reco_storage



eval $(docker-machine env worker1)

# docker build -t musica-fingerprint ./fingerprint

# docker build -t musica-suggest ./music_suggest

docker build -t musica-storage-mongodb ./reco_storage/docker/reco-storage-mongodb

# docker build -t musica-storage-webserver ./reco_storage



eval $(docker-machine env worker2)

# docker build -t musica-fingerprint ./fingerprint

# docker build -t musica-suggest ./music_suggest

docker build -t musica-storage-mongodb ./reco_storage/docker/reco-storage-mongodb

# docker build -t musica-storage-webserver ./reco_storage



eval $(docker-machine env worker3)

# docker build -t musica-fingerprint ./fingerprint

# docker build -t musica-suggest ./music_suggest

docker build -t musica-storage-mongodb ./reco_storage/docker/reco-storage-mongodb

# docker build -t musica-storage-webserver ./reco_storage

