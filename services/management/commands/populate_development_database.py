# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

import datetime
from decimal import Decimal

# Django imports
from django.conf import settings
from django.core.management.base import BaseCommand

from semillas_backend.users.factory import UserFactory
from services.factory import ServiceFactory, CategoryFactory
from services.factory import categories
from wallet.factory import WalletFactory
from semillas_backend.users.models import User

class Command(BaseCommand):
    help = "This command will create some users and some services for development purpose"

    def handle(self, *args, **kwargs):
        UserFactory.create_batch(size=10)
				# CategoryFactory.create_batch(size=20)
        for i in range(len(categories)):
            CategoryFactory(name=categories[i],order=i)
        ServiceFactory.create_batch(size=50)

        WalletFactory.create_batch(size=User.objects.count())

