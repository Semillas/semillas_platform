# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

import datetime
from decimal import Decimal
from random import randint

# Django imports
from django.conf import settings
from django.core.management.base import BaseCommand

from semillas_backend.users.factory import UserFactory
from semillas_backend.users.models import User

from services.factory import ServiceFactory, CategoryFactory
from services.factory import categories
from services.models import Category

from wallet.factory import WalletFactory
from wallet import models

from faker import Factory

class Command(BaseCommand):
    help = "This command will create some users and some services for development purpose"
    fake = Factory.create()

    def handle(self, *args, **kwargs):
        UserFactory.create_batch(size=10)
        # CategoryFactory.create_batch(size=20)

        Category.objects.all().delete()
        for i in range(len(categories)):
            CategoryFactory(name=categories[i],order=i)
        ServiceFactory.create_batch(size=50)

        #WalletFactory.create_batch(size=User.objects.count())

        # Create transactions
        count = Wallet.objects.count()
        random_index = randint(0, count - 1)
        for wallet in Wallet.objects.all():
            for i in range(4):
                random_index = randint(0, count - 2)
                dst_wallet = Wallet.objects.exclude(id=wallet.id)[random_index]
                val=randint(1, 2)
                new_transaction = Transaction.objects.create(
                    value=val,
                    wallet_dest=dst_wallet,
                    wallet_source=wallet,
                    balance_dest=dst_wallet.balance + val,
                    balance_source=wallet.balance - val,
                )
                new_transaction.save()
                wallet.balance-=val
                wallet.save()
                dst_wallet.balance+=val
                dst_wallet.save()