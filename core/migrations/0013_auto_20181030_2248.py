# Generated by Django 2.1.2 on 2018-10-31 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20181030_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='Region',
            new_name='IdRegion',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='Ciudad',
            new_name='IdCiudad',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='Region',
            new_name='IdRegion',
        ),
    ]
