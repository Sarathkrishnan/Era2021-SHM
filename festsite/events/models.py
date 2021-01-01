from django.db import models
# from datetime import datetime
# from django.utils import timezone

# Create your models here.
class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=200,default="")
    #date = models.DateField
    #time = models.TimeField
    fees = models.IntegerField
    contact = models.CharField(max_length=15)

    
    def __str__(self):
        return self.name

