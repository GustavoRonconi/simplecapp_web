from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..tasks import generate_report


class GenerateReportView(APIView):
    def get(self, request):
        generate_report.delay(10)

        return Response(status=status.HTTP_200_OK, data={})
