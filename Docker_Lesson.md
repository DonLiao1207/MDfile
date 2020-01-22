## Docker 課程實作
##### before
```
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
sudo gpasswd -d user group
```
##### 1. pull image
```
docker pull python:3.6
docker pull tensorflow/tensorflow:1.15.0-py3-jupyter
sudo docker run -id -p 8888:8888 --name dontensor tensorflow/tensorflow:nightly-py3-jupyter
docker run 
docker pull ubuntu
https://hub.docker.com
docker pull ubuntu
docker pull ubuntu:18.04
docker images
```
##### 2. docker run
```
docker ps -a
docker run  ubuntu:18.04
docker ps -a
docker run --name don_ubuntu ubuntu
docker ps -a
docker rm 
docker run -idt --name test ubuntu:18.04
docker exec -it test /bin/bash
apt update
apt install -y software-properties-common
add-apt-repository ppa:jonathonf/python-3.6
apt update
apt install vi
apt install python3.6
```

##### 3. docker mount
```
docker run -idt --name test -v /home/don/grafana/test.py:/test.py ubuntu:latest
sudo add-apt-repository ppa:jonathonf/python-3.6
apt install software-properties-common
>>>mount test<<<

docker cp 8ba143885be3:/test.py /home/don/Desktop/test_cp.py

```
##### 4. commit image from container
```
docker commit -m '2019-11-05' 8ba143885be3 don/test:1.0
```
##### 5. docker export-import / save-load
```
#export/import
docker export -o test.tar test
ls -al test.tar
docker import test.tar test:1.01
docker import link

#save/load
docker save -o test.tar test:01
docker load -i test.tar
```

##### 6. docker rm
```
docker rm container id or name
docker rmi image id
```
##### 7. docker bind port
```
docker pull nginx
docker run --name nginx-hello -p 8080:80 nginx 
```

##### 8.dockerfile
```
# build ubuntu and python3.6 dockerfile
# docker build -t ubuntu1604py36
FROM ubuntu:18.04

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:jonathonf/python-3.6
  
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
	apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

```

##### 9.docker-compose
```
apt install docker-compose

```
