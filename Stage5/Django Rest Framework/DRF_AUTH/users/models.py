from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
from django.conf import settings
class User(AbstractUser):
    pass 

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Profile of {self.user.username}"

class UploadFile(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="file_upload"
    )
    file = models.FileField(
        upload_to="uploads/"
    )
    original_name=models.CharField(max_length=255)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.original_name
