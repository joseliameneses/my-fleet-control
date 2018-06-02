from django.test import TestCase
from django.test.client import Client

from model_mommy import mommy

from .models import Vehicle

# Create your tests here.

class ReserveTestCase(TestCase):
    
    def setUp(self):
        self.vehicle = mommy.make(
            'vehicle.Vehicle', reservation_code='1', _quantity=10
        )
        self.client = Client()

    def tearDown(self):
        self.vehicle.delete()

