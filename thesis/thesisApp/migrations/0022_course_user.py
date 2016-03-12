# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0021_auto_20160312_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to='thesisApp.User', through='thesisApp.CourseUser'),
            preserve_default=True,
        ),
    ]
