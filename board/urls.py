# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ServiceListView
    url(
        regex=r'^$',
        view=views.ServiceListView.as_view(),
        name='list'
    ),

    # URL pattern for the ServiceRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.ServiceRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the ServiceDetailView
    url(
        regex=r'^(?P<Servicename>[\w.@+-]+)/$',
        view=views.ServiceDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the ServiceUpdateView
    url(
        regex=r'^~update/$',
        view=views.ServiceUpdateView.as_view(),
        name='update'
    ),
]
