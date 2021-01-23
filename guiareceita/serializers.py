from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import APIException
from .models import Viagem, ClassificacaoViagem


class ViagemSerializer(ModelSerializer):
    class Meta:
        model = Viagem
        fields = ("data_inicio", "data_fim", "classificacao", "nota")
    
    def update(self, instance, validated_data):
        instance.classificacao = validated_data.get('classificacao', instance.classificacao)
        if not(1 <= validated_data.get('nota') <= 5):
            raise APIException('A nota deve ser um valor de 1 a 5', code=400)
        instance.nota = validated_data.get('nota', instance.nota)
        instance.save()

        return instance


class ClassificacaoViagemSerializer(ModelSerializer):
    class Meta:
        model = ClassificacaoViagem
        fields = ("classificacao",)
