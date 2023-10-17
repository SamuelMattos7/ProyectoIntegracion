from django.urls import path
from .import views

urlpatterns = [
    path('pagos/', views.Pagos, name='home'),
]