from  rest_framework import serializers
from users.models import User
from post.Serializer import postSerializer
from events.Serializer import AnnouncementSerializer

class ProfileSerializer(serializers.ModelSerializer):
    posts=postSerializer(many=True,read_only=True) #! fro  how  all user  post  
    announcement=AnnouncementSerializer(many=True,read_only=True)
    
    
    class Meta:
        model = User
        fields = ['full_name',"dateofbirth", "email",
            "bio",
            "profile_image","posts","announcement",'branch']
        
        
        
        
        
        