from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from graphs.views import graphview,  testgraphview
  
urlpatterns = patterns('',
    url(r'^(?P<symbol>\w+)/$', graphview.as_view() ),
    
    url(r'test/(?P<symbol>\w+)/$', testgraphview.as_view() ),
)