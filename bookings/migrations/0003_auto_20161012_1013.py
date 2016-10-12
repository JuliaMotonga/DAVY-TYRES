# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20160918_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='Confirmed', max_length=100, choices=[('CF', 'Confirmed'), ('CM', 'Completed'), ('UF', 'Unfulfilled'), ('CN', 'Canceled')]),
        ),
    ]
