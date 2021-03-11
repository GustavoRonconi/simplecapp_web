from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import StatesModel
from ..serializers import StatesSerializer


class StateView(APIView):

    def get(self, request):
        states = StatesModel.objects.all()

        serializer = StatesSerializer(states, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
