from django.shortcuts import get_object_or_404, render_to_response, render
from django.utils import timezone # auto generate create time.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.time2eat.models import Order, UserOrder, SmallOrder, EatUser, Dish, ResProf
from apps.time2eat.view.api import rest_api, user_api
from apps.time2eat.view.purchase import purchase
import requests, json

def index(request):
	return render_to_response('time2eat/index.html', locals())

def all_list(request):
	res = ResProf.objects.all()
	return render_to_response('time2eat/all_list.html', locals())

def inside_resturant(request, res_id):
	res = ResProf.objects.get(id=res_id)
	return render_to_response('time2eat/inside_resturant.html',locals())

def check(request):
	return render_to_response('time2eat/check.html',locals())
