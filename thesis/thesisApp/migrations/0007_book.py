# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesisApp', '0006_auto_20160311_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
