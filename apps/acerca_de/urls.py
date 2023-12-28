from django.urls import path
from . import views

app_name = 'apps.acerca_de'

urlpatterns = [
    path('acerca_de/', views.acerca_de, name='acerca_de'),
]
