#coding:utf-8
from django.db import models
 
 
# # Create your models here.
class  User(models.Model):
                user_id = models.CharField(max_length=30)
                user_name= models.CharField(max_length=30)
                number = models.CharField(max_length=50)
                card = models.CharField(max_length=50)
                sex = models.CharField(max_length=50)
                telphone = models.CharField(max_length=50)
                email = models.CharField(max_length=50)
                head_url = models.CharField(max_length=50)
                create_time = models.CharField(max_length=50)
                major_id= models.CharField(max_length=50)
                academy_id = models.CharField(max_length=50)
                class_id = models.CharField(max_length=50)
                def __unicode__(self):
                                return self.name 


class  LocalAuth(models.Model):
                auth_id = models.CharField(max_length=30)
                user_id= models.CharField(max_length=30)
                user_account = models.CharField(max_length=50)
                user_password = models.CharField(max_length=50)
                sex = models.CharField(max_length=50)
                role_id = models.CharField(max_length=50)
                create_time = models.CharField(max_length=50)
                can_login= models.CharField(max_length=50)
                def __unicode__(self):
                                return self.name 

class  Class(models.Model):
                class_id = models.CharField(max_length=30)
                class_name= models.CharField(max_length=30)
                class_create_time = models.CharField(max_length=50)
                def __unicode__(self):
                            return self.name 

class  TeacherCourse(models.Model):
                user_id= models.CharField(max_length=30)
                coures_id= models.CharField(max_length=30)
                def __unicode__(self):
                            return self.name

class  StuCourse(models.Model):
                user_id = models.CharField(max_length=30)
                coures_id = models.CharField(max_length=30)
                sc_create_tiem = models.CharField(max_length=30)
                def __unicode__(self):
                            return self.name  

class  Conversation(models.Model):
                cs_id = models.CharField(max_length=30)
                from_id = models.EmailField(max_length=30)
                to_id = models.EmailField(max_length=30)
                cs_content = models.EmailField(max_length=30)
                cs_create_tiem = models.EmailField(max_length=30)
                cs_opened = models.EmailField(max_length=30)
                def __unicode__(self):
                            return self.name 

class  Exercise(models.Model):
                ex_id = models.CharField(max_length=30)
                ex_course_id = models.EmailField(max_length=30)
                ex_user_id = models.EmailField(max_length=30)
                ex_content = models.EmailField(max_length=30)
                ex_title = models.EmailField(max_length=30)
                cs_opened = models.EmailField(max_length=30)
                ex_end_time = models.EmailField(max_length=30)
                ex_url = models.EmailField(max_length=30)
                def __unicode__(self):
                            return self.name 

class  Answer(models.Model):
                answer_guid_exercise = models.CharField(max_length=30)
                answer_user_id = models.EmailField(max_length=30)
                score = models.EmailField(max_length=30)
                answer_create_time = models.EmailField(max_length=30)
                ex_title = models.EmailField(max_length=30)
                cs_opened = models.EmailField(max_length=30)
                ex_end_time = models.EmailField(max_length=30)
                ex_url = models.EmailField(max_length=30)
                def __unicode__(self):
                            return self.name 

class StuRole(models.Model):
                role_id = models.CharField(max_length=30)
                role_name = models.CharField(max_length=30)
                user_id = models.CharField(max_length=30)
                create_time = models.CharField(max_length=30)
                role_description = models.CharField(max_length=30)
                class Meta:
                    permissions = (
                        ("view_exercisec", "Can see exercisec"),
                        ("put_answer", "Can put answer"),
                        ("change_answer", "Can change answer"),
                    )
                def __unicode__(self):
                        return self.name      

class TeacherRole(models.Model):
                role_id = models.CharField(max_length=30)
                role_name = models.CharField(max_length=30)
                user_id = models.CharField(max_length=30)
                create_time = models.CharField(max_length=30)
                role_description = models.CharField(max_length=30)
                class Meta:
                    permissions = (
                        ("view_exercisec", "Can see exercisec"),
                        ("change_exercisec", "Can change the exercisec"),
                        ("del_exercisec", "Can delete exercisec"),
                    )
                def __unicode__(self):
                        return self.name   

class SubjectManager(models.Model):
    def get_Subject_list(self):
        subjects = Subject.objects.all()
        subjects_list = []
        for i  in range(len(subjects)):
            subjects_list.append([])
        for i  in range(len(subjects)):
            temp = Subject.objects.get(name = subjects[i]) 
            posts = temp.article_set.all()
            subjects_list[i].append(subjects[i].name)
            subjects_list[i].append(len(posts))
        return subjects_list
        
class Subject(models.Model):
    name = models.CharField(max_length=20,blank=True)
    creat_time = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=10,blank=True)

    objects = models.Manager()
    subject_list = SubjectManager()


    @models.permalink
    def get_absolute_url(self):
        return('subjectDetail', (), {
      'subject':self.name})
    def __unicode__(self):
        return self.name