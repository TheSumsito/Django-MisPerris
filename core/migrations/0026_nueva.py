# Generated by Django 2.1.2 on 2018-11-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20181101_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nueva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=45)),
            ],
        ),
    ]
