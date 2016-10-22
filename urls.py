# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import apps.time2eat
urlpatterns = patterns('apps.time2eat.views',
  url(r'^$','index', name='index'),#這樣做似乎是對應到,首頁
  url(r'^all_list/$', 'all_list', name='all_list'),
  url(r'^inside_resturant/$', 'inside_resturant', name='inside_resturant'),
  url(r'^purchase/$', 'purchase', name='purchase'),
  url(r'^check/$', 'check', name='check'),
  url(r'^api/order/$', 'rest_api', name='rest_api'),
  url(r'^api/order/user/$', 'user_api', name='user_api'),
  url(r'^api/restaurant_prof/$', 'restaurant_prof', name='restaurant_prof'),
)
