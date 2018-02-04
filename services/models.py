# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
from uuid import uuid4
from random import randint

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.gis.db.models.functions import Distance


@python_2_unicode_compatible
class Service(models.Model):
    """
    Represents an advert of a user on the platform. Its intended to be
    exchangeable for seeds and mainly geolocated oriented (TODOs!)
    """
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    title = models.TextField(max_length=100,
                             help_text="A title for what you offer.")
    date = models.DateTimeField(auto_now_add=True,
                                help_text="Date of the post.")
    description = models.TextField(max_length=2000,
                                   help_text="A description of the service.")

    available = models.BooleanField(default=True)  # user easily can disable it

    url = models.URLField(
        verbose_name="your website",
        help_text="Your website.",
        default=None, blank=True, null=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='services',
    )

    seeds_price = models.PositiveIntegerField(
        help_text="Proposed price in seeds",
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        'Category',
        null=False,
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('api_service:detail', kwargs={'pk': self.id})

    def get_distance(self, ref_loc):
        return Distance(self.author.location, ref_loc)


@python_2_unicode_compatible
class Category(models.Model):
    """
    Represents an category of a Service
    """
    name = models.CharField(
        unique=True,
        max_length=100,
        help_text="A name for the category.")

    def category_photo_upload(instance, filename):
        extension = os.path.splitext(filename)[1]
        return "media/categries/%s%s" % (str(instance.id), extension)

    photo = models.ImageField(
        null=True,
        blank=True,
        help_text='Category Picture',
        upload_to=category_photo_upload,
    )

    order = models.IntegerField()

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#        return reverse('users:detail', kwargs={'username': self.username})


class ServicePhoto(models.Model):
    """ This model is a relation 1:N to Service.
        There could exists many photos related to one service.
    """

    def service_photo_upload(instance, filename):
        extension = os.path.splitext(filename)[1]
        return "media/services/%s_%s%s" % (
            str(instance.service.id),
            str(randint(0, 99999)),
            extension
        )

    service = models.ForeignKey(
        Service,
        related_name='photos',
    )

    photo = models.ImageField(
        max_length=300,
        null=True,
        blank=True,
        upload_to=service_photo_upload,
        help_text="Photos of the service being offered",
        default=None
    )

    date = models.DateTimeField(auto_now_add=True,
                                help_text="Date of the post.")
