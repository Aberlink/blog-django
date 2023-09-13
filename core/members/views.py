from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import PermissionDenied


from .forms import SignUpForm, UpdateUserForm


class UserRegistrationView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserDetailView(DetailView):
    model = User
    template_name = "registration/user_profile.html"

    def get_object(self):
        username = self.kwargs["user"]
        current_user = self.request.user

        if username == current_user.username:
            return get_object_or_404(User, username=username)
        else:
            raise PermissionDenied(
                "You don't have permission to view this user's profile"
            )


class UpdateUserView(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = "registration/edit_user.html"

    def get_object(self):
        username = self.kwargs["user"]
        current_user = self.request.user

        if username == current_user.username:
            return get_object_or_404(User, username=username)
        else:
            raise PermissionDenied(
                "You don't have permission to view this user's profile"
            )

    def get_success_url(self):
        username = self.kwargs["user"]
        return reverse("user_profile", kwargs={"user": username})
    
    
class ChangePasswordView(PasswordChangeView):
    model = User
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    
    def get_success_url(self):
        username = self.request.user
        return reverse("user_profile", kwargs={"user": username})
