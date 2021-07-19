# Image From Ubuntu
FROM ubuntu:18.04
  
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
 apt-get -y upgrade && \
 apt-get -y dist-upgrade && \
 apt-get -y autoremove

# Install Python3 and required libraries

RUN apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy libpython3-all-dev python3-pip libpython3-all-dev python3-all && \
 apt-get install -y libzbar0 && \
 apt install -y poppler-utils && pip3 install --upgrade pip

RUN apt-get install -y locales && locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

WORKDIR /app

# Requirements.txt
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Copy App
COPY PDFSolvent /app

# Create PDF Workdir
WORKDIR /pdf

ENTRYPOINT [ "python3", "/app"]
