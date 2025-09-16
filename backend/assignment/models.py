from django.db import models
from  users.models import User
import datetime
from django.utils import timezone



class assigment(models.Model):
    users= models.ForeignKey(User,null=True,blank=True , on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    file= models.FileField(upload_to="assignment/",null=True,blank=True)
    section= models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    last_date=models.DateField(null=True,blank=True)
    
    
    
    # @property
    # def is_due_soon(self):
    #     if self.last_date is None:
    #         return False
    #     today = timezone.localdate()
    #     return (self.last_date - today).days <= 1 and self.last_date >= today
        
     

    # @property
    # def is_overdue(self):
    #     today = timezone.localdate()
    #     return today > self.last_date
    
    
    