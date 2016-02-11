from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self,*args, **kwargs):
        return self.get_queryset().active()




class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    prices = models.DecimalField(decimal_places= 2, max_digits=1000 )
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('product_details', kwargs={"pk":self.pk})

    def __unicode__(self):
        return "%s"%self.title
