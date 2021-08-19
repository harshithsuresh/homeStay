from django.db import models
from django.db.models.deletion import CASCADE
from stays.models import Stay

class Review(models.Model):
    stayTitle=models.CharField(max_length=300)
    stayID=models.IntegerField()
    userName=models.CharField(max_length=40)
    comments=models.TextField(blank=True)
    rating=models.IntegerField(default=5)

    def __str__(self):
        return self.stayTitle