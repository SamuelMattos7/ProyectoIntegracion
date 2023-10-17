from django import forms
from .models import Producto

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Nombre', 'Cantidad', 'Tipo', 'Marca']

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['Nombre', 'Cantidad', 'Tipo', 'Marca']
