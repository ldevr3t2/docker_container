#!/bin/bash

docker-machine create manager

docker-machine create worker1

docker-machine create worker2

docker-machine create worker3

VBoxManage controlvm manager natpf2 webapp,tcp,,8080,,8080

VBoxManage controlvm manager natpf2 fingerprint,tcp,,8081,,8081

VBoxManage controlvm manager natpf2 suggestion,tcp,,8082,,8082

VBoxManage controlvm manager natpf2 storage,tcp,,8083,,8083

