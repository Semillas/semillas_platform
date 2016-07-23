try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.views.generic import TemplateView

# place app url patterns here


urlpatterns = [
    # url pattern for the userlistview
    url(
        regex=r'^people/$',
        view=TemplateView.as_view(template_name='landing/people.html'),
        name='people'
    ),
    url(
        regex=r'^contact/$',
        view=TemplateView.as_view(template_name='pages/contact.html'),
        name='contact'
    ),
    
]
