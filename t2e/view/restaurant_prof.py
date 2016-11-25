from django.shortcuts import get_object_or_404
from t2e.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder, EatUser
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from djangoApiDec.djangoApiDec import queryString_required, date_proc

# 顯示特定一間餐廳的詳細簡介資料
@queryString_required(['res_id'])
def restaurant_prof(request):
	resObject = get_object_or_404(ResProf, id=request.GET['res_id'])
	json = dict(ResName = resObject.ResName, address = resObject.address, ResLike = int(resObject.ResLike), score = int(resObject.score), last_reserv = resObject.last_reserv, country = resObject.country, avatar = resObject.avatar.url, environment = resObject.environment.url, envText = resObject.envText, feature = resObject.feature.url, featureText = resObject.featureText)
	json['phone'] = [str(i) for i in resObject.phone_set.all() ]
	json['ResFavorDish'] = [ (i.dish.DishName.__str__(), int(i.freq)) for i in resObject.resfavordish_set.all() ]
	json['date'] = [ i.DayOfWeek for i in resObject.date_set.all() ]

	return JsonResponse(json, safe=False)
