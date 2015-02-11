from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from . import views

urlpatterns = patterns('',
	url(r'^bunks/$', views.bunk_feed, name='bunk_feed'),
	url(r'^$', RedirectView.as_view(pattern_name='bunk_feed'), name="main_page"),
	url(r'^bunks/bunk/$', views.bunk_someone, name="bunk_someone"),
	url(r'^bunks/(?P<user_key>[0-9]+)/$', views.my_feed, name="my_feed"),
)