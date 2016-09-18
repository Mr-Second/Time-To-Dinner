from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone # auto generate create time.
from apps.time2eat.models import Type , ResProf 
import json


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
<<<<<<< HEAD
def purchase(request):
	return render_to_response('time2eat/purchase.html',locals())
=======

def import_json(request):
	t={}
	t['country'] = '台灣' 
	t['ResType'] = '便當'  
	Tobj =Type.objects.create(**t)


	d = {}
	d['restaurant'] = '鼎日竹葉蒸飯' 
	d['address'] = '台中市南區仁義街89號' 
	d['district'] = '南區'
	d['service_h'] = 'Mon-Fri, Sun:11:00 am - 2:00 pm5:00 pm - 8:00 pm'
	d['phone'] = '04-2285-2888'
	d['ResLike'] = 3
	d['score'] = 3
	d['last_reserv'] = '無'
	d['create'] = timezone.localtime(timezone.now())
	ResObj, created = ResProf.objects.update_or_create(restaurant=d['restaurant'],defaults=d)
	ResObj.ResType.add(Tobj)
	return render_to_response('time2eat/all_list.html', locals())
>>>>>>> 8fa446c96a6667210dc3d8abe6501fa0b2dde8f7
