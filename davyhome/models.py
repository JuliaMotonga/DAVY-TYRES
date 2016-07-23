from __future__ import unicode_literals
from django.db import models


class PriceRange(models.Model):
    min_price = models.DecimalField(max_digits=7, decimal_places=2)
    max_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return "{} - {}".format(self.min_price, self.max_price)


class SaleValue(models.Model):
    percentage = models.IntegerField()

    def __unicode__(self):
        return "{}".format(self.percentage)


class Tyre(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.ForeignKey(PriceRange, related_name='tyre_price_range', on_delete=models.CASCADE)
    width = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    sale = models.ForeignKey(SaleValue, related_name='tyre_sale_item', on_delete=models.CASCADE, null=True, blank=True,
                             default=None)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.product_name


class Catalogue(models.Model):
    catalogue_name = models.CharField(max_length=50)
    tyres = models.ManyToManyField(Tyre, blank=True, default=None)

    def __unicode__(self):
        return self.catalogue_name
