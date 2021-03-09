from rest_framework import serializers

from ..models import StatesModel


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatesModel
        fields = "__all__"
