from rest_framework import serializers
from ..models import BrokerageFeesModel, BrokerModel
from ..serializers import BrokerSerializer


class BrokerageFeesSerializer(serializers.ModelSerializer):
    broker = BrokerSerializer(read_only=True)

    class Meta:
        model = BrokerageFeesModel
        fields = (
            "id",
            "begin_date",
            "end_date",
            "brokerage_fee_value",
            "broker",            
        )
        depth = 1

    def validate(self, data):
        return data
