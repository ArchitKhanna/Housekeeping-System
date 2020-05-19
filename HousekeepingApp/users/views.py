from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
#Types of messages:
    #messages.debug/.info/.success/.warning/.error

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('hk-Home')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Housekeeper - Register',
        'form': form
    }
    return render(request, 'users/register.html', context)
