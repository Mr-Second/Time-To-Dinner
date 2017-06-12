from django.shortcuts import render_to_response, render, redirect
from django.http import JsonResponse, Http404, HttpResponse
from djangoApiDec.djangoApiDec import queryString_required
from slothTw.models import Course, Comment
from slothTw.views import CreateComment, logPage
from infernoWeb.models import User
import datetime, json

@queryString_required(['school'])
def index(request):
    clist = Course.objects.all()
    school = request.GET['school']
    urlpattern = '/infernoWeb/sloth/search'
    return render_to_response('slothWeb/index.html', locals())

@queryString_required(['id'])
def inside(request):
    id = request.GET['id']
    c = Course.objects.get(id=id)
    if request.method == 'POST': 
        logPage(request)
        if 'comments' in request.POST:
            if CreateComment(request)==False:
                return HttpResponse("SORRY 目前只開放留言一次喔~~ 未來會再依照情況調整")
    school = c.school
    urlpattern = '/infernoWeb/sloth/search'
    return render(request, 'slothWeb/inside.html', locals())

@queryString_required(['school', 'keyword'])
def search(request):
    school = request.GET['school']
    urlpattern = '/infernoWeb/sloth/search'
    return render(request, 'slothWeb/search.html', locals())