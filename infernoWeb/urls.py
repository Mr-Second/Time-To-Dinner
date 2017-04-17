
# -*- coding: utf-8 -*-
from django.conf.urls import url
from infernoWeb import views
from infernoWeb.view import sloth
urlpatterns = [
  url(r'^$',views.index, name='index'),#這樣做似乎是對應到,首頁
  url(r'^inside_resturant/$', views.inside_resturant, name='inside_resturant'),
  url(r'^purchase/$', views.purchase, name='purchase'),
  url(r'^check/$', views.check, name='check'),
  url(r'^boss/$', views.boss, name='boss'),
] + [
  # 課程心得的部份
  url(r'^sloth$',sloth.index, name='sloth')
]

