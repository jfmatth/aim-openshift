from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Root
    url(r'^$', TemplateView.as_view(template_name = "index.html") ),
    
    # main app, AIM
    url(r'^aim/', include('aim.urls') ),
    url(r'^loader/', include('loader.urls') ),
    url(r'^graph/', include('graphs.urls')),

    # django registration
    (r'^accounts/', include('registration.backends.default.urls')), 

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
