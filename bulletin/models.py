from django.db import models
from psutil import users

# Create your models here.

class TempUser(models.Model):
#    id = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=15)
    profile_img = models.CharField(max_length=255)

class BulletinFeed(models.Model):
#    id = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=255)
    upload_time = models.DateTimeField()
    txt_path    = models.CharField(max_length=255)
    img_path    = models.CharField(max_length=255)
    user        = models.ForeignKey(TempUser, on_delete=models.SET_NULL, null = True)