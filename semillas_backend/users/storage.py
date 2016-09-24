# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage

user_store = FileSystemStorage(location='/media/users')
