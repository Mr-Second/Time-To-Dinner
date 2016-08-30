from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your vie(ws here.
def time2eat(request):
	return render_to_response('time2eat/time2eat.html',locals())
def all_list(request):
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