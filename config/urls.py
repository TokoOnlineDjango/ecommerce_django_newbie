# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    url(
        r'^$',
        include('toko.apps.pages.urls', namespace="pages")
    ),
    url(
        r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'), name="about",
    ),
    url(
        r'^accounts/',
        include('allauth.urls')
    ),
    url(
        r'^products/',
        include('toko.apps.products.urls', namespace="products")
    ),
    url(
        r'^categories/',
        include('toko.apps.categories.urls', namespace="categories")
    ),
    url(
        r'^users/',
        include("toko.apps.users.urls", namespace="users")
    ),
    url(
        r'^ckeditor/',
        include('ckeditor_uploader.urls', namespace="ckedior")
    ),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(
            r'^400/$',
            default_views.bad_request,
            kwargs={'exception': Exception("Bad Request!")}
        ),
        url(
            r'^403/$',
            default_views.permission_denied,
            kwargs={'exception': Exception("Permissin Denied")}
        ),
        url(
            r'^404/$',
            default_views.page_not_found,
            kwargs={'exception': Exception("Page not Found")}
        ),
        url(
            r'^500/$',
            default_views.server_error
        ),
    ]
