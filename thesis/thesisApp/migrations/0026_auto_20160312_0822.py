# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0025_auto_20160312_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='teacher_id',
        ),
        migrations.AddField(
            model_name='user',
            name='Exercise',
            field=models.ManyToManyField(to='thesisApp.Exercise', through='thesisApp.ExerciseUserAnswer'),
            preserve_default=True,
        ),
    ]
