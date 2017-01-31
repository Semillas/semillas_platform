# -*- coding: utf-8 -*-

import factory
import faker
import datetime

from django.conf import settings

from .models import Wallet
from semillas_backend.users.models import User

faker = faker.Factory.create()


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet
    
    balance = 0

class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    wallet_source = factory.Iterator(Wallet.objects.all())
    balance_source = 0
    wallet_dest = factory.Iterator(Wallet.objects.all())
    balance_dest = 0
    value = factory.Faker('pyint')