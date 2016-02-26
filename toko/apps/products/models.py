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

    def featured(self):
        return self.filter(is_featured=True).active()


class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return self.active()


class Product(TimeStampedModel):
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name', unique=True, overwrite=False)
    description = RichTextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_by = models.ForeignKey('users.User', related_name='products',
                                   blank=True, null=True, editable=False)
    price = models.DecimalField(validators=[MinValueValidator(0)], blank=True,
                                null=True, decimal_places=2, max_digits=1000)
    categories = models.ManyToManyField('categories.Category', blank=True,
                                        related_name='products')
    objects = ProductManager.from_queryset(ProductQuerySet)()

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def get_related(self):
        return Product.objects.prefetch_related('photos') \
            .filter(categories__in=self.categories.all()) \
            .exclude(id=self.id).distinct()

    @property
    def primary_image(self):
        photo = sorted(self.photos.all(), key=lambda x: x.id)
        return photo[0].image if photo else None


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


class Photo(TimeStampedModel):
    product = models.ForeignKey('products.Product', related_name='photos')
    image = ThumbnailerImageField(upload_to=FilenameGenerator('products'))
    created_by = models.ForeignKey('users.User', related_name='product_photos',
                                   blank=True, null=True, editable=False)

    def __unicode__(self):
        return u"%s" % self.image


@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        image = get_thumbnailer(instance.image)
        image.delete(save=False)
