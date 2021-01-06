from django.db import models
from django.utils import timezone

# Create your models here.
class Festevent(models.Model):
    #Basic details
    name=models.CharField(max_length=55)
    details=models.TextField(max_length=None)
    banner=models.ImageField(upload_to='images/')
    contact=models.CharField(max_length=10)
    no_of_seats=models.IntegerField(blank=True)

    
    #Event shedule
    event_date=models.DateField(default=timezone.now)
    event_time=models.TimeField(default=timezone.now)

    #Price deatils
    isCompatition=models.BooleanField(default=False)
    first_price=models.FloatField(blank=True, null=True)
    second_price=models.FloatField(blank=True, null=True)
    third_price=models.FloatField(blank=True, null=True)

    #group deatils
    isGroup=models.BooleanField(default=False)
    max_members=models.IntegerField(blank=True, null=True)
    min_members=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class EventRegistration(models.Model):
    event=models.ForeignKey(Festevent, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    college=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name