# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0017_auto_20160312_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_content', models.CharField(max_length=30)),
                ('is_finished', models.CharField(max_length=30)),
                ('score', models.CharField(max_length=30)),
                ('exercisec', models.ForeignKey(to='thesisApp.Exercise')),
                ('stu_user', models.ForeignKey(to='thesisApp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='CourseUser',
            new_name='CoursesUser',
        ),
        migrations.RemoveField(
            model_name='exerciseuseranswer',
            name='exercisec',
        ),
        migrations.RemoveField(
            model_name='exerciseuseranswer',
            name='stu_user',
        ),
        migrations.DeleteModel(
            name='ExerciseUserAnswer',
        ),
    ]
