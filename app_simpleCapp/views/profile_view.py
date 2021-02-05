from rest_framework import response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from app_simpleCapp.models.profile_model import ProfileModel
from app_simpleCapp.serializers.profile_serializer import ProfileSerializer
from rest_framework import permissions


class IsPostOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user and request.user.is_authenticated


class ProfileView(APIView):
    permission_classes = (IsPostOrIsAuthenticated,)

    def get(self, request):
        response = {}

        profile = ProfileModel.objects.filter(user_id=request.user.id).first()
        if profile is not None:
            response = {"teste": 1}
            return Response(status=status.HTTP_203_NO_CONTENT, data=response)

        return Response(status=status.HTTP_204_NO_CONTENT, data=response)

    def post(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data, context={"request": request})
        if not (request.user.is_authenticated) and "user" not in data.keys():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors": "Para criar um perfil sem estar autenticado é necessário informar os dados de usuario."
                },
            )
        else:
            profile = ProfileModel.objects.filter(user_id=request.user.id).first()
            if profile is not None:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"errors": "Já existe um perfil associado a este usuário."},
                )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
