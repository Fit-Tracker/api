from django.db import models
from django.contrib.auth.models import User
#  from datetime import datetime

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)   # one to many with Foreign Key


class Stat(models.Model):
    timestamp = models.DateField(null=True)
    stat = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity)
