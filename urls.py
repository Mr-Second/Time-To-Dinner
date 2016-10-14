# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import apps.time2eat
urlpatterns = patterns('apps.time2eat.views',
  url(r'^$','index', name='index'),#這樣做似乎是對應到,首頁
  url(r'^all_list/$', 'all_list', name='all_list'),
  url(r'^inside_resturant/(?P<res_id>\d+)/$', 'inside_resturant', name='inside_resturant'),
  url(r'^purchase/(?P<res_id>\d+)/$', 'purchase', name='purchase'),
  url(r'^check/$', 'check', name='check'),
  url(r'^rest_api/(?P<res_id>\d+)/(?P<dateString>[0-9-]*)$', 'rest_api', name='rest_api'),
  url(r'^user_api/(?P<dateString>[0-9-]*)$', 'user_api', name='user_api'),
)
