# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

import datetime
from decimal import Decimal

# Django imports
from django.conf import settings
from django.core.management.base import BaseCommand

from allauth.socialaccount.providers import registry
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.oauth.provider import OAuthProvider
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = "This command will create dummy tokens for OAuth based providers of `allauth`"

    def handle(self, *args, **kwargs):
        site = Site.objects.get_current()
        for provider in registry.get_list():
            if (isinstance(provider, OAuth2Provider) or
                isinstance(provider, OAuthProvider)):
                try:
                    SocialApp.objects.get(provider=provider.id,
                                          sites=site)
                except SocialApp.DoesNotExist:
                    print ("Installing dummy application credentials for %s."
                           " Authentication via this provider will not work"
                           " until you configure proper credentials via the"
                           " Django admin (`SocialApp` models)" % provider.id)
                    app = SocialApp.objects.create(
                        provider=provider.id,
                        secret='secret',
                        client_id='client-id',
                        name='Dummy %s app' % provider.id)
                    app.sites.add(site)
