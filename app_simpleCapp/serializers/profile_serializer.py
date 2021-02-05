from rest_framework import serializers
from app_simpleCapp.models.profile_model import ProfileModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "last_login",
            "date_joined",
        )


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for profile user
    """

    user = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProfileModel
        fields = "__all__"
