from rest_framework import serializers
from .models import Post ,Likes,comments



        
        
        
 #! like  serilizer
 
class  likeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields="__all__"
        
        
        
        
# #! comment serilizer  


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model=comments
        fields=['id','comment_user','comment','created_at']                
        
        
        
 #! post  relizer         
class postSerializer(serializers.ModelSerializer):
    comments= commentSerializer(many=True,read_only=True)
#likes_counts=likeSerializer(many=True,read_only=True)

    class Meta:
        model=Post
        fields= ["id","user","title","decpription","created_at","file","comments"]
        read_only_fields = ["user", "created_at", "updated_at",]
        
      #! create  the post  
    def create(self, validated_data):
        
        user = self.context["request"].user #! current user  in ser  
        post = Post.objects.create(user=user, **validated_data)
        post.save()
        return post
        
 
    
       

        
        
        
        
                