from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import apartment, block, status, task
#On adding a new view, ensure it is rendering the right html page and has the
# right name along with variables data etc.

@login_required
def home(request):
    context = {
        'title': 'Housekeeper'
    }
    return render(request, 'HKmanager/home.html', context)

@login_required
def tutorial(request):
    context = {
        'title': 'Housekeeper - Tutorial'
    }
    return render(request, 'HKmanager/tutorial.html', context)

@login_required
def thomondvillage(request):
    context = {
        'apartment': apartment.objects.all(),
        'title': 'Thomond Village Panel'
    }
    return render(request, 'HKmanager/thomondvillage.html', context)
