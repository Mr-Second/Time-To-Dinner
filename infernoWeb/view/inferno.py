from django.http import JsonResponse, Http404
from infernoWeb.models import User
from functools import wraps
from inferno.settings import USERPOOL_URL as USERPOOL_URL
import requests

# def user_verify(v_id, v_key):
#     r = requests.get(
#         USERPOOL_URL + '/fb/user/verify/{}/{}'.format(v_id, v_key))
#     if r.text == 'Ok':
#         return True
#     return False

def user_verify(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        try:
            r = requests.get(
                USERPOOL_URL + '/fb/user/verify/{}/{}'.format(request.POST['id'], request.POST['verify']))
            if r.text == 'Ok':
                return function(request, *args, **kwargs)
        except Exception as e:
            print(e)
        raise Http404("you need to login!!")
    return wrap

def createUser(request):
    user, created = User.objects.get_or_create(facebookid=request.POST['id'],defaults={
        'major':request.POST['profile[major]'],
        'career':request.POST['profile[career]'],
        'grade':request.POST['profile[grade]'],
        'school':request.POST['profile[school]']
    })
    return user