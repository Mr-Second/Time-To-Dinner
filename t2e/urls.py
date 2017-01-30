# -*- coding: utf-8 -*-
from django.conf.urls import url
from t2e import views
from t2e.view import restaurant
from t2e.view import order

urlpatterns = [
  url(r'^$',views.index, name='index'),#這樣做似乎是對應到,首頁
  url(r'^all_list/$', views.all_list, name='all_list'),
  url(r'^inside_resturant/$', views.inside_resturant, name='inside_resturant'),
  url(r'^purchase/$', views.purchase, name='purchase'),
  url(r'^check/$', views.check, name='check'),
]

# restaurant api
urlpatterns += [
  url(r'^api/restaurant/$', restaurant.rest_api, name='rest_api'),
  url(r'^api/restaurant/prof/$', restaurant.restaurant_prof, name='restaurant_prof'),
  url(r'^api/restaurant/list/$', restaurant.restaurant_list, name='restaurant_list'),
  url(r'^api/restaurant/menu/$', restaurant.restaurant_menu, name='restaurant_menu'),
]

# order api
urlpatterns += [
  url(r'^api/order/user/$', order.user_api, name='user_api'),
  url(r'^api/order/join$', order.join_order, name='join_order'),
  url(r'^api/order/join_order_list$', order.join_order_list, name='join_order_list'),
]
