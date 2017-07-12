from django.shortcuts import render_to_response, render
from slothTw.views import CreateComment, logPage
from djangoApiDec.djangoApiDec import queryString_required

def index(request):
    return render_to_response('greed/index.html', {})

@queryString_required(['id'])
def inside(request):
    if request.method == 'POST': 
        logPage(request)
        if 'comments' in request.POST:
            if CreateComment(request)==False:
                return HttpResponse("SORRY 目前只開放留言一次喔~~ 未來會再依照情況調整")
    return render(request, 'greed/inside.html', locals())