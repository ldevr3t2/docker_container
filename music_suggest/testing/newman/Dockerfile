FROM postman/newman_ubuntu1404
RUN apt-get install -y wget
COPY music-suggest.postman_collection.json /etc/newman
COPY music-suggest.postman_environment.json /etc/newman
COPY data.csv /etc/newman
ENTRYPOINT ["newman", "run", "/etc/newman/music-suggest.postman_collection.json", "-e", "/etc/newman/music-suggest.postman_environment.json", "-d", "/etc/newman/data.csv", "--delay-request", "100"]
