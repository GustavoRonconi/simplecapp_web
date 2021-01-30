from rest_framework import response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from app_simpleCapp.models.profile_model import ProfileModel
from app_simpleCapp.serializers.profile_serializer import ProfileSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = {}

        profile = ProfileModel.objects.filter(user_id=request.user.id).first()
        if profile is not None:
            response = {
                "teste": 1
            }

        return Response(status=status.HTTP_204_NO_CONTENT, data=response)

    def post(self, request):
        response = {}
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
