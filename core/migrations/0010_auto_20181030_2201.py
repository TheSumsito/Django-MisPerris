# Generated by Django 2.1.2 on 2018-10-31 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20181030_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('Foto', models.FileField(upload_to='')),
                ('Nombre', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('Descripcion', models.TextField(max_length=45)),
                ('Raza', models.CharField(max_length=45)),
                ('Estado', models.CharField(max_length=45)),
            ],
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]