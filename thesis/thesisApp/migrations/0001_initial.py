# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_guid_exercise', models.CharField(max_length=30)),
                ('answer_user_id', models.CharField(max_length=30)),
                ('score', models.CharField(max_length=30)),
                ('answer_create_time', models.CharField(max_length=30)),
                ('ex_title', models.CharField(max_length=30)),
                ('cs_opened', models.CharField(max_length=30)),
                ('ex_end_time', models.CharField(max_length=30)),
                ('ex_url', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_id', models.CharField(max_length=30)),
                ('class_name', models.CharField(max_length=30)),
                ('class_create_time', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cs_id', models.CharField(max_length=30)),
                ('from_id', models.CharField(max_length=30)),
                ('to_id', models.CharField(max_length=30)),
                ('cs_content', models.CharField(max_length=30)),
                ('cs_create_tiem', models.CharField(max_length=30)),
                ('cs_opened', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coures_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ex_id', models.CharField(max_length=30)),
                ('ex_course_id', models.CharField(max_length=30)),
                ('ex_user_id', models.CharField(max_length=30)),
                ('ex_content', models.CharField(max_length=10000)),
                ('ex_title', models.CharField(max_length=30)),
                ('cs_opened', models.CharField(max_length=30)),
                ('ex_end_time', models.CharField(max_length=30)),
                ('ex_url', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocalAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_id', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=30)),
                ('user_account', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('role_id', models.CharField(max_length=50)),
                ('create_time', models.CharField(max_length=50)),
                ('can_login', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StuCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30)),
                ('sc_create_tiem', models.CharField(max_length=30)),
                ('coures_id', models.ForeignKey(to='thesisApp.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StuRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_id', models.CharField(max_length=30)),
                ('role_name', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=30)),
                ('create_time', models.CharField(max_length=30)),
                ('role_description', models.CharField(max_length=30)),
            ],
            options={
                'permissions': (('view_exercisec', 'Can see exercisec'), ('put_answer', 'Can put answer'), ('change_answer', 'Can change answer')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, blank=True)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('identifier', models.CharField(max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubjectManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30)),
                ('coures_id', models.ForeignKey(to='thesisApp.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeacherRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_id', models.CharField(max_length=30)),
                ('role_name', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=30)),
                ('create_time', models.CharField(max_length=30)),
                ('role_description', models.CharField(max_length=30)),
            ],
            options={
                'permissions': (('view_exercisec', 'Can see exercisec'), ('change_exercisec', 'Can change the exercisec'), ('del_exercisec', 'Can delete exercisec')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=50)),
                ('card', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('telphone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('head_url', models.CharField(max_length=50)),
                ('create_time', models.CharField(max_length=50)),
                ('major_id', models.CharField(max_length=50)),
                ('academy_id', models.CharField(max_length=50)),
                ('class_id', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
