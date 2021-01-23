from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Viagem, ClassificacaoViagem
from .serializers import ViagemSerializer, ClassificacaoViagemSerializer


class IndexView(APIView):
    def get(self, request):
        content = {"message": "API Integração Guia Receita"}
        return Response(content)


class ViagemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        list_viagem = Viagem.objects.all()
        serializer = ViagemSerializer(list_viagem, many=True)
        return Response(serializer.data)


class ViagemInsert(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = ViagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViagemUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer


class ClassificacaoViagemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        list_classificacao_viagem = ClassificacaoViagem.objects.all()
        serializer = ClassificacaoViagemSerializer(list_classificacao_viagem, many=True)
        return Response(serializer.data)
