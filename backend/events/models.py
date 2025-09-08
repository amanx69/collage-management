from django.db import models
from users.models import User
# Create your models here.

class Announcement(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, related_name="announcement")#!  stroe user id
    types=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    file=models.FileField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    
    
