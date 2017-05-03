FROM python

ADD ./reco-storage_flask /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-m", "swagger_server"]
