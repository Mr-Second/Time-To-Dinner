from django.shortcuts import render_to_response, render
from djangoApiDec.djangoApiDec import queryString_required
from arrogant.models import Job, Comment
import datetime

def index(request):
    jlist = Job.objects.all()
    return render_to_response('arrogantWeb/index.html', locals())

@queryString_required(['id'])
def inside(request):
    id = request.GET['id']
    j = Job.objects.get(id=id)
    if request.method == 'POST' and request.POST:
    	Comment.objects.create(Job=j, create=datetime.datetime.now(), raw=request.POST['comments'])
    return render(request, 'arrogantWeb/inside.html', locals())