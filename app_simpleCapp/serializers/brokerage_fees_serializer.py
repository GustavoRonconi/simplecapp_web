from collections import OrderedDict
from rest_framework import serializers
from ..models import BrokerageFeesModel
from ..serializers import BrokerSerializer


class BrokerageFeesListSerializer(serializers.ListSerializer):
    def validate(self, data):
        brokers_ids = [v["broker_id"] for v in data]
        brokerage_fees_by_broker = {}
        for brokers_id in brokers_ids:
            brokerage_fees_by_broker[brokers_id] = []
            for brokerage_fee in data:
                if brokerage_fee["broker_id"] == brokers_id:
                    brokerage_fees_by_broker[brokers_id].append(brokerage_fee)
        brokerage_fees_by_broker = {
            key: sorted(value, key=lambda k: k["begin_date"])
            for key, value in brokerage_fees_by_broker.items()
        }
        for brokers_id, brokerage_fees in brokerage_fees_by_broker.items():
            for index, brokerage_fee in enumerate(brokerage_fees, 1):
                if index < len(brokerage_fees):
                    if (
                        brokerage_fee["end_date"] is None
                        or (
                            brokerage_fees[index]["begin_date"]
                            - brokerage_fee["end_date"]
                        ).days
                        != 1
                    ):
                        raise serializers.ValidationError(
                            {
                                "brokerage_fees": "Existem inconsistências na lista de vigências"
                            }
                        )

        return data


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
