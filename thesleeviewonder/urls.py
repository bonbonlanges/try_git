from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
    url(r'^product', 'website.views.product'),
    url(r'^about', 'website.views.about'),
    url(r'^contact', 'website.views.contact'),
    url(r'^$', 'website.views.index'),
)
