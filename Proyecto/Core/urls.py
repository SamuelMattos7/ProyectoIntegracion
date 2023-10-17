from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('AdminProductList', views.VerProduct, name='AdminProductList'),
    path('CrearProduct/', views.CrearProduct, name='CrearProduct'),
    path('ActulizarProduct/<int:id>/', views.UpdateProducto, name='ActulizarProduct'),
    path('EliminarProduct/<int:id>/', views.DeleteProducto, name='EliminarProduct'),
]