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
		regex=r'^owner/(?P<owner_uuid>[^/]+)/$',
		view=views.UserWalletDetail.as_view(),
		name='list'
	),
	url(
		regex=r'^(?P<uuid>[^/]+)/$',
		view=views.WalletDetail.as_view(),
		name='detail'
	),
	url(
		regex=r'^owner/(?P<owner_uuid>[0-9]+)/transactions/$',
		view=views.UserTransactionsList.as_view(),
		name='list'
	),
	url(
		regex=r'^transactions/(?P<id>[0-9]+)/$',
		view=views.TransactionDetail.as_view(),
		name='detail'
	),
]
