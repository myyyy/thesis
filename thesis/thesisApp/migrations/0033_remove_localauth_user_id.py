# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0032_courseuser_num_unfinished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localauth',
            name='user_id',
        ),
    ]
