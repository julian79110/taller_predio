# Generated by Django 5.0 on 2024-01-02 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0008_tipopredio_tipopredio_and_more'),
        ('predio', '0020_alter_propietario_tipopropietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='tipoPropietario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dominios.tipospropietario', to_field='tipoPropietario'),
        ),
    ]
