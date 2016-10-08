from django.shortcuts import get_object_or_404, render_to_response, render
from django.utils import timezone # auto generate create time.
from apps.time2eat.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder
from django.http import JsonResponse
import datetime
from apps.time2eat.view.rest_api import *
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
def purchase(request):
	return render_to_response('time2eat/purchase.html',locals())

# def rest_api(request, res, year, month, date):
# 	# 回傳餐廳物件
# 	Res = get_object_or_404(ResProf, id=res)
# 	result = {
# 		"ResName" : Res.ResName,
# 		"ResAddress" : Res.address,
# 		"Score" : Res.score,
# 		"Type" : [ str(t) for t in Res.ResType.all() ],
# 		"OrderList" : [],
# 		"Date" : ''
# 	}
# 	# 篩選出特定日期的訂單物件
# 	for OrderObject in Res.order_set.filter(create__date=datetime.date(int(year), int(month), int(date))):
# 		result['Date'] = str(OrderObject.create.year) +'-'+ str(OrderObject.create.month) +'-'+ str(OrderObject.create.day)
# 		json = {
# 			'total' : int(OrderObject.total),
# 			'ResOrder' : {},
# 			"Create" : ""
# 		}

# 		# 迭代訂單所有的使用者
# 		for uOrder in OrderObject.userorder_set.all():
# 			# 迭代一個使用者所訂的所有餐點
# 			for sOrder in uOrder.smallorder_set.all():
# 				if sOrder.dish.DishName not in json['ResOrder']:
# 					json['ResOrder'][sOrder.dish.DishName] = sOrder.amount
# 				else:
# 					json['ResOrder'][sOrder.dish.DishName] += sOrder.amount
# 			json['Create'] = OrderObject.create
# 		result['OrderList'].append(json)
# 	return JsonResponse(result, safe=False)