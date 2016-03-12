from django.conf.urls import *
from thesisApp.views import stu_course


from django.conf.urls import *
from models import *
from views import *

urlpatterns = patterns('',
	url(r'^$',stu_course),
	 (r'^admin/', include('django.contrib.admin.urls')),
)


