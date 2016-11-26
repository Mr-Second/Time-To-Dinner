from django.shortcuts import get_object_or_404, render
from t2e.models import Type, ResProf, Phone, Dish, Order, UserOrder, EatUser
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from djangoApiDec.djangoApiDec import queryString_required, date_proc
from django.utils import timezone # auto generate create time.
from django.urls import reverse
from t2e.models import ResProf, Order, UserOrder, SmallOrder, EatUser, Dish
from t2e.view.api import get_user
import urllib, requests, json

# 顯示特定一間餐廳的詳細簡介資料
@queryString_required(['res_id', 'orderId'])
def join_order(request):
	res = ResProf.objects.get(id=request.GET['res_id'])
	ob = get_object_or_404(Order, id=request.GET['orderId'])
	EatU, upperuser = get_user(request)

	if request.POST:
		data = request.POST
		data=data.dict()
		uorder = UserOrder.objects.create( orderUser=EatU, total=0, order=ob, create=timezone.localtime(timezone.now()) )
		# Check whether Post Data is not Attack
		validOrder(data.items(), res, request)

		# Iterate through all item user ordered
		# then calculate the money you need to pay.
		total = 0
		for i in data.items():
			# if not these two kind of value
			# it will be dish that user ordered.
			if checkValidOrder(i):
				db = Dish.objects.get(DishName=i[0])
				total+=int(db.price)*int(i[1])
				smorder = SmallOrder.objects.create(dish=db, amount=i[1], UserOrder=uorder)
		# and then update the real total value into UserOrder
		# UserOrder has the many SmallOrder points to it.
		UserOrder.objects.filter(id=uorder.id).update(total=total)
		oldTotal = Order.objects.get(id=ob.id).total
		Order.objects.filter(id=ob.id).update(total= oldTotal+total)
		return JsonResponse({}, safe=False)
	return render(request, 'time2eat/join.html', locals())

def checkValidOrder(items):
	if items[0]!= 'period' and items[0]!= 'csrfmiddlewaretoken' and items[1]!='':
		return True
	return False

def validOrder(order, res, request):
	urlPattern = reverse('t2e:restaurant_menu')
	apiURL = request.get_host() + urlPattern + "?res_id={}".format(urllib.parse.quote('1'))
	jsonText = requests.get('http://' + apiURL)
	jsonText = json.loads(jsonText.text)
	menuList = tuple(i['name'] for i in jsonText['dish'])
	for i in order:
		if i[0] not in menuList and checkValidOrder(i):
			raise Http404("api does not exist")
