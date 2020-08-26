from django.db import models
from django.conf import settings

class prediction(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Pregnancies = models.FloatField(default=0)
    Glucose = models.FloatField(default=0)
    BloodPressure = models.FloatField(default=0)
    Insulin = models.FloatField(default=0)
    BMI = models.FloatField(default=0)
    Age = models.FloatField(default=0)



    def __str__(self):
       return '{}, {}'.format(self.lastname, self.firstname)

   

