from  rest_framework import serializers

from events.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):

    
    
    class Meta:
        model = Announcement
        fields = ["id", "title", "description", "createdon","types","file","user"]
        
        
    
        
        
    def create(self, validated_data):
        if isinstance(validated_data, list):
            announcements = [Announcement.objects.create(**item) for item in validated_data]
            return announcements
        return Announcement.objects.create(**validated_data)

       
        
        
    def validate_title(self, value):
        if value is None:
           raise serializers.ValidationError("Title is required.")
        return value
    def validate_types(self, value):
        if value is None:
           raise serializers.ValidationError("Type is required.")
        return value
    #! update  function  for  announcement
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.types = validated_data.get('types', instance.types)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance
     
        
        
        
        
        
        
            