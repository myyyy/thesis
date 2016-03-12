# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0014_auto_20160312_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User', models.ForeignKey(to='thesisApp.User')),
                ('coure', models.ForeignKey(to='thesisApp.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise_Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_finished', models.CharField(max_length=30)),
                ('score', models.CharField(max_length=30)),
                ('answer', models.ForeignKey(to='thesisApp.Answer')),
                ('exercisec', models.ForeignKey(to='thesisApp.Exercise')),
                ('stu_user', models.ForeignKey(to='thesisApp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='exerciseusers',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='exerciseusers',
            name='exercisec',
        ),
        migrations.RemoveField(
            model_name='exerciseusers',
            name='stu_user',
        ),
        migrations.DeleteModel(
            name='ExerciseUsers',
        ),
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
    ]
