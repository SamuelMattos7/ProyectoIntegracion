from django import forms
from .models import Producto

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('Nombre', 'Creado_por', 'Cantidad', 'Codigos', 'Tipo',  'Marca', 'Precio')

    widgets = {
        'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'Creado_por': forms.Select(attrs={'class': 'form-control'}),
        'Cantidad': forms.TextInput(attrs={'class': 'form-control'}),
        'Codigos': forms.Select(attrs={'class': 'form-control'}),
        'Tipo': forms.Select(attrs={'class': 'form-control'}),
        'Marca': forms.TextInput(attrs={'class': 'form-control'}),
        'Precio': forms.TextInput(attrs={'class': 'form-control'}),
    }

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['Nombre', 'Cantidad', 'Codigos', 'Tipo',  'Marca', 'Precio']
    
        widget = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'Codigos': forms.TextInput(attrs={'class': 'form-control'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'Precio': forms.TextInput(attrs={'class': 'form-control'}),
        }