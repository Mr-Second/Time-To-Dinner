from django.shortcuts import get_object_or_404, render
from t2e.models import Type, ResProf, Phone, Dish, Order, UserOrder, EatUser
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from djangoApiDec.djangoApiDec import queryString_required, date_proc
from django.utils import timezone # auto generate create time.
from django.urls import reverse
from t2e.models import ResProf, Order, UserOrder, SmallOrder, EatUser, Dish
from t2e.view.api import get_user
from t2e.class_file.purchaseProc import purchaseProc
import urllib, requests, json

# 顯示特定一間餐廳的詳細簡介資料
@queryString_required(['res_id', 'orderId'])
def join_order(request):
	ob = get_object_or_404(Order, id=request.GET['orderId'])
	if ob.isFinished(): raise Http404('api not found')
	res = ResProf.objects.get(id=request.GET['res_id'])
	EatU, upperuser = get_user(request)

	if request.POST:
		data = request.POST
		data=data.dict()
		uorder = UserOrder.objects.create( orderUser=EatU, total=0, order=ob, create=timezone.localtime(timezone.now()) )

		p = purchaseProc(res, data, request, uorder)
		p.placeingOrder()

		# and then update the real total value into UserOrder
		# UserOrder has the many SmallOrder points to it.
		UserOrder.objects.filter(id=uorder.id).update(total=p.total)
		oldTotal = Order.objects.get(id=ob.id).total
		Order.objects.filter(id=ob.id).update(total= oldTotal+p.total)
		return JsonResponse({}, safe=False)
	return render(request, 'time2eat/join.html', locals())