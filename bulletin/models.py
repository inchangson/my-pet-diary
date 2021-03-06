from django.db import models
from psutil import users
from sqlalchemy import null

# Create your models here.

#임시 사용자 객체
class TempUser(models.Model):
#    id = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=15, null=True)
    profile_img = models.CharField(max_length=255, null=True)

class BulletinFeed(models.Model):
#    id = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=255,  null=True)
    upload_time = models.DateTimeField( null=True)
    
    #txt_path로 바꿀지 확인
    content     = models.TextField(max_length=255,  null=True)
    
    img_path    = models.CharField(max_length=255,  null=True)
    user        = models.ForeignKey(TempUser, on_delete=models.SET_NULL, null = True)