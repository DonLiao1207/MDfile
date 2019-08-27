## OAuth 2.0
##### http://www.ruanyifeng.com/blog/2019/04/oauth_design.html

##### 專用名詞
```
（1）Third-party application：第三方應用程序，本文中又稱"客戶端"（cli​​ent），ex : Kibana。

（2）HTTP service：HTTP服務提供商，簡稱"服務提供商"，ex : SSO。

（3）Resource Owner：資源所有者，又稱"用戶"（user）。

（4）User Agent：用戶代理，就是指瀏覽器。

（5）Authorization server：認證服務器，即服務提供商專門用來處理認證的服務器。

（6）Resource server：資源服務器，即服務提供商存放用戶生成的資源的服務器。它與認證服務器，可以是同一台服務器，也可以是不同的服務器。
```

##### 流程
```
（A）用戶打開客戶端以後，客戶端要求用戶給予授權。

（B）用戶同意給予客戶端授權。

（C）客戶端使用上一步獲得的授權，向認證服務器申請令牌。

（D）認證服務器對客戶端進行認證以後，確認無誤，同意發放令牌。

（E）客戶端使用令牌，向資源服務器申請獲取資源。

（F）資源服務器確認令牌無誤，同意向客戶端開放資源。
```