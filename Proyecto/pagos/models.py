from django.db import models
from django.conf import settings

# Create your models here.
class Pagos(models.Model):
    PagoID = models.BigAutoField(primary_key=True, verbose_name='codigo_pago')
    Compador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='UserID', 
        related_name='Pagos_Comprador',
        on_delete=models.CASCADE 
    )
    FechaPago = models.DateTimeField(auto_now_add=True, verbose_name='Fecha_pago')
    TipoPago = models.CharField(verbose_name='Tipo de pago')
    

