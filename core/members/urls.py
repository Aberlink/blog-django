from django.urls import path, include
from .views import UserRegistrationView, UserDetailView, UpdateUserView, ChangePasswordView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("profile/<str:user>", UserDetailView.as_view(), name="user_profile"),
    path("profile/edit/<str:user>", UpdateUserView.as_view(), name="update_user"),
    path("password/", ChangePasswordView.as_view(), name="change_password"),
]
