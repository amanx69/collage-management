from rest_framework import serializers
from .models import User
import  re 
import datetime
from post.Serializer  import postSerializer
from events.Serializer import AnnouncementSerializer





class UserSerializer(serializers.ModelSerializer):

  
    posts=postSerializer(many=True,read_only=True) #! fro  how  all user  post  
    announcement=AnnouncementSerializer(many=True,read_only=True)
    
    # full_name = serializers.EmailField()
   # phone = serializers.EmailField()


    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "full_name",
            "phone",
            "bio",
            "profile_image",
            "branch",
            'role',
            "created_at",
            "dateofbirth",
            "password",
            "posts",
            "announcement",
           
        ]
        # ! password will be required but not shown in API response
        extra_kwargs = {
            "password": {"write_only": True, "required": True}
        }

    # ! CREATE USER
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        user.profile_image = validated_data.get("profile_image")
        user.role=validated_data.get("role")
        user.save()
        return user
    
    
    
    
    def validate_email(self,vlaue):
        if User.objects.filter(email=vlaue).exists():
            raise serializers.ValidationError("email already  exists please  enter another email")
        if vlaue is  None:
            raise serializers.ValidationError("please enter email address")
        elif not vlaue.endswith("@gmail.com"):
            raise serializers.ValidationError("email must end with @gmail.com")
        return vlaue
    
    

		
    # ! VALIDATE PHONE


    
    def validate_password(self, value):
        
        if value is  None:
            raise serializers.ValidationError("password  is required")
        if len(value) < 6:
            raise serializers.ValidationError("password must be at least 6 characters")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("password must contain at least one uppercase letter")
        if not re.search(r"[0-9]",value):
            raise serializers.ValidationError("password must contain at least one number")
        if not re.search(r"[!@#$%^&*]", value):
            raise serializers.ValidationError("password must contain at least one special character")
        if " "in value:
            raise serializers.ValidationError("password must not contain space ")
        
		
        return value
    

    
    
    
    
    #! serlizer for  update  name and date of  birth 
    

    
class NameSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    dateofbirth = serializers.DateField()
 


    class Meta:
        model = User
        fields = ['full_name', 'dateofbirth',]

#! update name and date of birth
    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.dateofbirth = validated_data.get('dateofbirth', instance.dateofbirth)
        instance.branch = validated_data.get('branch', instance.branch)
        instance.save()
        return instance

    # ! VALIDATE FULL NAME
    def validate_full_name(self, value):
        if value is None:
            raise serializers.ValidationError("Full name is required.")
        elif len(value)<4:
            raise serializers.ValidationError("Full name must be at least 4 characters.")
        return value
    
    
    # ! VALIDATE DATE OF BIRTH
    def validate_dateofbirth(self, value):
        if value is None:
            raise serializers.ValidationError("Date of birth is required.")
        elif value > datetime.date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value
#     def validate_branch(self, value):
#         if value is None:
#             raise serializers.ValidationError("Branch is required.")
#         return value
    
#  #!   class  of  bioo and profile image
  
class BioSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['bio','profile_image']      
        
        
        
    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()
        return instance
    
     
        
    
    
    
		
  
   
		

		