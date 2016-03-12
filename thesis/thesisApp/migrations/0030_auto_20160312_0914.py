# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0029_auto_20160312_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Exercise',
            new_name='exercise',
        ),
    ]
