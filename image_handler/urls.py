from django.urls import path
from image_handler.views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='test_view'),

]
