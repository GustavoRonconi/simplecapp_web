from rest_framework import serializers
from ..models import BrokerModel


class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokerModel
        fields = "__all__"
