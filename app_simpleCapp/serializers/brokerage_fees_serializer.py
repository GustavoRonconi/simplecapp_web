from rest_framework import serializers
from ..models import BrokerageFeesModel, BrokerModel
from ..serializers import BrokerSerializer


class BrokerageFeesSerializer(serializers.ModelSerializer):
    broker = BrokerSerializer(read_only=True)
    broker_id = serializers.PrimaryKeyRelatedField(
        queryset=BrokerModel.objects.all(), source="broker"
    )

    class Meta:
        model = BrokerageFeesModel
        fields = (
            "begin_date",
            "end_date",
            "brokerage_fee_value",
            "broker",
            "broker_id",
        )
        depth = 1

    def validate(self, data):
        return data
