# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0012_auto_20160312_0544'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseUsers',
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
            model_name='exerciseuser',
            name='exercisec',
        ),
        migrations.RemoveField(
            model_name='exerciseuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='ExerciseUser',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_exercise_id',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_user_id',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='score',
        ),
        migrations.AddField(
            model_name='exercise',
            name='teacher',
            field=models.ForeignKey(default=b'', editable=False, to='thesisApp.User', max_length=50),
            preserve_default=True,
        ),
    ]
