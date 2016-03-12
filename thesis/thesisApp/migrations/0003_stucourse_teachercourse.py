# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0002_auto_20160311_1333'),
    ]

    operations = [
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
    ]
