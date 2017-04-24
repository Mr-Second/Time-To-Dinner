from django.shortcuts import render_to_response, render
from djangoApiDec.djangoApiDec import queryString_required
from arrogant.models import Job, Comment

def index(request):
    jlist = Job.objects.all()
    return render_to_response('arrogantWeb/index.html', locals())

@queryString_required(['id'])
def inside(request):
    id = request.GET['id']
    j = Job.objects.get(id=id)
    # comments = Comment.objects.filter(c)
    return render_to_response('arrogantWeb/inside.html', locals())