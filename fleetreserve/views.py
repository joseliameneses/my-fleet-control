from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from fleetreserve.models import Reserve

from fleetreserve.forms import ReserveForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.template import Context, loader, context

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Classes pertaining to Reserve CRUD
@method_decorator(login_required, name='dispatch')
class Create(CreateView):
    template_name = 'schedule.html'
    model = Reserve
    form_class = ReserveForm
    success_url = reverse_lazy('home')
    
class List(ListView):
    template_name = 'home.html'
    model = Reserve
    form_class = ReserveForm
    context_object = 'list'

# Determining that the reserve editing screen needs login
@method_decorator(login_required, name='dispatch')
class Edit(UpdateView):
    reserves = Reserve.objects.order_by('reservation_code')
    template_name = 'edit_schedule.html'
    model = Reserve
    form_class = ReserveForm
    success_url = reverse_lazy('home')

class Delete(DeleteView):
    reserves = Reserve.objects.order_by('reservation_code')
    template_name = 'delete.html'
    model = Reserve
    form_class = ReserveForm
    success_url = reverse_lazy('home')
   
def teste(request):
    return render(request, 'teste.html')
