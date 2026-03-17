from django.urls import path
from .views import inicio, buscar, resultados

urlpatterns = [
    path('', inicio),
    path('buscar/', buscar),
    path('resultados/', resultados),
]