# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20150728_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='meeting_day',
            field=models.CharField(default='Wednesday', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='meeting_time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 28, 4, 14, 59, 758601, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
