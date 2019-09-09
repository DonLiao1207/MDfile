## ELK視覺化

##### 1.Kibana mapping
```
1.1.進入Kibana Console
1.2.先定義所需屬性

GET _search/template ///檢視範本
GET /_template
1.3.加入新索引並設定資料格式, for ex:

PUT orisol
{
 "mappings": {
      "properties": {
        "tool": {"type": "keyword"},
        "time": {
            "type": "date", 
            "format":"yyyy/MM/dd HH:mm:ssZZ"},
        "temp": {"type": "integer"},
        "voltage": {"type": "float"}
  }
 }
}

1.4.插入新資料
#POST _index/_type/_id ///可詳細指定

POST orisol/_doc
{
  "tool": "oven1",
  "time": "2019/08/15 10:03:11+0800",
  "temp": 49,
  "voltage": 757
}
```
##### 2.建立index pattern
```
2.1 左側選單選擇Management
2.2 Kibana->index pattern->create index pattern
2.3 選擇你#3所PUT的索引
2.4 選擇時間field
2.5 Create
```

##### 3.儲存你的Dicover
```
3.1 左側選單選擇Discover
3.2 選擇你Create的index pattern
3.3 選擇你的屬性並確認資料是否出現
3.4 存檔
```

##### 4.視覺化
```
4.1 選擇你要的圖形Create new visualization
4.2 選擇你儲存的Discover
4.3  x軸選擇時間, y軸顯示max,min,median...等等
4.4 選擇你的field, 完成
```

#####安全查詢
```
設定role及index選項
curl -XGET "http://localhost:9200/p1/_search" -u p1user:771207
role:
read_ccr
read_ilm
monitor

privileages:

Privileges
view_index_metadata
monitor
read
read_cross_cluster

#資料範圍授權，限定白金板使用
grant privileges
{
        "range" : {
            "temp" : {
                "gte" : 10,
                "lte" : 50,
                "boost" : 2.0
            }
        }
}
```

