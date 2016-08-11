try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.views.generic import TemplateView

# place app url patterns here


urlpatterns = [
    # url pattern for the userlistview
    url(
        regex=r'^terms/$',
        view=TemplateView.as_view(template_name='landing/terms.html'),
        name='terms'
    ),
    url(
        regex=r'^privacy/$',
        view=TemplateView.as_view(template_name='landing/privacy.html'),
        name='privacy'
    ),
    url(
        regex=r'^license/$',
        view=TemplateView.as_view(template_name='landing/license.html'),
        name='license'
    ),
    url(
        regex=r'^about/$',
        view=TemplateView.as_view(template_name='landing/about.html'),
        name='about'
    ),
    url(
        regex=r'^FAQ/$',
        view=TemplateView.as_view(template_name='landing/FAQ.html'),
        name='FAQ'
    ),
    url(
        regex=r'^people/$',
        view=TemplateView.as_view(template_name='landing/who_we_are.html'),
        name='people'
    ),
    url(
        regex=r'^contact/$',
        view=TemplateView.as_view(template_name='pages/contact.html'),
        name='contact'
    ),


]
