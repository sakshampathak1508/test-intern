# Generated by Django 3.2.11 on 2022-01-13 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='hours',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='menu.hour'),
            preserve_default=False,
        ),
    ]