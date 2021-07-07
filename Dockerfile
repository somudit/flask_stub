FROM python:3.6-slim-buster

RUN python3 -m venv /venv

RUN apt-get -qy update && apt-get -qy install \
        git \
        openssl \
        curl \
        build-essential \
        libc6-dev \
        default-mysql-client \
        zlib1g-dev \
        libssl-dev \
        default-libmysqlclient-dev \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir -p /usr/local/aerospike/lua

WORKDIR /flask_stub
COPY requirement.txt requirement.txt
RUN /venv/bin/pip install -r requirement.txt

RUN rm requirement.txt

ENV TZ=Asia/Kolkata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo ${TZ} > /etc/timezone

COPY . /flask_stub

EXPOSE 5000

CMD ["/venv/bin/gunicorn", "app:app", "--config=gunicorn.conf",  "--max-requests=5000", "--max-requests-jitter=5000"]
