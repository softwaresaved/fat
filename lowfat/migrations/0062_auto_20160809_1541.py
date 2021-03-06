# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0061_auto_20160809_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='event',
            new_name='fund',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='event',
            new_name='fund',
        ),
        migrations.AlterField(
            model_name='blog',
            name='final',
            field=models.BooleanField(default=False, help_text='This is your last blog post about the fund'),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_approved',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In £', max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_attendance_fees',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In £', max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_catering',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In £', max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_others',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In £', max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_subsistence_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In £', max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_travel',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In £', max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_venue_hire',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In £', max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('A', 'Attending a conference/workshop'), ('H', 'Organising a conference/workshop (e.g. Software Carpentry)'), ('P', 'Policy related fund'), ('O', 'Other')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='expense',
            name='final',
            field=models.BooleanField(default=False, help_text='This is your last expense claim for the fund'),
        ),
    ]
