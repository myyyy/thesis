# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0035_remove_user_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localauth',
            name='user',
            field=models.OneToOneField(to='thesisApp.User'),
            preserve_default=True,
        ),
    ]
