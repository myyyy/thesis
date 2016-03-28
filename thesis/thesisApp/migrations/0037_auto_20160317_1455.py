# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0036_auto_20160316_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localauth',
            name='role_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='academy_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='major_id',
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
