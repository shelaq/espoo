# Generated by Django 2.1.3 on 2018-11-24 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_espooregions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espooregions',
            old_name='kunta',
            new_name='greater',
        ),
        migrations.RenameField(
            model_name='espooregions',
            old_name='nimi',
            new_name='municipality',
        ),
        migrations.RenameField(
            model_name='espooregions',
            old_name='nimi_iso',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='espooregions',
            old_name='pien',
            new_name='name_larger',
        ),
        migrations.RenameField(
            model_name='espooregions',
            old_name='suur',
            new_name='smaller',
        ),
        migrations.RenameField(
            model_name='espooregions',
            old_name='mtryhm',
            new_name='some_group',
        ),
        migrations.RenameField(
            model_name='espooregions',
            old_name='tila',
            new_name='space',
        ),
    ]
