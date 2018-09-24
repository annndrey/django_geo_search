# Generated by Django 2.0.6 on 2018-06-13 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField(max_length=2500)),
                ('short_description', tinymce.models.HTMLField(default=None, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('order', models.IntegerField(default=0, help_text='Activity priority (bigger is better)')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('tagline', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('price_currency', models.CharField(choices=[('1', 'RON'), ('2', 'EUR')], default=1, max_length=3)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
                'ordering': ['-order'],
            },
        ),
        migrations.CreateModel(
            name='ActivityAgeInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Interval Name', max_length=250)),
            ],
            options={
                'verbose_name': 'Activity Age Interval',
                'verbose_name_plural': 'Activity Age Intervals',
            },
        ),
        migrations.CreateModel(
            name='ActivityLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('tagline', models.TextField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Activity Location',
                'verbose_name_plural': 'Activity Locations',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'supplier',
                'verbose_name_plural': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'activity_type',
                'verbose_name_plural': 'activities_type',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ManyToManyField(default=None, to='core.Type'),
        ),
        migrations.AddField(
            model_name='activity',
            name='age_interval',
            field=models.ManyToManyField(default=None, to='core.ActivityAgeInterval'),
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ManyToManyField(default=None, to='core.Category'),
        ),
        migrations.AddField(
            model_name='activity',
            name='location_tags',
            field=models.ManyToManyField(default=None, to='core.ActivityLocation'),
        ),
        migrations.AddField(
            model_name='activity',
            name='supplier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Supplier'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]