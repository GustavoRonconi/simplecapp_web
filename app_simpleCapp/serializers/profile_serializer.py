from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import ProfileModel

User._meta.get_field("email")._unique = True


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
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for profile user
    """

    user = UserSerializer(required=False)

    class Meta:
        model = ProfileModel
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        if "user" in validated_data.keys():
            user_data = validated_data.pop("user")
            user_data["password"] = make_password(user_data["password"])
            user = User.objects.create(**user_data)
            profile = ProfileModel.objects.create(**validated_data, user=user)

            return profile
        validated_data["user_id"] = self.context["request"].user.id
        profile = ProfileModel.objects.create(**validated_data)
        return profile

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        # instance.description = validated_data.get('description', instance.description)
        # instance.body = validated_data.get('body', instance.body)
        # instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
