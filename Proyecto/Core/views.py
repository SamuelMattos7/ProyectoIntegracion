from django.shortcuts import render, get_object_or_404
from django.views import generic
from Core.models import Producto
from django.http import HttpResponseRedirect
from .form import ProductUpdateForm, ProductCreateForm
from django.urls import reverse 
from django.shortcuts import redirect

# Create your views here.
def Home(request): 
    return render(request, template_name="home.html")

def VerProduct(request):

    Item = Producto.objects.all().values()

    template_name = 'productosTest.html'
    
    contexto = {
        'Object': Item,
    }

    return render(request, template_name, contexto)

def CrearProduct(request):
    
    form = ProductCreateForm()
    
    if request.method == 'POST':

        form = ProductCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AdminProductList'))
        else:
            form = ProductCreateForm()

    return render(request, 'CrearProducto.html', {'form':form})
        
def UpdateProducto(request, id):
    
    instance = get_object_or_404(Producto, ProductID = id)

    if request.method == 'POST':
        
        form = ProductUpdateForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AdminProductList'))
    else:
        form = ProductUpdateForm(instance=instance)

    return render(request, 'UpdateProductos.html', {'form':form})

def DeleteProducto(request, id):

    instance = get_object_or_404(Producto, ProductID = id)
    product = {'producto': instance}

    if request.method == 'GET':
        return render(request, 'BorrarProducto.html' ,product)
    
    elif request.method == 'POST':
        instance.delete()
        return redirect('AdminProductList')

