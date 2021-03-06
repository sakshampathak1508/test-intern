# Generated by Django 3.2.11 on 2022-01-13 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='', max_length=10)),
                ('open_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('close_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('res_type', models.CharField(default='', max_length=256)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
    ]
