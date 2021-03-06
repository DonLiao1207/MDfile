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

#若ssh密碼正確確無法使用->進入伺服器端
#清空錯誤登入紀錄
faillog -r
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

##### Linux  firewall
```
ufw stop...
```

##### Linux 對時
```
sudo ntpdate time.stdtime.gov.tw
sudo date -s "2019-11-01 10:06:00"
```

##### Linux check port
```
sudo lsof -i -P -n
#確認python 版本
sudo update-alternatives --config python3
x11vnc -display :0 -auth /var/run/lightdm/root/:0 -forever -bg -o /var/log/x11vnc.log -rfbauth /etc/x11vnc.pass -rfbport 5900

end script

```

##### Http server web folder
```
1.curl -sL https://vnt87.github.io/nodemx/nodesetupmx_12.x | sudo bash -
2.sudo apt-get install -y nodejs
3.sudo npm install http-server-with-auth -g
4.http-server-with-auth --username pcg --password pcg [path]
```

##### truncate
```
#設定檔案為此大小（清空檔案）
truncate -s 0 out.csv
```
##### awk
```
#指定輸出行＋指定輸出欄
free --mega  | awk 'FNR == 2' | awk '{print $2 "\t" $4}'
```