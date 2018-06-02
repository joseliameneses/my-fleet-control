from django.test import TestCase
from django.test.client import Client

from model_mommy import mommy

from .models import Reserve

# Create your tests here.

class ReserveTestCase(TestCase):

    def setUp(self):
        self.reserve = mommy.make('reserve.Reserve', _quantity=10)
        self.client = Client()

    def tearDown(self):
        self.reserve.delete()

