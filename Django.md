## 1.Install
````
https://github.com/twtrubiks/django-tutorial
````
---
## 2.url path

##### 從settung.py中的TEMPLATES 修改 DIR
````
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/don/django_tutorial/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
````
---

## 3.APP

##### 從setting加入你的app名稱
````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
]
````
---
## 4.urls.py更改網址，對應到views.py

## 5.修改default page
```
https://www.youtube.com/watch?v=zf3VWSbKXMg
```
## 6.連結到sql
```
#1.更改setting.py內的database
#2.使用物件方式呼叫，不會被sql injection

http://yltang.net/tutorial/django/7/
https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989
```