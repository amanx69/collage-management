from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
import re
import  post.models as post

# Custom Manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)   
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


 ##!Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)   # used for login
    full_name = models.CharField(max_length=100,blank=True,)
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio=models.TextField(blank=True,max_length=50)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    branch=models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    dateofbirth = models.DateField(null=True, blank=True)

    # Required fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"   # login field
    REQUIRED_FIELDS = ["full_name"]   # when creating superuser
    read_only_fields = ["id", "full_name", "email","created_at"]

    def __str__(self):
        return self.email
