import pytest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from ..models import ProfileModel, StatesModel


@pytest.fixture(scope="session")
def factory():
    return APIRequestFactory()


@pytest.fixture
def valid_user_with_profile():
    valid_profile1 = {
        "gender": 1,
        "date_of_birth": "1995-05-05",
        "occupation": "IT Analyst",
        "phone_number": "4564656477",
        "cpf": "0924807890877",
        "cep": "88880000",
    }
    valid_user1 = {
        "username": "gustavoronconi",
        "password": make_password("gustavoronconi"),
        "email": "gustavo.ronconi@gmail.com.br",
        "first_name": "Gustavo A.",
        "last_name": "Ronconi",
        "is_staff": True,
    }
    valid_state = {"name": "Santa Catarina", "state_abbr": "SC", "cod_uf": 1}

    user1 = User.objects.create(**valid_user1)
    state = StatesModel.objects.create(**valid_state)
    profile = ProfileModel.objects.create(**valid_profile1, user=user1, state=state)
    return profile
