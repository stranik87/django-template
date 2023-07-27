from django.shortcuts import render
import requests



def index(request):
    n = request.GET.get('n', 1)
    gender = request.GET.get('gender')
    r = requests.get(f'https://randomuser.me/api/?results={n}&gender={gender}')
    if r.status_code == 200:
        users = r.json()['results']
        
    else:
        users = None
    
    return render(request, 'index.html', {'users': users})
