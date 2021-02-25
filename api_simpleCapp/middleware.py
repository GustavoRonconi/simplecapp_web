from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from channels.auth import AuthMiddlewareStack
import jwt
from api_simpleCapp.settings import SECRET_KEY


@database_sync_to_async
def get_user(token_key):
    try:
        valid_data = jwt.decode(token_key, SECRET_KEY, algorithms=["HS256"])
        return User.objects.get(pk=valid_data["user_id"])

    except:
        return AnonymousUser()


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        query = dict((x.split("=") for x in scope["query_string"].decode().split("&")))
        token_key = query.get("token")
        scope["user"] = get_user(token_key)

        return self.inner(scope)


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
