# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20161012_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='CF', max_length=100, choices=[('CF', 'Confirmed'), ('CM', 'Completed'), ('UF', 'Unfulfilled'), ('CN', 'Canceled')]),
        ),
    ]
