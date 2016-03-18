from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel

class ChartItem(TimeStampedModel):
    chart = models.ForeignKey('charts.Chart', blank=True, null=True)
    item = models.ForeignKey('products.ProductVariation', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u"%s" % self.item.name


class Chart(TimeStampedModel):
    user = models.ForeignKey('users.User', related_name='user_chart',
                             blank=True, null=True)
    items = models.ManyToManyField('products.ProductVariation',
                                   through='charts.ChartItem',
                                   related_name='chart')

    def __unicode__(self):
        return str(self.id)
