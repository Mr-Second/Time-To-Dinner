# -*- coding: utf-8 -*-
from django.conf.urls import url
from t2e import views
from t2e.view.join_order import join_order
urlpatterns = [
  url(r'^$',views.index, name='index'),#這樣做似乎是對應到,首頁
  url(r'^all_list/$', views.all_list, name='all_list'),
  url(r'^inside_resturant/$', views.inside_resturant, name='inside_resturant'),
  url(r'^purchase/$', views.purchase, name='purchase'),
  url(r'^check/$', views.check, name='check'),
  url(r'^api/order/$', views.rest_api, name='rest_api'),
  url(r'^api/order/user/$', views.user_api, name='user_api'),
  url(r'^api/order/join$', views.join_order, name='join_order'),
  url(r'^api/order/join_order_list$', views.join_order_list, name='join_order_list'),
  url(r'^api/restaurant/prof/$', views.restaurant_prof, name='restaurant_prof'),
  url(r'^api/restaurant/list/$', views.restaurant_list, name='restaurant_list'),
  url(r'^api/restaurant/menu/$', views.restaurant_menu, name='restaurant_menu'),
]
