from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .managers import UserManager
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name =  models.CharField(max_length=100,null=False)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_picture/",
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    objects= UserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]
    
    def __str__(self):
        return self.email