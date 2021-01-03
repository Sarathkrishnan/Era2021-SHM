from django.db import models
import datetime
import django.utils
# from datetime import datetime
# from django.utils import timezone

# Create your models here.


class Events(models.Model):

    name = models.CharField(max_length=20)
    details = models.CharField(max_length=200, default="")

    #programme details
    event_banner= models.ImageField(upload_to=None,default=None)
    no_of_seats = models.FloatField(default=0)
    date = models.DateField(default=django.utils.timezone.now)
    time = models.TimeField(default=django.utils.timezone.now)
    fees = models.FloatField(default=0)
    contact = models.CharField(max_length=15)

    #Price Details
    first_price = models.FloatField(default=0)
    second_price = models.FloatField(default=0)
    third_price = models.FloatField(default=0)

    #Group programmes's details
    is_Group = models.BooleanField(default=True)
    max_GroupMembers = models.IntegerField(default=1)
    min_GroupMembers = models.IntegerField(default=1)

    def __str__(self):
        return self.name
