from django.db import models

class Video(models.Model):
    Url =  models.CharField()
    User = models.ForeignKey("User")
    Title = models.CharField()
    Created = models.DateTimeField()
    on_delete = models.CASCADE
# Create your models here.

class User(models.Model):
    Username = models.CharField()
    Password = models.CharField()

class Reactions(models.Model):
    User = models.ForeignKey
    Video = models.ForeignKey
    Type = models.CharField()