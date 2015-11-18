# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        #('clubs', '0003_auto_20151018_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='meets_biweekly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='club',
            name='meets_irregularly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='club',
            name='meets_monthly',
            field=models.BooleanField(default=False),
        ),
    ]
