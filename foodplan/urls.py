from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin', include(admin.site.urls)),
    url(r'^signin', 'main.views.signin'),
    url(r'^signup', 'main.views.signup'),
    url(r'^dashboard', 'main.views.dashboard'),
    url(r'^$', 'main.views.home'),
    url(r'^pantry', 'main.views.pantry'),
    url(r'^improve', 'main.views.improve'),
    url(r'^about', 'main.views.about'),
    url(r'^reroll', 'main.views.reroll'),
    url(r'^export', 'main.views.export'),
)
