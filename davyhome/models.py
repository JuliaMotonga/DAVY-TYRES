from __future__ import unicode_literals

from django.db import models


class Catalogue(models.Model):
    catalogue_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.catalogue_name

