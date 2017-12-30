# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

app_name = 'services'

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
    url(
        regex=r'^edit/(?P<uuid>[^/]+)/$',
        view=views.UpdateService.as_view(),
        name='edit'
    ),
    # URL pattern for the ServiceDetailView --> Get Services by Category
    url(
        regex=r'^feed$',
        view=views.FeedServiceList.as_view(),
        name='feed'
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
    # URL pattern for upload service photo
    url(
        regex=r'^photo_upload/(?P<uuid>[^/]+)/$',
        view=views.ServicePhotoUpload.as_view(),
        name='post_photo'
    ),
    url(
        regex=r'^delete/(?P<uuid>[^/]+)/$',
        view=views.ServiceDelete.as_view(),
        name='delete'
    ),
    url(
        regex=r'^photo/delete/(?P<id>[^/]+)/$',
        view=views.ServicePhotoDelete.as_view(),
        name='photo_delete'
    ),
]
