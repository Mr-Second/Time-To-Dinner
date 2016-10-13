from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import JsonResponse
from apps.time2eat.view.api import *
def all_list(request):
	res = ResProf.objects.all()
	return render_to_response('time2eat/all_list.html', locals())
def inside_resturant(request, res_id):
	res = ResProf.objects.get(id=res_id)
	return render_to_response('time2eat/inside_resturant.html',locals())
def purchase(request, res_id):
	res = ResProf.objects.get(id=res_id)
	return render_to_response('time2eat/purchase.html',locals())
