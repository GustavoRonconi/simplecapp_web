from collections import OrderedDict
from rest_framework import serializers
from ..models import BrokerageFeesModel
from ..serializers import BrokerSerializer


class BrokerageFeesListSerializer(serializers.ListSerializer):
    def validate(self, data):
        ordered_begin_date = sorted(data, key=lambda k: k["begin_date"])
        return ordered_begin_date


class BrokerageFeesSerializer(serializers.ModelSerializer):
    broker = BrokerSerializer(read_only=True)
    broker_id = serializers.IntegerField(write_only=True)
    profile_id = serializers.IntegerField(write_only=True)

    class Meta:
        list_serializer_class = BrokerageFeesListSerializer
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

    # def validate(self, data):
    #     # ordered_begin_date = OrderedDict(sorted(data.items(), key=lambda item: item[1]['begin_date']))
    #     return data
