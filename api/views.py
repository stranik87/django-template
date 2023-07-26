from django.shortcuts import render


def index(request):
    name = 'Dunyo'
    return render(request, 'index.html', {'name': name})
