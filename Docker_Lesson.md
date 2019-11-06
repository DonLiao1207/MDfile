## Docker 課程實作
##### 1. pull image
```
docker pull ubuntu
https://hub.docker.com
docker pull ubuntu
docker pull ubuntu:latest
docker pull ubuntu:xenial-20191024
docker images
```
##### 2. docker run
```
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
##### 5. docker export and import

```
docker export -o test.tar test
ls -al test.tar
docker import test.tar test:1.01
docker import link
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
