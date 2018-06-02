from django.db import models
from vehicles.models import Vehicle
from django.contrib.auth import get_user_model

AccountUser = get_user_model()
# Create your models here.

#Definition of class Reserve (setting the reservation validation)
#the reserve class has as attributes a car and a user, each reserve is defined by the reserve interval associated with the car
class Reserve(models.Model):
    vehicle_reserve = models.ForeignKey (Vehicle, on_delete=models.CASCADE)
    user_reserve = models.ForeignKey( AccountUser, on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    reservation_code = models.AutoField(primary_key=True,max_length=5)

    # Returning each attribute to class for use in form
    def __str__(self):
        return '%s %s %s %s %s' % (self.vehicle_reserve, self.user_reserve, self.date_start, self.date_end, self.reservation_code)
        