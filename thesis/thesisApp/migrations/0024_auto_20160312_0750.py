# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0023_auto_20160312_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseuser',
            name='coure',
            field=models.ForeignKey(related_name='courses', to='thesisApp.Course'),
            preserve_default=True,
        ),
    ]
