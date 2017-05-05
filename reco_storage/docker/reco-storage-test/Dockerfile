FROM postman/newman_ubuntu1404
COPY Music_Suggestion_Storage_API_new.postman_collection.json /etc/newman
COPY RecoStorage-Docker.postman_environment.json /etc/newman
ENTRYPOINT ["newman", "run", "/etc/newman/Music_Suggestion_Storage_API_new.postman_collection.json", "-e", "/etc/newman/RecoStorage-Docker.postman_environment.json"]

