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

#####PostgreSql row-level security
```
-- 權限組定義
CREATE TABLE groups (group_id int PRIMARY KEY,
                     group_name text NOT NULL);

INSERT INTO groups VALUES
  (1, 'low'),
  (2, 'medium'),
  (5, 'high');

GRANT ALL ON groups TO alice; -- alice is the administrator
GRANT SELECT ON groups TO public;

-- 用戶的權限級別定義
CREATE TABLE users (user_name text PRIMARY KEY,
                    group_id int NOT NULL REFERENCES groups);

INSERT INTO users VALUES
  ('alice', 5),
  ('bob', 2),
  ('mallory', 2);

GRANT ALL ON users TO alice;
GRANT SELECT ON users TO public;

-- 保持受保護信息的表
CREATE TABLE information (info text,
                          group_id int NOT NULL REFERENCES groups);

INSERT INTO information VALUES
  ('barely secret', 1),
  ('slightly secret', 2),
  ('very secret', 5);

ALTER TABLE information ENABLE ROW LEVEL SECURITY;

-- 行對於安全group_id大於或者等於行的group_id的用戶是可見的/可更新的
CREATE POLICY fp_s ON information FOR SELECT
  USING (group_id <= (SELECT group_id FROM users WHERE user_name = current_user));
CREATE POLICY fp_u ON information FOR UPDATE
  USING (group_id <= (SELECT group_id FROM users WHERE user_name = current_user));

-- 我們只依賴RLS保護信息表
GRANT ALL ON information TO public;
```

```
"SELECT concat(gateway_id, lpad(ns_id::text, 3, '0')) as row_id, node_id, name "+
"FROM sensor_bk "+
"WHERE gateway_id = "+
"(SELECT id "+
"FROM gateway "+
"WHERE ai_tag is not null) "
```
```
89	【L1】0000528331	100	12
90	【L2】0000522107	100	12
91	【L3】0000170266	100	12
92	【L4】88706060310	100	12
93	【L5】0000150974	100	12
94	【L6】0000094147	100	12
95	【L7】0000163101	100	12
96	【L8】88290060173	100	12
97	【L9】0000522618	100	12
98	【L10】0000516045	100	12
```
```
#!/bin/bash

let x=0

for i in {1..5};
do
    sh /home/don/PHM_Learning/Orisol/dev_B0KI_Oven_0.1/dev_B0KI_Oven/dev_B0KI_Oven_run.sh
    sleep 10s
    let x=x+1
    echo $x
    if [ $x -eq 5 ]
    then
      matlab -nodisplay -nosplash -nodesktop -r "run('/home/don/PHM_Learning/Orisol/Matlab_Code/Matlab_Inference/Inference.m'); exit;"
    else
      :
    fi

donedevice check 有更新才有值

```
```
"SELECT concat(gateway_id, lpad(ns_id::text, 2, '0')) as row_id, node_id, name  "+
"FROM sensor_bk "+
"WHERE  id = 2 AND gateway_id = 2 
OR  id = 9 AND gateway_id = 2 
OR  id = 12 AND gateway_id = 2 
OR  id = 15 AND gateway_id = 2 
OR  id = 3 AND gateway_id = 2"

"SELECT concat(gateway_id, lpad(ns_id::text, 3, '0')) as row_id, node_id, name  "+
"FROM sensor_bk "+
"WHERE  id = 2 AND gateway_id = 2"+
"OR  id = 9 AND gateway_id = 2"+
"OR  id = 12 AND gateway_id = 2"+
"OR  id = 15 AND gateway_id = 2"+
"OR  id = 3 AND gateway_id = 2"
25004:6011:O4-Power<>25004:6014:O4-Voltage<>25004:6017:O4-Current<>25004:6004:O4-Temp-a<>25004:6005:O4-Temp-b

```

