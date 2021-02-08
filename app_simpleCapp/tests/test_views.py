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
        mocked_profile = {
            "age": 25,
            "gender": 1,
            "date_of_birth": "1995-05-05",
            "occupation": "IT Analyst",
            "phone_number": "55489980505587785",
            "cpf": "09248078908",
            "state": {"name": "Santa Catarina", "state_abbr": "SC", "cod_uf": 1},
            "cep": "88880000",
            "user": {
                "username": "novo_gustavo5",
                "password": "novo_gustavo5",
                "email": "gustavo.ronconi@teste5.com.br",
                "first_name": "Gustavo A.",
                "last_name": "Ronconi",
            },
        }
        user_without_profile = {
            "username": "novo_gustavo6",
            "password": "novo_gustavo6",
            "email": "gustavo.ronconi@teste6.com.br",
            "first_name": "Gustavo A.",
            "last_name": "Ronconi",
        }
        user_with_profile_data = mocked_profile.pop("user")
        state_data = mocked_profile.pop("state")
        user_without_profile["password"] = make_password(
            user_without_profile["password"]
        )
        user_with_profile_data["password"] = make_password(
            user_with_profile_data["password"]
        )
        user_with_profile_ = User.objects.create(**user_with_profile_data)
        User.objects.create(**user_without_profile)
        state = StatesModel.objects.create(**state_data)
        self.profile_with_user = ProfileModel.objects.create(
            **mocked_profile, user=user_with_profile_, state=state
        )

    def test_get_profile_valid_authenticate(self):
        profile_to_check = ProfileModel.objects.get(pk=self.profile_with_user.pk)
        serializer = ProfileSerializer(profile_to_check)
        user = User.objects.get(username="novo_gustavo5")
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
        user = User.objects.get(username="novo_gustavo6")
        view = ProfileView.as_view()
        request = factory.get("/profile/")
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

