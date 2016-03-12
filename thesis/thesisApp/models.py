#coding:utf-8
from django.db import models
from django.contrib import admin
class  Class(models.Model):
                class_name= models.CharField(max_length=30)
                class_create_time = models.CharField(max_length=50)
                def __unicode__(self):
                                return self.class_name          
# # Create your models here.
class  Course(models.Model):
                coures_name= models.CharField(max_length=30)
                def __unicode__(self):
                            return self.coures_name

class  Exercise(models.Model):
                ex_id = models.CharField(max_length=30)
                course_id = models.ForeignKey(Course)
                ex_content = models.CharField(max_length=10000)
                ex_title = models.CharField(max_length=30)
                cs_opened = models.CharField(max_length=30)
                ex_end_time = models.CharField(max_length=30)
                ex_url = models.CharField(max_length=30)
                def __unicode__(self):
                            return self.ex_title
class  Conversation(models.Model):
                cs_id = models.CharField(max_length=30)
                from_id = models.CharField(max_length=30)
                to_id = models.CharField(max_length=30)
                cs_content = models.CharField(max_length=30)
                cs_create_tiem = models.CharField(max_length=30)
                cs_opened = models.CharField(max_length=30)
                def __unicode__(self):
                            return self.cs_id  
class  User(models.Model):
                user_name= models.CharField(max_length=30)
                number = models.CharField(max_length=50)
                card = models.CharField(max_length=50)
                sex = models.CharField(max_length=50)
                telphone = models.CharField(max_length=50)
                email = models.EmailField(max_length=50)
                head_url = models.CharField(max_length=50)
                create_time = models.CharField(max_length=50)
                major_id= models.CharField(max_length=50)
                academy_id = models.CharField(max_length=50)
                class_id = models.ForeignKey(Class)
                course = models.ManyToManyField(Course, through = "CourseUser")
                exercise = models.ManyToManyField(Exercise, through = "ExerciseUserAnswer")
                def __unicode__(self):
                            return self.user_name  


class  CourseUser(models.Model):
                coure = models.ForeignKey(Course)
                user = models.ForeignKey(User)

class  LocalAuth(models.Model):
                user_id= models.ForeignKey(User)
                user_account = models.CharField(max_length=50)
                user_password = models.CharField(max_length=50)
                role_id = models.CharField(max_length=50)
                create_time = models.CharField(max_length=50)
                is_login= models.BooleanField(default=False)
                def __unicode__(self):
                            return self.user_account 

class ExerciseUserAnswer(models.Model):
                exercisec = models.ForeignKey(Exercise)
                user= models.ForeignKey(User)
                answer_content = models.CharField(max_length=30)
                is_finished = models.BooleanField(default=False)
                score = models.CharField(max_length=30)



# class  TeacherCourse(models.Model):
#                 user_id= models.CharField(max_length=30)
#                 coures_id= models.ForeignKey(Course)
#                 # def __unicode__(self):
#                 #             return self.name

# class  StuCourse(models.Model):
               
#                 user_id = models.CharField(max_length=30)
#                 coures_id= models.ForeignKey(Course)
#                 sc_create_tiem = models.CharField(max_length=30)
#                 # def __unicode__(self):
#                 #             return self.name  

# class StuRole(models.Model):
#                 role_id = models.CharField(max_length=30)
#                 role_name = models.CharField(max_length=30)
#                 user_id = models.CharField(max_length=30)
#                 create_time = models.CharField(max_length=30)
#                 role_description = models.CharField(max_length=30)
#                 class Meta:
#                     permissions = (
#                         ("view_exercisec", "Can see exercisec"),
#                         ("put_answer", "Can put answer"),
#                         ("change_answer", "Can change answer"),
#                     )
#                 # def __unicode__(self):
#                 #         return self.name      

# class TeacherRole(models.Model):
#                 role_id = models.CharField(max_length=30)
#                 role_name = models.CharField(max_length=30)
#                 user_id = models.CharField(max_length=30)
#                 create_time = models.CharField(max_length=30)
#                 role_description = models.CharField(max_length=30)
#                 class Meta:
#                     permissions = (
#                         ("view_exercisec", "Can see exercisec"),
#                         ("change_exercisec", "Can change the exercisec"),
#                         ("del_exercisec", "Can delete exercisec"),
#                     )
                # def __unicode__(self):
                #         return self.name   

# class SubjectManager(models.Model):
#     def get_Subject_list(self):
#         subjects = Subject.objects.all()
#         subjects_list = []
#         for i  in range(len(subjects)):
#             subjects_list.append([])
#         for i  in range(len(subjects)):
#             temp = Subject.objects.get(name = subjects[i]) 
#             posts = temp.article_set.all()
#             subjects_list[i].append(subjects[i].name)
#             subjects_list[i].append(len(posts))
#         return subjects_list
        
# class Subject(models.Model):
#     name = models.CharField(max_length=20,blank=True)
#     creat_time = models.DateTimeField(auto_now_add=True)
#     identifier = models.CharField(max_length=10,blank=True)

#     objects = models.Manager()
#     subject_list = SubjectManager()


#     @models.permalink
#     def get_absolute_url(self):
#         return('subjectDetail', (), {
#       'subject':self.name})
#     def __unicode__(self):
#         return self.name