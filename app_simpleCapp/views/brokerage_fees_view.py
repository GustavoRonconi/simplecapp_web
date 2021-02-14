from app_simpleCapp.models import brokerage_fees_models
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from ..models import BrokerageFeesModel, ProfileModel
from ..serializers import BrokerageFeesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch


class BrokerageFeesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = ProfileModel.objects.filter(user_id=request.user.id).first()
        if profile is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"errors": "O usuário informado não possui um perfil associado."},
            )
        brokerage_fees = BrokerageFeesModel.objects.prefetch_related(
            Prefetch(
                "broker",
                queryset=BrokerageFeesModel.objects.filter(profile_id=profile.id),
            )
        )
        if len(brokerage_fees) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT, data=[],)
        serializer = BrokerageFeesSerializer(
            brokerage_fees, many=True, context={"request": request}
        )

        return Response(status=status.HTTP_200_OK, data=serializer.data)
