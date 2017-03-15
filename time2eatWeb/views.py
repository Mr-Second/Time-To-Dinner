from django.shortcuts import render_to_response, render
from gluttonyTw.models import ResProf
from gluttonyTw.models import Order
from djangoApiDec.djangoApiDec import queryString_required

def index(request):
	res =''
	isChkGroup=''
	print('chkgroup' in request.GET and request.GET['chkgroup']=='T')
	if 'chkgroup' in request.GET and request.GET['chkgroup']=='T':
		isChkGroup =True
		res =Order.objects.all()
	else:
		isChkGroup =False
		res = ResProf.objects.all()

	print(res)
	print(isChkGroup)
	return render_to_response('time2eatWeb/index.html', locals())

def inside_resturant(request):
	if 'res_id' in request.GET and request.GET['res_id']!='':
		res = ResProf.objects.get(id=request.GET['res_id'])
	return render_to_response('time2eatWeb/inside_resturant.html',locals())

def check(request):
	return render_to_response('time2eatWeb/check.html',locals())

@queryString_required(['res_id'])
def purchase(request):
	from gluttonyTw.view.get_user import get_user
	res = ResProf.objects.get(id=request.GET['res_id'])
	EatU, upperuser = get_user(request)
	return render(request, 'time2eatWeb/purchase.html', locals())