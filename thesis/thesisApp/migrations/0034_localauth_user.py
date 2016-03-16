# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0033_remove_localauth_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='localauth',
            name='user',
            field=models.ForeignKey(default=1, to='thesisApp.User'),
            preserve_default=False,
        ),
    ]
