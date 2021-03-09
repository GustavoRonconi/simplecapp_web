from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from api.serializers.profile_serializer import ProfileSerializer
from rest_framework import permissions
from ..serializers import decorators
from ..models import ProfileModel
from django.contrib.auth.models import User


class IsPostOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user and request.user.is_authenticated


class OnlyOwners(permissions.BasePermission):
    message = "Usuário não tem permissão pra visualizar/atualizar o perfil informado."

    @decorators.profile_analyser
    def has_permission(self, request, view, profile):
        if (
            request.method != "POST"
            and view.kwargs.get("pk")
            and profile.id != view.kwargs["pk"]
        ):
            return False
        return True


class ProfileView(APIView):
    permission_classes = (IsPostOrIsAuthenticated, OnlyOwners)

    @decorators.profile_analyser
    def get(self, request, profile, pk=None):
        if pk and profile.id != pk:
            profile = ProfileModel.objects.filter(pk=pk).first()
        if profile is not None:
            serializer = ProfileSerializer(profile)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        return Response(status=status.HTTP_204_NO_CONTENT)        

    @decorators.profile_analyser
    def post(self, request, profile):
        data = request.data
        serializer = ProfileSerializer(data=data, context={"request": request})
        if not (request.user.is_authenticated) and "user" not in data.keys():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "detail": "Para criar um perfil sem estar autenticado é necessário informar os dados de usuario."
                },
            )
        if profile is not None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"detail": "Já existe um perfil associado a este usuário."},
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @decorators.profile_analyser
    def put(self, request, profile, pk=None):
        if pk and profile.id != pk:
            profile = get_object_or_404(ProfileModel.objects.all(), pk=pk)
        data = request.data
        serializer = ProfileSerializer(
            instance=profile, data=data, partial=True, context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @decorators.profile_analyser
    def delete(self, request, profile, pk=None):
        if pk and profile.id != pk:
            profile = get_object_or_404(ProfileModel.objects.all(), pk=pk)

        user = User.objects.get(pk=profile.user.id)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
