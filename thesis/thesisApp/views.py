#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
# from thesisApp.models import User,LocalAuth,Class,TeacherCourse,StuCourse,Conversation,Exercise,Answer,StuRole,TeacherRole,SubjectManager,Subject
from thesisApp.models import User,Course,LocalAuth,Class,Conversation,Exercise
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
	#查询指定用户的课程
	 courses = User.objects.get(number = str(id)).course.all()
  	 return render(request, 'stuTwo/projects.html',  locals(),
            		context_instance=RequestContext(request))

#该课程下的习题
def course_exercise_detail (request,id):
	try:
		# course_exercises = Exercise.objects.all().filter(course_id = str(id))
		course_exercises = User.objects.get(number = str(id)).exerciseuseranswer_set.all()
	except Exercise.DoesNotExist:
		raise Http404
	return render_to_response('stuTwo/courseExerciseDetail.html',
           				locals(),
           				 context_instance=RequestContext(request))
# 习题详情及提交习题	
def show_exercise (request,id):
	try:
		course_exercise = Exercise.objects.get(ex_id = str(id))

	except Exercise.DoesNotExist:
		raise Http404
	return render(request, 'stuTwo/showExercise.html',
           				locals(),
           				 context_instance=RequestContext(request))

def submit_exercise (request,id):
	try:
		course_exercises = Exercise.objects.all().filter(ex_course_id = str(id))
	except Exercise.DoesNotExist:
		raise Http404
	return render_to_response('stuTwo/submitExercise.html',
           				locals(),
           				 context_instance=RequestContext(request))	
			
	# except StuCourse.DoesNotExist:
	# 	raise Http404("Poll does not exist")
	# return render_to_response('stu/menu.html',locals(),context_instance=RequestContext(request))	
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