from django.db import models
from  users.models import User


class Post(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, related_name="posts")#!  stroe user id
    title = models.CharField(max_length=100,null=True,blank=True)
    decpription = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posts= models.FileField(upload_to="posts/",null=True,blank=True)
    
    
    
    # def total_likes(self):
    #     return self.likes.count()  #! like count  

    # def __str__(self):
    #     return f"Post by {self.user.username} on {self.created_at}" 
    
    
    
    
    
# class likes(models.Model):
    
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
#     created_at = models.DateTimeField(auto_now_add=True)
    
    
    
# class  comment(models.Model):
    
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
#     comment= models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)        
   
     