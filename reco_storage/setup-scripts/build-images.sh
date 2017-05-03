#!/bin/bash

docker build -t reco-storage-mongodb ./docker/reco-storage-mongodb

docker build -t reco-storage-setup ./docker/reco-storage-setup

docker build -t reco-storage-webserver .
