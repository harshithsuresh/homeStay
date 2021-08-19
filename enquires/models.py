from django.db import models
from django.db.models.fields import IntegerField
from stays.models import Stay

class Enquire(models.Model):
    stayTitle=models.CharField(max_length=200)
    stayId=models.IntegerField()
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    bookingDate=models.DateField()
    closingDate=models.DateField()
    userName=models.CharField(max_length=30)
    userId=models.IntegerField(blank=True)
    
    def __str__(self):
        return self.userName  