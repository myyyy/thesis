# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0011_auto_20160312_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_finished', models.CharField(max_length=30)),
                ('exercisec', models.ForeignKey(to='thesisApp.Exercise')),
                ('user', models.ForeignKey(to='thesisApp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='user',
        ),
    ]
