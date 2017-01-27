# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from django.db.models import Q

from semillas_backend.users.models import User
from .models import Wallet, Transaction
from .serializers import WalletSerializer, CreateWalletSerializer, TransactionSerializer

class UserWalletDetail(generics.RetrieveUpdateAPIView):
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)

class WalletDetail(generics.RetrieveUpdateAPIView):
	queryset = Wallet.objects.all()
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)
	lookup_field = 'uuid'

class WalletList(generics.ListAPIView):
	queryset = Wallet.objects.all()
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)

class UserTransactionDetail(generics.ListAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = (permissions.IsAuthenticated,)

class UserTransactionsList(generics.RetrieveUpdateAPIView):
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)
	def get_queryset(self):
		if 'user_id' in self.kwargs:
			pk = self.kwargs['user_id']
			u=User.objects.get(uuid=pk)
			if u:
				return Transaction.objects.filter(Q(wallet_source__owner=u.id)|Q(wallet_dest__owner=u.id))
		else:
			return Transaction.objects.all()

class WalletList(generics.ListAPIView):
	queryset = Wallet.objects.all()
	serializer_class = WalletSerializer
	permission_classes = (permissions.IsAuthenticated,)



    



