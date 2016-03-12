# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0010_auto_20160312_0537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='ex_user',
            new_name='user',
        ),
    ]
