from django.contrib import admin
from django.urls import path, include
from vehicles import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

# Definition of all system urls
urlpatterns = [
    path('vehicle_list', views.Listened.as_view(), name='vehicle_list'),
    path('vehicle_create', views.Created.as_view(), name='vehicle_create'),
    path('edit_vehicle_<int:pk>', views.Edited.as_view(), name='edit_vehicle'),
    path('delete_vehicle_<int:pk>', views.Deleted.as_view(), name='delete_vehicle'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
