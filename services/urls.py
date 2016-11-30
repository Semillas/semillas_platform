# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ServiceListView
    url(
        regex=r'^all_services$',
        view=views.ServiceList.as_view(),
        name='list'
    ),
    # URL pattern for the ServiceDetailView
    url(
        regex=r'^(?P<uuid>[^/]+)/$',
        view=views.ServiceDetail.as_view(),
        name='detail'
    ),
    # URL pattern for the ServiceDetailView --> Get Services by Category
    url(
        regex=r'^feed$',
        view=views.CategoryServiceList.as_view(),
        name='detail'
    ),
    # URL pattern for the CategoryListView
    url(
        regex=r'^categories$',
        view=views.CategoryList.as_view(),
        name='list'
    ),
    # URL pattern for the CreateService
    url(
        regex=r'^$',
        view=views.CreateService.as_view(),
        name='create'
    ),
]
