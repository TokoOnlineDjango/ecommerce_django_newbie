# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.ProductDetailView.as_view(),
        name='details'
    ),  url(
        regex=r'^',
        view=views.ProductListlView.as_view(),
        name='list'
    ),
    # url(
    #     regex=r'^(?P<id>\d+)',
    #     view=views.product_detail_view_function,
    #     name='product_details_function'
    # ),

]
