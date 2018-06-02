from django.contrib import admin
from vehicles.models import Vehicle

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['plate', 'style', 'year', 'model']
    search_fields = ['plate','style']

admin.site.register(Vehicle, VehicleAdmin)
