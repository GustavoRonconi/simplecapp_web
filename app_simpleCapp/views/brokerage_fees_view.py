from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from ..models import BrokerageFeesModel
from ..serializers import BrokerageFeesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic
from ..serializers import decorators


class BrokerageFeesView(APIView):
    permission_classes = (IsAuthenticated,)

    @decorators.profile_analyser
    def get(self, request, profile):
        if profile is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"errors": "O usuário informado não possui um perfil associado."},
            )
        brokerage_fees = BrokerageFeesModel.objects.filter(profile_id=profile.id)

        if len(brokerage_fees) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT, data=[],)
        serializer = BrokerageFeesSerializer(
            brokerage_fees, many=True, context={"request": request}
        )

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @atomic
    @decorators.profile_analyser
    def post(self, request, profile):
        data_without_profile, data = request.data, []
        for v in data_without_profile:
            v["profile_id"] = profile.id
            data.append(v)
        
        serializer = BrokerageFeesSerializer(
            data=data, many=True, context={"request": request}
        )
        if serializer.is_valid():
            BrokerageFeesModel.objects.filter(profile_id=profile.id).delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
