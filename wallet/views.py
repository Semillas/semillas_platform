# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from django.db.models import Q

from semillas_backend.users.models import User
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer

class WalletList(generics.ListAPIView):
	queryset = Wallet.objects.all()
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)

class UserWalletDetail(generics.ListAPIView):
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		if 'owner_uuid' in self.kwargs:
			pk = self.kwargs['owner_uuid']
			u=User.objects.get(uuid=pk)
			if u:
				return Wallet.objects.filter(owner=u)
		else:
			return Wallet.objects.all()

class WalletDetail(generics.RetrieveUpdateAPIView):
	queryset = Wallet.objects.all()
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)
	lookup_field = 'uuid'

class UserTransactionsList(generics.ListAPIView):
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)
	def get_queryset(self):
		if 'owner_uuid' in self.kwargs:
			pk = self.kwargs['owner_uuid']
			u=User.objects.get(uuid=pk)
			if u:
				return Transaction.objects.filter(Q(wallet_source__owner=u)|Q(wallet_dest__owner=u))
		else:
			return Transaction.objects.all()

class TransactionDetail(generics.RetrieveUpdateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = (permissions.IsAuthenticated,)
	lookup_field = 'id'
