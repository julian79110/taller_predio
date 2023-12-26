# Generated by Django 5.0 on 2023-12-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0002_predio_numerocatastral_predio_numeromatricula_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePropietario', models.CharField(max_length=30)),
                ('tipoPropietario', models.CharField(choices=[('natural', 'Natural'), ('juridico', 'Juridico')], default='natural', max_length=9)),
                ('numeroDocumento', models.CharField(max_length=10, unique=True)),
                ('tipoDocumento', models.CharField(choices=[('cedula de ciudadania', 'Cedula'), ('cedula de extranjeria', 'Cedulae'), ('numero de identificacion tributaria', 'Tributaria'), ('tarjeta de identidad', 'Tarjeta Identidad')], default='cedula de ciudadania', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='predio',
            name='propietario',
            field=models.CharField(default='na', max_length=35),
        ),
    ]