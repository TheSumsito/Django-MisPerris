# Generated by Django 2.1.2 on 2018-10-31 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20181030_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='IdMascotas',
            field=models.IntegerField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mascota',
            name='Nombre',
            field=models.CharField(max_length=45),
        ),
    ]