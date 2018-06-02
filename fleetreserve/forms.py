from django import forms
from fleetreserve.models import Reserve
# from django.contrib.auth.models import User

# Simple form referring to the Reserve itself
class ReserveForm(forms.ModelForm):

        date_start = forms.SplitDateTimeField(label = 'Data Inicio',localize = True, required=False)
        date_end = forms.SplitDateTimeField(label = 'Data Fim', localize = True, required=False)

        class Meta:
                model = Reserve
                fields = ('vehicle_reserve','user_reserve','date_start','date_end','reservation_code',)
                # widgets = {
                #         'date_start': forms.DateTimeInput(attrs={'type':'datetime-local'}),
                #         'date_end': forms.DateTimeInput(attrs={'type':'datetime-local'}),
                # }

