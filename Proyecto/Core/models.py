from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator

class CodigosProductos(models.Model):

    TipoProd= [
        ("RADIO MOVIL","Movil"),
        ("RADIO PORTATIL","Portatil"),
        ("RADIO APX","APX")
    ] 

    CodigosProd= [
        ("PR7","R7"),
        ("PR2","R2"),
        ("PR5","DEP550"),
        ('PR3', 'EP350'),
        ('M8e', '8500e'),
        ('M5e', '5000e'),
        ('M8', 'DGM8000'),
        ('M5', 'DEM500'),
        ('APX0', 'APX'),
        ('APX2', 'APX'),
        ('APX1', 'APX'),
        
    ] 

    ProductoCodigo= models.CharField(verbose_name='Codigo de Producto', choices=CodigosProd, max_length=40, unique=True)
    TipoProducto = models.CharField(verbose_name='Tipo de Producto', choices=TipoProd, max_length=40, unique=True)

# Create your models here.
class Producto(models.Model):
    ProductID = models.AutoField(primary_key=True, verbose_name='ProductID')
    Creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Nombre = models.CharField(verbose_name="Nombre del producto", max_length=60)
    Cantidad = models.SmallIntegerField(verbose_name="Cantidad de producto", validators=[MinValueValidator(1)])
    Codigos= models.OneToOneField(
        CodigosProductos,
        to_field='ProductoCodigo', 
        related_name='ProductCodigo',
        on_delete=models.CASCADE 
    ) 
    Tipo = models.OneToOneField(
        CodigosProductos,
        to_field='TipoProducto', 
        related_name='CarritoDeUser',
        on_delete=models.CASCADE 
    )
    Marca = models.CharField(verbose_name="Marca del producto", max_length=60)
    Precio = models.IntegerField(verbose_name='Precio', null=False)
    Creado_el = models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)
    Modificado_el = models.DateTimeField(verbose_name='Fecha de Modificacion', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('AdminProductList', args=str((self.ProductID)))
