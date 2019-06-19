# [Chapter 3.6](https://www.obeythetestinggoat.com/book/chapter_unit_test_first_view.html#_urls_py)
Commit
## Original implementation (Django 1.1)
```
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
]
```
## Django 2.2 implementation
```
from django.urls import path
from lists import views


urlpatterns = [
    path('', views.home_page, name='home')
]
```

# [Chapter 7.4](https://www.obeythetestinggoat.com/book/chapter_working_incrementally.html#_iterating_towards_the_new_design)
Commit
## Original implementation (Django 1.1)
```
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),
]
```
## Django 2.2 implementation
```
urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/the-only-list-in-the-world/', views.view_list, name='view_list'),
]
```

Chapter 7.8
## Original implementation (Django 1.1)
```
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),
]
```
## Django 2.2 implementation
```
urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    path('lists/the-only-list-in-the-world/', views.view_list, name='view_list'),
]
```

Chapter 7.9
## Original implementation (Django 1.1)
```
from django.db import models

class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
```
## Django 2.2 implementation
```
from django.db import models

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey('List', default=None, on_delete=models.CASCADE)

class List(models.Model):
    pass
```

Chapter 7.10
## Original implementation (Django 1.1)
```
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/(.+)/$', views.view_list, name='view_list'),
]
```
## Django 2.2 implementation
```
urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    path('lists/<int:list_id>/', views.view_list, name='view_list'),
]
```
Chapter 7.12
## Original implementation (Django 1.1)
```
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/(\d+)/$', views.view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),
]
```
## Django 2.2 implementation
```
urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    path('lists/<int:list_id>/', views.view_list, name='view_list'),
    path('lists/<int:list_id>/add_item', views.add_item, name='add_item')
]
```
