from django.db import models
from  users.models import User



class assigment(models.Model):
    users= models.ForeignKey(User,null=True,blank=True , on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    file= models.FileField(upload_to="assignment/",null=True,blank=True)
    section= models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    sumbite_date=models.DateField()
    
    
    