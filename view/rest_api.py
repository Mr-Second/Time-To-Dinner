from django.shortcuts import get_object_or_404
from apps.time2eat.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder, EatUser
from collections import namedtuple
from datetime import datetime, date
from django.http import JsonResponse
def rest_api(request, res_id, dateString = datetime.today()):
	# return_date will return a datetime Object 
	# which has attribute of year, month, day
	dateTuple = return_datetime(dateString)
	# 回傳餐廳物件
	Res = get_object_or_404(ResProf, id=res_id)
	result = {
		"ResName" : Res.ResName,
		"ResAddress" : Res.address,
		"Score" : int(Res.score),
		"Type" : [ str(t) for t in Res.ResType.all() ],
		"OrderList" : [],
		"Date" : str(dateTuple.year)+'-'+str(dateTuple.month)+'-'+str(dateTuple.day)
	}
	# 篩選出特定日期的訂單物件
	for OrderObject in Res.order_set.filter(create__date=date(dateTuple.year, dateTuple.month, dateTuple.day)):
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
					json['ResOrder'][sOrder.dish.DishName] = int(sOrder.amount)
				else:
					json['ResOrder'][sOrder.dish.DishName] += int(sOrder.amount)
		result['OrderList'].append(json)
	return JsonResponse(result, safe=False)

def user_api(request, user_id, dateString = datetime.today()):
	# return_date will return a datetime Object 
	# which has attribute of year, month, day
	dateTuple = return_datetime(dateString)
	user = get_object_or_404(EatUser, id=user_id)
	# print(user.userorder_set.all())
	json = {
		'User' : user.UpperUser.name,
		"Date" : str(dateTuple.year)+'-'+str(dateTuple.month)+'-'+str(dateTuple.day),
		"FDish" : user.FDish.DishName,
		"Ftype" : user.FType.ResType,
		'Order' : []
	}
	for UOrderObject in user.userorder_set.filter(create__date=date(dateTuple.year, dateTuple.month, dateTuple.day)):
		tmp = {'create' : UOrderObject.create, 'total' : int(UOrderObject.total)}
		for SObject in UOrderObject.smallorder_set.all():
			tmp[SObject.dish.DishName] = int(SObject.amount)
		json['Order'].append(tmp)
	return JsonResponse(json, safe=False)

def return_datetime(dateString):
	if dateString=='': dateString=datetime.today()
	if type(dateString) == datetime: 
		return dateString
	date = ( int(intValue) for intValue in dateString.split('-'))
	d = datetime(*date)
	return d