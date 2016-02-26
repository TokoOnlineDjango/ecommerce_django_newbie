from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, overwrite=False)
    description = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey('users.User', blank=True, null=True,
                                   related_name='categories')

    def get_absolute_url(self):
        return reverse('categories:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return u"%s" % self.name
