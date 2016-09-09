# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import ServiceAdmin as AuthServiceAdmin
from django.contrib.auth.forms import ServiceChangeForm, ServiceCreationForm
from .models import Service


class MyServiceChangeForm(ServiceChangeForm):
    class Meta(ServiceChangeForm.Meta):
        model = Service


class MyServiceCreationForm(ServiceCreationForm):

    class Meta(ServiceCreationForm.Meta):
        model = Service

    def clean_title(self):
        title = self.cleaned_data["title"]
        try:
            Service.objects.get(title=title)
        except Service.DoesNotExist:
            return title
        raise forms.ValidationError(self.error_messages['duplicate_title'])


@admin.register(Service)
class MyServiceAdmin(AuthServiceAdmin):
    form = MyServiceChangeForm
    add_form = MyServiceCreationForm
    fieldsets = (
            ('Service Profile', {'fields': ('name',)}),
    ) + AuthServiceAdmin.fieldsets
    list_display = ('title', 'date', 'is_superService')
    search_fields = ['title']
