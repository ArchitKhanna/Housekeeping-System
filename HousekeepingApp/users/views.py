from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
#Types of messages:
    #messages.debug/.info/.success/.warning/.error

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            mobile = form.cleaned_data.get('mobile')
            user.profile.mobile = mobile
            user.save()
            messages.success(request, f'Account created for {username}! Please login.')
            return redirect('hk-user-login')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Housekeeper - Register',
        'form': form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    context = {
        'title': 'Housekeeper - Profile',
    }
    return render(request, 'users/profile.html', context)
