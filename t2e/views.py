from django.shortcuts import render_to_response, render
from t2e.models import ResProf
from djangoApiDec.djangoApiDec import queryString_required

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

@queryString_required(['res_id'])
def purchase(request):
	from t2e.view.api import get_user
	res = ResProf.objects.get(id=request.GET['res_id'])
	EatU, upperuser = get_user(request)
	return render(request, 'time2eat/purchase.html', locals())