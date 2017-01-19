# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from semillas_backend.users.models import User
from .models import Wallet
from .serializers import WalletSerializer, CreateWalletSerializer

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

    



