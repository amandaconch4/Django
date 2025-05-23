# Generated by Django 5.2 on 2025-04-11 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_perfil', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
                ('confir_contraseña', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/usuario')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='Wiki_the_forest.perfil')),
            ],
        ),
    ]
