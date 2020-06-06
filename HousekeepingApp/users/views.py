from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from HKmanager.models import apartment
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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your personal information has been updated!')
            return redirect('hk-user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm()

    context = {
        'title': 'Housekeeper - Profile',
        'apartments': apartment.objects.filter(assignee=request.user),
        'u_form': user_form,
        'p_form': profile_form,
    }

    return render(request, 'users/profile.html', context)
