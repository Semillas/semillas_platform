# -*- coding: utf-8 -*-

import os
from uuid import uuid4
from random import randint

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db.models import PointField

from phonenumber_field.modelfields import PhoneNumberField

from .validators import starts_with_at, is_blockchain_address


@python_2_unicode_compatible
class User(AbstractUser):

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    phone = PhoneNumberField(blank=True)
    phone_verified = models.BooleanField(default=False)

    location = PointField(
        null=True,
        blank=True,
        help_text='User Location, only read in production user admin panel'
    )

    location_manually_set = models.BooleanField(
        default=False,
        help_text="Flag indicating whether the user has introduced their location or not"
    )

    def user_photo_upload(instance, filename):
        extension = os.path.splitext(filename)[1]
        return "media/users/%s-%s%s" % (str(instance.id), str(randint(0, 9999)), extension)

    picture = models.ImageField(
        null=True,
        blank=True,
        help_text='Profile Picture',
        upload_to=user_photo_upload,
    )

    faircoin_address = models.CharField(
        max_length=36,
        blank=True,
        validators=[is_blockchain_address]
    )

    telegram_id = models.CharField(
        blank=True,
        max_length=60,
        validators=[starts_with_at],
        help_text="Telegram Id for peer communication. Example: @username"
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
