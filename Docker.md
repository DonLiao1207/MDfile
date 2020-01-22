## Docker無法安裝
##### 修改respository
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   stretch\
   stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

##  Docker 常用指令
```
#查看目前存活的cotainer
docker ps -a

#進入cotainer
docker exec -ti container_name bash

#刪除cotainer
docker rm -f container_id 

#刪除image
docker rmi -f image_id

#啟動container
docker start (container name)

```

## Docker run 指令
```
#mount local folder as volumes
-v host path:container path

#bind port/tcp
-p host port:container port/tcp

#bind port/udp
-p host port:container port/udp

#assign pid
--pid

#give name
--name

#detach mode
-d

#memory size
-m

#cmd
-it


```
##### docker 指定網段
```
#修改/etc/dokcer/daemon.js
{
  "bip": "192.168.200.1/24"
}

#docker-compose 會忽略 daemon.js, 必須自行設定

version: '3'

networks:
  outside:
    driver: bridge
    ipam:
      driver: default
      config:
      - subnet: 192.168.1.0/24
      
services:
  grafana:
    image: grafana/grafana:latest
    container_name: grafana_test
    ports:
      - '3000:3000'
    volumes:
      - ./grafana_config/grafana.ini:/etc/grafana/grafana.ini:ro
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - outside
```


## 安装portainer
##### 執行portainer
```
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
docker run --name portainer -d -p 9000:9000 --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /opt/portainer:/data portainer/portainer:1.20.0
```

## docker 實做練習

##### 1.Dokcer簡介
```
docker pull ubuntu
```
##### 2.Dokcer cmd
```
docker pull ubuntu
https://hub.docker.com
docker pull ubuntu
docker pull ubuntu:latest
docker pull ubuntu:xenial-20191024

docker ps -a
docker run  ubuntu:latest
docker ps -a
docker run --name don_ubuntu ubuntu
docker ps -a
docker rm 

docker run -idt --name test ubuntu:latest
docker exec -it test /bin/bash

apt install vi
apt install python3.6

docker export -o test.tar test
ls -al test.tar
docker import test.tar test:1.01
docker import link
docker run -idt --name test -v /home/don/grafana/test.py:/test.py ubuntu:latest
sudo add-apt-repository ppa:jonathonf/python-3.6
apt install software-properties-common

mount test


```

##### 3.Dockerfile
```

```
##### 4.Docker-compose
```
#create network 
driver:bridge
subnet:192.168.199.0/24
gateway:192.168.199.1
```