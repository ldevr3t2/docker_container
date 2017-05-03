FROM python
COPY python-flask-server /app
WORKDIR /app

RUN ls -la

# Get pip to download and install requirements:
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT python3 -m swagger_server
