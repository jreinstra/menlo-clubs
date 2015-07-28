# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_club_meeting_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='contact_email',
            field=models.CharField(default='john.reinstra@menloschool.org', max_length=200),
            preserve_default=False,
        ),
    ]
