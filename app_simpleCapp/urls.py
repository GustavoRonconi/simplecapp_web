from django.urls import path
from .views import SocialLoginView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("auth/social-login/", SocialLoginView.as_view()),
    path(
        "auth/login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("auth/login/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
