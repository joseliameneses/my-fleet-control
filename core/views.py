from django.shortcuts import render
from fleetreserve.models import Reserve
from django.views.generic import ListView
from fleetreserve.forms import ReserveForm

# Create your views here.

def erro(request):
    return render(request, 'erro.html')
    
class List(ListView):
    template_name = 'home.html'
    model = Reserve
    form_class = ReserveForm
    context_object = 'list'
