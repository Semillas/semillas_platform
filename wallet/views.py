# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from rest_framework import permissions

from .models import Wallet, Transaction, NegativeAmount
from .serializers import WalletSerializer


class WalletDetailView(LoginRequiredMixin, DetailView):
    model = Wallet
    slug_field = 'wallet.pk'
    # slug_url_kwarg = ''


class WalletRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('Wallets:detail',
                       kwargs={'Wallet': self.request.Wallet.pk})


class WalletUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['seeds', ]
    model = Wallet

    def get_success_url(self):
        return reverse('Wallets:detail',
                       kwargs={'Wallet': self.request.Wallet.pk})

    def get_object(self):
        return Wallet.objects.get(Wallet=self.request.Wallet.pk)


class WalletListView(LoginRequiredMixin, ListView):
    model = Wallet
    # These next two lines tell the view to index lookups by wallet
    slug_field = 'wallet.pk'
    slug_url_kwarg = 'wallet.pk'


class WalletList(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WalletDetail(generics.RetrieveUpdateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/Wallet/2/
    """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (permissions.IsAuthenticated,)
