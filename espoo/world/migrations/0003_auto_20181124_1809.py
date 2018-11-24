# Generated by Django 2.1.3 on 2018-11-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_busstops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busstops',
            name='name',
            field=models.CharField(max_length=100, verbose_name='NIMI'),
        ),
        migrations.AlterField(
            model_name='busstops',
            name='route',
            field=models.CharField(max_length=100, verbose_name='REITTI'),
        ),
        migrations.AlterField(
            model_name='busstops',
            name='tariff_area',
            field=models.CharField(max_length=2, verbose_name='TARIFFIALU'),
        ),
    ]
