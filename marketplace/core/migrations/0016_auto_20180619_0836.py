# Generated by Django 2.0.6 on 2018-06-19 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_auto_20180616_1226'),
        ('core', '0015_auto_20180618_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_tagline', models.CharField(max_length=100)),
                ('seller_location', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, default=44.4268, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, default=-26.1025, max_digits=9)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='activity',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=44.4268, max_digits=9),
        ),
        migrations.AlterField(
            model_name='activity',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=-26.1025, max_digits=9),
        ),
        migrations.AddField(
            model_name='seller',
            name='activities',
            field=models.ManyToManyField(to='core.Activity'),
        ),
        migrations.AddField(
            model_name='seller',
            name='category',
            field=models.ManyToManyField(to='core.Category'),
        ),
        migrations.AddField(
            model_name='seller',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.SupplierAccount'),
        ),
    ]