# Generated by Django 2.1.2 on 2018-11-01 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20181101_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nueva',
            name='Ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ciudad'),
        ),
        migrations.AlterField(
            model_name='nueva',
            name='Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
    ]
