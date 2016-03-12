# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0022_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(to='thesisApp.Course', through='thesisApp.CourseUser'),
            preserve_default=True,
        ),
    ]
