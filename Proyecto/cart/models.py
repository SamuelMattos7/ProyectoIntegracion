from django.db import models
from django.conf import settings 
from django.core.validators import MinValueValidator
from Core.models import Producto
    
class Carrito(models.Model):
    CartID= models.AutoField(primary_key=True, verbose_name='CartID')
    UserCart= models.OneToOneField(
        settings.AUTH_USER_MODEL,
        to_field='UserID', 
        related_name='CarritoDeUser',
        on_delete=models.CASCADE 
    )

class CartItems(models.Model):
    CartItemsID = models.AutoField(primary_key=True, verbose_name='XID')
    Cart = models.ForeignKey(
        Carrito,
        to_field='CartID',
        related_name='Carrito',
        on_delete=models.CASCADE
    )
    Item = models.ForeignKey(
        Producto, 
        to_field='ProductID',
        related_name='Item', 
        on_delete= models.CASCADE,
    )
    Cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def PrecioTotal(self):
        return self.Cantidad * self.Item.Precio

