# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from services.views import UserServiceList

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^all_users$',
        view=views.UserList.as_view(),
        name='list'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<uuid>[^/]+)/$',
        view=views.UserDetail.as_view(),
        name='detail'
    ),
    # URL pattern for the UserServiceList
    url(
        regex=r'^(?P<user_uuid>[^/]+)/services$',
        view=UserServiceList.as_view(),
        name='list'
    ),

    url(
        regex=r'^update/(?P<uuid>[^/]+)/$',
        view=views.UserDetailUpdate.as_view(),
        name='update'
    ),
]
