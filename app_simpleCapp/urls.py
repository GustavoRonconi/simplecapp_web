from django.urls import path, include
from .views import (
    SocialLoginView,
    ProfileView,
    BrokerageFeesView,
    BrokerView,
    SyncCeiView,
    NotificationView,
    HomeView,
)
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
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("brokerage-fees/", BrokerageFeesView.as_view(), name="brokerage-fees"),
    path("broker/", BrokerView.as_view(), name="broker"),
    path("sync-cei/", SyncCeiView.as_view(), name="sync-cei"),
    path("celery-progress/", include("celery_progress.urls"), name="celery-progress"),
    path("notification/", NotificationView.as_view(), name="broker"),
    path("", HomeView.as_view()),
]
