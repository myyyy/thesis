# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0003_stucourse_teachercourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stucourse',
            name='coures_id',
        ),
        migrations.DeleteModel(
            name='StuCourse',
        ),
        migrations.RemoveField(
            model_name='teachercourse',
            name='coures_id',
        ),
        migrations.DeleteModel(
            name='TeacherCourse',
        ),
    ]
