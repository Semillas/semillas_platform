# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework_swagger.views import get_swagger_view
import debug_toolbar

schema_view = get_swagger_view(title='Semillas API')

urlpatterns = [

    # API
    url(r'^api/v1/user/', include('semillas_backend.users.api_urls', namespace='api_users')),
    url(r'^api/v1/service/', include('services.urls', namespace='api_service')),



    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^$', TemplateView.as_view(template_name='landing/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('semillas_backend.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^landing/', include('landing.urls', namespace='landing')),
    url(r'^docs/', schema_view),
    url(r'^webapp/', include('webapp.urls', namespace='webapp')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
