# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(null=True),
        ),
    ]
