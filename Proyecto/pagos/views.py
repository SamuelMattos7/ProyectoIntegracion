from django.shortcuts import render

# Create your views here.
def Pagos(request):
    return render(request, 'pagos.html')