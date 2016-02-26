# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^(?P<slug>[\w-]+)$',
        view=views.CategoryDetailView.as_view(),
        name='detail'
    ), url(
        regex=r'^$',
        view=views.CategoryListView.as_view(),
        name='list'
    ),
]
