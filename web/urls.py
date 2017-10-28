from django.conf.urls import patterns, include, url
from django.contrib import admin
from  web import views
urlpatterns = patterns('',

#    url(r'^index/', index),
##    url(r'^login/(\d*)/$', login),
#    url(r'^logout/(?P<name>\d*)/$', logout1),
#    url(r'^logout/(?P<name>\d*)/(?P<id>\d*)$', logout2),
#    url(r'^list/(?P<name>\d*)/$', list,{'id':222}), 
# 
#    url(r'^delete/(?P<id>\d*)/$', Delete),
#    url(r'^update/(?P<id>\d*)/(?P<name>\w*)/$', Update),
#    url(r'^get/(?P<hostname>\w*)/$', Get),
#    url(r'^assetlist2/', AssetList),
#    url(r'^login/', login),
#   url(r'^add/(?P<name>\d*)/$', views.Add),
#   url(r'^delete/(?P<id>\d*)/$', views.DeleteId),
#   url(r'^update/(?P<id>\d*)/(?P<hostname>\w*)/$', views.Update),
#   url(r'^get/(?P<hostname>\d*)/$', views.Get),
   url(r'^assetlist/$', views.AssetList),
   url(r'^login/$', views.Login),

)
