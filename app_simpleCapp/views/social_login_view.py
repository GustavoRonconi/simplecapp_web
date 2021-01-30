from rest_framework import generics, permissions, status
from rest_framework.response import Response
from requests.exceptions import HTTPError

from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from rest_framework_simplejwt.tokens import RefreshToken
from app_simpleCapp.serializers.social_login_serializer import SocialSerializer


class SocialLoginView(generics.GenericAPIView):
    """Log in using facebook"""

    serializer_class = SocialSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Authenticate user through the provider and access_token"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.data.get("provider", None)
        strategy = load_strategy(request)

        try:
            backend = load_backend(strategy=strategy, name=provider, redirect_uri=None)

        except MissingBackend:
            return Response(
                {"error": "Please provide a valid provider"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            access_token = None
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get("access_token")
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response(
                {"error": {"access_token": "Invalid token", "details": str(error)}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except AuthTokenError as error:
            return Response(
                {"error": "Invalid credentials", "details": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except AuthForbidden as error:
            return Response(
                {"error": "Invalid token", "details": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            authenticated_user = backend.do_auth(access_token, user=user)

        except HTTPError as error:
            return Response(
                {"error": "Invalid token", "details": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except AuthForbidden as error:
            return Response(
                {"error": "Invalid token", "details": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if authenticated_user and authenticated_user.is_active:
            refresh = RefreshToken.for_user(user)
            response = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(status=status.HTTP_200_OK, data=response)
