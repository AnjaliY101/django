from django.db import models

class Video(models.Model):
    Url =  models.CharField()
    User = models.ForeignKey
    "User"
    on_delete = models.CASCADE
# Create your models here.

class User(models.Model):
    Username = models.CharField()
    Password = models.CharField()