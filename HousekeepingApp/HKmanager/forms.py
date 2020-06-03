from django import forms
from django.contrib.auth.models import User
from .models import (
                    livingRoomCheckList,
                    kitchenCheckList,
                    corridorCheckList,
                    bedroomCheckList,
                    ensuiteCheckList
                    )

class CorridorUpdateForm(forms.ModelForm):
    class Meta:
        model = livingRoomCheckList
        fields = ['task', 'checked']
