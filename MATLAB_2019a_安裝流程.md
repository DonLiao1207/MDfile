20190708 - 新的安裝 程序解答
======================================
* How do I install or update the Network License Manager?
    * https://www.mathworks.com/matlabcentral/answers/105860-how-do-i-install-or-update-the-network-license-manager

* How do I install a MATLAB client for a network license?
    * https://www.mathworks.com/matlabcentral/answers/106003-how-do-i-install-a-matlab-client-for-a-network-license

* 安裝步驟
    * http://kmshareall.blogspot.tw/2015/03/matlab-r2015a-fik.html

* 2019a
    * File Installation Key (這是測試版的，有全部的包):
    * 28350-52195-55176-39251-05206-01263-33087-41606-23576-06280-03465-58983-29289-18349-41044-38687-64056-08931-20869-43607-41001-15127

* File Installation Key: 56752-18101-44527-22658-23899 (輸入這串才對，公司付錢版)

* 下面是 R2019a 下載連結，有購買授權客戶，歡迎下載安裝!
    * R2019a Windows (64bit)
        * https://drive.google.com/file/d/146Iysg6fsKX7bKbEm-jFaHZRJ4FZrysD/view?usp=sharing
    * R2019a Linux (64bit)
        * https://drive.google.com/file/d/16tg3f6wAo210x_jDatQvd6FeNNi8Eu7M/view?usp=sharing
    * R2019a macOS (64bit)
        * https://drive.google.com/file/d/1HCYqQqzW2Y60OkO3PtjecrxVFl3muH0A/view?usp=sharing

* MATLAB Linux 安裝流程
```bash 
# 注意1. 不要用root安裝
# 注意2. 不要在home或主機目錄資料夾安裝，在桌面創一個資料夾，然後把iso放進去解壓縮，在裡面做事情，不要放到home目錄裡面解壓縮，會壞光

mkdir /home/howard/Desktop/matlab_installer
cd  /home/howard/Desktop/matlab_installer
sudo 7z x R2019a_Linux.iso # 解壓縮

# 解壓縮完給資料夾權限
sudo chmod 777 -R /home/howard/Desktop/matlab_installer

# 開始安裝
cd /home/howard/Desktop/matlab_installer
./install 

# 安裝至：/home/howard/MATLAB/R2019a
# 輸入: File Installation Key: 56752-18101-44527-22658-23899
# 指令啟動 .lic 路徑：給 network.lic
# license.lic 是給昆文更新 License Server manager用的

# 啟動
cd /home/howard/MATLAB/R2019a/bin/
bash activate_matlab.sh
# 給 network.lic  -(內容為公司連線資訊)
# 啟動失敗跟 License Manager 有關需請昆文協助

# 開啟應用程式
cd /home/howard/MATLAB/R2019a/bin/
./matlab
```

File Installation Key:
  28350-52195-55176-39251-05206-01263-33087-41606-23576-06280-03465-58983-29289-18349-41044-38687-64056-08931-20869-43607-41001-15127