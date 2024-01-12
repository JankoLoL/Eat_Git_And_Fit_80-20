from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserEditView


app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit-profile', UserEditView.as_view(), name='edit-profile')

]
