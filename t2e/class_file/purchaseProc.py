import requests, urllib, json
from django.http import JsonResponse, Http404
from django.urls import reverse
from t2e.models import ResProf, Order, UserOrder, SmallOrder, EatUser, Dish
class purchaseProc(object):
	"""docstring for purchaseProc"""
	def __init__(self, res, postData, request, uorder):
		""" Create a object to handle with the process of placing an order.
		Args:
		    res: restaurant object
		    postDate: the dict data from request.POST
		    request: request object got from django
		    uorder: UserOrder object
		"""
		self.request = request
		self.restaurant = res
		self.postData = postData
		self.cleanPostData = self._verifyPostData()
		self.uorder = uorder
		self.total = 0

	
	def _verifyPostData(self):
		""" To verify whether the postData contains some malicious data.
		Returns:
		    A valid dict with only DishName and amounts.
		"""
		# Check whether Post Data is not Attack

		def checkValidOrder(dishName):
			if dishName!= 'period' and dishName!= 'csrfmiddlewaretoken' and dishName!='':
				return True
			return False

		urlPattern = reverse('t2e:restaurant_menu')
		apiURL = self.request.get_host() + urlPattern + "?res_id={}".format(urllib.parse.quote(str(self.restaurant.id)))
		jsonText = requests.get('http://' + apiURL)
		jsonText = json.loads(jsonText.text)
		menuList = tuple(i['name'] for i in jsonText['dish'])

		cleanPostData = {}
		for i in self.postData:
			if i not in menuList and checkValidOrder(i):
				raise Http404("api does not exist")
			elif checkValidOrder(i):
				cleanPostData[i] = self.postData[i]
		return cleanPostData

	def placeingOrder(self):
		""" Iterate through all item user ordered then calculate the money you need to pay.
		Returns:
		    None.
		"""
		# Check whether Post Data is not Attack

		for i in self.cleanPostData.items():
			db = Dish.objects.get(DishName=i[0])
			self.total+=int(db.price)*int(i[1])
			SmallOrder.objects.create(dish=db, amount=i[1], UserOrder=self.uorder)