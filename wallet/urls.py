# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ServiceListView
    url(
        regex=r'^all_wallets$',
        view=views.WalletList.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<owner__uuid>[^/]+)/$',
        view=views.WalletDetail.as_view(),
        name='detail'
    ),
]
