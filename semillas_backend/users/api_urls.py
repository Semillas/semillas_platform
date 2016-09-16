# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

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
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.UserDetail.as_view(),
        name='detail'
    ),


]
