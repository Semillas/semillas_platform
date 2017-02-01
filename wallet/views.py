# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from django.db.models import Q

from semillas_backend.users.models import User
from .models import Wallet, Transaction
from .serializers import WalletSerializer, CreateTransactionSerializer

class UserWalletDetail(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'owner__uuid'
    lookup_url_kwarg = 'owner_uuid'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        serializer_context = {
            'owner_uuid': self.owner_uuid
        }
        context.update(serializer_context)
        return context

    def get(self, request, owner_uuid, format=None):
        self.owner_uuid = owner_uuid
        return super(UserWalletDetail, self).get(request, owner_uuid, format)

class CreateTransaction(generics.CreateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    queryset = Transaction.objects.all()
    serializer_class = CreateTransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)
