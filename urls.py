# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import apps.time2eat 
urlpatterns = patterns('apps.time2eat.views',
  url(r'^$','time2eat'),#這樣做似乎是對應到首頁
  url(r'^all_list/$', 'all_list'),
  url(r'^all_picture/$', 'all_picture'),
  url(r'^inside_resturant/$', 'inside_resturant'),
  url(r'^inside_resturant/$', 'inside_resturant'),
  url(r'^nearby_picture/$', 'nearby_picture'),
  url(r'^nearby_list/$', 'nearby_list'),
  url(r'^nearby_listpic/$', 'nearby_listpic'),
<<<<<<< HEAD
  url(r'^purchase/$', 'purchase'),
=======
  url(r'^import_json/$', 'import_json', name='import_json'),
>>>>>>> 8fa446c96a6667210dc3d8abe6501fa0b2dde8f7
)