#coding:utf-8
from django.contrib import admin
from thesisApp.models import User,Course,LocalAuth,Class,Conversation,Exercise,CourseUser,ExerciseUserAnswer
# StuRole,TeacherRole,SubjectManager,Subject,TeacherCourse,StuCourse
# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(LocalAuth)
admin.site.register(Class)

admin.site.register(Conversation)
admin.site.register(Exercise)
admin.site.register(CourseUser)
admin.site.register(ExerciseUserAnswer)



# class AuthorAdmin(admin.ModelAdmin):
#     search_fields = ('user_name',)             #搜索
#    #自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
           
# admin.site.register(User,AuthorAdmin)
