# Generated by Django 2.2 on 2019-04-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='endTime',
        ),
        migrations.RemoveField(
            model_name='event',
            name='startTime',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
