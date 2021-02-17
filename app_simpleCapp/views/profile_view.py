from functools import partial
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from app_simpleCapp.serializers.profile_serializer import ProfileSerializer
from rest_framework import permissions
from ..serializers import decorators
from ..models import ProfileModel


class IsPostOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user and request.user.is_authenticated


class ProfileView(APIView):
    permission_classes = (IsPostOrIsAuthenticated,)

    @decorators.profile_analyser
    def get(self, request, profile, pk=None):
        if profile is not None:
            if pk and profile.id != pk:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        "errors": "Usuário não tem permissão pra acessar o perfil informado."
                    },
                )
            serializer = ProfileSerializer(profile)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        return Response(status=status.HTTP_204_NO_CONTENT, data={})

    @decorators.profile_analyser
    def post(self, request, profile):
        data = request.data
        serializer = ProfileSerializer(data=data, context={"request": request})
        if not (request.user.is_authenticated) and "user" not in data.keys():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors": "Para criar um perfil sem estar autenticado é necessário informar os dados de usuario."
                },
            )
        if profile is not None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"errors": "Já existe um perfil associado a este usuário."},
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @decorators.profile_analyser
    def put(self, request, profile, pk):
        saved_profile = ProfileModel.objects.get(pk=pk)
        if profile.id != pk:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors": "Usuário não tem permissão pra alterar o perfil informado."
                },
            )
        data = request.data
        serializer = ProfileSerializer(
            instance=saved_profile,
            data=data,
            partial=True,
            context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
