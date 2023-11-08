from django.db import models
from cart.models import CartItems
from django.conf import settings

# Create your models here.
class Pagos(models.Model):

    MEDIOS_DE_PAGO = (
        ('DEBITO', 'Tarjeta debito'),
        ('CREDITO', 'Tarjeta credito'),
        ('PREPAGO', 'Tarjeta prepago'),
    )

    PagoID = models.BigAutoField(primary_key=True, verbose_name='pagoID')
    Comprador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='UserID', 
        related_name='Pagos_Comprador',
        on_delete=models.CASCADE 
    )
    FechaPago = models.DateTimeField(auto_now_add=True, verbose_name='Fecha_pago')
    TipoPago = models.CharField(verbose_name='Tipo de pago', max_length=20, choices=MEDIOS_DE_PAGO)

class Ordenes(models.Model):
    STATUS = (
        ('PENDIENTE', 'No se ha procesado la orden todavía'),
        ('ENTREGADO', 'El cliente ha recibido el producto'),
        ('ENVIADO', 'El producto ha sido enviado al cliente'),
        ('CANCELADO', 'El cliente ha cancelado la orden'),
    )

    OrderID = models.BigAutoField(primary_key=True)
    Cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ordenes_comprador'  
    )
    Fecha_orden = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(
        verbose_name='Status de la orden',
        choices=STATUS,
        default='PENDIENTE',
        max_length=20 
    )
    MetodoPago = models.OneToOneField(
        Pagos,
        on_delete=models.CASCADE,
        related_name='metodo_pago_ordenes' 
    )
    ItemsComprados = models.ForeignKey(
        CartItems,
        on_delete=models.CASCADE,
        related_name='productos_comprados' 
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ItemsComprados'],
                name='unique_item_comprados'
            ),
            models.UniqueConstraint(
                fields=['MetodoPago'],
                name='unique_metodo_pago'
            )
        ]
