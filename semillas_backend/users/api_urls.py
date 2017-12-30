# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import re_path
from services.views import UserServiceList

from . import views

app_name = 'users'

urlpatterns = [
    # re_path pattern for the UserListView
    re_path(
        route=r'^$',
        view=views.UserList.as_view(),
        name='search'
    ),

    # re_path pattern for the UserDetailView
    re_path(
        route=r'^(?P<uuid>[^/]+)/$',
        view=views.UserDetail.as_view(),
        name='detail'
    ),
    # re_path pattern for the UserServiceList
    re_path(
        route=r'^(?P<user_uuid>[^/]+)/services$',
        view=UserServiceList.as_view(),
        name='list'
    ),

    re_path(
        route=r'^update/(?P<uuid>[^/]+)/$',
        view=views.UserDetailUpdate.as_view(),
        name='update'
    ),
]
