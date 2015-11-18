# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20150827_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='meets_biweekly',
            field=models.BooleanField(default=False)
        ),
        migrations.AddField(
            model_name='club',
            name='meets_irregularly',
            field=models.BooleanField(default=False)
        ),
        migrations.AddField(
            model_name='club',
            name='meets_monthly',
            field=models.BooleanField(default=False)
        ),
        migrations.AlterField(
            model_name='club',
            name='meeting_day',
            field=models.IntegerField(default=(0, b'Monday'), choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday'), (7, b'Non Weekly')])
        ),
    ]
