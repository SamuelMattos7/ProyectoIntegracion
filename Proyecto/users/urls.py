from django.contrib.auth import views as auth_views
from users.form import UsuarioLogin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Users, name='users'),
    path('registro/', views.Registro, name='registro'),
    path('activar/<slug:uidb64>/<slug:token>)/', views.Activacion_Cuenta, name='activar'),
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html', form_class=UsuarioLogin), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login/'), name='logout'),
]