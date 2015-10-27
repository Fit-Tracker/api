from django.db import models

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(  # need something here )


class Stat(models.Model):
    timestamp=models.DateField(null=True)
    stat=models.IntegerField()
    activity=models.ForeignKey(Activity)
