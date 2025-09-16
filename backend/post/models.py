from django.db import models
from  users.models import User


class Post(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, related_name="posts")#!  stroe user id
    title = models.CharField(max_length=100,null=True,blank=True)
    decpription = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file= models.FileField(upload_to="posts/",null=True,blank=True)
    
    
    def __int__(self):
        return self.id
    
    
    
class comments(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")    
    comment_user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment=models.CharField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def  __str__(self):return self.comment
    
    
class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)    
    

    
    
   