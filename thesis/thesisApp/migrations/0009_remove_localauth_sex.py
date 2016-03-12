# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0008_delete_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localauth',
            name='sex',
        ),
    ]
