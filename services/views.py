# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from rest_framework import generics
from rest_framework import permissions
from rest_framework import views
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework import status

from semillas_backend.users.models import User

from django.contrib.gis.db.models.functions import Distance

from django.contrib.gis.geos import Point
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError

from .models import Service, Category
from .serializers import *

logger = logging.getLogger(__name__)


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAdminUser,)


class ServiceDetail(generics.RetrieveAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'uuid'


class ServiceDelete(generics.DestroyAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get_queryset(self):
        return Service.objects.filter(author=self.request.user)


class CreateService(generics.CreateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UpdateService(generics.UpdateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    serializer_class = UpdateServiceSerializer
    # TODO: Make parmission only owner can edit
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get_queryset(self):
        return Service.objects.filter(author=self.request.user)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)


class UserServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        if 'user_uuid' in self.kwargs:
            return Service.objects.filter(author__uuid=self.kwargs['user_uuid'])
        return Service.objects.none()

# Filter services by category_id


class FeedServiceList(generics.ListAPIView):
    """ Main endpoint. This is the list of services being offered.
        get:
        params:
            search: string to search in title and description
            lat:    latitude to order the services by distance
            lon:    longitude to order the services by distance
            category: int the category id to filter by
    """
    serializer_class = ServiceSerializer
    permission_classes = (permissions.AllowAny,)
    filter_fields = ('category',)
    # columns to search in
    word_fields = ('title', 'description',)

    def get_queryset(self):
        queryset = Service.objects.all()
        # Order all the services by distance to the requester user location
        if 'lat' in self.request.query_params and 'lon' in self.request.query_params:
            # Brings lat and lon in request parameters
            ref_location = Point(float(self.request.query_params['lon']), float(
                self.request.query_params['lat']), srid=4326)
            if not self.request.user.is_anonymous() and \
                    not self.request.user.location_manually_set:
                # If user is logged in, save his location
                self.request.user.location = ref_location
                self.request.user.save()
        elif not self.request.user.is_anonymous and (self.request.user.location is not None):
            # User has a location previously saved
            ref_location = self.request.user.location
        else:
            # if no location at all
            geoip = GeoIP2()
            ip = self.request.META['REMOTE_ADDR']
            try:
                ref_location = Point(geoip.lon_lat(ip), srid=4326)
            except AddressNotFoundError:
                logger.warning('Location could not been retrieved by any mean')
                ref_location = Point((-3.8196228, 40.4378698), srid=4326)  # Madrid
            if not self.request.user.is_anonymous:
                self.request.user.location = ref_location
                self.request.user.save()
        return queryset.annotate(dist=Distance('author__location', ref_location)).order_by('dist')


class ServicePhotoUpload(generics.CreateAPIView):
    """ Test this view with the following Curl Command:
    curl -X POST
    -H "Content-Type:multipart/form-data"
    -H "Content-Disposition: attachment; filename*=UTF-8''joaquin.jpg"
    -H "Authorization: Token 04601a00e6499ade89b55caf37dba949ec99b082"
    -F "file=@/home/ismael/Downloads/heroquest.jpg"
    http://localhost:8000/api/v1/service/photo_upload/c561b263-06e4-44d6-b72c-7d8ad2b03986/

    and for production:

    curl -X POST
    -H "Content-Type:multipart/form-data"
    -H "Content-Disposition: attachment; filename*=UTF-8''heroquest.jpg"
    -H "Authorization: Token f81422024a991f76d7bc1a11c4974206cb31c481"
    -F "photo=@/home/ismael/Downloads/heroquest.jpg;type=image/jpg"
    https://www.semillasocial.org/api/v1/service/photo_upload/da27db5b-09eb-44de-864a-a005d4645af8/
    """

    # queryset = ServicePhoto.objects.all()
    serializer_class = ServicePhotoUploadSerializer
    parser_classes = (parsers.MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        # TODO: Check the service belongs to the user.
        service_id = Service.objects.get(uuid=kwargs['uuid']).id
        request.data['service'] = service_id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ServicePhotoDelete(generics.DestroyAPIView):
    """ Test this view with the following Curl Command:
    """

    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return ServicePhoto.objects.filter(service__author=self.request.user)
