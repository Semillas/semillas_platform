# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
from uuid import uuid4

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


@python_2_unicode_compatible
class Wallet(models.Model):
    """
    Represents an advert of a user on the platform. Its intended to be
    exchangeable for seeds and mainly geolocated oriented (TODOs!)
    """
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wallet',
    )

    balance = models.PositiveIntegerField(
        help_text="Available seeds in wallet",
        null=False,
        blank=False,
    )

    last_updated = models.DateTimeField(
        auto_now_add=True, 
    )


    def get_absolute_url(self):
        return reverse('api_wallet:detail', kwargs={'pk': self.id})

class Transaction(models.Model):
    # The wallet that holds this transaction.
    wallet = models.ForeignKey(
        Wallet,
        related_name='transactions',
    )

    # The value of this transaction.
    value = models.PositiveIntegerField(
        help_text="Value of the tansaction",
        null=False,
        blank=False,
    )

    # The value of the wallet at the time of this
    # transaction. Useful for displaying transaction
    # history.
    running_balance = models.PositiveIntegerField(
        help_text="Value of the wallet at the time of this transaction",
        null=False,
        blank=False,
    )

    # The date/time of the creation of this transaction.
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
