from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.http import JsonResponse, Http404
from django.utils import timezone # auto generate create time.
from django.contrib.auth.decorators import login_required
from t2e.models import ResProf, Order, UserOrder, SmallOrder, EatUser, Dish
from t2e.view.api import get_user
from t2e.class_file.purchaseProc import purchaseProc
from djangoApiDec.djangoApiDec import queryString_required, date_proc
from django.urls import reverse
import urllib, requests, json


# @login_required
@queryString_required(['res_id'])
def purchase(request):
	res = ResProf.objects.get(id=request.GET['res_id'])
	EatU, upperuser = get_user(request)
	return render(request, 'time2eat/purchase.html', locals())

