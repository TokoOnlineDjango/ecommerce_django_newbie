from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

# Create your models here.

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = RichTextField()
    prices = models.DecimalField(decimal_places=2, max_digits=1000)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:details', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "%s" % self.title


class ProductVariation(models.Model):
    title = models.CharField(max_length=120)
    product = models.ForeignKey(Product)
    stock = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    prices = models.DecimalField(decimal_places=2, max_digits=1000)

    def get_absolute_url(self):
        return self.product.get_absolute_url

    def __unicode__(self):
        return '%s'% self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='product/')



def product_post_save_recivers(sender, instance, created ,*args, **kwrgs):
    product = instance
    obj = product.productvariation_set.all()
    if obj.count() == 0:
        new_var = ProductVariation()
        new_var.title = 'Variation not Avaible'
        new_var.product = product
        new_var.prices = product.prices
        new_var.save()

post_save.connect(product_post_save_recivers, sender=Product)
