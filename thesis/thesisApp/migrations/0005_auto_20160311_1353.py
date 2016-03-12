# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0004_auto_20160311_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='coures',
            new_name='courses',
        ),
    ]
