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