from django.contrib import admin
from django.contrib.auth import get_user_model

AccountUser = get_user_model()
# from django.contrib.auth.models import User

# Register your models here.

class User_reserveAdmin(admin.ModelAdmin):
    list_display = ['username', 'registration','name', 'email']
    search_fields = ['username','registration','name']

admin.site.register(AccountUser, User_reserveAdmin)
    