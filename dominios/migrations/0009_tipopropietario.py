# Generated by Django 5.0 on 2024-01-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0008_tipopredio_tipopredio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPropietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True, verbose_name='Tipo De Propietario')),
            ],
        ),
    ]
