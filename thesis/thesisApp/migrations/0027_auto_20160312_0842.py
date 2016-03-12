# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0026_auto_20160312_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localauth',
            name='can_login',
        ),
        migrations.AddField(
            model_name='localauth',
            name='is_login',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exerciseuseranswer',
            name='is_finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
