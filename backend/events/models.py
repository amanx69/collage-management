from django.db import models
from users.models import User
# Create your models here.

class Announcement(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, related_name="announcement")#!  stroe user 
    
    types_CHOICES = (
        ('events', 'events'),
        ('final exam', 'final exam'),
        ('mst', 'mst'),
        ('warning', 'warning'),
    )
    types = models.CharField(max_length=10, choices=types_CHOICES, blank=True, null=True)

    title = models.CharField(max_length=500)
    description = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    file=models.FileField(upload_to="announcement image/",null=True,blank=True)

    
    
