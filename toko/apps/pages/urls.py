from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [

    # url(r'^$', 'toko.apps.pages.views.home', name='home'),
    url(regex=r'^$', view=views.HomeView.as_view(), name='home'),


]
