from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

# Create your models here.
from django.core.validators import MinValueValidator

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from easy_thumbnails.fields import ThumbnailerImageField

from toko.core.utils import FilenameGenerator


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()


class Product(TimeStampedModel):
    name = models.CharField(max_length=120)
    description = RichTextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey('users.User', related_name='products',
                                   blank=True, null=True)
    category = models.ForeignKey('products.Category', related_name='products',
                                 blank=True, null=True)
    price = models.DecimalField(validators=[MinValueValidator(0)], blank=True,
                                null=True, decimal_places=2, max_digits=1000)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return u"%s" % self.name


class ProductVariation(models.Model):
    name = models.CharField(max_length=120)
    product = models.ForeignKey('products.Product', related_name = 'variations')
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(validators=[MinValueValidator(0)],blank = True,
                                null=True, decimal_places=2, max_digits=1000)

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def __unicode__(self):
        return u"%s" % self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, overwrite=False)
    created_by = models.ForeignKey('users.User', related_name='product_categories',
                                   blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class Photo(TimeStampedModel):
    product = models.ForeignKey('products.Product', related_name='photos')
    image = ThumbnailerImageField(upload_to=FilenameGenerator('products'))
    created_by = models.ForeignKey('users.User', related_name='product_photos',
                                   blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.image