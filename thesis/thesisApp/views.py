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
    if user:
	user = request.session.get('user_obj', False)
	courses = User.objects.get(id = str(user.id)).courseuser_set.all()
	if user.is_teacher:
		return render_to_response('teacher/course.html',locals(),context_instance=RequestContext(request))
	else:
	  	return render_to_response( 'stuTwo/course.html',  locals(),
	            		context_instance=RequestContext(request))
    else:
        return render_to_response('stuTwo/userLogin.html',context_instance=RequestContext(request))

#该课程下的习题
def course_exercise_detail (request,id):

    user = request.session.get('user_obj', False)
    if user:
 
	course_name = Course.objects.get(id = str(id))
	course_exercises = User.objects.get(id= str(user.id)).exerciseuseranswer_set.filter(course_id =str(id))
	if user.is_teacher:
		course =  Course.objects.get(id = str(id)).courseuser_set.all()
		return render_to_response('teacher/courseUser.html',locals(),context_instance=RequestContext(request))
	else:
	  	return render_to_response( 'stuTwo/courseExerciseDetail.html',  locals(),
	            		context_instance=RequestContext(request))
    else:
        return render_to_response('stuTwo/userLogin.html',context_instance=RequestContext(request))	

# 习题详情及提交习题	
def show_exercise (request,id):
	try:
		course_exercise = Exercise.objects.get(id = str(id))

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
    m = hashlib.md5()
    if request.method == 'POST':
            #获取表单用户密码
            username=request.POST.get('name','')  
            password=request.POST.get('password','')  
            m.update(password)
            #获取的表单数据与数据库进行比较
            user = LocalAuth.objects.filter(user_account = username,user_password = m.hexdigest())
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
                return render_to_response('login.html',context_instance=RequestContext(request))
    else:
        return render_to_response('login.html',context_instance=RequestContext(request))

def msg (request):
	user = request.session.get('user_obj', False)
	if user:
		return render_to_response('msg.html',
           				locals(),
           				 context_instance=RequestContext(request))
	else:
		return render_to_response('stuTwo/userLogin.html',context_instance=RequestContext(request))

def info (request):
    user = request.session.get('user_obj', False)
    if user:
        if request.method == 'POST':
            user = User.objects.get(id = str(user.id))
            account=request.POST.get('account','')  
            emali=request.POST.get('email','')  
            user.user_name = account
            user.email = emali
            user.save()
            request.session['user_obj'] = user
            return render_to_response('info.html',
                                    locals(),
                        context_instance=RequestContext(request))
        else:
            return render_to_response('info.html',
                                    locals(),
                        context_instance=RequestContext(request))
    else:
        return render_to_response('stuTwo/userLogin.html',context_instance=RequestContext(request))

def index (request):
	user = request.session.get('user_obj', False)
	if user:
		if user.is_teacher:
			return render_to_response('teacher/index.html',context_instance=RequestContext(request))
		else:
	  		return render(request, 'stuTwo/index.html',  locals(),
	            		context_instance=RequestContext(request))
	
	else:
		return render_to_response('stuTwo/userLogin.html',context_instance=RequestContext(request))

def logout(request):
    try:
        del request.session['user_obj']
    except KeyError:
        pass
    return HttpResponseRedirect('/thesisApp/login/')

def register(request):
    if request.method == "POST":
            #获取表单信息
            m = hashlib.md5()

            username = request.POST.get('account','')  
            if LocalAuth.objects.filter(user_account = str(username)):
	            	return render_to_response('register.html',
	           				locals(),
	           				 context_instance=RequestContext(request))
            else:
	            password = request.POST.get('password','')  
	            m.update(password)

	            is_teacher = request.POST.get('role','')  
	            number = request.POST.get('number','')  
	            email = request.POST.get('email','')  
	            tel = request.POST.get('tel','')  

	            #将表单写入数据库
	            user = User()
	            user.user_name =  username
	            user.number =number
	            user.email = email
	            user.telphone = tel
	            user.is_teacher = is_teacher
	            user.create_time = datetime.now()
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
 	return render_to_response('register.html',
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

