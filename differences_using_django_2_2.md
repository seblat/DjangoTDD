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
