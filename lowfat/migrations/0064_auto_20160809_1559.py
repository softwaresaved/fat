# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-09 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0063_auto_20160809_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='status',
            field=models.CharField(choices=[('W', 'Not submitted yet'), ('S', 'Submitted (awaiting processing)'), ('C', 'Administrator checking'), ('P', 'Authoriser checking'), ('A', 'Approved (submitted to finance)'), ('F', 'Finished')], default='P', max_length=1),
        ),
    ]
