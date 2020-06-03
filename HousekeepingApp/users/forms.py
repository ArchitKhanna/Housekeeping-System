from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    mobile = PhoneNumberField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','mobile','password1','password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ProfileUpdateForm(forms.ModelForm):
   class Meta:
       model = Profile
       fields = ['mobile', 'image']
