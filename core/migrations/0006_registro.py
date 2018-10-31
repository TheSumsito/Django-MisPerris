# Generated by Django 2.1.2 on 2018-10-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Foto', models.FileField(upload_to='')),
                ('Nombre', models.CharField(max_length=45)),
                ('Descripcion', models.TextField(max_length=45)),
                ('Raza', models.CharField(max_length=45)),
                ('Estado', models.CharField(max_length=45)),
            ],
        ),
    ]