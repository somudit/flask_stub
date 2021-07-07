Table of Contents
=================

#### Build payment_service for Dev Environment

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y --no-install-recommends binutils \
    build-essential \
    curl \
    gdal-bin \
    less \
    libffi-dev \
    libfreetype6-dev \
    libgeoip1 \
    libgeos-dev \
    libjpeg8-dev \
    liblcms2-dev \
    libmysqlclient-dev \
    libncurses5-dev \
    libproj-dev \
    libssl-dev \
    libtiff5-dev \
    libwebp-dev \
    libxml2-dev \
    libxslt1-dev \
    net-tools \
    netcat \
    python-gdal \
    python3-dev \
    python3.6-dev \
    software-properties-common \
    tzdata \
    unzip \
    && rm -rf /var/lib/apt/lists/* \
```
    
##### Creating Virtual Environment
```
virtualenv -p python3.6 payment_service

source activate payment_service
```

##### Installing python dependencies
```
pip install -r requirements.txt
```

#### Running pylint
For files in last commit:
git log --format="%H" -n 1 | xargs git diff-tree --no-commit-id --name-only -r | grep .*.py | xargs pylint

#### Running pytest


#### Building with Docker


#### Running Docker
  


