
# -*- coding: utf-8 -*-
from django.conf.urls import url
from time2eatWeb import views
urlpatterns = [
  url(r'^$',views.index, name='index'),#這樣做似乎是對應到,首頁
  url(r'^all_list/$', views.all_list, name='all_list'),
  url(r'^inside_resturant/$', views.inside_resturant, name='inside_resturant'),
  url(r'^purchase/$', views.purchase, name='purchase'),
  url(r'^check/$', views.check, name='check'),
]