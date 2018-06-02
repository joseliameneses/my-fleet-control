from django.contrib import admin
from fleetreserve.models import Reserve

# Register your models here.

class ReserveAdmin(admin.ModelAdmin):
    list_display = ['reservation_code', 'vehicle_reserve', 'user_reserve', 'date_start', 'date_end']
    search_fields = ['vehicle_reserve','user_reserve', 'reservation_code']


# Code to take each class of bank to be administered in admin
admin.site.register(Reserve, ReserveAdmin)
