# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20170220_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='balance_dest',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Value of the wallet at the time of this transaction', max_digits=6),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='balance_source',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Value of the wallet at the time of this transaction', max_digits=6),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='value',
            field=models.DecimalField(decimal_places=2, help_text='Value of the tansaction', max_digits=6),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, help_text='Available seeds in wallet', max_digits=6),
        ),
    ]
