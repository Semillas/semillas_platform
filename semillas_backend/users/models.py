# -*- coding: utf-8 -*-

import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db.models import PointField

from phonenumber_field.modelfields import PhoneNumberField

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

    def user_photo_upload(instance, filename):
        extension = os.path.splitext(filename)[1]
        return "media/users/%s%s" % (str(instance.id), extension)


    picture = models.ImageField(
        null=True,
        blank=True,
        help_text='Profile Picture',
        upload_to=user_photo_upload,
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
