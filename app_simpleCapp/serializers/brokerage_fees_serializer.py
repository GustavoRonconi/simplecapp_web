from collections import OrderedDict
from rest_framework import serializers
from ..models import BrokerageFeesModel
from ..serializers import BrokerSerializer


class BrokerageFeesListSerializer(serializers.ListSerializer):
    def validate(self, attrs):
        print(1)
        # Here attrs contains list of Params You can validate it here
        pass

class BrokerageFeesSerializer(serializers.ModelSerializer):
    broker = BrokerSerializer(read_only=True)
    broker_id = serializers.IntegerField(write_only=True)
    profile_id = serializers.IntegerField(write_only=True)

    list_serializer_class = BrokerageFeesListSerializer

    class Meta:
        model = BrokerageFeesModel
        fields = (
            "begin_date",
            "end_date",
            "brokerage_fee_value",
            "broker",
            "broker_id",
            "profile_id",
        )
        depth = 1

    def validate(self, data):
        # ordered_begin_date = OrderedDict(sorted(data.items(), key=lambda item: item[1]['begin_date']))
        return data
