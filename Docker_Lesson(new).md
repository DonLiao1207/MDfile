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
#Docker hub網址
https://hub.docker.com

#docker hub pull image
docker pull jupyter/base-notebook:latest

#確認pull好的image
docker images
```

##### 2. docker run
```
#確認執行中的container
docker ps 

#確認已有的container
docker ps -a

#根據image啟動container
1.不帶指令
docker run --name jup_test1 jupyter/base-notebook:latest

2.bind port
docker run --name jup_test2 -p 8888:8888 jupyter/base-notebook:latest

3.刪除container
docker rm jup_test1 jup_test2

3.bind port and volume
docker run --name jup_test -v /home/don/jupyter/:/home/jovyan/jupyter -p 8888:8888 jupyter/base-notebook:latest
>>>mount test<<<

#停止container
docker stop jup_test

#啟動container
docker start jup_test

```
##### 3. docker exec and commit
```
#進入已啟動的container
docker exec -it jup_test /bin/bash

conda install pandas
>>>python-jupyter test<<<

docker commit -m '20200219' jup_test don/jup:1.0

```

##### 4. docker export-import
```
#export/import
docker export -o jup_test.tar jup_test
docker import jup_test.tar jup_test:1.01

```

##### 5. dockerfile

```
https://hub.docker.com/r/jupyter/base-notebook/dockerfile

# build ubuntu and python3.6 dockerfile
# docker build -t ubuntu1804py36
FROM ubuntu:18.04

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:jonathonf/python-3.6
  
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
	apt-get install -y git

# update pip

RUN python3.6 -m pip install pip --upgrade && pip3 install --upgrade setuptools &&  pip3 install pyarrow==0.13.0 \
&& pip3 install tensorflow==1.12.0 \
&& pip3 install pandas==0.24.2 \
&& pip3 install keras==2.2.4 \
&& pip3 install psycopg2-binary

RUN python3.6 -m pip install wheel

```

##### 6. docker-compose
```
#根據docker-compose.yml內容建立container
docker-compose build 
docker-compose up

#停止container
docker-compose stop

#移除container
docker-compose down
```
