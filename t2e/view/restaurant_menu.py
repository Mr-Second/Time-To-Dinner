from django.shortcuts import get_object_or_404
from t2e.models import Type, ResProf, Date, Phone, Dish, Order, UserOrder, EatUser
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
# 顯示特定一間餐廳的菜單
def restaurant_menu(request):
	if 'res_id' not in request.GET or request.GET['res_id'] == '':
		raise Http404("api does not exist")

	resObject = get_object_or_404(ResProf, id=request.GET['res_id'])
	json = dict(menu = [i.image.url for i in resObject.menu_set.all()], dish = [ dict(name = i.DishName, price = int(i.price), isSpicy = i.isSpicy, image= i.image.url) for i in resObject.dish_set.all() ] )

	return JsonResponse(json, safe=False)