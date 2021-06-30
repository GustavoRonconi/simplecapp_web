from api import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.processed_irpf_serializer import ProcessedIRPFSerializer


class ProcessedIRPFView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ProcessedIRPFSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
