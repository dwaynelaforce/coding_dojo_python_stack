# Generated by Django 2.2 on 2020-11-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201104_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='None', max_length=255),
            preserve_default=False,
        ),
    ]
