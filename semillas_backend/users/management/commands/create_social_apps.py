# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

import datetime
from decimal import Decimal

# Django imports
from django.conf import settings
from django.core.management.base import BaseCommand

from allauth.socialaccount.models import SocialApp

class Command(BaseCommand):
    help = "This command will create some users and some services for development purpose"

    def handle(self, *args, **kwargs):
        # If SocialApp created at all, create some
        #if not SocialApp.objects.all():
        print("Aquí vamos!!!")
