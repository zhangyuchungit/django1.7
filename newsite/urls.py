from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import urls
from app04 import urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newsite.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^index/', index),
#    url(r'^login/(\d*)/$', login),
#    url(r'^logout/(?P<name>\d*)/$', logout1),
#    url(r'^logout/(?P<name>\d*)/(?P<id>\d*)$', logout2),
#    url(r'^list/(?P<name>\d*)/$', list,{'id':222}),

#    url(r'^web/', include('web.urls')),
    url(r'^web/', include('web.urls')),
    url(r'^app04/', include('app04.urls')),
)