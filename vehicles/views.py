from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from vehicles.models import Vehicle

from vehicles.forms import VehicleForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.template import Context, loader, context

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Classes pertaining to Reserve CRUD
@method_decorator(login_required, name='dispatch')
class Created(CreateView):
    template_name = 'vehicle_create.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')

class Listened(ListView):
    template_name = 'vehicle_list.html'
    model = Vehicle
    form_class = VehicleForm
    context_object = 'list'

# Determining that the reserve editing screen needs login
@method_decorator(login_required, name='dispatch')
class Edited(UpdateView):
    vehicles = Vehicle.objects.order_by('vehicle_id')
    template_name = 'edit_vehicle.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')


class Deleted(DeleteView):
    vehicles = Vehicle.objects.order_by('vehicle_id')
    template_name = 'delete_vehicle.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')