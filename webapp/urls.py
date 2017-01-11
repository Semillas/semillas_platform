try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.views.generic import TemplateView

urlpatterns = [
    url(
        regex=r'',
        view=TemplateView.as_view(template_name='webapp/index.html'),
        name='webapp'
    ),
    url(
        regex=r'^geolocation$',
        view=TemplateView.as_view(template_name='webapp/geolocation.html'),
        name='geolocation'
    ),
]
