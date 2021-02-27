from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
import jwt
from simplecapp.settings import SECRET_KEY
from channels.auth import AuthMiddlewareStack

User = get_user_model()


@database_sync_to_async
def get_user(token_key):
    try:
        valid_data = jwt.decode(token_key, SECRET_KEY, algorithms=["HS256"])
        return User.objects.get(id=valid_data["user_id"])

    except:
        return AnonymousUser()


class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return TokenAuthMiddlewareInstance(scope, self)


class TokenAuthMiddlewareInstance:
    def __init__(self, scope, middleware):
        self.middleware = middleware
        self.scope = dict(scope)
        self.inner = self.middleware.inner

    async def __call__(self, receive, send):
        try:
            query = dict(
                (x.split("=") for x in self.scope["query_string"].decode().split("&"))
            )
            token_key = query.get("token")
            self.scope["user"] = await get_user(token_key)
        except:
            self.scope["user"] = AnonymousUser()
        return await self.inner(self.scope, receive, send)


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
