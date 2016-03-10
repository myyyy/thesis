#coding:utf-8
from django.contrib import admin
from thesisApp.models import User,LocalAuth,Class,TeacherCourse,StuCourse,Conversation,Exercise,Answer,StuRole,TeacherRole,SubjectManager,Subject
# Register your models here.
admin.site.register(User)
admin.site.register(LocalAuth)
admin.site.register(Class)
admin.site.register(TeacherCourse)
admin.site.register(StuCourse)
admin.site.register(Conversation)
admin.site.register(Exercise)
admin.site.register(Answer)
admin.site.register(StuRole)
admin.site.register(TeacherRole)
admin.site.register(SubjectManager)
admin.site.register(Subject)