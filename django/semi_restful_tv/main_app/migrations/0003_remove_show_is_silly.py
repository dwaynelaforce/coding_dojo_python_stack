# Generated by Django 2.2 on 2020-11-09 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201108_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='is_silly',
        ),
    ]