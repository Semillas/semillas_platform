# -*- coding: utf-8 -*-
import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def starts_with_at(value):
    if value[0] != '@':
        raise ValidationError(
            _('%(value)s Does not start with @'),
            params={'value': value},
        )

def is_blockchain_address(value):

    value = value.strip()

    if "\n" in value:
        raise ValidationError(
            _('Multiple lines in the Faircoin address')
        )

    if " " in value:
        raise ValidationError(
            _('Spaces in the Faircoin address')
        )

    if re.match(r"[a-zA-Z1-9]{27,35}$", value) is None:
        raise ValidationError(
            _('Faircoin format not correct')
        )
    return value

