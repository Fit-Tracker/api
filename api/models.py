from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)  # took out null=True

    def __str__(self):
        return(self.title)


class Stat(models.Model):
    activity = models.ForeignKey(Activity)
    stat = models.IntegerField()
    timestamp = models.DateField()  # took out null=True
