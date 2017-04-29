from django.shortcuts import render_to_response, render
from djangoApiDec.djangoApiDec import queryString_required
from slothTw.models import Course, Comment
from django.urls import reverse
import datetime

def index(request):
    clist = Course.objects.all()
    return render_to_response('slothWeb/index.html', locals())

@queryString_required(['id'])
def inside(request):
    id = request.GET['id']
    c = Course.objects.get(id=id)
    if request.method == 'POST' and request.POST:
    	Comment.objects.create(course=c, create=datetime.datetime.now(), raw=request.POST['comments'])
    comments = Comment.objects.filter(course=c)
    urlPattern = reverse('infernoWeb:slothquestion') + '?id={}'.format(id)
    return render(request, 'slothWeb/inside.html', locals())

def question(request):
    return render_to_response('slothWeb/questionnaire.html', locals())