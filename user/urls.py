from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserEditView, UserPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit-profile', UserEditView.as_view(), name='edit-profile'),
    path('password-change/', UserPasswordChangeView.as_view(), name='change-password'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='user/password-change-done.html')
         , name='password_change_done'),
]
