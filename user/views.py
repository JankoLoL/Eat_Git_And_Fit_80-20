from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import CreateView, UpdateView
from .forms import EditUserProfileForm


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        valid = super(UserRegisterView, self).form_valid(form)

        return valid


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserProfileForm
    template_name = 'user/edit-profile.html'
    success_url = reverse_lazy('user:edit-profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        super(UserEditView, self).form_valid(form)
        messages.success(self.request, 'Profile successfully updated')
        return redirect('user:edit-profile')


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/change-password.html'
    success_url = reverse_lazy('user:password_change_done')

    def form_valid(self, form):
        messages.success(self.request, "Your password was successfully updated!")
        return super().form_valid(form)