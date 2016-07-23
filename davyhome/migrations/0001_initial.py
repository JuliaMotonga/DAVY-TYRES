# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalogue_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('max_price', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='SaleValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tyre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=50)),
                ('width', models.CharField(max_length=50)),
                ('profile', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('speed', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.ForeignKey(related_name='tyre_price_range', to='davyhome.PriceRange')),
                ('sale', models.ForeignKey(related_name='tyre_sale_item', default=None, blank=True, to='davyhome.SaleValue', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='catalogue',
            name='tyres',
            field=models.ManyToManyField(default=None, to='davyhome.Tyre', blank=True),
        ),
    ]
