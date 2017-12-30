# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

app_name = 'wallet'

urlpatterns = [
	# URL pattern for the ServiceListView
	url(
		regex=r'^owner/(?P<owner_uuid>[^/]+)/$',
		view=views.UserWalletDetail.as_view(),
		name='list'
	),
	url(
        regex=r'^transactions/create/$',
        view=views.CreateTransaction.as_view(),
        name='create'
    ),
]
