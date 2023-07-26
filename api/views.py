from django.shortcuts import render
import requests


def index(request):
    r = requests.get('https://randomuser.me/api/')
    if r.status_code == 200:
        user = r.json()['results'][0]
    else:
        user = None
    
    return render(request, 'index.html', {'user': user})
