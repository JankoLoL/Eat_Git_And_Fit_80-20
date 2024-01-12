from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from .forms import EditUserProfileForm


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super(UserRegisterView, self).form_valid(form)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(self.request, username=username, password=password)
        if new_user:
            login(self.request, new_user)
        return valid


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class UserEditView(UpdateView):
    model = User
    form_class = EditUserProfileForm
    template_name = 'user/edit-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('index')
