# -*- coding: utf-8 -*-

import factory
import faker

from .models import Wallet, Transaction
from django.conf import settings

faker = faker.Factory.create()

class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    balance = settings.WALLET_INITIAL_AMOUNT

class TransactionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Transaction

    wallet_source = factory.Iterator(Wallet.objects.all())
    balance_source = 0
    wallet_dest = factory.Iterator(Wallet.objects.all())
    balance_dest = 0
    value = factory.Faker('pyint')
