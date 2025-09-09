from rest_framework import serializers
from .models import Post



        
        
        
 #! like  serilizer
 
# class  likeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=likes
#         fields="__all__"
        
        
        
        
# #! comment serilizer  


# class commentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=comment   
#         fields="__all__"                
        
        
        
 #! post  relizer         
class postSerializer(serializers.ModelSerializer):
    # comments= commentSerializer(many=True,read_only=True)
    # likes_counts=likeSerializer(many=True,read_only=True)

    class Meta:
        model=Post
        fields= ["id","user","title","decpription","created_at","posts"]
                