from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^register/', include('register.urls')),
    url(r'^connexion/', include('connexion.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('trip.urls')),
)
