## Gitgub
---
##### 1.設定config
```
#使用者及mail
git config --global user.name "<Your Name>"
git config --global user.email "<your@gmail.com>"
```
##### 2.新增git repository
```
#到目錄下
git init
```
##### 3.add file to git space
```
git add file
```
##### 4.commit 檔案到local
```
git commit file
```
##### 5.github page create your repository
##### 6.add 本地commit檔案到遠端
```
git remote add origin 網址
```  
##### 7.push 到遠端完成上傳
```
git push -u origin master (-f)
#git push origin master
#git checkout master
#git branch -u origin/master
#若兩邊已有的檔案中，遠端與當地的內容不同則須先pull再push
git pull
DonLiao1207

```
##### 8.修改檔案後更新到github
```
#1. 查看不同
git diff
#2. 新增修改
git add .
#3. 確認修改
git commit
#4. 上傳修改（推上）
git push -u origin master 
```
##### Git repo取得信任
```
git config credential.helper store
$ git push https://github.com/owner/repo.git

Username for 'https://github.com': <USERNAME>
Token for 'https://USERNAME@github.com': <Token>

#設定timeout
git config --global credential.helper 'cache --timeout 7200'
```
