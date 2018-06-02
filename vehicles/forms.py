from django import forms
from vehicles.models import Vehicle
# from django.contrib.auth.models import User

# Simple form referring to the Reserve itself
class VehicleForm(forms.ModelForm):

        class Meta:
                model = Vehicle
                fields = ('style','year','plate','model')
                # widgets = {
                #         'date_start': forms.DateTimeInput(attrs={'type':'datetime-local'}),
                #         'date_end': forms.DateTimeInput(attrs={'type':'datetime-local'}),
                # }
