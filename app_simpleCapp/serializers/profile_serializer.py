from rest_framework import serializers
from app_simpleCapp.models.profile_model import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for profile user
    """

    class Meta:
        model = ProfileModel
        fields = "__all__"
