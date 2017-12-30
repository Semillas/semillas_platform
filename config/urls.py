# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from semillas_backend.users.views import FacebookLogin

import allauth.account.views as allauth_views

urlpatterns = [

    # API
    re_path(r'^api/v1/user/', include('semillas_backend.users.api_urls', namespace='api_users')),
    re_path(r'^api/v1/service/', include('services.urls', namespace='api_service')),
    re_path(r'^api/v1/wallet/', include('wallet.urls', namespace='api_wallet')),


    re_path(r'^i18n/', include('django.conf.urls.i18n')),

    re_path(r'^$', TemplateView.as_view(template_name='landing/home.html'), name='home'),
    re_path(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),

    # User management
    re_path(r'^users/', include('semillas_backend.users.urls', namespace='users')),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', allauth_views.confirm_email,
        name="account_confirm_email"),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^', include('django.contrib.auth.urls')),

    # Your stuff: custom urls includes go here
    re_path(r'^landing/', include('landing.urls', namespace='landing')),
    re_path(r'^docs/', include('rest_framework_docs.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    import debug_toolbar
    urlpatterns += [
        re_path(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        re_path(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        re_path(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        re_path(r'^500/$', default_views.server_error),
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
