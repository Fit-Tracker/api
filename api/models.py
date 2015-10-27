from django.db import models
from django.contrib.auth.models import User
'''
Consider a database table with ForeignKey.
May want to set up something more flexible to add/delete new/old Activites
'''
#  from datetime import datetime

# Create your models here.
WALKING = 'Walking'
RUNNING = 'RUNNING'
CYCLING = 'Cycling'
WEIGHTS = 'Weights'
YOGA = 'Yoga'
SWIMMING = 'Swimming'

ACTIVITY_LIST = (
    (WALKING, 'Walking'),
    (RUNNING, 'Running'),
    (CYCLING, 'Cycling'),
    (WEIGHTS, 'Weights'),
    (YOGA, 'Yoga'),
    (SWIMMING, 'Swimming'),
    )


class Activity(models.Model):
    title = models.CharField(max_length=10, choices=ACTIVITY_LIST)
    user = models.ForeignKey(User)   # one to many with Foreign Key


class Stat(models.Model):
    timestamp = models.DateField(null=True)
    stat = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity)
