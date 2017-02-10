# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .models import Wallet

from .serializers import WalletSerializer, CreateTransactionSerializer

from .errors import InsufficientBalance

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

class CreateTransaction(APIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    serializer_class = CreateTransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # import ipdb;ipdb.set_trace()
        if request.data['wallet_source']!=request.data['wallet_dest']:
            if request.data['value'] == "":
                return Response("Value can't be empty", status=status.HTTP_400_BAD_REQUEST)
            wallet_src = Wallet.objects.get(id=request.data['wallet_source'])
            destination_wallet = Wallet.objects.get(id=request.data['wallet_dest'])
            try:
                trans = wallet_src.transfer(destination_wallet, int(request.data['value']))
                # import ipdb;ipdb.set_trace()
                if trans:
                    return Response("Transaction created correctly!", status=status.HTTP_201_CREATED)
                return Response("The transaction was not created correctly!", status=status.HTTP_400_BAD_REQUEST)
            except InsufficientBalance:
                return Response("The Source wallet does not contain enough balance", status=status.HTTP_400_BAD_REQUEST)
        return Response("Source and destination wallets can not be the same!", status=status.HTTP_400_BAD_REQUEST)
