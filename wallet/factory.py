# -*- coding: utf-8 -*-

import factory
import faker
import datetime

from django.conf import settings

from .models import Wallet, Transaction
from semillas_backend.users.models import User

faker = faker.Factory.create()


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    owner = factory.Iterator(User.objects.all())
    balance = 10

class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    wallet_source = factory.Iterator(Wallet.objects.all())
    balance_source = 0
    wallet_dst = factory.Iterator(Wallet.objects.all())
    balance_dst = 0
    value = factory.Faker('pyint')

