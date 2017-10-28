# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app04', '0003_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
