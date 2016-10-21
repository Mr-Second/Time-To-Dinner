from django.shortcuts import get_object_or_404
from apps.time2eat.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder, EatUser
from collections import namedtuple
from datetime import datetime, date
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from oscar.core.compat import get_user_model
from apps.user.models import User
User = get_user_model()


@login_required
def rest_api(request):
	if 'res_id' not in request.GET or request.GET['res_id'] == '':
		raise Http404("api does not exist")

	Res = get_object_or_404(ResProf, id=request.GET['res_id'])  # 回傳餐廳物件

	# return_date will return a datetime Object
	# which has attribute of year, month, day
	dateTuple = return_datetime(request.GET)

	result = {
		"ResName": Res.ResName,
		"ResAddress": Res.address,
		"Score": int(Res.score),
		"Type": [str(t) for t in Res.ResType.all()],
		"OrderList": [],
		"Date": str(dateTuple.year) + '-' + str(dateTuple.month) + '-' + str(dateTuple.day)
	}

	# 篩選出特定日期的訂單物件
	for OrderObject in Res.order_set.filter(create__date=date(dateTuple.year, dateTuple.month, dateTuple.day)):
		json = {
			'total': int(OrderObject.total),
			'ResOrder': {},
			"Create": OrderObject.create
		}

		# 迭代訂單所有的使用者
		for uOrder in OrderObject.userorder_set.all():
			# 迭代一個使用者所訂的所有餐點
			for sOrder in uOrder.smallorder_set.all():
				if sOrder.dish.DishName not in json['ResOrder']:
					json['ResOrder'][sOrder.dish.DishName] = int(
						sOrder.amount)
				else:
					json['ResOrder'][
						sOrder.dish.DishName] += int(sOrder.amount)
		result['OrderList'].append(json)

	return JsonResponse(result, safe=False)


@login_required
def user_api(request):
	# use session to determine your user id
	# Cause UpUser and EatUser is in OneToOne Relationship
	# so use it to find user's EatUser object instance.
	UpUser = User.objects.get(id=request.user.id)
	user = get_object_or_404(EatUser, id=UpUser.eatuser.id)
	# return_date will return a datetime Object
	# which has attribute of year, month, day
	dateTuple = return_datetime(request.GET)
	json = {
		'User': user.UpperUser.name,
		"Date": str(dateTuple.year) + '-' + str(dateTuple.month) + '-' + str(dateTuple.day),
		"FDish": user.FDish.DishName,
		"Ftype": user.FType.ResType,
		'Order': []
	}

	for UOrderObject in user.userorder_set.filter(create__date=date(dateTuple.year, dateTuple.month, dateTuple.day)):
		tmp = {
			'create': UOrderObject.create,
			'total': int(UOrderObject.total),
			# meal是一個餐點的陣列 裏面的tuple第一位是餐點名稱，第2位是數量
			'meal': [(SObject.dish.DishName, int(SObject.amount)) for SObject in UOrderObject.smallorder_set.all()]
		}
		json['Order'].append(tmp)

	return JsonResponse(json, safe=False)


def return_datetime(dateString):
	if 'dateString' in dateString:
		date = (int(intValue) for intValue in dateString['dateString'].split('-'))
		d = datetime(*date)
		return d
	else:
		dateString = datetime.today()
		return dateString