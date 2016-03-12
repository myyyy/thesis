# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stucourse',
            name='coures_id',
        ),
        migrations.DeleteModel(
            name='StuCourse',
        ),
        migrations.DeleteModel(
            name='StuRole',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='SubjectManager',
        ),
        migrations.RemoveField(
            model_name='teachercourse',
            name='coures_id',
        ),
        migrations.DeleteModel(
            name='TeacherCourse',
        ),
        migrations.DeleteModel(
            name='TeacherRole',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='answer_guid_exercise',
            new_name='answer_exercise_id',
        ),
        migrations.RemoveField(
            model_name='class',
            name='class_id',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='ex_course_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AddField(
            model_name='exercise',
            name='course_id',
            field=models.ForeignKey(default=1, to='thesisApp.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='coures',
            field=models.ManyToManyField(to='thesisApp.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_user_id',
            field=models.ForeignKey(to='thesisApp.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='localauth',
            name='user_id',
            field=models.ForeignKey(to='thesisApp.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='class_id',
            field=models.ForeignKey(to='thesisApp.Class'),
            preserve_default=True,
        ),
    ]
