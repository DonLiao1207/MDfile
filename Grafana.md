##Grafana
#####grafana on docker
```
https://grafana.com/docs/installation/docker/
```
#####script
```
$ docker run \
  -d \
  -p 3000:3000 \
  --name=grafana \
  -e "GF_SERVER_ROOT_URL=http://grafana.server.name" \
  -e "GF_SECURITY_ADMIN_PASSWORD=9527" \
  grafana/grafana
```
#####設定連線到postgresql
```
#host必須選擇container ip, 而非localhost:5432
```

#####Grafana 連接 Postgresql
```
#1.timestamp不能有null值
#2.資料型態要正確
#3.table 不能用graph繪圖
```