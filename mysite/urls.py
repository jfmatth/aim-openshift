from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^$', TemplateView.as_view(template_name = "index.html"),name="index" ),
    url(r'^aim/', include('aim.urls') ),
    url(r'^loader/', include('loader.urls') ),
    url(r'^graph/', include('graphs.urls')),

    (r'^accounts/', include('registration.backends.default.urls')), 
    
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
