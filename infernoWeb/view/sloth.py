from django.shortcuts import render_to_response, render
from djangoApiDec.djangoApiDec import queryString_required
from slothTw.models import Course, Comment
import datetime, json

def index(request):
    clist = Course.objects.all()
    return render_to_response('slothWeb/index.html', locals())

@queryString_required(['id'])
def inside(request):
    id = request.GET['id']
    c = Course.objects.get(id=id)
    if request.method == 'POST' and request.POST:
        if 'rating' in request.POST:
            data = json.loads(request.POST.dict()['rating'])
            amount = c.feedback_amount + 1
            modelDict = {'feedback_amount':amount}
            modelDict['feedback_freedom'] = (c.feedback_freedom*(amount-1) + (data[0]*3/4 + data[1]/4)) /amount
            modelDict['feedback_GPA'] = (c.feedback_GPA*(amount-1) + data[2]) / amount
            modelDict['feedback_easy'] = (c.feedback_easy*(amount-1) + (data[3]/12 + data[4]/12  + data[7]*9/12 + data[8]/12)) / amount
            modelDict['feedback_knowledgeable'] = (c.feedback_knowledgeable*(amount-1) + data[6]) / amount
            modelDict['feedback_FU'] = (c.feedback_FU*(amount-1) + data[5]) / amount
            Course.objects.update_or_create(id=id, defaults=modelDict)
        else:
            Comment.objects.create(course=c, create=datetime.datetime.now(), raw=request.POST['comments'])
    comments = Comment.objects.filter(course=c)
    return render(request, 'slothWeb/inside.html', locals())

def question(request):
    return render_to_response('slothWeb/questionnaire.html', locals())