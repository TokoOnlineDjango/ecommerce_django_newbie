from __future__ import unicode_literals

from ckeditor.fields import RichTextField

from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.db import models
from django.dispatch.dispatcher import receiver

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer

from toko.core.utils import FilenameGenerator


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()

    def get_related(self, instance):
        return self.get_queryset().filter(categories__in=instance.categories.all())


class Product(TimeStampedModel):
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name', unique=True, overwrite=False)
    description = RichTextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey('users.User', related_name='products',
                                   blank=True, null=True)
    price = models.DecimalField(validators=[MinValueValidator(0)], blank=True,
                                null=True, decimal_places=2, max_digits=1000)
    categories = models.ManyToManyField('products.Category',
                                        related_name='products',
                                        blank=True, null=True)
    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def get_image_detail_url(self):
        crop_photo = {'size': (50, 50), 'crop': True}
        photos = get_thumbnailer(self.photos.first().image).get_thumbnail(crop_photo).url
        return photos

    def get_image_list_url(self):
        crop_photo = {'size': (306, 160), 'crop': True}
        photos = get_thumbnailer(self.photos.first().image).get_thumbnail(crop_photo).url
        return photos

    def __unicode__(self):
        return u"%s" % self.name


class ProductVariation(models.Model):
    name = models.CharField(max_length=120)
    product = models.ForeignKey('products.Product', related_name='variations')
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(validators=[MinValueValidator(0)], blank=True,
                                null=True, decimal_places=2, max_digits=1000)

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def __unicode__(self):
        return u"%s" % self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, overwrite=False)
    description = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey('users.User', related_name='product_categories',
                                   blank=True, null=True)

    def get_absolute_url(self):
        return reverse('categories:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return u"%s" % self.name


class PhotoFeatured(TimeStampedModel):
    product = models.ForeignKey('products.ProductFeatured', related_name='photos')
    image = ThumbnailerImageField(upload_to=FilenameGenerator('products/featured'))
    created_by = models.ForeignKey('users.User', related_name='photos_featured',
                                   blank=True, null=True)


class ProductFeatured(TimeStampedModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey('products.Product',
                                related_name='products')
    text = RichTextField(blank=True, null=True)
    show_price = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def get_image_featured_url(self):
        crop_photo = {'size': (306, 160), 'crop': True}
        photos = get_thumbnailer(self.photos.first().image).get_thumbnail(crop_photo).url
        return photos

    def __unicode__(self):
        return u"%s" % self.product.name


class Photo(TimeStampedModel):
    product = models.ForeignKey('products.Product', related_name='photos')
    image = ThumbnailerImageField(upload_to=FilenameGenerator('products'))
    created_by = models.ForeignKey('users.User', related_name='product_photos',
                                   blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.image


@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        image = get_thumbnailer(instance.image)
        image.delete(save=False)


@receiver(models.signals.post_delete, sender=PhotoFeatured)
def auto_delete_image_featured_on_delete(sender, instance, **kwargs):
    if instance.image:
        image = get_thumbnailer(instance.image)
        image.delete(save=False)
