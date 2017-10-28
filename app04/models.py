from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username =  models.CharField(max_length=50)
    age = models.IntegerField()
class UserData(models.Model):
    username =  models.CharField(max_length=50)
    age = models.IntegerField()
class UserList(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)