from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "name"
        ]
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data["email"],
            password= validated_data["password"],
            name = validated_data["name"]
        )
        return user     


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields=[
            "name",
            "bio",
            "phone_number",
            "profile_picture"
        ]


class GoogleSerializer(serializers.Serializer):
    id_token = serializers.CharField(required=True,trim_whitespace=True)
