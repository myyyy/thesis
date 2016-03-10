#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from thesisApp.models import User,LocalAuth,Class,TeacherCourse,StuCourse,Conversation,Exercise,Answer,StuRole,TeacherRole,SubjectManager,Subject
from django.http import Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.syndication.views import Feed #订阅RSS
import json
from django.core import serializers

from django.template import loader,Context
from django.http import HttpResponse
# Create your views here
#显示课程
def  stu_course(request,id):
	try:
		stu_course = StuCourse.objects.filter(user_id = str(id))
	except StuCourse.DoesNotExist:
		raise Http404("Poll does not exist")
	return render(request, 'stu/menu.html')	
	# is_home = True
	# stu_course = StuCourse.objects.all(); 
	# paginator = Paginator(stu_course,6)
	# page_num = request.GET.get('page')
	# try:
	# 	stu_course = paginator.page(page_num)
	# except PageNotAnInteger:
	# 	stu_course = paginator.page(1)
	# except EmptyPage:
	# 	stu_course = paginator.page(paginator.page_num)

# def exercise_detail (request,id):
# 	try:
# 		exercise = Exercise.objects.get(course_id = str(id))
# 	except Exercise.DoesNotExist:
# 		raise Http404
# 	return render_to_response('biger/content.html',
#            				locals(),
#            				 context_instance=RequestContext(request))
# 	