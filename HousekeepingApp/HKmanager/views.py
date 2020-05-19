from django.shortcuts import render
from .models import apartment, block, status, task
#On adding a new view, ensure it is rendering the right html page and has the
# right name along with variables data etc.

def home(request):
    context = {
        'title': 'Housekeeper'
    }
    return render(request, 'HKmanager/home.html', context)

def tutorial(request):
    context = {
        'title': 'Housekeeper - Tutorial'
    }
    return render(request, 'HKmanager/tutorial.html', context)

def thomondvillage(request):
    context = {
        'apartment': apartment.objects.all(),
        'title': 'Thomond Village Panel'
    }
    return render(request, 'HKmanager/thomondvillage.html', context)
