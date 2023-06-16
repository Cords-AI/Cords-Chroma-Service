FROM ubuntu:22.04

RUN apt-get update

# User
RUN apt-get install sudo -y
RUN useradd -ms /bin/bash ubuntu -u 1000
RUN echo "ubuntu   ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN echo 'PATH=/home/ubuntu/.local/bin:$PATH' >> /home/ubuntu/.bashrc

# Utils
RUN apt-get install wget -y
RUN apt-get install curl -y

# universal-sentence-encoder-multilingual
RUN mkdir /model
WORKDIR /model
RUN wget https://tfhub.dev/google/universal-sentence-encoder-multilingual/3?tf-hub-format=compressed -O 3.tar.gz
RUN tar xfvz 3.tar.gz
RUN rm 3.tar.gz

# Chroma
RUN apt-get install python3.10-venv -y
RUN apt-get install git -y
RUN apt-get install build-essential -y
RUN apt-get install python3-dev -y
