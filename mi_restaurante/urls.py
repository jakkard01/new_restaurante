# mi_restaurante/urls.py

from django.urls import path
from .views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    # Otras rutas según sea necesario
]