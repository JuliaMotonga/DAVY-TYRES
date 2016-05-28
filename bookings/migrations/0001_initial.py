# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityCalender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking_time', models.DateTimeField()),
                ('status', models.CharField(default=('CF', 'Confirmed'), max_length=20, choices=[('CF', 'Confirmed'), ('CM', 'Completed'), ('UF', 'Unfulfilled'), ('CN', 'Canceled')])),
                ('additional_information', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('cost', models.DecimalField(max_digits=6, decimal_places=2)),
                ('description', models.TextField()),
                ('availability', models.ForeignKey(to='bookings.AvailabilityCalender')),
            ],
        ),
        migrations.CreateModel(
            name='TimeRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='time_allocated',
            field=models.ForeignKey(to='bookings.TimeRange'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(to='bookings.Customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(to='bookings.Service'),
        ),
        migrations.AddField(
            model_name='booking',
            name='service_employee',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='availabilitycalender',
            name='friday',
            field=models.ForeignKey(related_name='friday_time_range', to='bookings.TimeRange'),
        ),
        migrations.AddField(
            model_name='availabilitycalender',
            name='monday',
            field=models.ForeignKey(related_name='monday_time_range', to='bookings.TimeRange'),
        ),
        migrations.AddField(
            model_name='availabilitycalender',
            name='saturday',
            field=models.ForeignKey(related_name='saturday_time_range', to='bookings.TimeRange'),
        ),
        migrations.AddField(
            model_name='availabilitycalender',
            name='sunday',
            field=models.ForeignKey(related_name='sunday_time_range', to='bookings.TimeRange'),
        ),
        migrations.AddField(
            model_name='availabilitycalender',
            name='thursday',
            field=models.ForeignKey(related_name='thursday_time_range', to='bookings.TimeRange'),
        ),
        migrations.AddField(
            model_name='availabilitycalender',
            name='tuesday',
            field=models.ForeignKey(related_name='tuesday_time_range', to='bookings.TimeRange'),
        ),
        migrations.AddField(
            model_name='availabilitycalender',
            name='wednesday',
            field=models.ForeignKey(related_name='wednesday_time_range', to='bookings.TimeRange'),
        ),
    ]
