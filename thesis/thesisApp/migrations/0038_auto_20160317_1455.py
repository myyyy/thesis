# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0037_auto_20160317_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='card',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]
