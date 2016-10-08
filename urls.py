# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import apps.time2eat 
urlpatterns = patterns('apps.time2eat.views',
  url(r'^$','index', name='index'),#這樣做似乎是對應到,首頁
  url(r'^all_list/$', 'all_list', name='all_list'),
  url(r'^all_picture/$', 'all_picture', name='all_picture'),
  url(r'^inside_resturant/$', 'inside_resturant', name='inside_resturant'),
  url(r'^nearby_picture/$', 'nearby_picture', name='nearby_picture'),
  url(r'^nearby_list/$', 'nearby_list', name='nearby_list'),
  url(r'^nearby_listpic/$', 'nearby_listpic', name='nearby_listpic'),
  url(r'^purchase/$', 'purchase', name='purchase'),
  # url(r'^rest_api/(?P<res>\d+)/(?P<dateString>\w)/$|^$', 'rest_api', name='rest_api'),
  url(r'^rest_api/(?P<res_id>\d+)/(?P<dateString>[0-9-]*)$', 'rest_api', name='rest_api'),
  url(r'^user_api/(?P<user_id>\d+)/(?P<dateString>[0-9-]*)$', 'user_api', name='user_api'),
)
