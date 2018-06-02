from django.contrib import admin
from django.urls import path, include
from fleetreserve import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

# Definition of all system urls
urlpatterns = [
    path('schedule', views.Create.as_view(), name='schedule'),
    path('edit_schedule_<int:pk>', views.Edit.as_view(), name='edit_schedule'),
    path('delete_schedule_<int:pk>', views.Delete.as_view(), name='delete_schedule'),
    path('teste/', views.teste,name='teste')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
