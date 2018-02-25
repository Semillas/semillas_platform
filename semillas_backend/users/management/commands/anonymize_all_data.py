# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from factory import Faker

# Django imports
from django.conf import settings
from django.core.management.base import BaseCommand

from semillas_backend.users.models import User



class Command(BaseCommand):
    help = "This command will create dummy tokens for OAuth based providers of `allauth`"

    def handle(self, *args, **kwargs):
        faker = Faker('email')
        for user in User.objects.filter(is_superuser=False):
            user.email = faker.generate('')
            user.telegram_id = ''
            user.phone = ''
            user.save()

