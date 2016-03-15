from django.conf.urls import *
from thesisApp.views import stu_course


from django.conf.urls import *
from models import *
from views import *

urlpatterns = patterns('',
	url(r'^login/$', 'thesisApp.views.user_login',name = 'login'),
	url(r'^course/$', 'thesisApp.views.stu_course',name='course'),
 	url(r'^course/exercises/(?P<id>\d+)/$', 'thesisApp.views.course_exercise_detail',name = 'courseExercises'),
 	url(r'^course/exercises/show/(?P<id>\d+)/$', 'thesisApp.views.show_exercise',name = 'exercisesDetail'),
 	url(r'^thesisApp/course/submit/(?P<id>\d+)/$', 'thesisApp.views.submit_exercise',name = 'submitExercise'),
 	
)


