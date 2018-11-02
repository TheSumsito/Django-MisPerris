# Generated by Django 2.1.2 on 2018-11-01 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_delete_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('Rut', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
                ('Correo', models.EmailField(max_length=45)),
                ('FechaNaci', models.DateField()),
                ('Telefono', models.IntegerField()),
                ('Vivienda', models.CharField(max_length=45)),
                ('IdCiudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ciudad')),
                ('IdRegion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region')),
            ],
        ),
    ]