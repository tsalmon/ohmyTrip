from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('trip.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
