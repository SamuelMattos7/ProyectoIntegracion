# Generated by Django 4.1.3 on 2023-10-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ordenes",
            fields=[
                ("OrderID", models.BigAutoField(primary_key=True, serialize=False)),
                ("Fecha_orden", models.DateTimeField(auto_now_add=True)),
                (
                    "Status",
                    models.CharField(
                        choices=[
                            ("PENDIENTE", "No se ha procesado la orden todavía"),
                            ("ENTREGADO", "El cliente ha recibido el producto"),
                            ("ENVIADO", "El producto ha sido enviado al cliente"),
                            ("CANCELADO", "El cliente ha cancelado la orden"),
                        ],
                        default="PENDIENTE",
                        max_length=20,
                        verbose_name="Status de la orden",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pagos",
            fields=[
                (
                    "PagoID",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="pagoID"
                    ),
                ),
                (
                    "FechaPago",
                    models.DateTimeField(auto_now_add=True, verbose_name="Fecha_pago"),
                ),
                (
                    "TipoPago",
                    models.CharField(
                        choices=[
                            ("DEBITO", "Tarjeta debito"),
                            ("CREDITO", "Tarjeta credito"),
                            ("PREPAGO", "Tarjeta prepago"),
                        ],
                        max_length=20,
                        verbose_name="Tipo de pago",
                    ),
                ),
            ],
        ),
    ]
