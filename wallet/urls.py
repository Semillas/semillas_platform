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
		regex=r'^(?P<owner_uuid>[^/]+)/$',
		view=views.UserWalletDetail.as_view(),
		name='list'
	),
	url(
		regex=r'^(?P<uuid>[^/]+)/$',
		view=views.WalletDetail.as_view(),
		name='detail'
	),
	url(
		regex=r'^(?P<user_id>[0-9]+)/transactions/$',
		view=views.UserTransactionsList.as_view(),
		name='list'
	),
	url(
		regex=r'^(?P<id_wallet>[0-9]+)/transactions/(?P<id_trans>[0-9]+)/$',
		view=views.UserTransactionDetail.as_view(),
		name='detail'
	),
]
