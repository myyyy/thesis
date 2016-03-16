# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0031_exerciseuseranswer_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseuser',
            name='num_unfinished',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
