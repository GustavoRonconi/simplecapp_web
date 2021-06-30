from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import BrokerModel
from ..serializers import BrokerSerializer


class BrokerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        brokers = BrokerModel.objects.all()
        serializer = BrokerSerializer(brokers, many=True, context={"request": request})

        return Response(status=status.HTTP_200_OK, data=serializer.data)
