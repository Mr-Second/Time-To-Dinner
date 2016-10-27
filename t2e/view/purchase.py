from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.utils import timezone # auto generate create time.
from django.contrib.auth.decorators import login_required
from t2e.models import ResProf, Order, UserOrder, SmallOrder, EatUser, Dish
from t2e.view.api import get_user

# @login_required
def purchase(request):
	if 'res_id' not in request.GET or request.GET['res_id'] == '':
		raise Http404("api does not exist")

	res = ResProf.objects.get(id=request.GET['res_id'])
	EatU, upperuser = get_user(request)

	if request.POST:
		data = request.POST
		data=data.dict()
		ob = Order.objects.create( restaurant=res, create=timezone.localtime(timezone.now()), total=0, period=data['period'] )
		uorder = UserOrder.objects.create( orderUser=EatU, total=0, order=ob, create=timezone.localtime(timezone.now()) )
		# Iterate through all item user ordered
		# then calculate the money you need to pay.
		total = 0
		for i in data.items():
			# if not these two kind of value
			# it will be dish that user ordered.
			if ifElse_determiner(i):
				db = Dish.objects.get(DishName=i[0])
				total+=int(db.price)*int(i[1])
				smorder = SmallOrder.objects.create(dish=db, amount=i[1], UserOrder=uorder)
		# and then update the real total value into UserOrder
		# UserOrder has the many SmallOrder points to it.
		UserOrder.objects.filter(id=uorder.id).update(total=total)
		Order.objects.filter(id=ob.id).update(total=total)
		return redirect('t2e:check')
	return render(request, 'time2eat/purchase.html', locals())

def ifElse_determiner(items):
	if items[0]!= 'period' and items[0]!= 'csrfmiddlewaretoken' and items[1]!='':
		return True
	else:
		return False
