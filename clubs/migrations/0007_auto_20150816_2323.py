# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_auto_20150728_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='meeting_day',
            field=models.IntegerField(default=(0, b'Monday'), max_length=9, choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday')]),
        ),
    ]
