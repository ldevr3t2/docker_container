# Web App 
The web application for VT Musica

## Build and run
1. `$ docker build -t [mysite] .`, where *mysite* is the name of your website
2. `$ docker run -p 80:80 -d mysite`

*To check that your instance is running, use `curl localhost`