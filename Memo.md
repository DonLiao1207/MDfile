##DGX Station ip
```
ssh don@172.23.172.247;Az9527
```

##lab Station
```
ssh don@172.23.165.78;Az9527
```
##檢查514port使用情況
```
lsof -i :514
```

##map 514 port map logfile
```
sudo docker run -ti -d -p 514:514/udp -v /home/don/workspace/WannaCry/:/workpace don:1.0 /bin/bash
docker exec -ti ***id /bin/bash
```

##build dockerfile use host network
```
sudo docker build --network=host -t='don:1.0' .
```

##pycharm docker
```
xhost +
docker run --rm \
  -e DISPLAY=${DISPLAY} \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/.PyCharm:/home/don/.PyCharm \
  -v ~/.PyCharm.java:/home/don/.java \
  -v ~/.PyCharm.py2:/usr/local/lib/python2.7 \
  -v ~/.PyCharm.py3:/usr/local/lib/python3.5 \
  -v ~/Project:/home/don/Project \
  --name pycharm-$(head -c 4 /dev/urandom | xxd -p)-$(date +'%Y%m%d-%H%M%S') \
  pycharm:latest
```

##Linux

#####wc file 計算檔案的列數、字數、及位元數。
```
cat filename| head -n 3000 | tail -n +1000 顯示1000行到3000行

```
#####echo 檔案內容利用nc以udp傳入elk.pouchen.com port5146
```
echo '' > /var/log/rsyslog/172.23.174.9/LOGSTASH.log
echo "***text***" | nc -v -u elk.pouchen.com 516
bash read.sh | nc -v -u 172.23.181.193 516
#!/bin/bash

cat '0417.log' | while read line
do
        echo $line
        sleep 1
done


```

#####scp用法
```
scp sysadmin@172.16.5.231:/var/log/syslog-ng/172.16.5.9/2019_02_14.txt /home/don/Downloads/2019_02_14.txt
scp WannaCry/ don@172.23.165.78:/home/don/workspace
```

#####udpsvd
```
cat syslog UDP 514 port
sudo udpsvd 0.0.0.0 514 cat
```
#####tee
```
#tee命令相當於把stdout副本寫入檔案，再把stdout傳給下一個命令，但是錯誤內容是無法用tee傳遞的，如同使用>>追加內容,tee可以使用-a選項追加：
複製程式碼 程式碼如下:
sudo udpsvd 0.0.0.0 514 tee /home/don/t2.log
```
#####程序記憶體使用排序
```
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
```

#####程序CPU使用排序
```
top -b -o +%CPU | head -n 17
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

##Wanna Cry的Attack，log會有此關鍵字
```
[MS.SMB.Server.Trans.Peeking.Data.Information.Disclosure」、「Backdoor.DoublePulsar」。
```


##Thrift
#####Tresult
```
try:
      num_rows = 1000
      results = cl.getScannerRows(scanner_id, num_rows)
      
      arr={'Data1':[],'Data2':[]}
      
      for item in results: 
            #arr.get('Data1').append(item.columnValues)
            #arr.get('Data2').append(item.row)
            print(len(results))
finally:

results = 掃到幾行row key (0,9001)-> result=2

```

#####使用thrift2的timerange從python取得hbase data，
```
1.happybase底層是使用thrift的api，不支援timerange
2.thrift2支援,但是thrift compiler0.10.0以後版本才支持python3+
3.安裝0.10.0版本後重開機才有用
4.下載hbase有thrift2的src..的壓縮檔，對hbase-thrift/source---裡面的hbase.thrift使用0.10.0以後編譯產生py檔，整包hbase資料夾丟到python lib sitepackage裡
5.若有找不到TReservice檔去網路找
6.timerange的使用方法是

sc=TScan(columns=[TColumn(family=b'v',qualifier=b'6018')],timeRange=TTimeRange(1548201600000,1548302082000))

scanner_id = cl.openScanner(
    table=t2,
    tscan=sc,
)
之後scan
```


##Apache Arrow 筆記
```
1.有提供parquet，hdfs,csv,featerfomat
2.shared_ptr[InputStream] stream
3.Cython,C++11
4.Arrow利用現代Intel CPU中的數據並行性（SIMD）•Arrow優化CPU預取和緩存
5.SIMD即單指令多數據流，能夠複製多個操作數，並把它們打包在大型寄存器的一組指令集。以同步方式，在同一時間內執行同一條指令。

原文網址：https://kknews.cc/zh-tw/tech/r9kxzxr.html
```


##docker安裝
#####修改respository
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   stretch\
   stable"
```

##thunderbird郵件過濾檔案
```
msgFilterRules.dat
```