from django.shortcuts import render_to_response, render
from djangoApiDec.djangoApiDec import queryString_required
from slothTw.models import Course

def index(request):
    clist = Course.objects.filter(name='倫理學與當代議題')
    return render_to_response('slothWeb/index.html', locals())