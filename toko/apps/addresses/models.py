from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel
from ckeditor.fields import RichTextField

from toko.core.validators import validate_mobile_phone


class Province(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.name


class City(TimeStampedModel):
    province = models.ForeignKey('addresses.Province', related_name='cities')
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'cities'

    def __unicode__(self):
        return u"%s" % self.name


class SubDistrict(TimeStampedModel):
    city = models.ForeignKey('addresses.City', related_name='sub_districts')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.name


class Village(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.name


class AddressBook(TimeStampedModel):
    user = models.ForeignKey('users.User', related_name='addresses')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, validators=[validate_mobile_phone])
    address = RichTextField()
    sub_district = models.ForeignKey('addresses.SubDistrict', related_name='addresses')
    village = models.ForeignKey('addresses.Village', related_name='addresses',
                                blank=True, null=True)
    postal_code = models.PositiveIntegerField(max_length=5)

    def __unicode__(self):
        return u"%s" % self.name
