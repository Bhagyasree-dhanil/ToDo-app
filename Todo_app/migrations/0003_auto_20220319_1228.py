# Generated by Django 3.2.7 on 2022-03-19 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0002_todo_db_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_db',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo_db',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 6, 58, 0, 570122, tzinfo=utc)),
        ),
    ]
