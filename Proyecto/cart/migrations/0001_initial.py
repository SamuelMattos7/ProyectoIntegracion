# Generated by Django 4.1.3 on 2023-10-14 19:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrito",
            fields=[
                (
                    "CartID",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="CartID"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartItems",
            fields=[
                (
                    "XID",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="XID"
                    ),
                ),
                (
                    "Cantidad",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "Cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Carrito",
                        to="cart.carrito",
                    ),
                ),
                (
                    "Item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Item",
                        to="Core.producto",
                    ),
                ),
            ],
        ),
    ]