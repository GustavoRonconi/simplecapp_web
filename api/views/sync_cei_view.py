from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..tasks import sync_cei


class SyncCeiView(APIView):
    def get(self, request):
        sync_cei.delay(10)

        return Response(status=status.HTTP_200_OK, data={})
