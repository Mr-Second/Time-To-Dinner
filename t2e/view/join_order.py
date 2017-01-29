from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, Http404
from djangoApiDec.djangoApiDec import queryString_required
from t2e.models import ResProf, Order
from t2e.class_file.purchaseProc import purchaseProc

# 顯示特定一間餐廳的詳細簡介資料
@queryString_required(['res_id', 'orderId'])
def join_order(request):
	ob = get_object_or_404(Order, id=request.GET['orderId'])
	if ob.isFinished(): raise Http404('api not found')
	res = ResProf.objects.get(id=request.GET['res_id'])

	if request.POST:
		data = request.POST
		data=data.dict()

		p = purchaseProc(res, data, request, ob)

		return JsonResponse({"purchase":"success"}, safe=False)
	raise Http404('you didnt supply post data.')