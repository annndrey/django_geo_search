# Generated by Django 2.0.6 on 2018-06-16 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplieraccount',
            options={'verbose_name': 'supplier', 'verbose_name_plural': 'suppliers'},
        ),
    ]