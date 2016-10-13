# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from .models import Service, Category
from .serializers import ServiceSerializer, CategorySerializer

class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ServiceDetail(generics.RetrieveUpdateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

