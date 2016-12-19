try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.views.generic import TemplateView

# place app url patterns here


urlpatterns = [
    # url pattern for the userlistview
    
    url(
        regex=r'^philosophy/$',
        view=TemplateView.as_view(template_name='landing/philosophy.html'),
        name='philosophy'
    ),
    url(
        regex=r'^product/$',
        view=TemplateView.as_view(template_name='landing/product_and_code.html'),
        name='product'
    ),
    url(
        regex=r'^people/$',
        view=TemplateView.as_view(template_name='landing/who_we_are.html'),
        name='people'
    ),
]
