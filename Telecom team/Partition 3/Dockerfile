FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests

WORKDIR /app

COPY http_script.sh .
COPY http_script.py .

RUN chmod +x http_script.sh http_script.py

CMD ["./http_script.sh"]