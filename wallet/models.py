# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from uuid import uuid4

from django.urls import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import get_template

from allauth.account.signals import user_logged_in

from .errors import InsufficientBalance
from django.conf import settings


@python_2_unicode_compatible
class Wallet(models.Model):
    """
    Represents an advert of a user on the platform. Its intended to be
    exchangeable for seeds and mainly geolocated oriented (TODOs!)
    """
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wallet',
    )

    balance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Available seeds in wallet",
        null=False,
        blank=False,
    )

    last_updated = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.id)+" - "+self.owner.name+" - Balance: "+ str(self.balance)

    @property
    def transactions(self):
        return self.transactions_outbound.all() | self.transactions_inbound.all()

    def get_absolute_url(self):
        return reverse('api_wallet:detail', kwargs={'pk': self.id})

    def __deposit(self, value, transaction):
        """Deposits a value to the wallet. Also updates the transaction
        balance_dest field
        """
        # Save source values on transaction
        transaction.balance_dest=self.balance + value
        transaction.wallet_dest=self
        # Save values on wallet
        self.balance += value
        self.save()

    def __withdraw(self, value, transaction):
        """Withdraw's a value from the wallet.
        Should the withdrawn amount is greater than the
        balance this wallet currently has, it raises an
        :mod:`InsufficientBalance` error. This exception
        inherits from :mod:`django.db.IntegrityError`. So
        that it automatically rolls-back during a
        transaction lifecycle.
        """
        if (self.balance - value) < settings.WALLET_MINIMUM_AMOUNT:
            raise InsufficientBalance('The balance cannot go below {minimum}.'.format(
                minimum=settings.WALLET_MINIMUM_AMOUNT))
        # Save source values on transaction
        transaction.wallet_source=self
        transaction.balance_source = self.balance - value
        # Save values on wallet
        self.balance -= value
        self.save()

    def notify_transaction(self, value, destination_wallet):
        """ TODO: This should be taken off-line
        """

        # Send Transaction Email to recipient
        send_mail(
            _('You just received a transaction'),
             _("You just received {amount} {currency} from {sender}").format(
                amount=str(value),
                currency=settings.CURRENCY_NAME,
                sender=self.owner.name,
                ),
            'noresponse@semillasocial.org',
            [destination_wallet.owner.email],
            fail_silently=True
        )

        # Send Transaction Email to sender
        send_mail(
            _('You just send a transaction'),
            _("You just sent {amount} {currency} to {recipient}").format(
                amount=str(value),
                currency=settings.CURRENCY_NAME,
                recipient=destination_wallet.owner.name,
                ),
            'noresponse@semillasocial.org',
            [self.owner.email],
            fail_silently=True
        )

    def transfer(self, destination_wallet, value):
        """Transfers an value to another wallet.
        Uses `deposit` and `withdraw` internally.
        Creates the transaction record and links it to
        the 2 wallets (source and destination wallets)
        """
        transaction = Transaction(
            value=value,
            wallet_dest=destination_wallet,
            wallet_source=self,
            balance_dest=0,
            balance_source=0,
        )

        self.__withdraw(value, transaction)
        destination_wallet.__deposit(value, transaction)
        transaction.save()

        # If no exception raised we must have reached here.
        self.notify_transaction(value, destination_wallet)

        return transaction

class Transaction(models.Model):
    """Referes to the wallet owned by the user
    that is paying for the service"""

    wallet_source = models.ForeignKey(
        Wallet,
        related_name='transactions_outbound',
        blank=True,
        default=0,
        on_delete=models.CASCADE,
    )

    """Referes to the wallet owned by the user
    that is offering for the service"""
    wallet_dest = models.ForeignKey(
        Wallet,
        related_name='transactions_inbound',
        default=0,
        on_delete=models.CASCADE,
    )

    # The value of this transaction.
    value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Value of the tansaction",
        null=False,
        blank=False,
    )

    """The balance of the source wallet after the
    transaction. Useful for displaying transaction
    history."""
    balance_source = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Value of the wallet at the time of this transaction",
        null=False,
        blank=True,
        default=0,
    )

    """The balance of the destination wallet after the
    transaction. Useful for displaying transaction
    history."""
    balance_dest = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Value of the wallet at the time of this transaction",
        null=False,
        blank=False,
        default=0,
    )

    # The date/time of the creation of this transaction.
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.id)+" - From:"+str(self.wallet_source.owner.id)+" To:"+str(self.wallet_dest.owner.id)

    # place this in models.py
    from allauth.account.signals import user_logged_in
    from django.dispatch import receiver


@receiver(user_logged_in)
def login_logger(request, user, **kwargs):
    if not hasattr(user, 'wallet'):
        wallet = Wallet.objects.create(
            owner=user,
            balance=settings.WALLET_INITIAL_AMOUNT
        )
