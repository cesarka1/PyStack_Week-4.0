from urllib.parse import urlparse
from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [

    path('pacientes/', views.pacientes, name="pacientes")
]