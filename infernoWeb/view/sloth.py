from django.shortcuts import render_to_response, render, redirect
from django.http import JsonResponse, Http404
from djangoApiDec.djangoApiDec import queryString_required
from slothTw.models import Course, Comment
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
    if request.method == 'POST' and request.POST['comments']:
        Comment.objects.create(course=c, create=datetime.datetime.now(), raw=request.POST['comments'], emotion=request.POST['emotion'])
        return redirect(request.get_full_path())
    school = c.school
    urlpattern = '/infernoWeb/sloth/search'
    return render(request, 'slothWeb/inside.html', locals())

@queryString_required(['school', 'keyword'])
def search(request):
    school = request.GET['school']
    urlpattern = '/infernoWeb/sloth/search'
    return render(request, 'slothWeb/search.html', locals())

def createUser(request):
    if request.POST['id']:
        User.objects.update_or_create(facebookid=request.POST['id'], major=request.POST['profile[major]'], career=request.POST['profile[career]'], grade=request.POST['profile[grade]'], school=request.POST['profile[school]'], )
        return JsonResponse({"createUser":'success'})
    raise Http404("createUser error")