# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Service(models.Model):
    """
    Represents an advert of a user on the platform. Its intended to be
    exchangeable for seeds and mainly geolocated oriented (TODOs!)
    """
    title = models.TextField(max_length=100,
                             help_text="A title for what you offer.")
    date = models.DateTimeField(auto_now_add=True,
                                help_text="Date of the post.")
    text = models.TextField(max_length=2000,
                            help_text="A description of the service.")
    period = models.DurationField(blank=False,
                                  help_text="If your service is in a period "
                                            "of time.")
    start_hour = models.TimeField(blank=True,
                                  help_text="If you start serving from an "
                                            "hour")
    end_hour = models.TimeField(blank=True,
                                help_text="The finishing hour of the service.")
    available = models.BooleanField(default=False)  # user easily can disable it
    url = models.URLField(verbose_name="your website",
                          help_text="Your website.",
                          default=None, blank=True)
    # TODO: gps intentional: map = models.¿?
    # TODO: seeds ammount - bucket
    # TODO: photomanager album 1-N relationship

    pic = models.ImageField(upload_to=None,
                            height_field=None,
                            width_field=None,
                            max_length=100,
                            help_text="Upload a picture.")
    #  TODO: https://github.com/zsiciarz/django-pgallery/blob/master/pgallery
    # /models.py#L90   <- a cool image manager django app

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

#    def __str__(self):
#        return u'something goes here'

#    def get_absolute_url(self):
#        return reverse('users:detail', kwargs={'username': self.username})
