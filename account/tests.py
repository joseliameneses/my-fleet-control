from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

AccountUser = get_user_model()

from .models import AccountUser

# Create your tests here.

class ContactAccountUserTestCase(TestCase):
    
    def test_page_access_logout(self):
        c = Client()
        response = c.get('/')
        c.login(username = 'admin', password='admin@admin')
        c.logout()
        response = c.get(reverse('dashboard'))
        
    def test_page_access_login(self):
        c = Client()
        response = c.get('/')
        response = c.get(reverse('dashboard'))