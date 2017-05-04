FROM kyma/docker-nginx
COPY ./ /var/www

RUN echo "# Added proxy locations \n\
location /suggestion { \n\
    proxy_pass http://suggest-server:8080/v1; \n\
}\n\
\n\
location /fingerprint {\n\
    proxy_pass http://fingerprint-server:8080/team2/fingerprint;\n\
}" >> /etc/nginx/nginx.conf

CMD 'nginx'
