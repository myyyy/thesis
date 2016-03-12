# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0009_remove_localauth_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='ex_user_id',
        ),
        migrations.AddField(
            model_name='exercise',
            name='ex_user',
            field=models.ManyToManyField(to='thesisApp.User'),
            preserve_default=True,
        ),
    ]
