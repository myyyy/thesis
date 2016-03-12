# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0028_remove_localauth_auth_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseuser',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='exerciseuseranswer',
            old_name='stu_user',
            new_name='user',
        ),
    ]
