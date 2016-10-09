from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import JsonResponse
from apps.time2eat.view.api import *
def index(request):
	return render_to_response('time2eat/index.html',locals())
def base(request):
	return render_to_response('time2eat/base/base.html',locals())
def all_list(request):
	res = ResProf.objects.all()
	return render_to_response('time2eat/all_list.html', locals())
def all_picture(request):
	return render_to_response('time2eat/all_picture.html',locals())
def inside_resturant(request, res_id):
	res = ResProf.objects.get(id=res_id)
	return render_to_response('time2eat/inside_resturant.html',locals())
def nearby_list(request):
	return render_to_response('time2eat/nearby_list.html',locals())
def nearby_picture(request):
	return render_to_response('time2eat/nearby_picture.html',locals())
def nearby_listpic(request):
	return render_to_response('time2eat/nearby_listpic.html',locals())
def purchase(request, res_id):
	res = ResProf.objects.get(id=res_id)
	i = res
	return render_to_response('time2eat/purchase.html',locals())
