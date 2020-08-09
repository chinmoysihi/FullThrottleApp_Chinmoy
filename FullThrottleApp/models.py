# from django.db import models
from django.db import models
from timezone_field  import TimeZoneField
from datetime import datetime
# Create your models here.
dateFormat =  '%b %d %Y %I:%M%p'
class Employee(models.Model):
    id = models.CharField(primary_key=True,max_length=9)
    real_name = models.CharField(max_length=50)
    tz = TimeZoneField(default='Asia/Kolkata')

class ActivityPeriods(models.Model):
    Employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    id = models.IntegerField
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
