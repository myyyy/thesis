# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0038_auto_20160317_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseuser',
            old_name='coure',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='cs_id',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='ex_id',
        ),
    ]
