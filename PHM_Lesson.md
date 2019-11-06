## PHM Lesson
##### 1.Step1_Data_Preprocessing

##### 2.Step2_Feature_Extration

##### 3.Step3_Feature_Selection

##### 4.Step4_Train_LR_Model

##### 5.Step5_Train_SVM_Model2

##### 6.Step6_Data_Visualization

##### Day2 Case1
```
1.費雪分數越大表示越能分開兩特徵
2.normalization(zscore, 除n非n-1)
3.研究特徵重要性是否合乎物理意義
#SVM
#混淆矩陣
#交叉驗證
#kfloss
#accuracy = 1-classloss
#LR label 決定也許考慮設備狀況
#DL資料量要夠要夠對等，ML資料量不對等較無差
#ML提取特徵具有物理意義, DL不知物理意義
#CV Value 對 
#生產出相同品質產品，經過大保養後回覆最高品質（用pca檢驗），label值可以區分

```
##### Day4 Case2
```
#x, y 三軸加速規
#資料疊合必需要做
#function 與檔名需一致
#matlab語法[a b]= 並排兩組矩陣 [a; b]= 縱排兩組矩陣
#RMS的物理意義代表振動的能量
#數據間相依性在feature draven時看得出來
#檢定方法可以幫忙檢定數據交互性
#需確定normalization的前後結果是否不同
#雷達圖上代表cv value
#baseFreq1=108; %直接觀察振動FFT頻譜圖base freq取得
#李捷教授常用四種data visualization
#Degradation chart- cv value
#Radar chart cv value
#Classification and Fault map -SOM
#Risk radar
```
##### Day5 Case3
```
#FCFT fix cycle 根據機器做動的一個標準循環
#5000? all answer?
#如果看不出來載波
#一開始圖要有跡象
#如果多個faulty資訊的費雪分數如何處理→選解釋力強的case
#SVM一次無法分很多類(mulitclasses)只能一層一層分
#PCA只能告訴你其他分類與baseline有統計上的顯著差異
#可以分出幾類狀態後再回推
#ROC curve 分出底下面積為正確率
#T2 and SPE根據pca算出
#閥值取法？有公式，確認問題可以接受的誤報率
```

##### Day6 PCA
```
#T^2 and SPE(累積error值)
#Prognosability study of ball screw degradation systematic
#bathub curve
#FIR BandPass Filter
#envlope filter包絡線，希爾波特濾波器
```
##### 0值過濾
```
#每日power會歸0（累積功率）
#暫停時會有null值
#前溫有值，後溫無值
#前溫無值，後溫有值
#每天剛開始都是從0開始

```
##### oven
```
#跨日問題
#異常值刪除：平均值+-三倍標準差設為資料閥值
#60秒取一點沒有對應到實際的60秒
#分成三群，找出"可能引起嚴重的故障"
#

```
