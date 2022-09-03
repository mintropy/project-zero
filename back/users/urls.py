from re import A
from django.urls import path
from .views import UserViewSet

sign_up = UserViewSet.as_view({"post": "signup"})
profile = UserViewSet.as_view(
    {
        "get": "retrieve_profile",
        "post": "update_profile",
    }
)

urlpatterns = [
    path("signup/", sign_up, name="sign up"),
    path("profile/", profile, name="profile"),
]
    