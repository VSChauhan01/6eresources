from django.db import models

# Create your models here.
class dht(models.Model):
    temp=models.CharField(max_length=600)
    hum=models.CharField(max_length=600)