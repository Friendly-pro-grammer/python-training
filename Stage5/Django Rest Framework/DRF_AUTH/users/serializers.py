from pathlib import Path

from rest_framework import serializers
from .models import User,UserProfile,UploadFile
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email = validated_data["email"],
            password=validated_data["password"]
        )
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)


class UploadedFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    class Meta:
        model = UploadFile
        fields=[
            "id",
            "file",
            "original_name",
            "uploaded_at"
        ]
        read_only_fields=[
            "id",
            "original_name",
            "uploaded_at"
        ]
    def validate_file(self,value):
        max_size = 5*1024*1024
        if value.size>max_size:
            raise serializers.ValidationError("file should not exceed 5MB")
        allowed_extensions = {".pdf",".png",".jpg",".jpeg"}
        extension = Path(value.name).suffix.lower()
        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Only PDF, PNG and JPEG files are allowed."
            )
        return value
    def create(self, validated_data):
        uploaded_file = validated_data["file"]
        return UploadFile.objects.create(
            owner=self.context["request"].user,
            file=uploaded_file,
            original_name=uploaded_file.name,
        )