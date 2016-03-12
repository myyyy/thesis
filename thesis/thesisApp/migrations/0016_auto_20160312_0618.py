# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0015_auto_20160312_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseUserAnswer',
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
        migrations.RemoveField(
            model_name='exercise_users',
            name='answer',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='exercise_users',
            name='exercisec',
        ),
        migrations.RemoveField(
            model_name='exercise_users',
            name='stu_user',
        ),
        migrations.DeleteModel(
            name='Exercise_Users',
        ),
    ]
