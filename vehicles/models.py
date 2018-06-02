from django.db import models

# Create your models here.

class Vehicle(models.Model):
    style = models.CharField(max_length=9)
    year = models.PositiveSmallIntegerField()
    plate = models.CharField(max_length=7) #create validation from plate = XYZ-1234
    model = models.CharField(max_length=50)

    def __str__(self):
         return self.plate
  