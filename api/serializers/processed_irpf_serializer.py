from rest_framework import serializers

from api.models.processed_irpf_model import ProcessedIRPFModel


class ProcessedIRPFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedIRPFModel
        fields = ("reference_year", "profile")
