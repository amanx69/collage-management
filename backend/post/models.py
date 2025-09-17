from django.db import models
from  users.models import User

#!  post  model 
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",default=1)#!  stroe user id
    title = models.CharField(max_length=100,null=True,blank=True)
    decpription = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file= models.FileField(upload_to="posts/",null=True,blank=True)
    
    
    
    def __int__(self):
        return self.id
    def likes_count(self):
        return self.likes.count()
    
    
    
    
#! comment model 
class comments(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")    
    comment_user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment=models.CharField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def  __int__(self):return self.id
    
    #!  like  model 
class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    
#!  one user  can like only one post
    class Meta:
        unique_together = ("post", "user")
    
    def __str__(self):
           return f"{self.user.full_name} likes {self.post.title}"    
    

    
    
   