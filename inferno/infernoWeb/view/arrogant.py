from django.shortcuts import render_to_response, render
from djangoApiDec.djangoApiDec import queryString_required
from arrogant.models import Job, Comment
import datetime
from django.http import HttpResponse
from arrogant.views import CreateComment, logPage

def index(request):
    return render_to_response('arrogantWeb/index.html', locals())

@queryString_required(['id'])
def inside(request):
    id = request.GET['id']
    j = Job.objects.get(id=id)
    if request.method == 'POST' and request.POST: 
        logPage(request)
        if 'comments' in request.POST:
            if CreateComment(request)==False:
                return HttpResponse("SORRY 目前只開放留言一次喔~~ 未來會再依照情況調整")
    return render(request, 'arrogantWeb/inside.html', locals())

@queryString_required(['school', 'keyword'])
def search(request):
    school = request.GET['school']
    urlpattern = '/infernoWeb/sloth/search'
    return render(request, 'slothWeb/search.html', locals())