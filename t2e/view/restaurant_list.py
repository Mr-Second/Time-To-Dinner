from django.shortcuts import get_object_or_404
from t2e.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder, EatUser
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required

# 顯示所有餐廳的簡略資料
def restaurant_list(request):
	json = []
	resObject = ResProf.objects.all()
	for i in resObject:
		tempT = dict(ResName=i.ResName, ResLike = int(i.ResLike), score = int(i.score),  avatar = i.avatar.url)
		json.append(tempT)
	return JsonResponse(json, safe=False)