# Generated by Django 5.1.5 on 2025-02-18 15:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/', verbose_name='Imagen del producto')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('estado', models.TextField(blank=True, null=True, verbose_name='Estado del producto')),
                ('volumen', models.FloatField(verbose_name='Volumen (metros cúbicos)')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
        ),
    ]
