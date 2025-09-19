from rest_framework import serializers
from .models import Post ,Likes,comments
from django.contrib.auth.models import User

        


#! serlizer for postuser
class postuserSerializer(serializers.ModelSerializer):
    class  Meta:
        model=User
        fields=[
            "id",
            "email",
            "full_name",
            "phone",
            "bio",
            "profile_image",
           
        ]
        read_only_fields = [fields]
     
        
 #! like  serilizer
 
class  likeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields=['id','post','user','created_at']
        read_only_fields = ["user", "created_at"]
        
        
        
        
# #! comment serilizer  

class commentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=comments
        fields=['id','comment_user','comment','created_at','post']    
        read_only_fields = ["comment_user", "created_at", "post",] 
        #! create the comment  
        def create(self, validated_data):
            request = self.context.get("request")
            post=self.context.get("post") #! current  post in ser
            comment=comments.objects.create( **validated_data)    
            comment.save(post=post,comment_user=request.user)  
            return comment     
        def update(self, instance, validated_data):
            instance.comment= validated_data.get('comment',instance.comment)
            instance.save()
            return instance
        
        
        
 #! post  relizer         
class postSerializer(serializers.ModelSerializer):
    comments= commentSerializer(many=True,read_only=True)
    likes_count = serializers.SerializerMethodField()
    
    
   
  
   
#likes_counts=likeSerializer(many=True,read_only=True)

    class Meta:
        model=Post
        fields= ["id","user","title","decpription","created_at","file","comments",'likes_count']
        read_only_fields = ["user", "created_at", "updated_at"]
        
 
      #! create  the post  
    def create(self, validated_data):
        
        user = self.context["request"].user #! current user  in ser  
        post = Post.objects.create(user=user, **validated_data)
        return  post
    
    #! give like counnt 
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    
    def update(self, instance, validated_data):
        instance.title= validated_data.get('title',instance.title)
        instance.decpription= validated_data.get('decpription',instance.decpription)
        instance.save()
        return instance
        
 
    
       

        
        
        
        
                