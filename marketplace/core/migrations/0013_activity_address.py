# Generated by Django 2.0.6 on 2018-06-18 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180618_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Venue'),
            preserve_default=False,
        ),
    ]
