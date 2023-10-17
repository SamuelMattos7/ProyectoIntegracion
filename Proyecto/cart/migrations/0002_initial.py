# Generated by Django 4.1.3 on 2023-10-14 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cart", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="carrito",
            name="UserCart",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="CarritoDeUser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
