from os import name
from django.urls import path
from lotes.views import BuscarLotes
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view( template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('consultar-lote/', views.BuscarLotes, name='consultar-lote'),
]   