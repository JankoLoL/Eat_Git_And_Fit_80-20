"""
URL configuration for eat_fit_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from eat_fit_app.views import *
from image_handler.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eat_fit_app.urls')),
    path('image/', include('image_handler.urls')),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)