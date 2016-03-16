# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0034_localauth_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='class_id',
        ),
    ]
