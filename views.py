from django.shortcuts import render_to_response,  get_object_or_404, render
from django.utils import timezone # auto generate create time.
from apps.time2eat.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder
from django.http import JsonResponse
import datetime
def index(request):
	return render_to_response('time2eat/index.html',locals())
def all_list(request):
	# with open('sites/sandbox/apps/time2eat/Crawler/json/final.json', 'r', encoding='UTF-8') as f:
	# 	j = json.load(f)
	# # print(j['台中'])
	# for typeRes in j['台中'].items():
	# 	for r in typeRes[1]:
	# 		d = {}
	# 		d['last_reserv'] = r['last_reserv']
	# 		d['score'] = r['score']
	# 		d['']
	# 		ResObj, created = ResProf.objects.get_or_create(restaurant=r['restaurant'],defaults=d)
	res = ResProf.objects.all()
	# print(res)
	return render_to_response('time2eat/all_list.html', locals())
def all_picture(request):
	return render_to_response('time2eat/all_picture.html',locals())
def inside_resturant(request):
	return render_to_response('time2eat/inside_resturant.html',locals())
def nearby_list(request):
	return render_to_response('time2eat/nearby_list.html',locals())
def nearby_picture(request):
	return render_to_response('time2eat/nearby_picture.html',locals())
def nearby_listpic(request):
	return render_to_response('time2eat/nearby_listpic.html',locals())
def purchase(request):
	return render_to_response('time2eat/purchase.html',locals())

