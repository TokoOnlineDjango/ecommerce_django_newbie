# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^(?P<slug>[\w-]+)$',
        view=views.ProductDetailView.as_view(),
        name='detail'
    ), url(
        regex=r'^$',
        view=views.ProductListlView.as_view(),
        name='list'
    ),
]
