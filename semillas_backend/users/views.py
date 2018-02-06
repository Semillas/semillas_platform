# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from rest_framework import permissions
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from .models import User
from .serializers import UserSerializer
from .serializers import UpdateUserSerializer
from .permissions import IsOwnerOrReadOnly


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    word_fields = ('name', 'email', 'phone', 'telegram_id')

    def get(self, request, format=None):
        if not request.query_params.get(api_settings.SEARCH_PARAM, ''):
            return Response("User not found", status=status.HTTP_400_BAD_REQUEST)
        else:
            return super(UserList, self).get(request, format)


class UserDetail(generics.RetrieveAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'


class UserDetailUpdate(generics.UpdateAPIView):
    """
    Usage:
    curl \
        -X PATCH \
        -H "Content-Type:multipart/form-data" \
        -H "Content-Disposition: attachment; filename*=UTF-8''joaquin.jpg" \
        -H "Authorization: Token 04601a00e6499ade89b55caf37dba949ec99b082" \
        -F "picture=@/home/ismael/Downloads/heroquest.jpg" \
        -F "phone=+34 679 923 555" \
        -F "location={'latitude': '40.4378698','longitude': '-3.8196228'}" \
        http://localhost:8000/api/v1/user/update/e0d21ae6-13c1-4eb5-b216-ba251b83ce67/
    """
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        if 'location' in request.data:
            request.data['location_manually_set'] = True
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if 'location' in request.data:
            request.data['location_manually_set'] = True
        return super().put(request, *args, **kwargs)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
