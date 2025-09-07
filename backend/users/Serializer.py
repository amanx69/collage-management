from rest_framework import serializers
from .models import User
import  re 
import datetime
from post.Serializer  import postSerializer




#! post  serilizer  








class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    user_post=postSerializer(many=True,read_only=True)
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
            "created_at",
            "user_post",
            "dateofbirth",
            "password",
            "user_post"
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
    def validate_phone(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value
    
    
    #! full name  velidation 
    def validate_full_name(self, value):
        if value is None:
            raise serializers.ValidationError("Full name is required.")
        elif len(value)<4:
            raise serializers.ValidationError("Full name must be at least 4 characters.")
        return 
    
    
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


    class Meta:
        model = User
        fields = ['full_name', 'dateofbirth']

#! update name and date of birth
    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.dateofbirth = validated_data.get('dateofbirth', instance.dateofbirth)
        instance.save()
        return instance

    # ! VALIDATE FULL NAME
    # def validate_full_name(self,value):
    #     if value is None:
    #         raise serializers.ValidationError("Full name is required.")
    #     elif len(value)<4:
    #         raise serializers.ValidationError("Full name must be at least 4 characters.")
    #     return value

    # def validate_dateofbirth(self, value):
    #     if value is None:
    #         raise serializers.ValidationError("Date of birth is required.")

    #     today= datetime.date.today()
    #     age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

    #     if age < 18:
    #         raise serializers.ValidationError("You must be at least 18 years old.")
    #     return value
		
  
   
		

		