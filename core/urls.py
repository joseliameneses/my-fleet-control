from django.contrib import admin
from django.urls import path, include
from core import views 

urlpatterns = [
    path('', views.List.as_view(), name='home'),
    path('erro/', views.erro,name='erro'),

]