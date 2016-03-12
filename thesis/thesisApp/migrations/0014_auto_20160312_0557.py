# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0013_auto_20160312_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='teacher',
        ),
        migrations.AddField(
            model_name='exercise',
            name='teacher_id',
            field=models.ForeignKey(default=1, to='thesisApp.User'),
            preserve_default=False,
        ),
    ]
