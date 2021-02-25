from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..serializers import NotificationSerializer
from rest_framework.response import Response
from rest_framework import status
from ..utils import send_notifications


class NotificationView(APIView):
    """Endpoint to send notification to especific or all users"""

    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            send_notifications(request.data["message"], all_user=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

