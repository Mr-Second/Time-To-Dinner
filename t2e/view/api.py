from django.shortcuts import get_object_or_404
from t2e.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder, EatUser
from collections import namedtuple
from datetime import datetime, date
from django.http import JsonResponse, Http404, QueryDict
from django.contrib.auth.decorators import login_required
from userper import Userper

# 顯示餐廳當天或特定日期的訂單資料
# @login_required
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

# 使用者的訂單資料，可指定當天或特定日期
# @login_required
def user_api(request):
	# will return eatuser and user of System.
	EatU, upperuser = get_user(request)

	# return_date will return a datetime Object
	# which has attribute of year, month, day
	dateTuple = return_datetime(request.GET)
	json = {
		'User': EatU.userName,
		"Date": str(dateTuple.year) + '-' + str(dateTuple.month) + '-' + str(dateTuple.day),
		"FDish": EatU.FDish.DishName,
		"Ftype": EatU.FType.ResType,
		'Order': []
	}

	for UOrderObject in EatU.userorder_set.filter(create__date=date(dateTuple.year, dateTuple.month, dateTuple.day)):
		tmp = {
			'create': UOrderObject.create,
			'total': int(UOrderObject.total),
			# meal是一個餐點的陣列 裏面的tuple第一位是餐點名稱，第2位是數量
			'meal': [(SObject.dish.DishName, int(SObject.amount)) for SObject in UOrderObject.smallorder_set.all()]
		}
		json['Order'].append(tmp)

	return JsonResponse(json, safe=False)

# 透過川哲寫的userper套件，利用同一個session抓到系統的會員資料
def get_user(request):
	# use session to determine your user id
	# so use it to find user's EatUser object instance.
	session = request.session.session_key
	upperuser = Userper('login.stufinite.faith')
	upperuser.get_test(session)
	EatU = get_object_or_404(EatUser, userName=upperuser.name)
	return EatU, upperuser

def return_datetime(dateString):
	if 'dateString' in dateString:
		date = (int(intValue) for intValue in dateString['dateString'].split('-'))
		d = datetime(*date)
		return d
	elif dateString==QueryDict() or ('res_id' in dateString and len(dateString)==1 ):
		# means didn't pass dateString parameter in.
		dateString = datetime.today()
		return dateString
	else:
		raise Http404("api does not exist")
