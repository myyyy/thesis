# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0027_auto_20160312_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localauth',
            name='auth_id',
        ),
    ]
