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
from api.views import get_equipos, get_mantenimientos, get_lecturas, create_equipo, create_mantenimiento, create_lectura

urlpatterns = [
    path('equipos/', get_equipos),
    path('mantenimientos/', get_mantenimientos),
    path('lecturas/', get_lecturas),
    path('crear-equipo/', create_equipo),
    path('crear-mantenimiento/', create_mantenimiento),
    path('crear-lectura/', create_lectura),
]

