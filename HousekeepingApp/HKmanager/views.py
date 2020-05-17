from django.shortcuts import render
from .models import apartment, block, status, task

#On adding a new view, ensure it is rendering the right html page and has the
# right name along with variables data etc.

apartments = [
    {
        'Name': 'Apartment 1',
        'Block': 'Mallard',
        'Status': 'Serviced',
        'Task': 'Callbacks',
        'Assigned': 'Sean Savicic'
    },
    {
        'Name': 'Apartment 62',
        'Block': 'Robin',
        'Status': 'Dirty',
        'Task': 'Clean',
        'Assigned': 'Housekeeper 1'
    }
]

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
        'apartments': apartment.objects.all(),
        'title': 'Thomond Village Panel'
    }
    return render(request, 'HKmanager/thomondvillage.html', context)
