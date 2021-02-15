from django.urls import path
from .views import SocialLoginView, ProfileView, BrokerageFeesView, BrokerView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("auth/social-login/", SocialLoginView.as_view(), name="social_login"),
    path(
        "auth/login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "auth/login/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("brokerage-fees/", BrokerageFeesView.as_view(), name="brokerage-fees"),
    path("broker/", BrokerView.as_view(), name="broker"),
]
