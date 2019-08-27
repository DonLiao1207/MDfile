## Thrift
#####  Tresult
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

#####  使用thrift2的timerange從python取得hbase data，
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


## Apache Arrow 筆記
```
1.有提供parquet，hdfs,csv,featerfomat
2.shared_ptr[InputStream] stream
3.Cython,C++11
4.Arrow利用現代Intel CPU中的數據並行性（SIMD）•Arrow優化CPU預取和緩存
5.SIMD即單指令多數據流，能夠複製多個操作數，並把它們打包在大型寄存器的一組指令集。以同步方式，在同一時間內執行同一條指令。

原文網址：https://kknews.cc/zh-tw/tech/r9kxzxr.html
```
## Python基本套件

##### 1.Anaconda 版本為 4.6.7

##### 2.Create AI python env
```
conda create -n AI python=3.6
conda activate AI
```

##### 3.Tensorflow-1.12.0(內含numpy-1.16.0, pandas-0.23.4)
```
conda install -c conda-forge tensorflow==1.12.0
```

##### 4.Pyarrow-0.11.1
```
conda install -c conda-forge pyarrow
```

##### 5.Keras-2.2.4
```
conda install keras==2.2.4
```

####6.thrift0.11.0
```
conda install -c anaconda thrift==0.11.0
    **6.1 下載hbase檔案
    wget https://www.apache.org/dist/hbase/hbase-1.2.11/hbase-1.2.11-src.tar.gz
    **6.2 解壓縮
    tar zxvf hbase-1.2.11-src.tar.gz 
    **6.3 到thrift2 目錄
    cd /home/***/hbase-1.2.11/hbase-thrift/src/main/resources/org/apache/hadoop/hbase/thrift2
    **6.4 使用thrift 指令生成python檔案，會產生一個gen-py資料夾，將其複製到anaconda AI的lib目錄下
    thrift --gen py hbase.thrift 
    cd /home/***/hbase-1.2.11/hbase-thrift/src/main/resources/org/apache/hadoop/hbase/thrift2/gen-py/hbase
    cp /home/***/hbase-1.2.11/hbase-thrift/src/main/resources/org/apache/hadoop/hbase/thrift2/gen-py/hbase /home/***/anaconda3/envs/AI/lib/python3.6/site-packages/hbase
```



