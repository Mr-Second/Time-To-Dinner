from django.shortcuts import render_to_response, render
from djangoApiDec.djangoApiDec import queryString_required
from slothTw.models import Course

def index(request):
    clist = Course.objects.all()
    return render_to_response('slothWeb/index.html', locals())

@queryString_required(['id'])
def inside(request):
    id = request.GET['id']
    c= Course.objects.get(id=id)
    return render_to_response('slothWeb/inside.html', locals())