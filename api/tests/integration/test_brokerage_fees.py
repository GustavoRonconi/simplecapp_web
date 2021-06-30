import json

import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import force_authenticate

from ...models import BrokerageFeesModel, BrokerModel
from ...serializers import BrokerageFeesSerializer
from ...views import BrokerageFeesView


@pytest.fixture
def valid_brokerage_fees():
    broker = {"broker_name": "Corretora para testes"}
    broker = BrokerModel.objects.create(**broker)
    return [
        {
            "begin_date": "2021-01-01",
            "end_date": None,
            "brokerage_fee_value": "35.70000",
            "broker_id": broker.pk,
        },
        {
            "begin_date": "2020-01-01",
            "end_date": "2020-12-31",
            "brokerage_fee_value": "35.60000",
            "broker_id": broker.pk,
        },
    ]


@pytest.mark.django_db
def test_get_brokerage_fees_by_profile(valid_user_with_profile, factory, valid_brokerage_fees):

    brokerage_fees_by_profile = BrokerageFeesModel.objects.bulk_create(
        [BrokerageFeesModel(**q, profile=valid_user_with_profile) for q in valid_brokerage_fees]
    )
    serializer = BrokerageFeesSerializer(brokerage_fees_by_profile, many=True)
    user = User.objects.get(username="gustavoronconi")
    view = BrokerageFeesView.as_view()
    request = factory.get("/brokerage-fees/")
    force_authenticate(request, user=user)
    response = view(request)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_post_valid_brokerage_fees(valid_user_with_profile, factory, valid_brokerage_fees):
    user = User.objects.get(username="gustavoronconi")
    view = BrokerageFeesView.as_view()
    request = factory.post(
        "/brokerage-fees/", json.dumps(valid_brokerage_fees), content_type="application/json",
    )

    force_authenticate(request, user=user)
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_invalid_brokerage_fees(valid_user_with_profile, factory, valid_brokerage_fees):
    invalid_brokerage_fees = valid_brokerage_fees.copy()
    invalid_brokerage_fees[0]["begin_date"] = "2021-01-02"
    user = User.objects.get(username="gustavoronconi")
    view = BrokerageFeesView.as_view()
    request = factory.post(
        "/brokerage-fees/", json.dumps(invalid_brokerage_fees), content_type="application/json",
    )

    force_authenticate(request, user=user)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
