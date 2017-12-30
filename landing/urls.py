try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.views.generic import TemplateView

# place app url patterns here

app_name = 'landing'

urlpatterns = [
    # url pattern for the userlistview

    url(
        regex=r'^porque/$',
        view=TemplateView.as_view(template_name='landing/porque.html'),
        name='porque'
    ),
    url(
        regex=r'^how_it_works/$',
        view=TemplateView.as_view(template_name='landing/how_it_works.html'),
        name='how_it_works'
    ),
    url(
        regex=r'^people/$',
        view=TemplateView.as_view(template_name='landing/who_we_are.html'),
        name='people'
    ),
    url(
        regex=r'^privacy/$',
        view=TemplateView.as_view(template_name='landing/privacy.html'),
        name='privacy'
    ),
]
