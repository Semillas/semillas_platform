# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from rest_framework import permissions

from .models import Service
from .serializers import ServiceSerializer


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class ServiceRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['name', ]
    model = Service

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return Service.objects.get(username=self.request.user.username)


class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = (permissions.IsAuthenticated,)


class ServiceDetail(generics.RetrieveUpdateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/service/2/
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = (permissions.IsAuthenticated,)
