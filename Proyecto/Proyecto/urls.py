from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('Core.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls')),
]
