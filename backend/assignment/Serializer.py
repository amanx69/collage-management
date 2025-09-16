from rest_framework import  serializers
from  .models import  assigment 



class AssignmentSerializer(serializers.ModelSerializer):

 
    class Meta:
        model = assigment
        fields = ["id","users","title","file","section","last_date",
                  "subject","created_at",]
        
        
        
    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Title must be less than 100 characters.")
        if  value is  None:
            return serializers.ValidationError("title is required")
        return value
    
    
    def validate_file(self, value):
        if  value is None:
            return serializers.ValidationError("file is required")
        return value
    
    
    def validate_subject(self, value):
        if  value is None:
            return serializers.ValidationError("subject is required")
        return value
    def validate_last_date(self, value):
        if  value is None:
            return serializers.ValidationError("last date is required")
        return value
    
    
    def create(self, validated_data):
        assignment = assigment.objects.create(**validated_data)
        assignment.save()
        return assignment
        
     
