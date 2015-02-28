from django.conf.urls import patterns, url
from . import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name="home.html")),
    #url(r'^$', views.TripIndex.as_view(), name="index"),
    url(r'^$', views.index, name='index'),
)
