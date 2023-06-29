"""
URL configuration for api_rest project.

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
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import get_equipos, get_mantenimientos, get_lecturas, create_equipo, create_mantenimiento, create_lectura, cargar_ejemplos, main_view, protected_view, register_user, login

urlpatterns = [
    path('main/', main_view),
    path('equipos/', get_equipos),
    path('mantenimientos/', get_mantenimientos),
    path('lecturas/', get_lecturas),
    path('crear-equipo/', create_equipo),
    path('crear-mantenimiento/', create_mantenimiento),
    path('crear-lectura/', create_lectura),
    path('cargar-ejemplos/', cargar_ejemplos),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', protected_view, name='protected'),
    path('register/', register_user, name='register'),
    # path('login/', login, name='login'),
]

