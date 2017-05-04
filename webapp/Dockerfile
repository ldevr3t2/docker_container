FROM kyma/docker-nginx
COPY ./ /var/www

RUN echo "# Added proxy locations \
location /suggestion { \
    proxy_pass http://suggest-server:8080/v1; \
} \
 \
location /fingerprint { \
    proxy_pass http://fingerprint-server:8080/team2/fingerprint; \
}" >> /etc/nginx/nginx.conf

CMD 'nginx'
