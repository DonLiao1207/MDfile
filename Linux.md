## Linux

##### wc file 計算檔案的列數、字數、及位元數。
```
cat filename| head -n 3000 | tail -n +1000 顯示1000行到3000行

```
##### echo 檔案內容利用nc以udp傳入elk.pouchen.com port5146
```
echo '' > /var/log/rsyslog/172.23.174.9/LOGSTASH.log
echo "***text***" | nc -v -u elk.pouchen.com 516
bash read.sh | nc -v -u 172.23.181.193 516
```

##### scp用法
```
scp sysadmin@172.16.5.231:/var/log/syslog-ng/172.16.5.9/2019_02_14.txt /home/don/Downloads/2019_02_14.txt
scp WannaCry/ don@172.23.165.78:/home/don/workspace
```

##### udpsvd
```
cat syslog UDP 514 port
sudo udpsvd 0.0.0.0 514 cat
```
##### tee
```
#tee命令相當於把stdout副本寫入檔案，再把stdout傳給下一個命令，但是錯誤內容是無法用tee傳遞的，如同使用>>追加內容,tee可以使用-a選項追加：
複製程式碼 程式碼如下:
sudo udpsvd 0.0.0.0 514 tee /home/don/t2.log
```
##### 程序記憶體使用排序
```
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
```

##### 程序CPU使用排序
```
top -b -o +%CPU | head -n 17
```

##### Thunderbird
```
#filter rule path
find ~/.thunderbird/ -name msgFilterRules.dat
```
##### MX linux browser input/output error
```
/usr/bin/google-chrome-stable --no-sandbox
```
##### x11vnc 安裝後啟動（遠端軟體） 
#####  增加使用者
```
sudo adduser don sudo 
```
##### ffmpeg
```
#以fps=5的速度輸出影片為圖片
ffmpeg -i 01.mp4 -vf fps=5 out%d.png

#

```

##### webcam即時轉成picture
```
#1.webcam找到rtsp的資訊
#2.fmpeg -i rtsp://admin:1234@172.23.160.44/ipcam_h264.sdp -vf fps=1 out%d.png
#guvcview
```

##### Linux big5 to utf-8
```
find . -type f -name '*.m' -print -exec iconv -f big5 -t utf-8 {} -o {} \;

```