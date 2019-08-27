## SQL 相關
##### 使用dbeaver管理
##### postgre on docker
```
#使用script 啟動docker postgresql
#!/bin/sh

docker run                                  \
  --name sql	\
  -d                                        \
  -p 5432:5432                          \
  -e POSTGRES_USER=don               \
  -e POSTGRES_PASSWORD=9527       \
  -v /home/don/postgre:/var/lib/postgresql/data \
  postgres
```
##### 從csv檔插入
```
https://justnumbersandthings.com/post/2018-06-12-dbeaver-import-csv/
1) Create a folder to be used as your CSV Database
2) Create a CSV database connection
3) Connect to your target database
4) Ensure that the mappings of each of your columns is correct
```
##### 建立表時不能加入null值
```
ALTER TABLE oven."data" DROP COLUMN tat;
ALTER TABLE oven."data" DROP COLUMN pwr;
ALTER TABLE oven."data" DROP COLUMN vtg;
ALTER TABLE oven."data" DROP COLUMN amp;
ALTER TABLE oven."data" DROP COLUMN ti;
ALTER TABLE oven."data" DROP COLUMN hdt;
```
