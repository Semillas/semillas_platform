# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ServiceListView
    url(
        regex=r'^$',
        view=views.ServiceList.as_view(),
        name='list'
    ),

    # URL pattern for the ServiceDetailView
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.ServiceDetail.as_view(),
        name='detail'
    ),


]
