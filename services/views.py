# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions
# import django_filters

from semillas_backend.users.models import User

from .models import Service, Category
from .serializers import ServiceSerializer, CategorySerializer, CreateServiceSerializer

class CreateService(generics.CreateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

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
    lookup_field = 'uuid'

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        pk = self.kwargs['user_id']
        u=User.objects.get(uuid=pk)
        if u:
            return Service.objects.filter(author=u.id)

# Filter services by category_id
class CategoryServiceList(generics.ListAPIView):
    """
    param1 -- A first parameter
    """
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # filter_fields = ('category',)
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = Service.objects.all()
    # def get_queryset(self):

    #     import pdb; pdb.set_trace();
        
    #         pk = self.kwargs['category_id']
    #         u=Category.objects.get(id=pk)
    #         if u:
    #             return u.services.all()