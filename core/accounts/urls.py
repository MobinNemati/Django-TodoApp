from django.urls import path
from .views import LoginPageView, RegisterPageView, LogoutPageView
from django.contrib.auth.views import LogoutView


app_name = "accounts"

urlpatterns = [
    path("login/", LoginPageView.as_view(), name="login"),
    path("logout/", LogoutPageView.as_view(), name="logout"),
    path("register/", RegisterPageView.as_view(), name="register"),
]
