# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci', '0018_testjob_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='implementation_type',
            field=models.CharField(choices=[('fake', 'fake'), ('lava', 'lava'), ('null', 'null')], default='null', max_length=64),
        ),
    ]
