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

# Chroma
RUN apt-get install python3.10-venv -y
RUN apt-get install git -y
RUN apt-get install build-essential -y
RUN apt-get install python3-dev -y

COPY . /app
WORKDIR /app

CMD ["/app/tools/init"]
