# Generated by Django 2.0.6 on 2018-06-16 23:40

import core.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180616_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='media',
            field=models.ImageField(blank=True, height_field='height_field', null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/cristido/Desktop/Hard/Hardenv/static_cdn/protected'), upload_to=core.models.media_location, width_field='width_field'),
        ),
    ]
