import json
from django.test import TestCase
from ..models import ProfileModel, StatesModel
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from django.contrib.auth.hashers import make_password
from ..views import ProfileView
from ..serializers import ProfileSerializer
from rest_framework import status


factory = APIRequestFactory()


class ProfileTest(TestCase):
    """ Test module for GET profile based USER TOKEN """

    def setUp(self):
        # CRIAÇÃO DE UM USUÁRIO COM PERFIL
        self.valid_profile1 = {
            "age": 25,
            "gender": 1,
            "date_of_birth": "1995-05-05",
            "occupation": "IT Analyst",
            "phone_number": "45646564",
            "cpf": "09248078908",
            "cep": "88880000",
        }
        self.valid_user1 = {
            "username": "gustavoronconi",
            "password": make_password("gustavoronconi"),
            "email": "gustavo.ronconi@gmail.com.br",
            "first_name": "Gustavo A.",
            "last_name": "Ronconi",
        }
        self.valid_state = {"name": "Santa Catarina", "state_abbr": "SC", "cod_uf": 1}

        user1 = User.objects.create(**self.valid_user1)
        self.state = StatesModel.objects.create(**self.valid_state)
        self.profile_with_user = ProfileModel.objects.create(
            **self.valid_profile1, user=user1, state=self.state
        )

        # CRIAÇÃO DE UM USUÁRIO SEM PERFIL (SOCIAL_LOGIN)
        self.valid_user2 = {
            "username": "gustavoronconi2",
            "password": make_password("gustavoronconi2"),
            "email": "gustavo.ronconi2@gmail.com.br",
            "first_name": "Gustavo A.",
            "last_name": "Ronconi",
        }
        User.objects.create(**self.valid_user2)

    def test_post_valid_profile_with_social_login(self):
        user = User.objects.get(username="gustavoronconi2")
        profile_to_post = {
            "age": 25,
            "gender": 1,
            "date_of_birth": "1995-05-05",
            "occupation": "IT Analyst",
            "phone_number": "456465642424",
            "cpf": "0924807892424",
            "cep": "88880000",
            "state": self.state.pk,
        }

        view = ProfileView.as_view()
        request = factory.post(
            "/profile/", json.dumps(profile_to_post), content_type="application/json",
        )
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_valid_profile_without_social_login(self):
        profile_to_post = {
            "age": 25,
            "gender": 1,
            "date_of_birth": "1995-05-05",
            "occupation": "IT Analyst",
            "phone_number": "4564656424",
            "cpf": "09248078924",
            "cep": "88880000",
            "user": {
                "username": "gustavoronconi3",
                "password": make_password("gustavoronconi3"),
                "email": "gustavo.ronconi3@gmail.com.br",
                "first_name": "Gustavo A.",
                "last_name": "Ronconi",
            },
            "state": self.state.pk,
        }
        request = factory.post(
            "/profile/", json.dumps(profile_to_post), content_type="application/json",
        )
        view = ProfileView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_profile_without_social_login(self):
        profile_to_post = {
            "age": 25,
            "gender": 1,
            "date_of_birth": "1995-05-05",
            "occupation": "IT Analyst",
            "phone_number": "45646564",
            "cpf": "09248078908",
            "cep": "88880000",
        }
        request = factory.post(
            "/profile/", json.dumps(profile_to_post), content_type="application/json",
        )
        view = ProfileView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_profile_valid_authenticate(self):
        profile_to_check = ProfileModel.objects.get(pk=self.profile_with_user.pk)
        serializer = ProfileSerializer(profile_to_check)
        user = User.objects.get(username="gustavoronconi")
        view = ProfileView.as_view()
        request = factory.get("/profile/")
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_profile_invalid_authenticate(self):
        view = ProfileView.as_view()
        request = factory.get("/profile/")
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_without_profile(self):
        user = User.objects.get(username="gustavoronconi2")
        view = ProfileView.as_view()
        request = factory.get("/profile/")
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

