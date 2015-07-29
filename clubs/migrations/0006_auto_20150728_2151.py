# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_club_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='meeting_day',
            field=models.CharField(default=b'Monday', max_length=9, choices=[(b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thursday'), (b'Saturday', b'Saturday'), (b'Sunday', b'Sunday')]),
        ),
    ]
