from django.shortcuts import render
from . models import *
# Create your views here.
def carrito(request):
    if request.user.is_authenticated:
        cliente = request.user
        carrito = Carrito.objects.get_or_create(UserCart=cliente, Completado=False)
        items = carrito.Carrito.all()
        total = carrito.PrecioTotal()
        cantidad = carrito.CantidadTotal()
    else:
        items = []
        total = 0
        cantidad = 0
    
    context = {'items':items, 'total':total, 'cantidad':cantidad}
    return render(request, 'carrito.html', context)