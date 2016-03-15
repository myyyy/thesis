# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0030_auto_20160312_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseuseranswer',
            name='course_id',
            field=models.ForeignKey(default=1, to='thesisApp.Course'),
            preserve_default=False,
        ),
    ]
