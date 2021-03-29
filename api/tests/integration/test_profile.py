import json

import pytest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import force_authenticate

from ...models import ProfileModel, StatesModel
from ...serializers import ProfileSerializer
from ...views import ProfileView


@pytest.fixture
def valid_user_without_profile():
    valid_user2 = {
        "username": "gustavoronconi2",
        "password": make_password("gustavoronconi2"),
        "email": "gustavo.ronconi2@gmail.com.br",
        "first_name": "Gustavo A.",
        "last_name": "Ronconi",
    }
    return User.objects.create(**valid_user2)


@pytest.mark.django_db
def test_post_valid_profile_with_social_login(
    valid_user_with_profile, valid_user_without_profile, factory
):
    user = User.objects.get(username="gustavoronconi2")
    profile_to_post = {
        "gender": 1,
        "date_of_birth": "1995-05-05",
        "occupation": "IT Analyst",
        "phone_number": "456465642424",
        "cpf": "0924807892424",
        "cep": "88880000",
        "street": "Rua Dr. Valdir Cotrin",
        "district": "Centro",
        "state": valid_user_with_profile.state.pk,
    }

    view = ProfileView.as_view()
    request = factory.post(
        "/profile/", json.dumps(profile_to_post), content_type="application/json",
    )
    force_authenticate(request, user=user)
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_valid_profile_without_social_login(factory, valid_user_with_profile):
    profile_to_post = {
        "gender": 1,
        "date_of_birth": "1995-05-05",
        "occupation": "IT Analyst",
        "phone_number": "4564656424",
        "cpf": "09248078924",
        "cep": "88880000",
        "street": "Rua Dr. Valdir Cotrin",
        "district": "Centro",
        "user": {
            "username": "gustavoronconi3",
            "password": make_password("gustavoronconi3"),
            "email": "gustavo.ronconi3@gmail.com.br",
            "first_name": "Gustavo A.",
            "last_name": "Ronconi",
        },
        "state": valid_user_with_profile.state.pk,
    }
    request = factory.post(
        "/profile/", json.dumps(profile_to_post), content_type="application/json",
    )
    view = ProfileView.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_profile(factory, valid_user_with_profile):
    user = User.objects.get(username="gustavoronconi")
    request = factory.delete("/profile/")
    view = ProfileView.as_view()
    force_authenticate(request, user=user)
    response = view(request)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_post_invalid_profile_without_social_login(factory, valid_user_with_profile):
    profile_to_post = {
        "gender": 1,
        "date_of_birth": "1995-05-05",
        "occupation": "IT Analyst",
        "phone_number": "45646564",
        "cpf": "09248078908",
        "cep": "88880000",
        "street": "Rua Dr. Valdir Cotrin",
        "district": "Centro",
    }
    request = factory.post(
        "/profile/", json.dumps(profile_to_post), content_type="application/json",
    )
    view = ProfileView.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_profile_valid_authenticate(factory, valid_user_with_profile):
    profile_to_check = ProfileModel.objects.get(pk=valid_user_with_profile.pk)
    serializer = ProfileSerializer(profile_to_check)
    user = User.objects.get(username="gustavoronconi")
    view = ProfileView.as_view()
    request = factory.get("/profile/")
    force_authenticate(request, user=user)
    response = view(request)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_get_profile_invalid_authenticate(factory, valid_user_with_profile):
    view = ProfileView.as_view()
    request = factory.get("/profile/")
    response = view(request)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_user_without_profile(factory, valid_user_without_profile):
    user = User.objects.get(username="gustavoronconi2")
    view = ProfileView.as_view()
    request = factory.get("/profile/")
    force_authenticate(request, user=user)
    response = view(request)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_put_valid_profile(factory, valid_user_with_profile):
    view = ProfileView.as_view()
    user = User.objects.get(username="gustavoronconi")
    profile_to_put = {
        "gender": 1,
        "user": {"email": "gustavo.ronconi@teste7.com.br"},
    }

    request = factory.put(
        f"/profile/{valid_user_with_profile.id}/",
        json.dumps(profile_to_put),
        content_type="application/json",
    )

    force_authenticate(request, user=user)
    response = view(request, pk=valid_user_with_profile.id)

    assert response.status_code == status.HTTP_200_OK
    assert {
        "gender": response.data["gender"],
        "user": {"email": response.data["user"]["email"]},
    } == profile_to_put


@pytest.mark.django_db
def test_put_invalid_profile(factory, valid_user_with_profile):
    view = ProfileView.as_view()
    user = User.objects.get(username="gustavoronconi")
    profile_to_put = {
        "cpf": "4164654",
    }

    request = factory.put(
        f"/profile/{valid_user_with_profile.id}/",
        json.dumps(profile_to_put),
        content_type="application/json",
    )

    force_authenticate(request, user=user)
    response = view(request, pk=valid_user_with_profile.id)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
