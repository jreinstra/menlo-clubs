# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20150728_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='meeting_location',
            field=models.CharField(default='A143', max_length=50),
            preserve_default=False,
        ),
    ]
