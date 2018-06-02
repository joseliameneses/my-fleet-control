from django.urls import path, include
from django.contrib.auth.views import login, logout
from .views import register, dashboard, edit_account, edit_password, password_reset, password_reset_confirm

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('login', login, {'template_name':'login.html'}, name='login'),
    path('logout', logout, {'next_page':'home'}, name='logout'),
    path('register', register, name='register'),
    path('password_reset_confirm/<key>', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset', password_reset, name='password_reset'),
    path('edit', edit_account, name='edit_account'),
    path('edit_password', edit_password, name='edit_password'),

]
