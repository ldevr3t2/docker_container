FROM python
COPY test_setup /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT python3 test_url_encoder.py
