# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_timerange_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='registration_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
