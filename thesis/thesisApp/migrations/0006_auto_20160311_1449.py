# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0005_auto_20160311_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(to='thesisApp.User'),
            preserve_default=True,
        ),
    ]
