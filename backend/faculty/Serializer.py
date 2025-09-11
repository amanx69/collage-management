from rest_framework import serializers
from .models import department



class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=department
        fields="__all__"