# -*- coding: utf-8 -*-

from django.db import models
from django.db import OperationalError
from __future__ import unicode_literals
from django.conf import settings


class NegativeAmount(OperationalError):
    """
    An error made to represent and raise when the
    unavailability of an operation occurs, usually because
    the movement would leave the value on negative.
    """
    pass


class Transaction(models.Model):
    """
    A logger of each movement of seeds.
    """
    wallet = models.ForeignKey(Wallet)
    value = models.BigIntegerField(default=0,
                                   help_text="Value of seeds to be transfer"
                                   )
    running_balance = models.BigIntegerField(default=0,
                                             help_text="How the seeds amount changes."
                                             )
    date = models.DateTimeField(auto_now_add=True,
                                help_text="When the transaction happened.")


class Wallet(models.Model):
    """Represents a holder for the seeds of a User, whose
    relationship is 1 to 1.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    seeds = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def deposit(self, value):
        """
        Put an amount into the wallet.
        Also creates a new transaction with
        the more detail and info.
        """
        transaction = Transaction(
                running_balance=self.seeds + value,
                value=value,
            )
        self.seeds += value
        self.save()

    def withdraw(self, value):
        """
        Withdraws a value from the wallet.
        Creates a new transaction with the withdraw
        value.
        """
        if value > self.balance:
            raise NegativeAmount("Not enough seeds :(.")
        transaction = Transaction(
                value=-value,
                running_balance=self.seeds - value
            )
        self.seeds -= value
        self.save()

    def transfer(self, wallet, value):
        """Transfers an value to another wallet.
        """
        self.withdraw(value)
        wallet.deposit(value)

