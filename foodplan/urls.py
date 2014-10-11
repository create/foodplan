from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
    url(r'^signin', 'main.views.signin'),
    url(r'^signup', 'main.views.signup'),
    url(r'^$', 'main.views.home'),
    url(r'^week', 'main.views.week'),
    url(r'^pantry', 'main.views.pantry'),
    url(r'^improve', 'main.views.improve')
)
