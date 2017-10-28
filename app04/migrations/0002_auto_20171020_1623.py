# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app04', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='password',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
