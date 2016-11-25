from django.shortcuts import get_object_or_404
from t2e.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder, EatUser
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from djangoApiDec.djangoApiDec import queryString_required, date_proc

# 顯示特定一間餐廳的詳細簡介資料
@date_proc
def join_order(request, date):
	Res = get_object_or_404(ResProf, id=request.GET['res_id'])
	return JsonResponse({}, safe=False)
