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

    owner = factory.Iterator(User.objects.all())
    balance = 10

