# Generated by Django 2.2 on 2019-04-09 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0003_auto_20190409_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endDate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]