## SVN
##### 1.checkout目錄回到本機
```
svn co svn網址 目錄
```

##### 2.操作新增刪除修改
```
#add
svn add file(folder)

#delete
svn delete file(folder)
```

##### 3.commit所作動作回svn
```
svn ci
```

##### svn show  file 
```
svn list -R | grep (....**
```

##### svn rename
```
#Target file does not exist:
svn mv old_file_name new_file_name

#Target file already exists in repository:
svn mv old_file_name new_file_name 

#Target file already exists locally 
svn mv old_file_name new_file_name 

```