# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from semillas_backend.users.models import User
from .models import Wallet
from .serializers import WalletSerializer, CreateWalletSerializer

class UserWalletDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
    



