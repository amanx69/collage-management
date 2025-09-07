# validators.py
import re
from rest_framework import serializers



class validate:
    def validate_custom_password(password):
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r"[0-9]", password):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*]", password):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return password
