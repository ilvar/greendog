from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
from greendog import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'start.views.index'),
    url(r'^works/$', 'works.views.works'),
    url(r'^works/(?P<slug>[^\.]+)/$', 'works.views.view_work'),
    # url(r'^greendog/', include('greendog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
