import pytest
from channels.testing import WebsocketCommunicator
from django.contrib.auth.models import User
import json
from rest_framework.test import force_authenticate
from ...views import NotificationView
import jwt
from api_simpleCapp.settings import SECRET_KEY
from channels.testing import WebsocketCommunicator
from channels.db import database_sync_to_async
from django.contrib.auth.hashers import make_password

from api_simpleCapp.asgi import application
from asgiref.sync import sync_to_async


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_send_receive_notification(factory):
    valid_user = {
        "username": "gustavoronconi",
        "password": make_password("gustavoronconi"),
        "email": "gustavo.ronconi@gmail.com.br",
        "first_name": "Gustavo A.",
        "last_name": "Ronconi",
        "is_staff": True,
    }
    user = await database_sync_to_async(User.objects.create)(**valid_user)

    token = str(
        jwt.encode(
            {
                "token_type": "access",
                "exp": 4580584862,
                "jti": "3f20a75d3ac543cfbe9c79bd247491fb",
                "user_id": user.id,
            },
            SECRET_KEY,
            algorithm="HS256",
        ),
        "utf-8",
    )

    communicator = WebsocketCommunicator(application, f"/notification/?token={token}",)
    connected, _ = await communicator.connect()
    assert connected

    request = await sync_to_async(factory.post)(
        "/notification/",
        json.dumps({"message": "Hello Word!"}),
        content_type="application/json",
    )
    force_authenticate(request, user=user)

    view = NotificationView.as_view()
    response = await sync_to_async(view)(request)

    response2 = await communicator.receive_from()
    assert response.data["message"] == json.loads(response2)["event"]
