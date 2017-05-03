docker rmi --force $(docker images -f "dangling=true" -q)
docker rm $(docker ps -a -f status=exited -q)
