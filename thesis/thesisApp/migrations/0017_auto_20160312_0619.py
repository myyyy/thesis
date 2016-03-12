# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0016_auto_20160312_0618'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course_User',
            new_name='CourseUser',
        ),
    ]
