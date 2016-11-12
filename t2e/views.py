from django.shortcuts import get_object_or_404, render_to_response, render
from django.utils import timezone # auto generate create time.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from t2e.models import Order, UserOrder, SmallOrder, EatUser, Dish, ResProf
from t2e.view.api import rest_api, user_api
from t2e.view.restaurant_list import restaurant_list
from t2e.view.restaurant_prof import restaurant_prof
from t2e.view.restaurant_menu import restaurant_menu
from t2e.view.purchase import purchase
import requests, json

def index(request):
	return render_to_response('time2eat/index.html', locals())

def all_list(request):
	res = ResProf.objects.all()
	print(res[0])
	print(res[0].avatar.url)
	return render_to_response('time2eat/all_list.html', locals())

def inside_resturant(request):
	if 'res_id' in request.GET and request.GET['res_id']!='':
		res = ResProf.objects.get(id=request.GET['res_id'])
	return render_to_response('time2eat/inside_resturant.html',locals())

def check(request):
	return render_to_response('time2eat/check.html',locals())
