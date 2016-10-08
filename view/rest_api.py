from django.shortcuts import get_object_or_404
from apps.time2eat.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder
from collections import namedtuple
from datetime import datetime, date
from django.http import JsonResponse
def rest_api(request, res, dateString = datetime.today()):
	# return_date will return a datetime Object 
	# which has attribute of year, month, day
	dateTuple = return_datetime(dateString)
	# 回傳餐廳物件
	Res = get_object_or_404(ResProf, id=res)
	result = {
		"ResName" : Res.ResName,
		"ResAddress" : Res.address,
		"Score" : Res.score,
		"Type" : [ str(t) for t in Res.ResType.all() ],
		"OrderList" : [],
		"Date" : str(dateTuple.year)+'-'+str(dateTuple.month)+'-'+str(dateTuple.day)
	}
	# 篩選出特定日期的訂單物件
	for OrderObject in Res.order_set.filter(create__date=date((dateTuple.year), dateTuple.month, dateTuple.day)):
		json = {
			'total' : int(OrderObject.total),
			'ResOrder' : {},
			"Create" : OrderObject.create
		}

		# 迭代訂單所有的使用者
		for uOrder in OrderObject.userorder_set.all():
			# 迭代一個使用者所訂的所有餐點
			for sOrder in uOrder.smallorder_set.all():
				if sOrder.dish.DishName not in json['ResOrder']:
					json['ResOrder'][sOrder.dish.DishName] = sOrder.amount
				else:
					json['ResOrder'][sOrder.dish.DishName] += sOrder.amount
		result['OrderList'].append(json)
	return JsonResponse(result, safe=False)

def return_datetime(dateString):
	if dateString=='': dateString=datetime.today()
	if type(dateString) == datetime: 
		return dateString
	date = ( int(intValue) for intValue in dateString.split('-'))
	d = datetime(*date)
	return d