from django.db import models

# Create your models here.

class Announcement(models.Model):
    type=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    file=models.FileField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    
    
