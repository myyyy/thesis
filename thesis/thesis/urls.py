from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thesis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    	# url(r'^static/(?P<path>.*)$','django.views.static.serve',),
 	url(r'^course/(?P<id>\d+)/$', 'thesisApp.views.stu_course'),

 	url(r'^admin/', include(admin.site.urls)),
 	url(r'^course/exercises/(?P<id>\d+)/$', 'thesisApp.views.course_exercise_detail'),
 	url(r'^course/exercises/show/(?P<id>\d+)/$', 'thesisApp.views.show_exercise'),
 	url(r'^thesisApp/course/submit/(?P<id>\d+)/$', 'thesisApp.views.submit_exercise'),
 	

)
