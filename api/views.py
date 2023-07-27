from django.shortcuts import render
import requests



def index(request):
    n = request.GET.get('n', 1)
    r = requests.get(f'https://randomuser.me/api/?results={n}')
    if r.status_code == 200:
        users = r.json()['results']
        
    else:
        users = None
    
    return render(request, 'index.html', {'users': users})
