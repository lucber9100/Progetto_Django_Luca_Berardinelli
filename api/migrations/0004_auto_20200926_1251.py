# Generated by Django 3.1.1 on 2020-09-26 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200922_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
