import re

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
        validated_data["cpf"] = re.sub("[^0-9]", "", validated_data["cpf"])
        validated_data["phone_number"] = re.sub(
            "[^0-9]", "", validated_data["phone_number"]
        )
        profile = ProfileModel.objects.create(**validated_data)

        return profile

    def update(self, instance, validated_data):
        if validated_data.get("phone_number"):
            validated_data["phone_number"] = re.sub(
                "[^0-9]", "", validated_data["phone_number"]
            )
        for key, value in validated_data.items():
            if key == "user":
                for k, v in value.items():
                    v = make_password(v) if k == "password" else v
                    setattr(instance.user, k, v)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance

    def validate(self, data):
        keys_not_allowed = ["cpf"]

        if self.context["request"].method == "PUT":
            for key in data.keys():
                if key in keys_not_allowed:
                    raise serializers.ValidationError(
                        {key: "Não é permitido alterar o campo."}
                    )
        return data
