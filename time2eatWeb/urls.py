
# -*- coding: utf-8 -*-
from django.conf.urls import url
from time2eatWeb import views
urlpatterns = [
  url(r'^$',views.index, name='index'),#這樣做似乎是對應到,首頁
  url(r'^inside_resturant/$', views.inside_resturant, name='inside_resturant'),
  url(r'^purchase/$', views.purchase, name='purchase'),
  url(r'^check/$', views.check, name='check'),
  url(r'^boss/$', views.boss, name='boss'),
]