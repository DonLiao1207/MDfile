##Docker無法安裝
#####修改respository
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   stretch\
   stable"
```

##Docker 常用指令
```
#查看目前存活的cotainer
docker ps -a

#進入cotainer
docker exec -ti container_name bash

#刪除cotainer
docker rm -f container_id 

#刪除image
docker rmi -f image_id
```
##安装portainer
#####執行portainer
```
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```
