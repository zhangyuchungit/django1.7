from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    
    password = models.CharField(max_length=50)
    
    Gender = models.BooleanField(default = False)
    
    age = models.IntegerField(default = 19)
    
    momo = models.TextField(default = 'zhangdachun')
    
    CreatDate = models.DateTimeField(default = '2017-10-12 15:59')

class Args(models.Model):
    name = models.CharField(max_length=50,null=True)
    not_name = models.CharField(max_length=50,null=False)

class Asset(models.Model):

    hostname = models.CharField(max_length=50,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

