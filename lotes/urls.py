from os import name
from django.urls import path
from lotes.views import BuscarLotes
from . import views

urlpatterns = [
  
    path('consultar-lote/', views.BuscarLotes, name='consultar-lote'),
]   