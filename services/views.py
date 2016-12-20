# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from semillas_backend.users.models import User
from rest_framework_word_filter.filter import FullWordSearchFilter

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
class FeedServiceList(generics.ListAPIView):
    """ access: GET /api/v1/services/feed
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # filter_fields = ('category',)
    # search_param = ('title','description',)
    word_fields = ('title','description',)

    def get_queryset(self):

        filter_services = FullWordSearchFilter()
        # self, request, queryset, view
        filtered_services = filter_services.filter_queryset(self.request, self.queryset, self)
        return filtered_services
