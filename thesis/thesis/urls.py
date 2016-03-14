from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thesis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    	# url(r'^static/(?P<path>.*)$','django.views.static.serve',),
 	
 	url(r'^admin/', include(admin.site.urls)),
 	url(r'^thesisApp/', include('thesisApp.urls')),
 	

)
