try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *
from .views import schema_view



urlpatterns = [
    url(r'', schema_view),
]
