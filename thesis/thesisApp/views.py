#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from thesisApp.models import User,LocalAuth,Class,TeacherCourse,StuCourse,Conversation,Exercise,Answer,StuRole,TeacherRole,SubjectManager,Subject
from thesisApp.models import User,Course,LocalAuth,Class,Conversation,Exercise
from django.http import Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.syndication.views import Feed #订阅RSS
import json
from django.core import serializers

from django.template import loader,Context
from django.http import HttpResponse
import hashlib
from datetime import datetime
# Create your views here
#显示课程
def  stu_course(request):
	#查询指定用户的课程
	user = request.session.get('user_obj', False)
	courses = User.objects.get(id = str(user.id)).courseuser_set.all()
  	return render(request, 'stuTwo/course.html',  locals(),
            		context_instance=RequestContext(request))

#该课程下的习题
def course_exercise_detail (request,id):
	try:
		# course_exercises = Exercise.objects.all().filter(course_id = str(id))
		user = request.session.get('user_obj', False)
		course_name = Course.objects.get(id = str(id))
		course_exercises = User.objects.get(number = str(user.number)).exerciseuseranswer_set.filter(course_id =str(id))
	except Exercise.DoesNotExist:
		raise Http404
	return render(request, 'stuTwo/courseExerciseDetail.html',
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


#登陆
def user_login(request):
    if request.method == 'POST':
            #获取表单用户密码
            username=request.POST.get('name','')  
            password=request.POST.get('password','')  
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(user_name = username,number = password)
            if user:
                #比较成功，跳转index
                user_obj = User.objects.get(user_name = username)
                response = HttpResponseRedirect('/thesisApp/course/')
                #将username写入浏览器cookie,失效时间为3600
                request.session['user_obj'] = user_obj
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('stuTwo/userLogin.html')
    else:
        return render_to_response('stuTwo/userLogin.html',context_instance=RequestContext(request))

def msg (request):

	return render_to_response('stuTwo/msg.html',
           				locals(),
           				 context_instance=RequestContext(request))	
def register(request):
    if request.method == "POST":
            #获取表单信息
            m = hashlib.md5()

            username = request.POST.get('account','')  
            if LocalAuth.objects.filter(user_account = str(username)):
	            	return render_to_response('reg.html',
	           				locals(),
	           				 context_instance=RequestContext(request))
            else:
	            password = request.POST.get('password','')  
	            m.update(password)
	            #将表单写入数据库
	            user = User()
	            user.user_name =  username
	            user.save()
	            userAuth = LocalAuth()
	            userAuth.user_account = username
	            userAuth.user_password= m.hexdigest()
	            userAuth.create_time = datetime.now()
	            userAuth.is_login = True
	            userAuth.user = user
	            userAuth.save()
	            #返回注册成功页面
	            response = HttpResponseRedirect('/thesisApp/course/')
	            request.session['user_obj'] = user
	            response.set_cookie('username',username,3600)
	            return response
	            	
    else:
 	return render_to_response('reg.html',
           				locals(),
           				 context_instance=RequestContext(request))
# def userLogout(request):  
#     auth.logout(request)  
#     return HttpResponseRedirect('/user') 			
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

